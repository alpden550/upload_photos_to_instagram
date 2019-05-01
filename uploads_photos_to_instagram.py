import os
from dotenv import load_dotenv
from instabot import Bot
load_dotenv()


INST_LOGIN = os.getenv('instagram_login')
INST_PASSW = os.getenv('instagram_passw')


def upload_photo_to_instagram(all_photos, instabot):
    for photo in all_photos:
        instabot.upload_photo(f'images/{photo}')


if __name__ == "__main__":
    all_photos = os.listdir('images')

    bot = Bot()
    bot.login(username=INST_LOGIN, password=INST_PASSW)
    upload_photo_to_instagram(all_photos, bot)
