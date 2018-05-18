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

#comparing differences
gdifferences = []
tdifferences = []
for i in range (0,len(gvalues)-1):
    gdifferences.append(int((1-(float(gvalues[i+1])/float(gvalues[i])))*100))
    tdifferences.append(int((1 -(float(tvalues[i + 1]) / float(tvalues[i])))*100))
# print(len(gvalues))
# print(len(gdifferences))

'''Pearson correlation coefficient'''
sum1=0
sum2=0
sum3=0
for i in range (0,len(gvalues)-1):
    sum1 = sum1 + (float(gdifferences[i])-float(np.mean(gdifferences)))*(tdifferences[i]-np.mean(tdifferences))
    sum2 = sum2 + (float(gdifferences[i])-float(np.mean(gdifferences)))**2
    sum3 = sum3 + (float(tdifferences[i])-float(np.mean(tdifferences)))**2
Pearson_cc=sum1/((np.sqrt(sum2))*(np.sqrt(sum3)))
print(abs(Pearson_cc))
# Pearson correlation coefficient shows correletion between two datasets. The more close to 1 the bigger correlation is.

'''adjust both results for better visibility'''
# #scaling the volume for ploting
# scaled=[]
# for volume in gvalues:
#     for tweet in tvalues:
#         scaled.append(tweet/volume)
# mean=np.mean(scaled)
# j=0
# for volume in gvalues:
#     gvalues[j]=int(volume/mean*4.3 + 180)
#     j=j+1
# print(mean)


'''plot'''
# indexes = np.arange(len(labels))
# plt.plot(indexes, gvalues,indexes,tvalues,)
# plt.legend(["cc volume","cc tweets"])
# plt.show()



#the results show the relationship between tweet occurances and market volume of cryptocurrencies