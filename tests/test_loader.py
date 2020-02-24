import os
from os import path

from page_loader.client import get_response
from page_loader.utils import get_file_name_from_url, write_data_to_file, \
    set_local_links

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


def test_save_html_file():
    file_name = get_file_name_from_url(TEST_URL)
    response = get_response(TEST_URL)
    path_to_file = path.join(TEST_PATH, file_name)
    edited_html = set_local_links(response.text, path_to_file, TEST_URL)
    write_data_to_file(edited_html, file_name=file_name,
                       _dir=TEST_PATH)

    path_to_resource_file = f'{path_to_file}_files'
    created_files = os.listdir(path_to_resource_file)
    assert len(created_files) >= 1, 'folder is empty'
