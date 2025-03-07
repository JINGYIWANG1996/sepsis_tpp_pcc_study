Codes to estimate critical closing pressure from hemodynamic data (including mean arterial pressure and estimated cardiac output). Companion code to the paper “The Role of Critical Closing Pressure and Tissue Perfusion Pressure in Sepsis Risk Stratification”.

The code in this repository is made available for the purposes of scientific research and educational activities in conjunction with the corresponding scientific manuscript.

The methods presented and the code provided are not intended for and should not be utilized for commercial purposes or for clinical evaluation, clinical decision making, or healthcare delivery. The user holds the authors and their corresponding institutions harmless from any claims arising out of its use. The authors and their corresponding institutions are not responsible for any treatment or medical applications or decisions made by users based on information contained in this repository.

Please direct any questions or further inquiries to the corresponding author at dubin98@gmail.com.

## Requirements 
The codes are tested on Python 3 with NumPy `1.26.4`, Pandas `2.1.4`, Scikit-learn `1.2.2`, and Matplotlib `3.8.0` (for visualization, if needed). 

## Code 
Two Python scripts (`.py`) for Pcc estimation are provided. The first script, `pcc_estimation_by_method1.py`, estimates Pcc using paired MAP and CO (represented as PP * HR in our study) over 3-hour intervals (e.g., H1-H2-H3, H2-H3-H4, etc.). The output includes `k_co`, `b_co`, and `rsquared_co`, representing the slope, intercept, and R-squared value of the fitted line, respectively, with the intercept serving as the estimated Pcc value. The second script, `pcc_estimation_by_method2.py`, offers an alternative approach to estimating Pcc. This method calculates hourly Pcc using paired MAP and CO data at 5-minute intervals, resulting in a total of 13 data points for each estimation. The output includes `k`, `b`, and `r2`, representing the slope, intercept, and R-squared value of the fitted line, respectively, with the intercept serving as the estimated Pcc value.


