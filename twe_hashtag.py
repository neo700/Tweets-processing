import tweepy
import csv
import pandas as pd


access_token = ""
access_secret = ""
consumer_key = ""
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('new9.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
f = open('FILENAME.json', 'a')

for tweet in tweepy.Cursor(api.search,q='#BJP OR #bjp OR BJP OR Modi OR modi',geocode="21.146633,79.088860,1756km",count=100,
                           lang="en").items():
    print (tweet.created_at, tweet.text, tweet.user.location)
    
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.location.encode('utf-8')])
