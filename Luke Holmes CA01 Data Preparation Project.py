#!/usr/bin/env python
# coding: utf-8

# In[144]:


import pandas as pd
import matplotlib.pyplot as plt #visualisation
import seaborn as sns #visualisation
import numpy as np 


# Here I have loaded the dataset. To save myself from typing 'aps_failure.csv' every single time I have given the dataset a simplfied name 'afs'. Line 1 below tells the program where the data is while line 2 renames it for ease of use. 

# In[145]:


data = pd.read_csv('aps_failure_set.csv')
afs=pd.read_csv('aps_failure_set.csv')


# Exploratory Analysis. 
# I am gathering some very basic information on my datset so I know what I'm dealing with. I start this process with gathering basic information 

# In[146]:


afs.shape


# The afs.shape above has told me I am dealing with a datset that has 171 columns and 60,000 rows. I will now use the afs.describe(include=object) function to provide me with some basic statistics on the data. This is useful for the following reasons:
# 
# -Count shows me that
# -Unique showes me that
# -Top shows me that
# -Freq shows me that

# In[147]:


afs.describe(include=object)


# Now I begin to view the data. data.head(10) gives me the first 10 rows of the data.
# 
# This allows me to get an understanding of what I am actually dealing with. It is a good way

# In[148]:


# Display the first 5 records
afs.head(5)


# In[149]:


afs.tail(5)


# In[150]:


print(afs.columns)


# Checking the data type

# In[151]:


afs.info


# In[ ]:





# As the 'neg' column is not applicable to this project, I will remove them from the data set before I explore any further. "The dataset’s  positive class consists of component failures for a specific component of the APS system.
# The negative class consists of trucks with failures for components not related to the APS." This data is unrelated and therefore not useful for my project. Firstly, I will change the data

# In[ ]:





# COoe source: https://www.w3docs.com/snippets/python/deleting-dataframe-row-in-pandas-based-on-column-value.html

# In[ ]:





# In[164]:


afs = afs.drop(afs[afs['class'] == 'neg'].index)


# In[165]:





# In[168]:


print("Negative count:", neg_count)


# This confirms that all 'neg' values have been dropped. Source: - See method 2 'Using the drop function' https://saturncloud.io/blog/how-to-remove-rows-with-specific-values-in-pandas-dataframe/#:~:text=Another%20method%20to%20remove%20rows,value%20we%20want%20to%20remove

# In[156]:


afs.describe(include=object)
print(afs)


# Above I have ran the neg_count function to ensure that the negitive values were dropped. I then ran the describe function to confirm that the value of "class" is now "1" instead of two. Source: https://www.w3docs.com/snippets/python/deleting-dataframe-row-in-pandas-based-on-column-value.html
# 
# 

# I need to get rid of the n/a in the ab_00 column. Below I will experiment with different strategies to do this. Forst, I will explore the classification and regression of the dataset. For this project, I will use multiclass classification. 

# In[157]:


afs.shape


# In[158]:


#Requesting basic info on the dataset
data.info()


# Basic Statistical Information on the dataset
# 

# In[159]:


data.describe()


# I am checking the code for blank data. Note for myself- add in why this is important from lecture notes

# In[160]:


afs.isnull().sum()


# In[161]:


print(afs.isnull().values.any())


# In[162]:


afs["class"].value_counts().sort_index()


# I have notcied my first issue with the data. I have 59,000 data points for negative and only 1000 for posiitve. The code column contains two attributes, negative (neg) and positive (pos). I will change these to numercal values so I can count them. neg=0, pos=1... Source: https://inria.github.io/scikit-learn-mooc/python_scripts/03_categorical_pipeline.html

# In[ ]:





# In[ ]:





# In[169]:


# Displaying the first few rows of the 'class' column and its distribution
(data['class'].head(), data['class'].value_counts(normalize=True))


# This indicates that my dataset has no missing values or invalid data types. This is a good sign as my data is 'complete' and no further action is required. 

# Now I will begin to visualise my data using seaborne. 

# In[ ]:




