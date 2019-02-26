#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2901722802-aZuvqYCV4wLbl6G5ZX5rbfKh54XwBK6HjJSnZYM"
access_token_secret = "21p1V3tNX698QKKug0Z4v9kUQ4bp3vkMb32143dvgDzWo"
consumer_key = "n30IbetTPayHbruKWryrd39v3"
consumer_secret = "ERJo6ZHexudlL23eoebJRSsey9cbAzptPOngcZT8kqFgJj6DCK"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
