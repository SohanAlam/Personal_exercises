import streamlit as st
import pandas as pd
import time
import plotly.express as px
import yfinance as yf
import matplotlib as plt


st.write('''
#friday challenge




''')

df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")
def convert_status_to_description(x):
    if x['Index'] == 0:
        return 'Extremely Weak'
    elif x['Index'] == 1:
        return 'Weak'
    elif x['Index'] == 2:
        return 'Normal'
    elif x['Index'] == 3:
        return 'Overweight'
    elif x['Index']== 4:
        return 'Obesity'
    elif x['Index'] == 5:
        return 'Extreme Obesity'
df['Type'] = df.apply(convert_status_to_description,axis=1)
df.head()
#print(df.iloc[1])

plt.figure(figsize=(15,8))
sns.set_style("white")
sns.scatterplot( x='Weight', y='Height', data=df, hue='Type',legend=True,palette="Set1")
ax1 = plt.gca()
ax1.set_title('Weight vs Height', size=15)
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5),prop={'size': 15})










st.line_chart(df.close)
st.line_chart(df.volume)