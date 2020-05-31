# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:04:05 2020

@author: tinal
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option('display.max.columns', None)
pd.set_option('display.precision', 2)

df18 = pd.read_csv('2018.csv')
df19 = pd.read_csv('2019.csv')

df18.info()
df19.info()


df18.shape
df19.shape


df18.head()
df19.head()


df18.describe(include=np.object)
df19.describe(include=np.object)


df18['Region'].value_counts()
df19['Region'].value_counts()

# 2018 - Sub-Saharan Africa has 39 countries
# Latin America and Caribbean has 22 countries

# 2019 - Sub-Saharan Africa has 40 countries
# Latin America and Caribbean has 21 countries

df18.axes
 
# Data Cleaning
# Checking if there are different countries in both years
unique_countries = df18[~df18.Country.isin(df19.Country)].append(df19[~df19.Country.isin(df18.Country)], ignore_index=True)

print(unique_countries)

# Removing unique countries in 2018
df18.drop(df18.index[48],inplace=True)
df18.drop(df18.index[88],inplace=True)
df18.drop(df18.index[136],inplace=True)
df18.drop(df18.index[141],inplace=True)
df18.sort_values(by='Country').head()


# Removing unique countries in 2019
df19.drop(df19.index[83],inplace=True)
df19.drop(df19.index[119],inplace=True)
df19.drop(df19.index[134],inplace=True)
df19.drop(df19.index[141],inplace=True)
df19.sort_values(by='Country').head()


df18.info()
df19.info()


# Checking if there are null values
null_columns = df18.columns[df18.isnull().any()]
df18[null_columns].isnull().sum()  # summary of columns
print(df18[df18.isnull().any(axis=1)][null_columns].head()) # single row

# Replacing null values with 0
df18['Perceptions of corruption'].fillna(
     value = 0,
     inplace = True
 )

df18.info()

# All data is now prepared

# Heathmap of correlation between variables 2018
f,ax = plt.subplots(figsize = (12, 12))
sns.heatmap(df18.corr(), annot = True, linewidths = 0.1, fmt = '.1f', ax = ax, square = True)

# Heathmap of correlation between variables 2019
f,ax = plt.subplots(figsize = (12, 12))
sns.heatmap(df19.corr(), annot = True, linewidths = 0.1, fmt = '.1f', ax = ax, square = True)


# Vizualization of a relation between variables
plt.figure(figsize=(20,20))
plt.subplot(2,1,1)
plt.plot(df19.Score,df19['GDP per capita'], color='blue', label= '2019')
plt.xlabel('Happiness Score')
plt.ylabel('GDP per capita')
plt.title('Correlation between Happiness Score and GPD per capita', color='Green', fontsize=30)
plt.subplot(2,1,2)
plt.plot(df19.Score,df19['Healthy life expectancy'], color='red', label= '2019')
plt.xlabel('Happiness Score')
plt.ylabel('Healthy life expectancy')
plt.title('Correlation between Happiness Score and Healthy life expectancy', color='Green', fontsize=30)



df18['Region'].value_counts()
df19['Region'].value_counts()

# Visualization of Number of Countries per Region in 2019
sns.set(font_scale = 1.5)
data19 = df19.Region.value_counts()
plt.figure(figsize=(10,7))
sns.barplot(x = data19.index, y = data19.values)
plt.xlabel('Region')
plt.xticks(rotation = 90)
plt.ylabel('Number of Countries')
plt.title('Number of Countries per Region in 2019', color = 'green', fontsize = 18)
plt.show()



# Pie chart
labels = df19.Region.value_counts().index
colors = ['grey', 'blue', 'red', 'yellow', 'green', 'brown', 'orange', 'purple', 'cyan', 'pink']
explode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sizes = df19.Region.value_counts().values

plt.figure(figsize = (7,7))
plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%')
plt.title('Ratio of Participating Countries to Regions in 2019', color = 'green', fontsize = 20)
plt.show()



# Drawing a scatterplot where one variable is categorical
# Observations on top of a box plot
sns.set(font_scale = 3)
ax = sns.boxplot(x = 'Score', y = 'Region', data = df19, whis=np.inf)
ax = sns.stripplot(x = 'Score', y = 'Region', data = df19, color=".2")
# plt.xticks(rotation = 90)
plt.title('Countries Happiness Score According to the Region in 2019', color = 'green', fontsize = 40)
plt.show()



# Number of countries above average score
df18.mean()
df19.mean()

# 2018
score_above_mean_18 =['Above World Average' if i >= 5.39 else 'Below World Average' for i in df18.Score]
df = pd.DataFrame({'Score' : score_above_mean_18})
sns.countplot(x = df.Score, palette='Set3')
plt.xlabel('Happiness Score')
plt.ylabel('Number of Countries')
plt.title('Number of Countries based on Happiness Score Average in 2018', color = 'green', fontsize = 30)
plt.show()


