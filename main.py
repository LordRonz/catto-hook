from utils.read_env import read_env
from reddit.reddit import get_reddit_instance
from utils.helper import is_image
from secrets import choice
from discord_webhook.discord_webhook import DiscordWebhook
import config
from datetime import datetime
import os


def main():
    read_env()
    webhook_url = os.getenv("WEBHOOK_URL", "")
    reddit = get_reddit_instance()
    result = list(reddit.subreddit("cats").top("week"))
    while True:
        img = choice(result).url
        if is_image(img):
            break

    while True:
        thumbnail = choice(result).url
        if is_image(img):
            break

    webhook = DiscordWebhook(
        url=webhook_url,
        username=config.USERNAME,
        avatar_url=config.AVATAR_URL,
    )

    webhook.add_embed(
        {
            "title": "Your daily cat pic has arrived",
            "color": 0x631313,
            "image": {
                "url": img,
            },
            "timestamp": datetime.now().isoformat(),
            "thumbnail": {
                "url": thumbnail,
            },
            "url": img,
        }
    )

    webhook.execute()


if __name__ == "__main__":
    main()
