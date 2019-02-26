import tweepy
access_token = "2901722802-aZuvqYCV4wLbl6G5ZX5rbfKh54XwBK6HjJSnZYM"
access_token_secret = "21p1V3tNX698QKKug0Z4v9kUQ4bp3vkMb32143dvgDzWo"
consumer_key = "n30IbetTPayHbruKWryrd39v3"
consumer_secret = "ERJo6ZHexudlL23eoebJRSsey9cbAzptPOngcZT8kqFgJj6DCK"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
places = api.geo_search(query="India", granularity="country")
place_id = places[0].id

tweets = api.search(q="place:%s" % place_id)
for tweet in tweets:
    print tweet.text + " | " + tweet.place.name if tweet.place else "Undefined place"
