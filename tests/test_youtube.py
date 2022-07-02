"""YouTube module tests"""
import pytest
from yt_dlp import YoutubeDL
from src.mediamon import youtube


test_url = 'https://www.youtube.com/user/l0de'


def test_YouTubeInterface():
    """Test YouTubeInterface (youtube-dlp wrapper class)."""
    yt = youtube.YouTubeInterface()
    assert isinstance(yt, youtube.YouTubeInterface)
    assert isinstance(yt, YoutubeDL)


def test_get_channel():
    """Test getting channel information and metadata."""
    info = youtube.get_channel(test_url)
    assert isinstance(info, dict)


@pytest.mark.skip
def test_download_video():
    """Test downloading a single video."""
    result = youtube.download_video(test_url)
    assert isinstance(result, dict)
