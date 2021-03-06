# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here
p_a = df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
print(p_a)
p_b = df[df['purpose'] == 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)
df1 = df[df['purpose'] == 'debt_consolidation']
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
print(p_a_b)
result = (p_a_b == p_a)
print(result)
new_df = df[df['paid.back.loan'] == 'Yes']
prob_lp = new_df.shape[0]/df.shape[0]
print(prob_lp)
prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]/df.shape[0]
print(prob_cs)
prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]
bayes = (prob_pd_cs * prob_lp)/ prob_cs
print(bayes)
df1 = df[df['paid.back.loan'] == 'No']
print(df1.shape)
df1['purpose'].value_counts().plot(kind="bar")
inst_median = df['installment'].median()
print(inst_median)
inst_mean = df['installment'].mean()
print(inst_mean)
df['installment'].hist(normed = True, bins=50)



