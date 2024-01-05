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

