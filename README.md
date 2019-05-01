# Upload photos to Instagram

This script can upload photos to your Instagram account.

Images might be downloaded from API SpaceX and API Hubble

## How to install

You have to have Instagram's account to post photos.

Create file .env in the root and write in it:

```.env
instagram_login=instagram login
instagram_passw=instagram password
```

Python3 must be already installed.

Should use virtual env for project isolation.

Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

## How to use

Run scripts in terminal

For downloading photos from SpaceX:

```bash
python fetch_spacex.py
```

For downloading photos from Hubble:

```bash
python fetch_hubble.py
```

For uploading photos from 'images' to Instagram:

```bash
python uploads_photos.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).