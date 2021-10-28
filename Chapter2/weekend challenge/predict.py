# import libraries for cmd
from os import error
import data_handler as dh
import numpy as np
import pandas as pd
from joblib import load
import argparse

model = load('./data/best_model.joblib')
scaler = load('./data/scaler.joblib')

features = ['age','sex','cp','trtbps','chol','fbs','restecg','thalachh','exng','oldpeak','slp','caa','thall']
# features_dic = {'age':'age', 'sex':'sex', 'cp':'Chest Pain type', 'trtbps':'Resting blood pressure (in mm Hg)',\
#     'chol':'Cholestoral in mg/dl fetched via BMI sensor','fbs':'(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)',\
#         'restecg':'Resting electrocardiographic results','thalachh':'maximum heart rate achieved',\
#             'exng':'Exercise induced angina (1 = yes; 0 = no)','oldpeak':'oldpeak','slp':'slp','caa':'caa','thall':'thall'}

parser = argparse.ArgumentParser()
for item in features:
    parser.add_argument(item, type=float, help=item)

args = parser.parse_args()
x_features = [args.age,args.sex,args.cp,args.trtbps,args.chol,args.fbs,args.restecg,args.thalachh,\
    args.exng,args.oldpeak,args.slp,args.caa,args.thall]

# no_of_arg = len(vars(args))
# expected_no_of_arg = len(features) + 1

# if no_of_arg != expected_no_of_arg:
#     error('Your passed {} arguments, must be {}'.format(no_of_arg, expected_no_of_arg))


# get and transform data
data = np.array(x_features).reshape(1, -1)
data = scaler.transform(data)


#predict with saved model
prediction = model.predict(data)

decisition = {1:'You have Heart Attack', 0:'You don\'t have Heart Attack'}
print("\n{}\n".format(decisition[int(prediction[0])]))

