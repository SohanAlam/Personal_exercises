import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer


def get_data(pth):

    data = pd.read_csv(pth)
    x_train, x_test, y_train, y_test = train_test_split(data.values[:,:-1], data.values[:,-1], test_size=0.2, random_state = 0)
    
    return x_train, x_test, y_train, y_test

# def transform(data):

#     ordinal_id = [1,4,5]
#     ct = ColumnTransformer( [('ordinal', OrdinalEncoder(handle_unknown= 'use_encoded_value', unknown_value = -1), ordinal_id )] )
#     data[:,ordinal_id] = ct.fit_transform(data)
    
#     return data