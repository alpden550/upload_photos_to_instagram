from download_photos import get_file_ext, download_image
import requests


def get_space_photos(url='https://api.spacexdata.com/v3/launches/latest'):
    response = requests.get(url)
    if response.ok:
        return response.json().get('links').get('flickr_images')


def fetch_spacex_last_launch(images_list, start=1):
    for image_number, image in enumerate(images_list, start=1):
        image_extension = get_file_ext(url=image)
        download_image(url=image, image_name=f'space_launch_{image_number}{image_extension}')


if __name__ == "__main__":
    try:
        spaces_photos = get_space_photos()
    except AttributeError as error:
        print(error)
        spaces_photos = []
    if spaces_photos is not None:
        fetch_spacex_last_launch(spaces_photos)
