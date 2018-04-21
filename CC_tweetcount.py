import json
import datetime
from collections import Counter
import pandas as pd

'''import tweet data from file'''
tweets_data_path = 'path'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
tweets = pd.DataFrame()
tweets['time'] = map(lambda tweet: tweet['created_at'], tweets_data)

'''occurances tracking'''
twittlist=[]
for i in tweets['time']: twittlist.append(float(datetime.datetime.strptime(str(i),'%a %b %d %H:%M:%S +%f %Y').strftime('%H%M')))
labels, values = zip(*Counter(twittlist).items())
labels, values = zip(*sorted(zip(labels, values)))