'''from matplotlib import pyplot
get_ipython().run_line_magic('matplotlib', 'inline')

#Import rcParams to set font styles
from matplotlib import rcParams

#Set font style and size 
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16'''


ibu_null =pandas.isnull(ibu_s)
abv_null =pandas.isnull(abv_s)


# In[32]:


ibu_null


# In[69]:


ibu_new=ibu_s.dropna()
abv_new=abv_s.dropna()