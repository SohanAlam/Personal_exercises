import time

import pandas as pd
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, \
    GradientBoostingClassifier, HistGradientBoostingClassifier
from sklearn import metrics, model_selection
import itertools

from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

dataset = pd.read_csv('./dataset_halfSecondWindow.csv')
dataset = dataset.iloc[:, 5:]
for name,col in zip(dataset.columns,dataset.isnull().sum()/dataset.shape[0]):
    if col>0.7:
        dataset.drop(name,axis=1, inplace=True)

for col in dataset.columns.to_list():
    for comp_col in dataset.columns.to_list():
        if col != comp_col and ((dataset[col]==dataset[comp_col]).sum()+dataset[col].isnull().sum())==dataset.shape[0]:
            dataset.drop(col,axis=1, inplace=True)
            break

#Find out which users combination is the best
"""
stuff = dataset['user'].unique()
groups_users=[]
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        if len(subset)==4 and 'U1' not in subset:
            groups_users.append(subset)
            
best_group = None
best_test_acc = 0
"""
groups_users=[['U2','U11','U5','U9']]



for group in groups_users:
    try:
        train, test = dataset[~dataset['user'].isin(group)],dataset[dataset['user'].isin(group)]

        """
        data_prev = train
        Q1 = train.quantile(0.25)
        Q3 = train.quantile(0.75)
        IQR = Q3 - Q1
        train_out = data_prev[~((data_prev < (Q1 - 1.5 * IQR)) | (data_prev > (Q3 + 1.5 * IQR))).any(axis=1)]
        """
        train_out = train #if we dont drop the outliers

        train_out.fillna(train_out.mean(), inplace=True)
        test.fillna(train_out.mean(), inplace=True)

        x_train, y_train = train_out.drop(['user','target'], axis=1), train_out['target']
        x_test, y_test = test.drop(['user','target'], axis=1), test['target']

        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)
        encoder = LabelEncoder()
        y_train = encoder.fit_transform(y_train)
        y_test = encoder.transform(y_test)

        tree_classifiers = {
            #"Decision Tree": DecisionTreeClassifier(),
            "Extra Trees": ExtraTreesClassifier(n_estimators=100),
            "Random Forest": RandomForestClassifier(n_estimators=100),
            #"AdaBoost": AdaBoostClassifier(n_estimators=100),
            #"Skl GBM": GradientBoostingClassifier(n_estimators=100),
            #"Skl HistGBM": HistGradientBoostingClassifier(max_iter=100),
            #"XGBoost": XGBClassifier(n_estimators=100),
            "LightGBM": LGBMClassifier(n_estimators=100),
            "CatBoost": CatBoostClassifier(n_estimators=100),
        }

        #skf = model_selection.StratifiedKFold(n_splits=10, shuffle=True, random_state=0)

        results = pd.DataFrame({'Model': [], 'Accuracy': [], 'Bal Acc.': [],"Test acc":[], 'Time': []})

        for model_name, model in tree_classifiers.items():
            start_time = time.time()
            #pred = model_selection.cross_val_predict(model, x_train, y_train, cv=skf)
            model.fit(x_train, y_train)
            pred_test = model.predict(x_test)
            total_time = time.time() - start_time

            results = results.append({"Model": model_name,
                                      #"Accuracy": metrics.accuracy_score(y_train, pred) * 100,
                                      #"Bal Acc.": metrics.balanced_accuracy_score(y_train, pred) * 100,
                                      "Test acc": metrics.balanced_accuracy_score(y_test, pred_test) * 100,
                                      "Time": total_time},
                                     ignore_index=True)

    except:
        pass

print(f'Best combination: {best_group} with an accuracy of {best_test_acc}')