import json
import numpy as np
import matplotlib.pyplot as plt

'''import file containing cryptocurrency tweet occurances and market volume '''
compared_path='path'
compared_data=[]
compared_file=open(compared_path,"r")
for line in compared_file:
    try:
        compared = json.loads(line)
        compared_data.append(compared)
    except:
        continue
#labels
labels=compared_data[0]
#cryptocurrency volume values
gvalues=compared_data[1]
#tweet values
tvalues=compared_data[2]

'''adjust both results for better visibility'''
#scaling the volume for ploting
scaled=[]
for volume in gvalues:
    for tweet in tvalues:
        scaled.append(tweet/volume)
mean=np.mean(scaled)
j=0
for volume in gvalues:
    gvalues[j]=int(volume/mean*4.3 + 180)
    j=j+1
print(mean)

'''plot'''
indexes = np.arange(len(labels))
plt.plot(indexes, gvalues,indexes,tvalues,)
plt.legend(["cc volume","cc tweets"])
plt.show()
print(gvalues)
print(tvalues)
#the results show the relationship between tweet occurances and market volume of cryptocurrencies