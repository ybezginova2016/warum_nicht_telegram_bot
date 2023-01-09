import tweepy
import os


from dto import Post

TW_ACCESS_TOKEN = os.getenv("TW_ACCESS_TOKEN")
TW_ACCESS_TOKEN_SECRET = os.getenv("TW_ACCESS_TOKEN_SECRET")
TW_CONSUMER_KEY = os.getenv("TW_CONSUMER_KEY")
TW_CONSUMER_KEY_SECRET = os.getenv("TW_CONSUMER_KEY_SECRET")

_client = tweepy.Client(
    consumer_key=TW_CONSUMER_KEY,
    consumer_secret=TW_CONSUMER_KEY_SECRET,
    access_token=TW_ACCESS_TOKEN,
    access_token_secret=TW_ACCESS_TOKEN_SECRET)


class TwitterApi:

    def create_tweet(self, post: Post) -> str:
        if post.tweet_id is not None:
            response = _client.create_tweet(text=post.tweet_text, quote_tweet_id=post.tweet_id)

            return response.data.get('id')
        else:
            response = _client.create_tweet(text=post.tweet_text)
            return response.data.get('id')
