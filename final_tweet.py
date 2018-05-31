import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
from tweepy import Stream
import tweepy as twp
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import datetime

#Variables that contains the user credentials to access Twitter API
access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = ''
def disconnect(self):
    if self.running is False:
        return
    self.running = False

class StdOutListener(StreamListener):

    def on_data(self, data,twittlist=[]):
        json_time=str(json.loads(data)['created_at'])
        date=int(datetime.datetime.strptime(json_time, '%a %b %d %H:%M:%S +%f %Y').strftime('%H%M%S'))
        twittlist.append(date)
        if twittlist[-1]-twittlist[0]>5:
            stream.disconnect()
            labels, values = zip(*Counter(twittlist).items())
            labels, values = zip(*sorted(zip(labels, values)))
            labels = list(labels)
            values = list(values)
            print(labels)
            print(values)
            return twittlist


'''auth'''
# This handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['bitcoin', 'btc'])

