# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
dt = pd.read_csv("D:\BHonly.txt", sep = '|') #Path to subscriber database as input

newdt=dt[['telephone_no','full_name','father_name','permanent_add1','permanent_add2','permanent_add3','permanent_add4','permanent_pincode']] #Required columns of database



rows = newdt.sample(frac =0.001) #Percentage of samples required

rows.to_csv (r'D:\data_sample.csv', index = False, header=True) #Path to sample data base as output

