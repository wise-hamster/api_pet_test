from src.request.requests import post_request
import pytest






@pytest.fixture(scope='session')
def test_post_pet ():
    response = post_request(
        url = url_post_pet,
        body=json)