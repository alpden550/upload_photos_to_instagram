from download_photos import get_file_ext, download_image
import requests


def get_id_from_hubble_collections(collections, hubble_url='http://hubblesite.org/api/v3/images'):
    photos_id = []
    for collection in collections:
        url = f'{hubble_url}/{collection}'
        response = requests.get(url).json()
        photos = [photo.get('id') for photo in response]
        photos_id.extend(photos)
    return photos_id


def download_hubble_image(url='http://hubblesite.org/api/v3/image/', image_id=1):
    url = f'{url}/{image_id}'
    response = requests.get(url).json()

    image_url = response.get('image_files')[-1].get('file_url')
    image_name = get_file_ext(image_url)
    download_image(url=image_url, image_name=f'hubble_photo_{image_id}{image_name}')


if __name__ == "__main__":
    hubble_collection = ['wallpaper', ]
    photos_id = get_id_from_hubble_collections(hubble_collection)
    for photo_id in photos_id:
        print(f'Downloading {photo_id} image')
        download_hubble_image(image_id=photo_id)
        print(f'Finished downloading.')
