# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
data['Gender'].replace('-','Agender',inplace = True)
data['Gender'].value_counts().plot(kind='bar')
data['Alignment'].value_counts().plot(kind = 'bar')
data['Combat'].corr(data['Intelligence'])
data['Combat'].corr(data['Strength'])
data['Total'].quantile(.99)
best = data[data['Total'] > 554.05]
best.head()
super_best_names = best['Name'].tolist()
print(super_best_names)



