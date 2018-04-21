from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

'''tweeter data streaming'''
#Variables that contain the user credentials to access Twitter API
access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = ''

class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True
    def on_error(self, status):
        print status

if __name__ == '__main__':
    #Twitter authetification and connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #filter Twitter Streams to capture data by the keywords
    stream.filter(track=['bitcoin', 'btc'])