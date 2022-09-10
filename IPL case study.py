#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


# In[2]:


ipl=pd.read_csv("data.csv")


# In[3]:


ipl.head()


# In[4]:


ipl.shape


# In[5]:


ipl["player_of_match"].value_counts()


# In[6]:


ipl["player_of_match"].value_counts()[0:10]


# In[7]:


ipl["player_of_match"].value_counts()[0:5]


# In[8]:


list(ipl["player_of_match"].value_counts()[0:5].keys())


# In[9]:


plt.figure(figsize=(12,8))
plt.bar(list(ipl["player_of_match"].value_counts()[0:5].keys()),list(ipl["player_of_match"].value_counts()[0:5]))
plt.show()


# In[10]:


ipl["result"].value_counts()


# In[11]:


ipl["toss_winner"].value_counts()


# In[12]:


batting_first=ipl[ipl["win_by_runs"]!=0]


# In[13]:


batting_first.shape


# In[14]:


batting_first.head()


# In[15]:


plt.figure(figsize=(5,7))
plt.hist(batting_first["win_by_runs"])
plt.title("Disturbution of runs")
plt.xlabel("Runs")
plt.show()


# In[16]:


batting_first["winner"].value_counts()


# In[17]:


plt.figure(figsize=(8,4))
plt.bar(list(batting_first["winner"].value_counts()[0:4].keys()),list(batting_first["winner"].value_counts()[0:4]),color=["red",'yellow',"green","blue"])
plt.title("MOST WINNING TEAM")
plt.xlabel("Team name")
plt.ylabel("Matches")
plt.grid()
plt.show()


# In[18]:


plt.figure(figsize=(10,10))
plt.pie(list(batting_first["winner"].value_counts()),labels=list(batting_first["winner"].value_counts().keys()),autopct="%0.1f%%")
plt.show()


# In[19]:


batting_second=ipl[ipl['win_by_wickets']!=0]


# In[20]:


batting_second.head()


# In[21]:


batting_second.shape


# In[22]:


plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


# In[23]:


batting_second['winner'].value_counts()


# In[24]:


plt.figure(figsize=(12,4))
plt.bar(list(batting_second['winner'].value_counts()[0:5].keys()),list(batting_second['winner'].value_counts()[0:5]),color=['red','yellow','pink','blue',"orange"])
plt.title("MOST WINNING TEAM")
plt.xlabel("Team name")
plt.ylabel("Matches")
plt.grid()
plt.show()


# In[25]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct="%0.1f%%")
plt.show()


# In[26]:


ipl['season'].value_counts()


# In[27]:


ipl['city'].value_counts()


# In[28]:


np.sum(ipl["toss_winner"]==ipl["winner"])


# In[29]:


291/577


# In[30]:


delivery=pd.read_csv("delivery.csv")


# In[31]:


delivery.head()


# In[32]:


delivery['match_id'].unique()


# In[33]:


delivery.shape


# In[34]:


match_1=delivery[delivery["match_id"]==1]


# In[35]:


match_1.head()


# In[36]:


match_1.shape


# In[37]:


krk=match_1[match_1['inning']==1]


# In[38]:


krk['batsman_runs'].value_counts()


# In[39]:


krk["dismissal_kind"].value_counts()


# In[ ]:





# In[40]:


rcb=match_1[match_1["inning"]==2]


# In[41]:


rcb.head()


# In[42]:


rcb["batsman_runs"].value_counts()


# In[43]:


rcb["dismissal_kind"].value_counts()


# In[ ]:




