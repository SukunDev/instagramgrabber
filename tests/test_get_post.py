import pytest

from InstagramGrabber import Instagram
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def instagram_instance():
    username = os.environ.get("IG_USERNAME", None)
    password = os.environ.get("IG_PASSWORD", None)
    return Instagram(username=username, password=password)

@pytest.mark.parametrize("expected_username", [(os.environ.get("IG_USERNAME", None))])
def test_login(instagram_instance, expected_username):
    user = instagram_instance.login()
    assert user['username'] == expected_username


@pytest.mark.parametrize("shortcode, expected_username", [
    ("B03lUoxj7uU", "admin_jejaka"),
    ("Bg5LxpRgI1b", "lutfiainun125"),

])
def test_get_post(instagram_instance, shortcode, expected_username):
    get_post = instagram_instance.get_post(url=f"https://www.instagram.com/p/{shortcode}")
    user = get_post.user
    assert user.username == expected_username
    media = get_post.media
    if media:
        assert len(media) > 1