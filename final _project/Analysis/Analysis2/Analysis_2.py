
# coding: utf-8

# In[1]:

import pandas as pd
import os
from glob import glob


# In[18]:

DATA_PATH_LOCATION = 'C:/Users/Andy/Documents/guo_pengcheng_001643483/Python4DataAnalysis/DataAnalysisPython/final _project/Data/Earnings Report 2012-2015/Earing Report 2012.csv'
data2 = pd.read_csv(DATA_PATH_LOCATION,encoding = "ISO-8859-1")
del data2['Unnamed: 0']
data2


# In[24]:

len((data2['total_earnings']))


# In[46]:

avg1=float(str(data2.sum(axis=0)['total_earnings']/len((data2['total_earnings'])))[0:8])
avg1


# In[35]:

DATA_PATH_LOCATION = 'C:/Users/Andy/Documents/guo_pengcheng_001643483/Python4DataAnalysis/DataAnalysisPython/final _project/Data/Earnings Report 2012-2015/Earing Report 2013.csv'
data3 = pd.read_csv(DATA_PATH_LOCATION,encoding = "ISO-8859-1")
del data3['Unnamed: 0']
data3


# In[37]:

len((data3['total_earnings']))


# In[47]:

avg2=float(str(data3.sum(axis=0)['total_earnings']/len((data3['total_earnings'])))[0:8])
avg2


# In[39]:

DATA_PATH_LOCATION = 'C:/Users/Andy/Documents/guo_pengcheng_001643483/Python4DataAnalysis/DataAnalysisPython/final _project/Data/Earnings Report 2012-2015/Earing Report 2014.csv'
data4 = pd.read_csv(DATA_PATH_LOCATION,encoding = "ISO-8859-1")
del data4['Unnamed: 0']
data4


# In[40]:

len((data4['total_earnings']))


# In[48]:

avg3=float(str(data4.sum(axis=0)['total_earnings']/len((data4['total_earnings'])))[0:8])
avg3


# In[42]:

DATA_PATH_LOCATION = 'C:/Users/Andy/Documents/guo_pengcheng_001643483/Python4DataAnalysis/DataAnalysisPython/final _project/Data/Earnings Report 2012-2015/Earing Report 2015.csv'
data5 = pd.read_csv(DATA_PATH_LOCATION,encoding = "ISO-8859-1")
del data5['Unnamed: 0']
data5


# In[43]:

len((data5['total_earnings']))


# In[49]:

avg4=float(str(data5.sum(axis=0)['total_earnings']/len((data5['total_earnings'])))[0:8])
avg4


# In[60]:

get_ipython().magic('matplotlib inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
s1 = pd.Series(['2012','2013','2014','2015'], name='Year')
s2 = pd.Series([avg1,avg2,avg3,avg4], name='Avg')
df = pd.concat([s1,s2],axis=1)
df


# In[83]:

plt.subplots(figsize=(20,8))     # 改变整个图大小
sns.set_style("whitegrid")
colors = ['#624ea7', 'g', 'yellow', 'k']
ax = sns.barplot(x="Year", y="Avg", data=df, palette=colors)  # 设置BOXPLOT
ax.set_title('Average  Earning')     # 添加标题
plt.setp(ax.xaxis.get_majorticklabels(), rotation=30)        # 设置横坐标
ax.xaxis.get_label().set_fontsize(30)      # 设置坐标题大小
ax.yaxis.get_label().set_fontsize(30)
ax.title.set_fontsize(45)                  # 设置大标题大小
ax.tick_params(axis='x', which='major', labelsize=24)      # 设置坐标值大小
ax.tick_params(axis='y', which='major', labelsize=24)
plt.savefig("output.png")


# In[ ]:




# In[ ]:



