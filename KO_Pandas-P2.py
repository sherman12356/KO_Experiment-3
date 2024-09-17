#!/usr/bin/env python
# coding: utf-8

# # Experiment 3 PYTHON DATA ANALYSIS (PANDAS)

# In[12]:


import pandas as pd


# ### PROBLEM 2

# In[58]:


# a.
#read the car_csv file
car=pd.read_csv('cars.csv')

# Display the first five odd number rows
car.iloc[1:10:2]


# In[60]:


# b.
#read the car_csv file
car=pd.read_csv('cars.csv')

#Display the row with the model "Mazda RX4"
car.loc[car['Model']=='Mazda RX4']


# In[72]:


#c.
#read the car_csv file
car=pd.read_csv('cars.csv')

#Display the cyl with the model"Camaro Z28"
car.loc[(car['Model']=='Camaro Z28'),['Model','cyl']]


# In[76]:


#d.
#read the car_csv file
car=pd.read_csv('cars.csv')

#Display the cyl, gear with the model"Camaro Z28" "Honda Civic" "Mazda RX4 Wag"
car.loc[(car['Model']== 'Mazda RX4 Wag')|(car['Model']=='Ford Pantera L')|(car['Model']=='Honda Civic'),['Model','cyl','gear']]

