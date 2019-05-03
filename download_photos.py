import os
from urllib.parse import urlparse
import requests


def get_file_ext(url):
    path = urlparse(url).path
    return os.path.splitext(path)[1]


def download_image(url, image_name, path='images'):
    os.makedirs(path, exist_ok=True)

    response = requests.get(url)
    if response.ok:
        with open(f'{path}/{image_name}', 'wb') as image:
            image.write(response.content)


if __name__ == "__main__":
    pass
