#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install ggplot==0.4.7


# In[2]:


get_ipython().system('pip install plotnine')


# In[3]:


# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


#Reading the dataset
data = pd.read_csv(r"C:\Users\yashwanth moparthi\Desktop\Recruitment_data.csv")


# In[5]:


#Evaluating top 5 values in the dataset
data.head()


# In[6]:


#Checking data-types of the data
data.dtypes


# In[7]:


#Checking values in the particular column
data['recruiting_source']


# In[8]:


data['sales_quota_pct']


# In[9]:


#Getting the average Sales Number grouped by Recruiting Source
n_by_recsrc = data.groupby("recruiting_source")["sales_quota_pct"].mean()


# In[10]:


n_by_recsrc.head()


# In[11]:


#Getting  the average Attrition Number grouped by Recruiting Source
n_by_attr = data.groupby("recruiting_source")['attrition'].mean()


# In[12]:


#Checking top mean values.
n_by_attr.head()


# In[13]:


#Importing Plotnine for ggplot.
get_ipython().run_line_magic('matplotlib', 'inline')
import plotnine as p9


# In[16]:


#Visualizing recruiting_source and sales_quota_pct using ggplot.
(p9.ggplot(data=data))
(p9.ggplot(data=data, mapping=p9.aes(x ='recruiting_source',
                                     y='sales_quota_pct')) 
    + p9.geom_col()
)


# In[15]:


#Visualizing recruiting_source and attriton using ggplot.
(p9.ggplot(data=data))
(p9.ggplot(data=data, mapping=p9.aes(x ='recruiting_source',
                                     y='attrition')) 
    + p9.geom_col()
)


# In[ ]:




