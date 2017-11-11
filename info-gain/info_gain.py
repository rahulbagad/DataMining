
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
from math import *


# In[14]:


def entropy(data, target_attr):
    val_freq = {}
    data_entropy = 0.0
 
    for record in data[target_attr]:
        if record in val_freq.keys():
            val_freq[record]+=1.0
        else:
            val_freq[record]=1
 
    for freq in val_freq.values():
        data_entropy += (-freq/len(data)) * log(freq/len(data), 2) 
 
    return data_entropy


# In[15]:


data=pn.read_csv("play.csv")


# In[16]:


data


# In[17]:


def gain(data, attr, target_attr):
    val_freq = {}
    subset_entropy = 0.0
 
    for record in data[attr]:
        if record in val_freq.keys():
            val_freq[record] += 1.0
        else:
            val_freq[record]  = 1.0
    #print(val_freq)

    for val in val_freq.keys():
        val_prob = val_freq[val] / sum(val_freq.values())
    #   print(round(val_prob,2))      
        d=pn.DataFrame()
        for i in range(len(data)):
            if data.loc[i][attr]==val:
                d=d.append(data.loc[i],ignore_index=True)
    #  print(d)        
        subset_entropy += val_prob * entropy(d, target_attr) 
    return (entropy(data, target_attr) - subset_entropy)


# In[18]:


for i in list(data):
    print("info_gain for attribute",i," = ",gain(data,i,"play"))

