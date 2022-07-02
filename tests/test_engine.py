"""MediaMonitor Engine tests"""
from queue import Queue
from src import mediamon


config = mediamon.util.load_yaml('src/conf/config.yml')


def test_engine():
    """Test MediaMonitor Engine"""
    engine = mediamon.MediaMonitor(config)

    assert isinstance(engine, mediamon.MediaMonitor)

    assert hasattr(engine, 'channels')
    assert isinstance(engine.channels, list)

    assert hasattr(engine, 'event_queue')
    assert isinstance(engine.event_queue, Queue)

    assert hasattr(engine, 'download_queue')
    assert isinstance(engine.download_queue, Queue)

    assert hasattr(engine, 'media_list')
    assert isinstance(engine.media_list, list)

    assert hasattr(engine, 'config')
    assert isinstance(engine.config, dict)

    assert hasattr(engine, 'is_running')
    assert isinstance(engine.is_running, bool)