# 2019
score_above_mean_19 =['Above World Average' if i >= 5.43 else 'Below World Average' for i in df19.Score]
df = pd.DataFrame({'Score' : score_above_mean_19})
sns.countplot(x = df.Score, palette='Set2')
plt.xlabel('Happiness Score')
plt.ylabel('Number of Countries')
plt.title('Number of Countries based on Happiness Score Average in 2019', color = 'green', fontsize = 30)
plt.show()



df18.set_index('Overall rank').sort_values(by = 'Overall rank',ascending = 'False').head(10)

df19.set_index('Overall rank').sort_values(by = 'Overall rank',ascending = 'False').head(10)


# GDP per capita vs perception of coruption
df18[['Country','GDP per capita','Perceptions of corruption']].sort_values(by = 'GDP per capita',ascending = 'False').head(20)
df19[['Country','GDP per capita','Perceptions of corruption']].sort_values(by = 'GDP per capita',ascending = 'False').head(20)



# Created Level for Classification
# Averages and Standard Deviations of variables to create levels
df19['GDP per capita'].describe()

stdscore = df19.Score.std()
scoremean = sum(df19.Score)/len(df19.Score)
print('Score Average: ', scoremean)
print('Score Standart Deviation: ', stdscore)


stdeco = df19['GDP per capita'].std()
ecomean = sum(df19['GDP per capita'])/len(df19['GDP per capita'])
print('Economy Average: ' , ecomean)
print('Economy Standard Deviation: ', stdeco)


stdhealth = df19['Healthy life expectancy'].std()
healthmean = sum(df19['Healthy life expectancy'])/len(df19['Healthy life expectancy'])
print('Health Average: ', healthmean)
print('Health Standart Deviation: ', stdhealth)


stdsocial = df19['Social support'].std()
socialmean = sum(df19['Social support'])/len(df19['Social support'])
print('Social support Average: ', socialmean)
print('Social support Deviation: ', stdsocial)


data_average = pd.DataFrame()
data_average['Country'] = df19.Country
data_average['Region'] = df19.Region
data_average['Score'] = df19.Score
data_average['Score_Level']=['High' if i>scoremean+stdscore else 'Normal' if (scoremean-stdscore)<i<(scoremean+stdscore) else 'Low' for i in df19.Score]
data_average['GDP per capita'] = df19['GDP per capita']
data_average['GDP per capita_Level']=['High' if i>ecomean+stdeco else 'Normal' if (ecomean-stdeco)<i<(ecomean+stdeco) else 'Low' for i in df19['GDP per capita']]
data_average['Healthy life expectancy'] = df19['Healthy life expectancy']
data_average['Health_Level']=['High' if i>healthmean+stdhealth else 'Normal' if (healthmean-stdhealth)<i<(healthmean+stdhealth) else 'Low' for i in df19['Healthy life expectancy']]
data_average['Social support'] = df19['Social support']
data_average['Social_Level']=['High' if i>socialmean+stdsocial else 'Normal' if (socialmean-stdsocial)<i<(socialmean+stdsocial) else 'Low' for i in df19['Social support']]
data_average.head(10)
data_average.tail(10)


# Swarm plot for Score Level
sns.set(font_scale = 3)
f,ax=plt.subplots(figsize = (15,15))
sns.swarmplot(x = data_average.Score_Level, y = data_average.Score, hue = data_average.Region, size = 14)
ax.legend(fontsize = 18)


# High level countries
group_data = data_average.set_index(['Score_Level','GDP per capita_Level','Health_Level','Social_Level'])
group_data.loc[['High','High','High','High'], ['Country']]

# Low level countries
group_data.loc['Low','Low','Low','Low']



# # Top 1 country in each of the region by score
# 2018 
g = df18.groupby(['Region']).apply(lambda x: x.sort_values(['Score'], ascending = False)).reset_index(drop=True)
# select top N rows within each continent
g.iloc[:, :4].groupby('Region').head(1)


# 2019
g = df19.groupby(['Region']).apply(lambda x: x.sort_values(['Score'], ascending = False)).reset_index(drop=True)
# select top N rows within each continent
g.iloc[:, :4].groupby('Region').head(1)



# Comparisment of variables average per region in 2019
group_by_region = df19.groupby(by=['Region'])
regions_avg = group_by_region.mean()
regions_avg
regions_count = group_by_region.count()
regions_count


region_comparisment = regions_avg.merge(regions_count, left_index=True, 
                    right_index=True, suffixes=['_avg','_count'])
region_comparisment

# Visualization of comparisment of variables average per region
region_comparisment[['GDP per capita_avg', 'Healthy life expectancy_avg','Freedom to make life choices_avg', 
                'Social support_avg', 'Generosity_avg', 'Perceptions of corruption_avg']].sort_values(by=['GDP per capita_avg', 
                'Healthy life expectancy_avg','Freedom to make life choices_avg', 'Social support_avg', 'Generosity_avg', 
                'Perceptions of corruption_avg'], ascending=True).plot.barh(stacked=True, fontsize=40)
