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


@pytest.mark.parametrize("expected_username", [
    ("admin_jejaka"),
    ("lutfiainun125"),

])
def test_get_user(instagram_instance, expected_username):
    user = instagram_instance.get_user(username=expected_username)
    assert user.username == expected_username

@pytest.mark.parametrize("expected_username", [
    ("admin_jejaka"),
    ("lutfiainun125"),

])
def test_get_user_posts(instagram_instance, expected_username):
    user = instagram_instance.get_user(username=expected_username)
    assert user.username == expected_username
    post = user.get_post()
    assert len(post.media) > 0

@pytest.mark.parametrize("expected_username", [
    ("admin_jejaka"),
    ("lutfiainun125"),

])
def test_get_user_reels(instagram_instance, expected_username):
    user = instagram_instance.get_user(username=expected_username)
    assert user.username == expected_username
    reels = user.get_reel()
    assert len(reels.media) > 0

