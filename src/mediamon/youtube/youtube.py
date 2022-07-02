"""YouTube module"""

__all__ = [
    'YouTubeInterface',
    'download_video',
    'get_channel',
]

from typing import Any
from yt_dlp import YoutubeDL  # type: ignore


class YouTubeInterface(YoutubeDL):
    """YouTubeDL Wrapper."""
    _default_params = {
        'output': 'downloads',
        'uploader': 'youtube',
        'yt-dlp': {
            'format': 'ba+bv/b',
            'noprogress': True,
            'restrictfilenames': True,
            'quiet': True,
            'writeinfojson': True,
            'paths': {},
        },
    }

    def __init__(self, params: Any = None) -> None:
        # Set defaults
        if params is None:
            params = YouTubeInterface._default_params

        output_dir = params['output'] + '/' + params['uploader']
        params['yt-dlp']['paths'] = {
            'home': output_dir,
            'temp': output_dir
        }

        self.params = params

        # Initialize parent YouTubeDL class
        super().__init__(self.params['yt-dlp'])


def download_video(
        url: str,
        yt: YouTubeInterface = YouTubeInterface()
) -> int:
    """Download a single video."""
    result = yt.download(url)

    return result


def get_channel(
        url: str,
        yt: YouTubeInterface = YouTubeInterface()
) -> dict:
    """Get channel information and metadata."""
    channel = yt.extract_info(
        url,
        download=False,
        process=False,
    )

    # Convert entries generator to list
    channel['entries'] = list(channel['entries'])

    return channel
