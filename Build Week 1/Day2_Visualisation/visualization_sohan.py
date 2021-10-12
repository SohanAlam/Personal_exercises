import pandas as pd
import numpy as np
import seaborn as sns

import csv
data =pd.read_csv('normalized_100_books_sohan.csv')
print(data)

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

