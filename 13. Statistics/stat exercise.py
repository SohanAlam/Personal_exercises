#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
import numpy 


# In[4]:


beers = pandas.read_csv("C:\\practice_september\\Personalexercises_september\\13. Statistics\\Part 1\\data\\beers.csv")


# In[5]:


beers


# In[46]:


abv_s = beers['abv']
#ibu_s = beers['ibu']


# In[12]:


#ibu_s


# In[22]:


ibu_null =pandas.isnull(ibu_s)
abv_null =pandas.isnull(abv_s)


# In[32]:


ibu_null


# In[69]:


ibu_new=ibu_s.dropna()
abv_new=abv_s.dropna()


# In[50]:


abv_new


# In[53]:


variance_cal = abv_new.to_numpy()


# In[54]:


variance_cal


# In[56]:


variance_cal1 = variance_cal.var()


# In[59]:


variance_cal1


# In[63]:


standard_deviation = variance_cal1 * variance_cal1


# In[64]:


standard_deviation


# In[65]:


from matplotlib import pyplot
get_ipython().run_line_magic('matplotlib', 'inline')

#Import rcParams to set font styles
from matplotlib import rcParams

#Set font style and size 
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16


# In[68]:


#You can set the size of the figure by doing:
pyplot.figure(figsize=(10,5))

#Plotting
pyplot.hist(abv_new, bins=20, color='#3498db', histtype='bar', edgecolor='white') 
#The \n is to leave a blank line between the title and the plot
pyplot.title('abv_new')
pyplot.xlabel('Alcohol by Volume (abv_new) ')
pyplot.ylabel('Frequency');


# In[70]:


#You can set the size of the figure by doing:
pyplot.figure(figsize=(10,5))

#Plotting
pyplot.hist(ibu_new, bins=20, color='#e67e22', histtype='bar', edgecolor='white') 
#The \n is to leave a blanck line between the title and the plot
pyplot.title('ibu \n')
pyplot.xlabel('International Bittering Units (ibu)')
pyplot.ylabel('Frequency');


# In[ ]:




