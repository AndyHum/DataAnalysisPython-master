
# coding: utf-8

# In[2]:

import requests
import json
import csv
from pandas.io.json import json_normalize
import os
from glob import glob


# In[3]:

url1 = 'https://data.cityofboston.gov/resource/ufcx-3fdn.json'
r1 = requests.get(url)
r1.json()


# In[11]:

PATH_TO_DATA = 'Data'
df1 = json_normalize(r1.json())
del df1[':@computed_region_aywg_kpfh']
if not os.path.exists(PATH_TO_DATA + '/' + 'Crime Incident Reports'):
    os.makedirs(PATH_TO_DATA + '/' + 'Crime Incident Reports')
path1 = PATH_TO_DATA + '/' + 'Crime Incident Reports/' + 'Crime Incident Reports.csv'
df1.to_csv(path1, sep='\t')


# In[12]:

url2 = 'https://data.cityofboston.gov/resource/wypd-uw2t.json'
r2 = requests.get(url2)
r2.json()
df2 = json_normalize(r2.json())
df2


# In[13]:

if not os.path.exists(PATH_TO_DATA + '/' + 'Earnings Report 2012-2015'):
    os.makedirs(PATH_TO_DATA + '/' + 'Earnings Report 2012-2015')
path2 = PATH_TO_DATA + '/' + 'Earnings Report 2012-2015/' + 'Earing Report 2012.csv'
df2.to_csv(path2, sep='\t')


# In[14]:

url3 = 'https://data.cityofboston.gov/resource/5kqy-n8eq.json'
r3 = requests.get(url3)
r3.json()
df3 = json_normalize(r3.json())
df3


# In[15]:

if not os.path.exists(PATH_TO_DATA + '/' + 'Earnings Report 2012-2015'):
    os.makedirs(PATH_TO_DATA + '/' + 'Earnings Report 2012-2015')
path3 = PATH_TO_DATA + '/' + 'Earnings Report 2012-2015/' + 'Earing Report 2013.csv'
df3.to_csv(path3, sep='\t')


# In[16]:

url4 = 'https://data.cityofboston.gov/resource/ntv7-hwjm.json'
r4 = requests.get(url4)
r4.json()
df4 = json_normalize(r4.json())
df4


# In[17]:

if not os.path.exists(PATH_TO_DATA + '/' + 'Earnings Report 2012-2015'):
    os.makedirs(PATH_TO_DATA + '/' + 'Earnings Report 2012-2015')
path4 = PATH_TO_DATA + '/' + 'Earnings Report 2012-2015/' + 'Earing Report 2014.csv'
df4.to_csv(path4, sep='\t')


# In[18]:

url5 = 'https://data.cityofboston.gov/resource/bejm-5s9g.json'
r5 = requests.get(url5)
r5.json()
df5 = json_normalize(r5.json())
df5


# In[19]:

if not os.path.exists(PATH_TO_DATA + '/' + 'Earnings Report 2012-2015'):
    os.makedirs(PATH_TO_DATA + '/' + 'Earnings Report 2012-2015')
path5 = PATH_TO_DATA + '/' + 'Earnings Report 2012-2015/' + 'Earing Report 2015.csv'
df5.to_csv(path5, sep='\t')


# In[ ]:



