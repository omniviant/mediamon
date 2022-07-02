"""Media monitoring engine"""

__all__ = [
    'MediaMonitor'
]

import threading
import time
from queue import Queue
from loguru import logger
from .youtube import YouTubeInterface, get_channel


class MediaMonitor:
    """Media Monitor Engine"""
    def __init__(self, config: dict):
        self.config = config

        self.channels = self.config['urls']
        self.event_queue = Queue()
        self.download_queue = Queue()
        self.media_list = []
        self.workers = []

        self.is_running = False

    def init_yt(self, config=None):
        """Initialize a YouTubeInterface."""
        if config is None:
            config = {
                'output': self.config['data_directory'],
                'uploader': '',
                'yt-dlp': self.config['yt-dlp'],
            }
        return YouTubeInterface(config)

    def start(self):
        """Start monitoring engine."""
        # Start monitor thread
        threading.Thread(
            target=self.monitor,
            daemon=True,
            name='Monitor'
        ).start()

        # Start event dispatcher
        threading.Thread(
            target=self.event_dispatcher,
            daemon=True,
            name='EventDispatcher'
        ).start()

        # Start downloader if "download" is enabled
        if self.config['download'] is True:
            for i in range(self.config['workers']):
                self.workers.append(threading.Thread(
                    target=self.downloader,
                    daemon=True,
                    name=f'Downloader{i}'
                ))
            for thread in self.workers:
                thread.start()

        self.is_running = True

    def event_dispatcher(self):
        """Watches event queue and dispatches events."""
        while True:
            event = self.event_queue.get()

            if event['type'] == 'new_video':
                uploader = event['channel']
                title = event['title']
                url = event['url']

                logger.info(f'New video: {uploader} - {title}')

                if self.config['download'] is True:
                    self.download_queue.put_nowait(
                        (uploader, title, url,)
                    )

    def downloader(self):
        """Watches the download queue and downloads media."""
        while True:
            # Get job
            job = self.download_queue.get()

            # Parse job
            uploader, title, url = job
            output_directory = f"{self.config['data_directory']}"
            config = {
                'output': output_directory,
                'uploader': uploader,
                'yt-dlp': dict(self.config['yt-dlp']),
            }

            # Log start
            logger.info(f'Downloading: {uploader} - {title}')
            yt = self.init_yt(config)
            yt.download([url])

            # Log completion
            logger.info(f'Download complete: {uploader} - {title}')

    def monitor(self):
        """Monitors channels for new content.

        Continuously gets channel index pages and adds new videos to a queue.
        """
        while True:
            seen = self.media_list
            for url in self.channels:
                # Create YouTubeInterface with config parameters
                yt = self.init_yt()

                # Get channel index and metadata
                channel = get_channel(url, yt)

                # Map entries and filter out new media
                new = list(filter(lambda x: x not in seen, channel['entries']))

                # Add new entries to queues
                for entry in new:
                    event = {
                        'type': 'new_video',
                        'channel': channel['uploader'],
                        'title': entry['title'],
                        'url': entry['url']
                    }
                    self.event_queue.put(event)
                    self.media_list.append(entry)

            # End cycle and sleep
            time.sleep(60)
