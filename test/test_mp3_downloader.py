import os
import requests_mock
from paradise.common.mp3_downloader import download_mp3


def test_download_mp3():
    url = 'http://example.com/test.mp3'
    filename = 'test_dir/test_file.mp3'

    with requests_mock.Mocker() as m:
        m.get(url, status_code=200, content=b'Test content')

        result = download_mp3(url, filename)
        assert os.path.exists(filename)
        assert result == f'{filename}'

        # Clean up (delete the downloaded file and directory)
        if os.path.exists(filename):
            os.remove(filename)
        if os.path.exists(os.path.dirname(filename)):
            os.rmdir(os.path.dirname(filename))
