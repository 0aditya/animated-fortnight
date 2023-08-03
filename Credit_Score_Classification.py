#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("C:\\Users\\ak269\\OneDrive\\Desktop\\train.csv")


# # Checking Null Values

# In[5]:


if data.isnull().sum().any():
    data = data.dropna()


# In[6]:


import plotly.express as px


# In[42]:


for i in column[6:27]:
    fig = px.box(data, x="Credit_Score", y = i, color="Credit_Score", title=f"Credit Scores Based on {i}", 
             color_discrete_map={'Poor':'red', 'Standard':'yellow', 'Good':'green'})
    fig.update_traces(quartilemethod="exclusive")
    fig.show()


# In[ ]:




