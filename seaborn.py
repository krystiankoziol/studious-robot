# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

# Rozdzienienie na DF po kolumnie jako słowniki
def groupby_column(df, column):
  gb = df.groupby(column)
  result = {g: gb.get_group(g) for g in gb.groups}
  return result

def analyze_medals(medal_df):
  teams = groupby_column(medal_df, 'Country')
  ret = {}
  for country, country_df in teams.items():
    counts = country_df['Medal'].value_counts()
    gold = counts['Gold'] if 'Gold' in counts else 0
    silver = counts['Silver'] if 'Silver' in counts else 0
    bronze = counts['Bronze'] if 'Bronze' in counts else 0
    ret[country] = (gold, silver, bronze)

  return ret

#%%
wine = pd.read_csv('Data/wine.csv')

print (wine.sample(10))


#%%
sns.lmplot(data=wine, x='Total phenols', y='Alcalinity of ash', fit_reg =False, hue='Class')
plt.show()
#%%
ax = sns.boxplot(data = wine.loc[:,'Alcohol':'Magnesium'])
ax.set_title('Tytuł')
plt.show()

#%%
ax = sns.violinplot(x = 'Class', y = 'Alcohol', data= wine)
ax.set_title('Tytuł')
plt.show()

#%%
population = pd.read_csv('Data/population.csv',index_col='City')
print(population.head())

sexes = groupby_column(population,'Sex')

both= sexes['Both Sexes']

ax = sns.barplot(x=both.index, y='Value', data=both)
ax.xaxis.set_tick_params(rotation =90)

plt.show()
#%%
olimpic = pd.read_csv('Data/medals.csv',index_col='Year')

medals= pd.DataFrame.from_dict(analyze_medals(olimpic), orient='index', columns=['Gold','Sliver','Bronze'])
medals_top = medals.sort_values(by=['Gold', 'Sliver','Bronze'],ascending=False)[:500]
print(medals_top.head(10))

medals_top = medals_top.reset_index()
print(medals_top.head(10))

melted_df = pd.melt(medals_top,  id_vars = 'index',  var_name = 'stat')
print(melted_df.head())

ax = sns.barplot( x = 'index', y= 'value', data=melted_df, hue='stat')
plt.legend(bbox_to_anchor=(1,1),loc=1)
plt.show()
#%%
print(population.head(10))
#%%
population=population.reset_index()
sexes = groupby_column(population,'Sex')

male_df = sexes['Male']
print(male_df.head(10))

#%%
#male_df.head(10)
female_df = sexes['Female']
male_df = male_df.nlargest(5,'Value').loc[:,'City':'Value']
female_df = female_df.nlargest(5,'Value').loc[:,'City':'Value']
print(male_df.head(10))
#female_df.head(10)

#%%
cars = pd.read_csv('Data/auto_mpg.csv', na_values='?')
print(cars.head())
ax= sns.pairplot(cars)
plt.show()
#%%
iris=pd.read_csv('Data/iris.csv')
iris.head()

ax= sns.pairplot(iris,hue='species')
plt.show()

print(iris.median())

#%%
ax= sns.pairplot(wine ,hue='Class')
plt.show()


