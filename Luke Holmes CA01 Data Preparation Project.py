#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:





# In[20]:


#Uploading the dataset and giving ity a shortcut name 'AFS'
data = pd.read_csv('aps_failure_set.csv')
afs=pd.read_csv('aps_failure_set.csv')


# In[21]:


# Display the first 5 records
afs.head()


# In[29]:


#Display the first 10 rows of the dataset
data.head(10)


# In[28]:


#Requesting basic info on the dataset
data.info()


# In[27]:


#Basic Statistical Information on the dataset
data.describe()


# In[25]:


afs.isnull().sum()


# In[ ]:




