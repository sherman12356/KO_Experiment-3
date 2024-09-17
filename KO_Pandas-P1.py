#!/usr/bin/env python
# coding: utf-8

# # Experiment 3 PYTHON DATA ANALYSIS (PANDAS)

# In[12]:


import pandas as pd


# ###   PROBLEM 1

# In[36]:


#read the car_csv file
car=pd.read_csv('cars.csv')

#Display the first five and last five rows of the cars
car.iloc[[*range(5), *range(-5, 0)]]

