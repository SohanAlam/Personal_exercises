#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


import csv
data =pd.read_csv('C:\\practice_september\\Personalexercises_september\\Build Week 1\\Day4\\merged.csv')
data


# In[ ]:





# In[171]:


# converting missing value to 0

data2= data.replace(np.NAN, 0, inplace=True)


# In[172]:


data


# In[173]:


#removing the books of no pages
df = data[data.num_pages != 0]


# In[174]:


df


# In[175]:


#counting awards
df1 = df.assign(Awards=df.awards.str.count(','))
df1


# In[176]:


df1.replace(np.NAN, 0, inplace=True)


# In[177]:


df1


# In[178]:


df1.drop("awards",'columns')


# In[179]:


df2['genres'] = df1['genres'].str.replace('>',',')


# In[180]:


df2


# In[181]:


df2.to_csv('normalized_books_final_.csv')


# In[ ]:





# In[166]:


from sklearn.preprocessing import MinMaxScaler


# In[167]:


scaling = MinMaxScaler()
reviews = scaling.fit_transform(df2[['num_reviews']])
ratings1 = scaling.fit_transform(df2[['num_ratings']])
ratings = scaling.fit_transform(df2[['avg_rating']])


# In[152]:


df2["Reviews"]=reviews
df2["Total_ratings"]=ratings1
df2["Average_rating"]=ratings
df2


# In[ ]:





# In[159]:


column_names = ['Unnamed: 0','title','author','Reviews','Total_ratings','Average_rating','num_pages','publish_year','first_published','series','genres','Awards','url']

df3 = df2.reindex(columns=column_names)


# In[160]:


df3


# In[154]:


df2.to_csv('normalized_books_final.csv',dtype=object)


# In[155]:


df2


# In[118]:


df3 = z.groupby(['Awards']).mean()
df3


# In[ ]:





# In[107]:



#Year vs total rating curve

import matplotlib.pyplot as plt
reviews= z['Reviews'].to_list()
total_rating= z['Total_ratings'].to_list()
avg_rating= z['Average_rating'].to_list()
pages= z['num_pages'].to_list()
year= z['original_publish_year'].to_list()
#print(x)
#print(y)
plt.figure(figsize=(10, 8))
plt.plot(year,total_rating, 'o:r', marker='o', mec='r', mfc='k', linewidth='3')
plt.xlabel("Publishing Year")
plt.ylabel("Rating")
plt.legend(["Rating vs Year"], loc ="lower right")
plt.show()


# In[112]:



#Page vs Reviews


plt.figure(figsize=(10, 8))
plt.scatter(pages,reviews)
plt.xlabel("Number of pages")
plt.ylabel("Reviews")
plt.legend(["Page vs Reviews"], loc ="upper right")
plt.show()


# In[121]:


plt.figure(figsize=(10, 10))
plt.plot(avg_rating,total_rating,label="Average ratings dependency on Total rating ", color='b', marker='o', ms='10' )
plt.legend(loc ="upper left")
plt.xlabel("average ratings")
plt.ylabel("total ratings")
plt.grid()
plt.show()


# In[ ]:




