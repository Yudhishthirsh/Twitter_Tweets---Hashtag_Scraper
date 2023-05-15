# Python Script to Extract tweets of a
# particular Hashtag using Tweepy and Pandas

# import modules
import pandas as pd
import tweepy
import parameter


# function to display data of each tweet
def printtweetdata(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"Username:{ith_tweet[0]}")
    print(f"Description:{ith_tweet[1]}")
    print(f"Location:{ith_tweet[2]}")
    print(f"Following Count:{ith_tweet[3]}")
    print(f"Follower Count:{ith_tweet[4]}")
    print(f"Total Tweets:{ith_tweet[5]}")
    print(f"Retweet Count:{ith_tweet[6]}")
    print(f"Tweet Text:{ith_tweet[7]}")
    print(f"Hashtags Used:{ith_tweet[8]}")


# function to perform data extraction
def scrape(words, date_since, numtweet):
    # Creating DataFrame using pandas
    db = pd.DataFrame(columns=['username',
                               'description',
                               'location',
                               'following',
                               'followers',
                               'totaltweets',
                               'retweetcount',
                               'text',
                               'hashtags'])

    # We are using .Cursor() to search
    # through twitter for the required tweets.
    # The number of tweets can be
    # restricted using .items(number of tweets)
    tweets = tweepy.Cursor(api.search_tweets,
                           parameter.hashtagName, lang="en",
                           since_id=parameter.dateSince,
                           tweet_mode='extended').items(numtweet)

    # .Cursor() returns an iterable object. Each item in
    # the iterator has various attributes
    # that you can access to
    # get information about each tweet
    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1

    # we will iterate over each tweet in the
    # list for extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totalTweets = tweet.user.statuses_count
        retweetCount = tweet.retweet_count
        hashTags = tweet.entities['hashtags']

        # Retweets can be distinguished by
        # a retweeted_status attribute,
        # in case it is an invalid reference,
        # except block will be executed
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashText = list()
        for j in range(0, len(hashTags)):
            hashText.append(hashTags[j]['text'])

        # Here we are appending all the
        # extracted information in the DataFrame
        ith_tweet = [username, description,
                     location, following,
                     followers, totalTweets,
                     retweetCount, text, hashText]
        db.loc[len(db)] = ith_tweet

        # Function call to print tweet data on screen
        printtweetdata(i, ith_tweet)
        i = i + 1
    filename = str(parameter.hashtagName) + '.csv'

    # we will save our database as a CSV file.
    db.to_csv(filename)


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(parameter.consumer_key, parameter.consumer_secret)
    auth.set_access_token(parameter.access_key, parameter.access_secret)
    api = tweepy.API(auth)

    # number of tweets you want to extract in one run
    numtweet = 2000
    scrape(parameter.hashtagName, parameter.dateSince, numtweet)
    print('Scraping has completed!')