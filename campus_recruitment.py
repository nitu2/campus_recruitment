from matplotlib import legend
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core import groupby
from pandas.core.frame import DataFrame
import seaborn as sns
from seaborn.palettes import color_palette
from six import viewvalues

data = pd.read_csv("C:/Users/1752144/Desktop/python practice/Data analysis projects/Campus recruitment/archive/Placement_Data_Full_Class.csv")
print(data.head())
#serial number column not required
data = data.drop('sl_no', axis=1)
#renaming columns
data_tidy = data.rename(columns= {'ssc_b' :'ssc_board', 'hsc_b': 'hsc_board','hsc_s': 'hsc_stream', 'degree_t': 'degree_tech', 'workex':'work_exp'})
#print(data_tidy.head())
#print(data_tidy.describe())
print(data_tidy.isnull().sum())
data_tidy['salary'].fillna(0, inplace=True)

data_tidy['status'].replace('Placed',1, inplace= True)
data_tidy['status'].replace('Not Placed', 0, inplace= True)
print(data_tidy.info())

sns.heatmap(data_tidy.corr(), annot=True)
plt.show()

# From heatmap it is clear that Etest and MBA percentage does not affect much placement results.

group_gender = pd.DataFrame(data_tidy.groupby(['gender', 'status'])['status'].count())
print(group_gender)
# gender status status
# F 0 28
# 1 48
# M 0 39
# 1 100
pie_df = pd.DataFrame(data_tidy.groupby('gender')['gender'].count())
plt.pie(pie_df['gender'], autopct='%.0f%%',explode = (0, 0.1),shadow=True, labels=['Female', 'Male'])
plt.show()

#status summary
sns.countplot(data_tidy['status'], palette='PuBu')
plt.grid(True)
plt.show()

#status and gender
sns.countplot(data_tidy['status'],hue= data_tidy['gender'] ,palette='PuBu')
plt.grid(True)
plt.show()

fig, axes = plt.subplots(3,2, figsize = (20,10))
sns.barplot(x='status',y='ssc_p',data = data_tidy, palette='PuBu', ax=axes[0][0])
sns.barplot(x='status',y='hsc_p',data = data_tidy,palette='PuBu', ax=axes[0][1])
sns.barplot(x='status',y='degree_p',data = data_tidy,palette='PuBu', ax=axes[1][0])
sns.barplot(x='status',y='etest_p' ,data = data_tidy,palette='PuBu', ax=axes[1][1])
sns.barplot(x='status',y='mba_p',data = data_tidy,palette='PuBu', ax=axes[2][0])
fig.delaxes(ax = axes[2][1])
plt.show()

sns.catplot(x='status', y='ssc_p', data = data_tidy, palette='PuBu')
sns.catplot(x='status', y='hsc_p', data = data_tidy, palette='PuBu')
sns.catplot(x='status', y='degree_p', data = data_tidy, palette='PuBu')
sns.catplot(x='status', y='etest_p', data = data_tidy, palette='PuBu')
sns.catplot(x='status', y='mba_p', data = data_tidy, palette='PuBu')
plt.show()

#workexperience relation with status
pie_df = pd.DataFrame(data_tidy.groupby('work_exp')['work_exp'].count())
plt.pie(pie_df['work_exp'], autopct='%.0f%%',shadow=True, labels=['Yes', 'No'])
plt.show()

sns.countplot(data_tidy['status'],hue= data_tidy['work_exp'] ,palette='PuBu')
plt.grid(True)
plt.show()

print(pd.DataFrame(data_tidy.groupby(['work_exp', 'status'])['status'].count()))
# work_exp status status
# No 0 57
# 1 84
# Yes 0 10
# 1 64
#Signifiance of Specialization

print(pd.DataFrame(data_tidy.groupby(['specialisation', 'status'])['status'].count()))
sns.barplot(x='specialisation', y='status', data = data_tidy, palette='PuBu')
plt.grid(True)
plt.show()
# specialisation status status
# Mkt&Fin 0 25
# 1 95
# Mkt&HR 0 42
# 1 53

sns.countplot(data_tidy['status'], hue= data_tidy['specialisation'],palette='PuBu')
plt.grid(True)
plt.show()

#Significance of Boards and Streams
fig, axes = plt.subplots(2,2, figsize = (20,10))
sns.barplot(x='status',y='ssc_board',data = data_tidy, palette='PuBu', ax=axes[0][0])
sns.barplot(x='status',y='hsc_board',data = data_tidy,palette='PuBu', ax=axes[0][1])
sns.barplot(x='status',y='hsc_stream',data = data_tidy,palette='PuBu', ax=axes[1][0])
sns.barplot(x='status',y='degree_tech' ,data = data_tidy,palette='PuBu', ax=axes[1][1])
#fig.delaxes(ax = axes[2][1])
plt.show()

#We can see here that there is not significant difference between selecting board in SSC or HSC will help you getting placed

#HSC Streams
sns.countplot(data_tidy['status'], hue= data_tidy['hsc_stream'], palette='PuBu')
plt.grid(True)
plt.show()

#Degree
sns.countplot(data_tidy['status'], hue= data_tidy['degree_tech'], palette='PuBu')
plt.grid(True)
plt.show()

#Commerce stream and Comm & management in Degree students is most beneficial to opt for.
#Science students are also getting placed but less than commerce but more than Arts.

#Result:
#Class 10 and class 12 percentage should be greater than 60% from any board
# You should have opted for commerce in HSC (science will also work)
# Degree from Commerce and managemnet will help you (Science and Tech will also work)
# Having work experience is like strawberry on cake. Students having work experience are more likley to get placed