plt.title('Comparisment of Variables Average per Region in 2019', color='Green',fontsize=50)
plt.rcParams['figure.figsize'] = [30,30]



# difference between 2 datasets
year_2018 = df18[['Country','Overall rank','Score']]
year_2019 = df19[['Country','Overall rank','Score']]


df_comparisment = pd.concat([year_2018.set_index('Country'), year_2019.set_index('Country')], 
                   axis='columns', keys=['2018', '2019'])
df_comparisment.head(10)
df_comparisment.tail(10)



# PIVOT TABLES
df19['Region'].value_counts()
combined_data = pd.concat([df18, df19], axis=0)
# combined_data.groupby(by='Year')['Score'].describe()


# sorting the df by ascending years and descending happiness scores
combined_data.sort_values(['Year', 'Score'], ascending=[True, False], inplace=True)
# display of first 10 rows
combined_data.iloc[:, 0:4].head(10)


# Average mean per year of a happiness score
pd.pivot_table(combined_data, index= 'Year', values= 'Score')


# Each region’s mean for both years documented
pd.pivot_table(combined_data, index = 'Region', values='Score')


# Creating a multi-index pivot table
pd.pivot_table(combined_data, index= 'Region', columns='Year', values='Score')


# Visualizing the pivot table 
sns.set(font_scale=3)
pd.pivot_table(combined_data, index= 'Region', columns= 'Year', values= 'Score').plot(kind= 'bar')
plt.ylabel('Happiness Score')
plt.title('Comparison of average Happiness Score per Region', fontsize=46, color='Green')


# Manipulating the data using aggfunc
pd.pivot_table(combined_data, index= 'Region', values= 'Score', aggfunc= [np.mean, np.median, min, max, np.std])

# The average number of countries in each region in a given year. 
pd.pivot_table(combined_data, index = 'Region', values='Score', aggfunc= [np.mean, min, max, np.std, lambda x: x.count()/2])


def remove_outliers(values):
    mid_quantiles = values.quantile([.25, .75])
    return np.mean(mid_quantiles)

pd.pivot_table(combined_data, index = 'Region', values='Score', aggfunc= [np.mean, remove_outliers, lambda x: x.count()/2])


# Results by continents
table = pd.pivot_table(combined_data, index = 'Region', values='Score', aggfunc= [np.mean, remove_outliers])
table[table.index.str.contains('Europe')]


# Conditioning multi-indexes
table = pd.pivot_table(combined_data, index = ['Region', 'Year'], values='Score',aggfunc= [np.mean, remove_outliers])
table.query('Year == [2018, 2019] and Region == ["Eastern Asia", "Southeastern Asia", "Southern Asia"]')


# Ireland vs Croatia
new = pd.concat([df19.loc[15], df19.loc[74]])
print (new)
type(new)


table2 = pd.pivot_table(combined_data, index = ['Country', 'Year'], values=['Score'] )
table2.query('Year == [2018, 2019] and Country == ["Croatia", "Ireland"]')


# Comparison of variables for Ireland and Croatia in a table
table2 = pd.pivot_table(combined_data, index = ['Country', 'Year'], values=['Score','GDP per capita', 'Social support',
                   'Healthy life expectancy', 'Freedom to make life choices','Generosity', 'Perceptions of corruption'] )
table2.query('Year == [2018, 2019] and Country == ["Croatia", "Ireland"]')


# Visual comparison of variables for Ireland and Croatia
sns.set(font_scale=2)
pd.pivot_table(table2.query('Year == [2018, 2019] and Country == ["Croatia", "Ireland"]')
, index= 'Country', columns= 'Year', values= ['GDP per capita', 'Social support',
                   'Healthy life expectancy', 'Freedom to make life choices','Generosity', 
                   'Perceptions of corruption']).plot(kind= 'bar')
plt.title('Comparison of Variables of Croatia and Ireland in 2018 and 2019', fontsize=50, color='Green')
plt.ylabel('Happiness Score', fontsize=40)
plt.xlabel('Country', fontsize=40)


# Happines Score in Central and Eastern Europe Countries
df_Central_Eastern_Europe = combined_data[combined_data.Region == 'Central and Eastern Europe']
df_Central_Eastern_Europe.head(20)


sns.set(font_scale=3)
table = pd.pivot_table(df_Central_Eastern_Europe, index= 'Country', columns = 'Year', values= 'Score').plot.barh(stacked=False, fontsize=20)
plt.title('Comparison of Happines Score in Central and Eastern Europe Countries', fontsize=50, color='Green')
plt.ylabel('Country', fontsize=40)
plt.xlabel('Happiness Score', fontsize=40)







