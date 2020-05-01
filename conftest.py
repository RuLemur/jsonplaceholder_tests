import pytest

from framework.jsonplaceholder_client import Client


@pytest.fixture(scope="session")
def api_client():
    return Client()
