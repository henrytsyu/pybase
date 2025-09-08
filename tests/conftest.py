import pytest

from app.utils.env import ENV


@pytest.fixture(autouse=True, scope="session")
def mock_env():
    """
    Patches the environment object.
    This avoids accidentally using environment variables in ``.env``.
    """
    ENV.__dict__.clear()
    ENV.SENTRY_DSN = "TEST_SENTRY_DSN"
