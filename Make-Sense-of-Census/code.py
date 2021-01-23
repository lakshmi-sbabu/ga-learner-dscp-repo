# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census = np.concatenate((data,new_record))
#Code starts here
print(census.shape)
print(data.shape)
age= census[:,0]
print(age)
max_age=age.max()
min_age=age.min()
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)
race=census[:,2]
race_0=race[race==0]
print(race_0)
race_1=race[race==1]
race_2=race[race==2]
race_3=race[race==3]
race_4=race[race==4]

len_0 = np.size(race_0)
len_1=np.size(race_1)
len_2=np.size(race_2)
len_3=np.size(race_3)
len_4=np.size(race_4)
print(len_0,len_1,len_2,len_3,len_4)
racesize= np.array([len_0,len_1,len_2,len_3,len_4])
minority_race= np.argmin(racesize)
print(minority_race)

senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=high[:,7].mean()
avg_pay_low=low[:,7].mean()
print(avg_pay_high)
print(avg_pay_low)
print(avg_pay_high==avg_pay_low)




