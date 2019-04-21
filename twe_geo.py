import tweepy
import csv
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

#authorisation for the account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
places = api.geo_search(query="India", granularity="country")
place_id = places[0].id

tweets = api.search(q="place:%s" % place_id)
for tweet in tweets:
    print tweet.text + " | " + tweet.place.name if tweet.place else "Undefined place"
