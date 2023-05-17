# TwitterTweets---HashtagScraper

Download pycharm and setup virtual enviroment in your pycharm inside the folder LinkedlnProfile_URLDataScraper using Command in terminal below.

pip install virtualenv or can follow the below link to create virtual Environment

https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#env-requirements

After creating virtual environment in your project. install scrapy package in pycharm , install instaloader package using pip install instaloader , install pandas into the terminal using pip install pandas command in the Terminal To install all these packages use command pip install r- requirement.text

Before Running the spider run this command to create python path for all python files in the directory $env:PYTHONPATH = "Path of Directory;$env:PYTHONPATH" Path of Directory:Main Project Directory which includes all files such as login,requirement and parameter

To scrape data from linkedln (Profile Urls) need Linkedln Credentials

Inside Parameter File Make these changes

1)Need to add your credentials(Twitter API credentials in Twitter Developer Account) in parameter.py file. 
2)Enter the Hashtag for which have to scrape data as object hashtagName in parameter.py file.
3)Enter the Since date upto which you have to scrape data as object dateSince in parameter.py file.
4)Enter the No. of Tweets you are looking particular username as object numberOfTweets in parameter.py file.
5)Enter the Username as object userName in parameter.py file.

Now Go to the open terminal in pycharm : 
1) Run command to scrape tweets of particular Username
For Windows os : python TweetsScraping.py 
For Mac os: python3 TweetsScraping.py 

2) Run command to scrape users data for as per hashtags
For Windows os : python Twitter_hashtag.py
For Mac os: python3 Twitter_hashtag.py

After Running these commands the ouptput for hashtags is generated as filename : hashtagname that given in parameter followed by '.csv'.
And output for tweet list for particular username will be generated in tweetsList.csv



Notes:
1) Twitter API has Rate limits over scraping data, after scrapping some data(example: 1000-3000) twitter will stops this automated script. Check Twitter documentation.
2) The Twitter API credentials has expiration period as per the edition you choose among Free, basic and enterprise.
