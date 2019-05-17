import tweepy
from dotenv import load_dotenv
import os
load_dotenv()

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_key = os.environ.get("access_key")
access_secret = os.environ.get("access_secret")

def get_tweets(username):

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)

        tweetData = []
        for tweet in tweets:
            tweetData.append([tweet.created_at, tweet.text, tweet.source, ",".join([hashTag['text'] for hashTag in tweet.entities['hashtags']]) ])

        for row in tweetData:
            print(row)
            print("\n")
        # print(datata)

get_tweets("ani")
