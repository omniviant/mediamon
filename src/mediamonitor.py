"""Media monitor"""
import time
from loguru import logger
import mediamon  # type: ignore


# Log to file that rotates every day at noon
logger.add('data/logs/mediamonitor-{time}.log', rotation='12:00')


def main():
    """Main entry point."""
    config = mediamon.util.load_yaml('conf/config.yml')

    engine = mediamon.MediaMonitor(config)
    engine.start()

    while True:
        if engine.is_running is False:
            logger.warning('Engine is not running.')
        time.sleep(60)


if __name__ == '__main__':
    main()
