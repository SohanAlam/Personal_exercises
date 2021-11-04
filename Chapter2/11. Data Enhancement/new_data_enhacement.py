import numpy    as np
import pandas   as pd
import matplotlib.pyplot as plt
import sklearn  as skl

import time

from sklearn import pipeline      # Pipeline
from sklearn import preprocessing # OrdinalEncoder, LabelEncoder
from sklearn import impute
from sklearn import compose
from sklearn import model_selection # train_test_split
from sklearn import metrics         # accuracy_score, balanced_accuracy_score, plot_confusion_matrix
from sklearn import set_config
from sklearn.preprocessing import StandardScaler

from sklearn.tree          import DecisionTreeRegressor
from sklearn.ensemble      import RandomForestRegressor
from sklearn.ensemble      import ExtraTreesRegressor
from sklearn.ensemble      import AdaBoostRegressor
from sklearn.ensemble      import GradientBoostingRegressor
from xgboost               import XGBRegressor
from lightgbm              import LGBMRegressor
from catboost              import CatBoostRegressor

data = pd.read_csv(r'data\london_merged.csv')

np.random.seed(0)

#checking for NaN values
#print(data.isnull().sum()) #no null values

data['hour'] = data['timestamp'].apply(lambda row: row.split(':')[0][-2:]) #Addition of feature

X = data.drop(['cnt','timestamp'],axis=1)  # splitting the feature value from csv
y = data['cnt']                       # splitting the target values from csv

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2,random_state=0) # train_test_split

X_train['cnt'] = y_train

def enhancement(train,deviation):
    gen_data = train.copy()
    for season in train['season'].unique():
        seasonal_data = gen_data[gen_data['season'] == season]
        hum_std = seasonal_data['hum'].std()
        windspeed_std = seasonal_data['wind_speed'].std()
        t1_std = seasonal_data['t1'].std()
        t2_std = seasonal_data['t2'].std()

        for row in train[train['season']==season].index:

            if np.random.randint(2) == 1:
                gen_data.loc[row,'hum'] += hum_std/deviation
            else:
                gen_data.loc[row,'hum'] -= hum_std/deviation

            if np.random.randint(2) == 1:
                gen_data.loc[row,'wind_speed'] += windspeed_std/deviation
            else:
                gen_data.loc[row,'wind_speed'] -= windspeed_std/deviation 

            if np.random.randint(2) == 1:
                gen_data.loc[row,'t1'] += t1_std/deviation
            else:
                gen_data.loc[row,'t1'] -= t1_std/deviation

            if np.random.randint(2) == 1:
                gen_data.loc[row,'t2'] += t2_std/deviation
            else:
                gen_data.loc[row,'t2'] -= t2_std/deviation
            
        return gen_data

#print(X.head())
#print(y.head())

X_new = enhancement(X_train,8).sample(X_train.shape[0]//4)


X_train = pd.concat([X_train, X_new.drop(['cnt'], axis=1 ) ]) # merge the new x values in original X_train
y_train = pd.concat([y_train, X_new['cnt'] ])                   # merge the new y values in original y_train

# generating a new feature in a new column
X_train['t1t2'] = (X_train['t1']+X_train['t2'])/2  # mean of actual temperature t1 and feels like t2
X_test['t1t2'] = (X_test['t1']+X_test['t2'])/2      # mean of actual temperature t1 and feels like t2
X_train, X_test = X_train.drop(['t1','t2'], axis=1), X_test.drop(['t1','t2'], axis=1)    

# print(X_train.head())
# print(X_test.head())

cat_vars = ['season','is_weekend','is_holiday','hour','weather_code']
num_vars = ['t1t2','hum','wind_speed']

tree_classifiers = {
  "Decision Tree": DecisionTreeRegressor(),
  "Random Forest": RandomForestRegressor(n_estimators=100),
  "AdaBoost":      AdaBoostRegressor(n_estimators=100),
  "Skl GBM":       GradientBoostingRegressor(n_estimators=100),
  "CatBoost":      CatBoostRegressor(n_estimators=100),
  "XGBoost":       XGBRegressor(n_estimators=100),
  "LightGBM":      LGBMRegressor(n_estimators=100),
}

rang = abs(y_train.max()) + abs(y_train.min())

num_features = pipeline.Pipeline(steps=[('standard', StandardScaler()),])

cat_features = pipeline.Pipeline(steps=[('ordinal', preprocessing.OrdinalEncoder())])

tree_prepro = compose.ColumnTransformer(transformers=[('num', num_features, num_vars),('cat', cat_features, cat_vars),], remainder='drop')

tree_classifiers = {name: pipeline.make_pipeline(tree_prepro, model) for name, model in tree_classifiers.items()}

results = pd.DataFrame({'Model': [], 'MSE': [], 'MAB': [], " % error": [], 'Time': [], 'Explained_variance': [], "R2-score": []})


for model_name, model in tree_classifiers.items():
    start_time = time.time()
    model.fit(X_train, y_train)
    total_time = time.time() - start_time

    y_pred = model.predict(X_test)

    results = results.append({"Model": model_name,"MSE": metrics.mean_squared_error(y_test, y_pred),"MAB": metrics.mean_absolute_error(y_test, y_pred)," % error": metrics.mean_squared_error(y_test, y_pred) / rang,"R2-score": metrics.r2_score(y_test,y_pred),"Time": total_time,"Explained_variance": metrics.explained_variance_score(y_test, y_pred),},ignore_index=True)   

print(results) # Catboost is among the best model because of less time, high explained_variance & R2-score