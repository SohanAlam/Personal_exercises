#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path
sys.executable


# In[2]:




# Import needed packages
# You may add or remove packages should you need them
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import datasets
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
# Display plots inline and change plot resolution to retina
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
# Set Seaborn aesthetic parameters to defaults
sns.set()


# In[3]:


def load_data():
    #load the dataset
    #return the dataset
  data = datasets.load_iris()
  return data


# In[4]:


assert load_data()['data'].shape == (150,4)


# In[5]:


dataset = load_data()
dataset.feature_names


# In[6]:


dataset


# In[7]:


dataset.target


# In[8]:


load_data().target_names


# In[9]:


def dataset_to_pandas():
    #put the dataset into a pandas DF using the feature names as columnsç
    #rename the column name so the dont include the '(cm)'
    #add 2 columns one with the target and another with the target_names
    df = pd.DataFrame(dataset.data,columns=['sepal length', 'sepal width', 'petal length', 'petal width'])
    df['target']=dataset.target
    df['class']=dataset.target_names[dataset.target]
    #df['target_names']=load_data().target_names
    return df


# In[10]:


df = dataset_to_pandas()
assert df['sepal length'].shape == (150,)
assert df['sepal width'].shape == (150,)
assert df['petal length'].shape == (150,)
assert df['petal width'].shape == (150,)
assert df['target'].shape == (150,)
assert df['class'].shape == (150,)


# In[11]:


df


# In[12]:


ohe_data = ohe()

assert ohe_data.shape == (150,8)


# In[13]:


def target_to_numpy():
    y = ohe_data["target"].to_numpy()

    return y
 
    #raise NotImplementedError()
def data_to_numpy():
    x = ohe_data[['sepal length','sepal width']].to_numpy()
    return x


# In[ ]:


Y = target_to_numpy()
X = data_to_numpy()
assert isinstance(Y, np.ndarray)
assert isinstance(X, np.ndarray)
assert X.shape == (150,2)


# In[ ]:


X = df_iris[['sepal length', 'sepal width']].values
print(X.shape)
X[:5]


# In[ ]:


#split train and test data 80/20
#your code here
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

# YOUR CODE HERE
#raise NotImplementedError()

print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)


# In[ ]:


X_train


# In[ ]:




assert X_train.shape == (120,2)
assert Y_train.shape == (120,)
assert X_test.shape  == (30,2)
assert Y_test.shape  == (30,)


# In[ ]:


scaler = StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#Y_train=Y_train.reshape(-1,1)
#Y_train=scaler.fit_transform(Y_train)
#Y_test = Y_test.reshape(-1,1)
#Y_test = scaler.transform(Y_test)
#create and fit the scaler object on the training data
# YOUR CODE HERE
#raise NotImplementedError()

X_train[:5]


# In[ ]:


Y_Y_train[:5]train[:5]


# In[ ]:


assert np.amin(X_train) >= -2.5
assert np.amax(X_train) <= 3.2
assert np.amin(X_test) >= -2
assert np.amin(X_test) <= 2.75


# In[ ]:


#initalize and fit with Logistic Regression
model_standard = LogisticRegression()
#model_standard
model_standard.fit(X_train,Y_train)

predictions = model_standard.predict(X_test)


#initalize the logistic regressor
#make predictions

#raise NotImplementedError()


# In[ ]:


#evaluating the performace of our first model
score = accuracy_score(Y_test,predictions)
#raise NotImplementedError()
score


# In[ ]:




assert score >=0.7


# In[ ]:


assert score >=0.72


# In[ ]:


assert score >=0.73


# In[ ]:


#model with cross validation
model_cross = LogisticRegression()
#kf = KFold(n_splits = 5, shuffle = True)
#cross validate the training set
cv = cross_validate(model_cross,X_train,Y_train,cv=5)
# YOUR CODE HERE
#raise NotImplementedError()

def print_scores(cv):
    #print out cross validation scores
    [print('Crossvalidation fold: {}  Accruacy: {}'.format(n, score)) for n, score in enumerate(cv['test_score'])]
    #print out the mean of the cross validation
    print('Mean train cross validation score {}'.format(cv['test_score'].mean()))
    
print_scores(cv)


# In[ ]:


assert len(cv['test_score']) == 5
assert max(cv['test_score']) >= 0.85
assert min(cv['test_score']) >= 0.69
assert cv['test_score'].mean() >= 0.77


# In[ ]:


#define the scaler
#define the classifier
#make the pipeline
#run the cross validation
#print results
scaler = preprocessing.StandardScaler()
classifier = LogisticRegression()
pipe = make_pipeline(scaler,classifier)
cv = cross_validate(pipe,X_train,Y_train,cv=5)
print_scores(cv)
#raise NotImplementedError()


# In[ ]:


assert type(pipe) == type(make_pipeline(scaler, classifier))
assert len(cv['test_score']) == 5
assert max(cv['test_score']) >= 0.83
assert min(cv['test_score']) >= 0.69
assert cv['test_score'].mean() >= 0.74


# In[ ]:




