import logging
import os
import json
from dotenv import load_dotenv
from instagrapi import Client
from instagrapi.exceptions import ClientError

load_dotenv()

# Configure logging
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

USERNAME = os.getenv("USERNAMEX")
PASSWORD = os.getenv("PASSWORD")

def login_user():
    """
    Attempts to login to Instagram using either the provided session information
    or the provided username and password.
    """

    client = Client()
    session_path = "session.json"
    if os.path.exists(session_path):
        try:
            client.load_settings(session_path)
            client.login(USERNAME, PASSWORD)
            logger.info("Logged in using session information")
            return client
        except Exception as e:
            logger.info("Couldn't load session or login: %s" % e)
    else:
        try:
            client.login(USERNAME, PASSWORD)
            client.dump_settings(session_path)
            logger.info("Logged in using username and password")
            return client
        except Exception as e:
            logger.info("Couldn't login user using username and password: %s" % e)

    raise Exception("Couldn't login user with either password or session")


# Get the user's followers
client = login_user()
followers = []

try:
    profile = client.user_info_by_username("myname")
    user_id = profile.pk
    followers_response = client.user_following(user_id)
    if len(followers_response) > 0 :
        for follower in followers_response:
            followers.append({
                "username": followers_response[follower].username,
                "full_name": followers_response[follower].full_name,
                "profile_pic_url": followers_response[follower].profile_pic_url
            })
    else:
        logger.info("No followers found in response")
    # Save followers to JSON file
    with open("followers.json", "w") as file:
        json.dump(followers, file, indent=4)
    logger.info("Followers saved to followers.json")
except ClientError as e:
    logger.info("An error occurred while retrieving followers: %s" % e)
