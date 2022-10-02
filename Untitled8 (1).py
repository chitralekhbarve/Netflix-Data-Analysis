#!/usr/bin/env python
# coding: utf-8

# Netlflix Data Analysis

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[17]:


data = pd.read_csv(r"C:\Users\chitr\Desktop\netflix\netflix.csv")


# In[18]:


data.head()


# In[19]:


data.tail()


# In[20]:


data.info()


# In[21]:





# In[22]:


data.size


# In[23]:


data.columns


# In[24]:


data.dtypes


# In[30]:


#To find the duplicate records in the dataset and removing them

data.head()


# In[32]:


data[data.duplicated()]


# In[34]:


data.drop_duplicates(inplace=True)


# In[35]:


data


# In[36]:


#finding null values
data.isnull()


# In[37]:


data.isnull().sum()


# In[39]:


#Null Values via heatmap
sns.heatmap(data.isnull())


# In[43]:


#Q1: for house of cards, what is the show id and Who is the director of the show?

#isin()

data[data['Title'].isin(['House of Cards'])]


# In[49]:


#method 2 
#str.contains()

data[data['Title'].str.contains('House of Cards')]


# In[52]:


#Q2: In which year the hightest number of TV shows and movies were released ?

data.dtypes


# In[53]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[55]:


data.head()


# In[66]:


data['Date_N'].dt.year.value_counts()


# In[67]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')  #Bar graph plotting


# In[68]:


#Q3: How many movies and TV shows are in the dataset, with graph?


# In[70]:


data.groupby(['Category']).Category.count()


# In[72]:


sns.countplot(data['Category']) 


# In[75]:


#Q4: Show all the movies relesead in the year 2000 ? 

data['Year'] = data['Date_N'].dt.year #Creating a new column 


# In[92]:


data[(data['Category'] == 'Movie') & (data['Year'] == 2020)]


# In[94]:


#Title of all the tv shows that were released in india 

data.head()


# In[107]:


data[(data['Country'] == "India") & (data['Category'] == "TV Show")]['Title']


# In[118]:


#Show top 10 director who has given highest number to TV shows and movies to NEtlfix
data["Director"].value_counts().head(10)


# In[120]:


#show all the movies where category is movie and type is comedies or Country is India

data.head(2)


# In[122]:


data[ (data['Category'] == "Movies") & (data['Type'] == 'Comedies') | (data['Country'] == "India")]


# In[134]:


#in how many movies tom cruise was actor?

data[data['Cast'].str.contains("Tom Cruise")]


# In[131]:


#Removing the null values (Cannot mask with non-boolean array containing NA / NaN values)

data_new=data.dropna()


# In[132]:


data_new


# In[135]:


#in how many movies tom cruise was actor?

data_new[data_new['Cast'].str.contains("Tom Cruise")]


# In[138]:


#Q: What are the different ratings by netflix?
#total unique values in rating column 
data['Rating'].nunique()


# In[139]:


data['Rating'].unique()


# In[156]:


#Q: how many movies got the TV 14 rating in India?

data[(data['Category'] == "Movie") & (data['Rating'] == "TV-14") & (data['Country'] == "India")].shape


# In[163]:


#Q How many tv shows got PG rating and was released after 2018

data[(data['Category'] == 'TV Show') & (data['Rating'] == "TV-PG") & (data['Year'] > 2018)].shape


# In[165]:


#Q: What is the maximum durating of a movie/show on Netflix

data['Duration'].unique()


# In[190]:


#Converting the data in numeric format

data[['Minutes', 'Unit']] = data['Duration'].str.split(' ', expand= True)


# In[191]:


data


# In[172]:


data['Minutes'].max()


# In[173]:


#Q which invidual country  has the highest no of tV Shows


# In[178]:


data_tvshow = data[data['Category'] == "TV Show"]


# In[179]:


data_tvshow


# In[183]:


data_tvshow['Country'].value_counts().head(1)


# In[184]:


#@ sorting the data by year 

data.head()


# In[187]:


data.sort_values(by='Year', ascending = False)


# In[ ]:




