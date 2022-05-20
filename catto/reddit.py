from os import getenv

import praw


def get_reddit_instance():
    return praw.Reddit(
        client_id=getenv("REDDIT_CLIENT_ID"),
        client_secret=getenv("REDDIT_CLIENT_SECRET"),
        user_agent="catto_hook script by u/znordrol",
    )
