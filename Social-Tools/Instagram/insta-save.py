from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import os
import time
import random
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a handler that directs log messages to the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a handler that writes log messages to a file
file_handler = logging.FileHandler('log_file.txt')
file_handler.setLevel(logging.INFO)

# Set the log message format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("Starting up")

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def login_user():
    """
    Attempts to login to Instagram using either the provided session information
    or the provided username and password.
    """

    cl = Client()
    session = None
    if os.path.exists("session.json"):
        session = cl.load_settings("session.json")

    login_via_session = False
    login_via_pw = False

    if session:
        try:
            cl.set_settings(session)
            cl.login(USERNAME, PASSWORD)

            # check if session is valid
            try:
                cl.get_timeline_feed()
            except LoginRequired:
                logger.info("Session is invalid, need to login via username and password")

                old_session = cl.get_settings()

                # use the same device uuids across logins
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])

                cl.login(USERNAME, PASSWORD)
            login_via_session = True
        except Exception as e:
            logger.info("Couldn't login user using session information: %s" % e)

    if not login_via_session:
        try:
            logger.info("Attempting to login via username and password. username: %s" % USERNAME)
            if cl.login(USERNAME, PASSWORD):
                login_via_pw = True
                cl.dump_settings("session.json")
        except Exception as e:
            logger.info("Couldn't login user using username and password: %s" % e)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")
    return cl
# Get the user's saved posts

cl = login_user()

collection_pk = cl.collection_pk_by_name(name="All Posts")
logger.info("Saved posts collection pk: %s" % collection_pk)
while True:
    try:
        saved_posts = cl.collection_medias( amount=20, collection_pk=collection_pk)
        if len(saved_posts) == 0:
            logger.info("No saved posts")
            break
        for m in saved_posts:
                paths = []
                folder_path = m.user.username

                # Check if the folder exists
                if not os.path.exists(folder_path):
                    # Create the folder
                    os.makedirs(folder_path)
                    logger.info(f'Created folder: {folder_path}')
                else:
                    logger.info(f'Folder already exists: {folder_path}')

                logger.info("Unsaving post %s" % m.pk)
                logger.info("Unsaving post %s" % m.user.username)
                logger.info("Unsaving post %s" % m.user.full_name)
                
                try:
                    if m.media_type == 1:
                        # Photo
                        paths.append(cl.photo_download(m.pk, folder=("./"+m.user.username)))
                    elif m.media_type == 2 and m.product_type == "feed":
                        # Video
                        paths.append(cl.video_download(m.pk, folder=("./"+m.user.username)))
                    elif m.media_type == 2 and m.product_type == "igtv":
                        # IGTV
                        paths.append(cl.video_download(m.pk, folder=("./"+m.user.username)))
                    elif m.media_type == 2 and m.product_type == "clips":
                        # Reels
                        paths.append(cl.video_download(m.pk, folder=("./"+m.user.username)))
                    elif m.media_type == 8:
                        # Album
                        for path in cl.album_download(m.pk, folder=("./"+m.user.username)):
                            sleep_duration = random.randint(1, 2)
                            time.sleep(sleep_duration)
                            paths.append(path)

                    cl.media_unsave(m.pk)
                    sleep_duration = random.randint(1, 10)
                    time.sleep(sleep_duration)
                except Exception as e:
                    logger.info(e)
                    continue

    except Exception as e:
        logger.info(e)
        sleep_duration = random.randint(5, 25)
        time.sleep(sleep_duration)