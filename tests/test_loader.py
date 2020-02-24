from page_loader.client import get_response
from page_loader.utils import get_file_name_from_url, write_data_to_file

TEST_URL = 'https://hexlet.io/courses'
TEST_PATH = '/var/tmp'
TEST_PATH_HTML = '/var/tmp/hexlet-io-courses.html'


def test_url_status():
    response = get_response(TEST_URL)
    assert response.status_code == 200, 'web site is not ok'


def test_match_file_path():
    response = get_response(TEST_URL)
    file_name = get_file_name_from_url(TEST_URL)
    file_path = write_data_to_file(response.text, file_name=file_name,
                                   _dir=TEST_PATH)
    assert file_path == TEST_PATH_HTML, 'paths do not match'
