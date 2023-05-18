import random
import string
import time
from datetime import datetime
# Enter your own credentials obtained
# from your developer account
consumer_key = "Your Twitter Developer Account Consumer_key"
consumer_secret = "Your Twitter Developer Account Consumer_secret"
access_key = "Your Twitter Developer Account access_key"
access_secret = "Your Twitter Developer Account access_secret"
hashtagName = "Enter The Hashtag"
dateSince = "Enter Date since The Tweets are required in yyyy-mm--dd"
numberOfTweets = 'enter the maximum number of tweets want to scrape for any userName'
userName = '@' + 'Enter username for which have to scrape tweets'

# Define the Random file name
length = 5
# Generate a random string
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
# Get the current timestamp
timestamp = time.strftime("%Y%m%d%H%M%S")
fileName = timestamp + random_string + '.csv' #this the generated filename
print("Your output file is: ",fileName )
