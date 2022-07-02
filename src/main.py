"""Media monitor"""
import time
from loguru import logger
import mediamon  # type: ignore


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
