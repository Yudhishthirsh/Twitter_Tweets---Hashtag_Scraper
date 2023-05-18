import tweepy
import pandas as pd
from datetime import datetime
import parameter


# twitter authentication
auth = tweepy.OAuthHandler(parameter.access_key, parameter.access_secret)
auth.set_access_token(parameter.consumer_key, parameter.consumer_secret)

# Creating an API object
api = tweepy.API(auth)
tweet_list = []
max_id = None

while True:
    tweets = api.user_timeline(screen_name=parameter.userName,
                               count=200,
                               include_rts=False,
                               tweet_mode='extended',
                               max_id= max_id)
    if len(tweets) == 0:
        break

    for tweet in tweets:
        text = tweet.full_text

        refined_tweet = {"user": tweet.user.screen_name,
                         'text': text,
                         'favorite_count': tweet.favorite_count,
                         'retweet_count': tweet.retweet_count,
                         'created_at': tweet.created_at}

        tweet_list.append(refined_tweet)

    max_id = tweets[-1].id - 1
    if len(tweet_list) >= int(parameter.numberOfTweets):
        break

df = pd.DataFrame(tweet_list)
df.to_csv(parameter.fileName)
