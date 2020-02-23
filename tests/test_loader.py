from page_loader.client import get_response

TEST_URL = 'https://hexlet.io/courses'


def test_url_status():
    response = get_response(TEST_URL)
    assert response.status_code == 200
