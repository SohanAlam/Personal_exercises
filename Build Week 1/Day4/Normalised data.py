#!/usr/bin/env python
# coding: utf-8

# In[167]:


import os
import pandas as pd
import numpy as np


# In[168]:


import csv
data =pd.read_csv('C:\\practice_september\\Personalexercises_september\\Build Week 1\\Day4\\final_2.csv')
data


# In[169]:


data['first_published'] = data['publish_year'].fillna(data['first_published'])


# In[170]:


data


# In[171]:


data.replace(np.NaN, 0, inplace=True)


# In[172]:


data


# In[173]:


data = data[data.first_published != 0]
data


# In[174]:


data.drop(["publish_year"], axis=1)


# In[175]:


from sklearn.preprocessing import MinMaxScaler


# In[176]:


scaling = MinMaxScaler()
reviews = scaling.fit_transform(data[['num_reviews']])
ratings1 = scaling.fit_transform(data[['num_ratings']])
ratings = scaling.fit_transform(data[['avg_rating']])


# In[177]:


data["Reviews"]=reviews
data["Total_ratings"]=ratings1
data["Average_rating"]=ratings
data


# In[178]:


column_names = ['Unnamed: 0','title','author','Reviews','Total_ratings','Average_rating','num_pages','publish_year','series','genres','awards','places','url','awards_count']

df3 = data.reindex(columns=column_names)


# In[179]:


df3['genres'] = df3['genres'].str.replace('>',',')


# In[180]:


df3


# In[181]:


#f3.to_csv'normalized_books_final.csv',float_format=None)


# In[185]:


df = df3.to_csv('final_7.csv',sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)


# In[ ]:





# In[186]:


df.dtypes



#path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=Non

