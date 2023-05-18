# TwitterTweets---HashtagScraper

1) Open the project and go to the Twitter in your windows terminal or on linux operating system.

2) Install all the required python packages using below command: 

        pip install -r requirements.txt

3) Now go to the project directory using command below:

         cd .\Twitter\

4) After reaching Twitter  directory run below command to create the Python path over all the directories and files in the project.

   a) Command for Windows OS:

              command = $env:PYTHONPATH = "Absolute Path of Directory;$env:PYTHONPATH" # Abslolute path of this "LinkedlnProfileUrlScraper" directory
  
       While entering Absolute path of the directory ensure to change backword Slash (/) into forward slash(\) inside the path in case when running in windows machine.

   b) Command for linux OS:   

              Command : export PYTHONPATH="Absolute Path of Directory" # Abslolute path of this "LinkedlnProfileUrlScraper" directory i your linux machine
  
      In this case there is no need to change backward slash.

5)Inside Parameter File Make these changes

    a)Need to add your credentials(Twitter API credentials in Twitter Developer Account) in parameter.py file. 

    b)Enter the Hashtag for which have to scrape data as object hashtagName in parameter.py file.

    c)Enter the Since date upto which you have to scrape data as object dateSince in parameter.py file.

    d)Enter the No. of Tweets you are looking particular username as object numberOfTweets in parameter.py file.

    e)Enter the Username as object userName in parameter.py file.

6)Now Go to the open terminal in pycharm : 

    a) Run command to scrape tweets of particular Usernam
    
         For Windows os : python TweetsScraping.py 
         
         For Mac os: python3 TweetsScraping.py 

    b) Run command to scrape users data for as per hashtags

         For Windows os : python Twitter_hashtag.py

         For Mac os: python3 Twitter_hashtag.py

7) The outputfile of the scraped records is generated inside Twitter folder having random name which has nomenclature as given below for Tweets scraping.

     Output File name exaample : 20230518142546cfzl3.csv, 

     a) Where 20230518 is the date on which file is created

     b) Where 142546 followed by date is the time at which the file is created.
 
     c) After time there are 5 alphanumeric characters
   
8) The output file for twitter hashtags scraping, it will be generated as per given hashtagName in parameter.py file.

Notes:
1) This automated Script run successfully in the scrapy framework and able to scrape approx. 500 Linkedin profile URLs after that google asking for captcha verification.

2) These Linked Profile URLs can be further used to scrape the profile data on linkedin.

Notes:
1) Twitter API has Rate limits over scraping data, after scrapping some data(example: 1000-3000) twitter will stops this automated script. Check Twitter documentation.
2) The Twitter API credentials has expiration period as per the edition you choose among Free, basic and enterprise.
