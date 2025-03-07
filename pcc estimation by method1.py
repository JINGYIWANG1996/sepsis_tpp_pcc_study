#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 22:00:05 2025

@author: jingxiaoyi
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


df=pd.read_csv("/Users/data.csv")

# Initialize empty lists to store extracted data
X_co = [] # Stores CO (cardiac output) values for regression
Y_map = [] # Stores MAP (mean arterial pressure) values for regression
patient_id = []  # Stores patient IDs

# Loop through each row in the dataframe
for i in range(len(df)):
    X_co_temp = [] # Temporary list to hold CO values for a given window
    Y_map_temp = [] # Temporary list to hold MAP values for a given window
    
    # Skip rows where the index modulo 24 equals 22 or 23
    if (i%24 == 22 or i%24 == 23):
        continue
    
    # Collect three consecutive values of CO and MAP for regression
    for j in range(3):
        X_co_temp.append(df['co'].iloc[i+j]) # Extract CO values
        Y_map_temp.append(df['map'].iloc[i+j]) # Extract MAP values
        
     # Append the collected values to the main lists    
    X_co.append(X_co_temp)
    Y_map.append(Y_map_temp)
    patient_id.append(df['id'].iloc[i])

# Initialize lists to store regression results
k_co = []  # Stores slope (coefficient) of linear regression
b_co = [] # Stores intercept of the linear regression
rsquared_co = [] # Stores R-squared values of the regression model

# Perform linear regression for each patient data segment
for i in range(len(patient_id)):
    X_co_temp = X_co[i]
    Y_map_temp = Y_map[i]
    
    # Convert lists to NumPy arrays and reshape for regression
    x_co_temp = np.array(X_co_temp).reshape(-1, 1)
    y_map_temp = np.array(Y_map_temp).reshape(-1, 1)
    
    # Perform linear regression using sklearn's LinearRegression
    reg_co = LinearRegression().fit(x_co_temp, y_map_temp)
    k_co.append(reg_co.coef_[0][0]) # Store the slope of the regression line
    b_co.append(reg_co.intercept_[0]) # Store the intercept of the regression line
    
    # Perform regression using statsmodels to obtain R-squared value
    _x_co_temp = sm.add_constant(X_co_temp)# Add constant term for OLS regression
    model = sm.OLS(Y_map_temp, _x_co_temp)# Create Ordinary Least Squares (OLS) model
    result_co = model.fit() # Fit the model
    rsquared_co.append(result_co.rsquared) # Store R-squared value

# Create a new DataFrame to store regression results

df1 = pd.DataFrame()
df1['patient_id'] = patient_id
df1['k_co'] = k_co
df1['b_co'] = b_co
df1['rsquared_co'] = rsquared_co

df1.to_csv("/Users/pcc.csv", index=False)