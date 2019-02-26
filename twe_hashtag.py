import tweepy
import csv
import pandas as pd

access_token = "2901722802-aZuvqYCV4wLbl6G5ZX5rbfKh54XwBK6HjJSnZYM"
access_token_secret = "21p1V3tNX698QKKug0Z4v9kUQ4bp3vkMb32143dvgDzWo"
consumer_key = "n30IbetTPayHbruKWryrd39v3"
consumer_secret = "ERJo6ZHexudlL23eoebJRSsey9cbAzptPOngcZT8kqFgJj6DCK"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('a.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#BJP",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.place])
