

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

df=pd.read_csv("/Users/data.csv")

# Initialize empty lists to store extracted data
x = []  # Stores CO (cardiac output) values grouped by 13 observations
y = [] # Stores MAP (mean arterial pressure) values grouped by 13 observations
x_temp = []# Temporary list for CO values within a 13-observation window
y_temp = []# Temporary list for MAP values within a 13-observation window
p_id = [] # Stores patient IDs corresponding to each group

# Iterate through each row in the dataframe
for i in range(len(df)):
    a = df['co'].iloc[i]  # Extract CO value
    b = df['map'].iloc[i] # Extract MAP value
    x_temp.append(a)  # Append CO value to temporary list
    y_temp.append(b) # Append MAP value to temporary list
    
    # Every 13th row (i % 13 == 12), store the collected data and reset temporary lists
    if (i%13 == 12):
        x.append(x_temp) # Store 13 CO values
        y.append(y_temp)  # Store 13 MAP values
        p_id.append(df['patient_id'].iloc[i])  # Store the patient ID
        x_temp = [] # Reset temporary CO list
        y_temp = [] # Reset temporary MAP list                                

# Initialize lists to store regression results
k_thirteen = [] # Stores slope (coefficient) of the linear regression
b_thirteen = []   # Stores intercept of the linear regression
rsquared = [] # Stores R-squared values to measure model fit

# Perform linear regression for each group of 13 observations
for i in range(len(p_id)):
    x_temp = x[i] # Get stored CO values for the patient
    y_temp = y[i] # Get stored MAP values for the patient
    
    # Convert lists to NumPy arrays and reshape for regression
    x_temp_13 = np.array(x_temp).reshape(-1, 1)
    y_temp_13 = np.array(y_temp).reshape(-1, 1)
    
    # Perform linear regression using sklearn's LinearRegression
    reg = LinearRegression().fit(x_temp_13, y_temp_13)
    k_thirteen.append(reg.coef_[0][0]) # Store the slope of the regression line
    b_thirteen.append(reg.intercept_[0])  # Store the intercept of the regression line
    
    # Perform regression using statsmodels to obtain R-squared value
    _x_temp = sm.add_constant(x_temp)  # Add constant term for OLS regression
    model = sm.OLS(y_temp, _x_temp)  # Create Ordinary Least Squares (OLS) model
    result = model.fit()  # Fit the model
    rsquared.append(result.rsquared) # Store R-squared value

# Initialize lists to store final output
p_id_list = []
k = []
b = []
r2 = []
index = []

# Populate final lists with computed regression results
for i in range(len(p_id)):
    p_id_list.append(p_id[i])
    k.append(k_thirteen[i])
    b.append(b_thirteen[i])
    r2.append(rsquared[i])
    index.append(i)

# Create a new DataFrame to store regression results
df1 = pd.DataFrame()
df1['id'] = p_id_list
df1['k'] = k
df1['b'] = b
df1['r2'] = r2
df1['index'] = index

df1.to_csv( "/Users/pcc.csv", index=False)
