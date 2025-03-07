#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 11:35:38 2025

@author: jingxiaoyi
"""

import numpy as np
from sklearn.impute import KNNImputer
import pandas as pd

# Create a CSV reader to read the data in chunks of 100,000 rows
reader = pd.read_csv ( "/Users/data.csv",
                      chunksize=100000,
                      iterator=True)
df_list = []  # List to store DataFrame chunks
i = 0 # Initialize a counter for the number of chunks processed

# Iterate over each chunk of the CSV file
for df in reader:
   # Initialize the KNNImputer with 10 neighbors and uniform weights  
    KI=KNNImputer(n_neighbors=10,weights="uniform")

    # Fit the imputer on the current chunk and transform the data to impute missing values
    df_imput=KI.fit_transform(df)

    # Convert the imputed numpy array back to a DataFrame
    df = pd.DataFrame(df_imput)

    # Append the DataFrame to the list
    df_list.append(df)

    # Increment the counter and print the current chunk number
    i = i+1
    print(i)

# Concatenate all DataFrame chunks into a single DataFrame   
df_output = pd.concat(df_list, ignore_index=True)

# Save the imputed DataFrame to a new CSV file
df_output.to_csv("/Users/data(imput).csv", index=False)