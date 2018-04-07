import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

compared_path=''
compared_data=[]
compared_file=open(compared_path,"r")
for line in compared_file:
    try:
        compared = json.loads(line)
        compared_data.append(compared)
    except:
        continue
labels=compared_data[0]
gvalues=compared_data[1]
tvalues=compared_data[2]
'''srednia'''
media=[]
for i in gvalues:
    for j in tvalues:
        media.append(j/i)
mean=np.mean(media)

'''przyblizanie wartosci'''
j=0
for i in gvalues:
    gvalues[j]=int(i/mean*4.3 + 180)
    j=j+1
print(mean)
# j=0
# for i in tvalues:
#     tvalues[j]=int(i/mean)
#     j=j+1

'''plot'''
indexes = np.arange(len(labels))

# width = 1
# plt.xlabel('time', fontsize=5,fontname='Arial')
# plt.ylabel('tweets',fontsize=15,fontname='Arial', rotation='horizontal')
# plt.title('BTC tweets / minute', fontsize=20, fontweight='bold',fontname='Arial')
# plt.plot(indexes, tvalues, color='salmon')
# plt.plot(indexes, values,width, color='lightblue')
# plt.xticks(indexes+width*0.5, labels,rotation=70)

plt.plot(indexes, gvalues,indexes,tvalues,)
plt.legend(["gielda","tweety"])
# plt.ylabel('gielda',fontsize=15,fontname='Arial',rotation='horizontal')
plt.show()
print(gvalues)
print(tvalues)
# , color='purple'