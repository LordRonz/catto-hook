from utils.read_env import read_env
from catto.reddit import get_reddit_instance
from catto.catapi import CatAPI
from utils.helper import is_image
from secrets import choice
from catto.fact import CatFact
from discord_webhook.discord_webhook import DiscordWebhook
import config
from datetime import datetime
import os


def main():
    read_env()
    is_ci = os.getenv("CI", "") == "true"

    webhook_url: str = os.getenv("WEBHOOK_URL_DEV" if is_ci else "WEBHOOK_URL", "")
    if is_ci and not webhook_url:
        webhook_url = os.getenv("WEBHOOK_URL", "")

    img = ''
    mode = choice(['reddit', 'catapi', 'catapi', 'catapi'])
    if mode == 'reddit':
        reddit = get_reddit_instance()
        result = list(reddit.subreddit("cats").top("week"))
        retry = 0
        while retry < 20:
            img = choice(result).url
            if is_image(img):
                break
            retry += 1

        retry = 0
        while retry < 20:
            thumbnail = choice(result).url
            if is_image(img):
                break
            retry += 1
    elif mode == 'catapi':
        img = CatAPI().get_cat()
        thumbnail = CatAPI().get_cat()

    webhook = DiscordWebhook(
        url=webhook_url,
        username=config.USERNAME,
        avatar_url=config.AVATAR_URL,
    )

    description = f"Random cat facts:\n{CatFact(10).get_fact()}"

    webhook.add_embed(
        {
            "title": "Your daily catto hook has arrived",
            "description": description,
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
