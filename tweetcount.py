import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import datetime

'''import data from tweeter'''
tweets_data_path = 'C:/Users/Anna/Documents/STUDIA/semestr 6/kaggle/TwittCrypto/twitter.txt'
# tweets_data_path = 'C:/Users/Anna/Documents/STUDIA/semestr 6/kaggle/twitter_data1.txt'
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

'''plot'''
indexes = np.arange(len(labels))
width = 1
plt.xlabel('time', fontsize=5,fontname='Arial')
plt.ylabel('tweets',fontsize=15,fontname='Arial', rotation='horizontal')
plt.title('BTC tweets / minute', fontsize=20, fontweight='bold',fontname='Arial')
plt.plot(indexes, values, color='lightblue')
# plt.plot(indexes, values,width, color='lightblue')
plt.xticks(indexes+width*0.5, labels,rotation=70)
# plt.show()
# print(tweets_file.head())