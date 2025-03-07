Codes to estimate critical closing pressure from hemodynamic data (including mean arterial pressure and estimated cardiac output). Companion code to the paper “The Role of Critical Closing Pressure and Tissue Perfusion Pressure in Sepsis Risk Stratification”.
The code in this repository is made available for the purposes of scientific research and educational activities in conjunction with the corresponding scientific manuscript.
The methods presented and the code provided are not intended for and should not be utilized for commercial purposes or for clinical evaluation, clinical decision making, or healthcare delivery. The user holds the authors and their corresponding institutions harmless from any claims arising out of its use. The authors and their corresponding institutions are not responsible for any treatment or medical applications or decisions made by users based on information contained in this repository.
Please direct any questions or further inquiries to the corresponding author at dubin98@gmail.com.

## Requirements 
The codes were tested on Python 3 with NumPy `1.26.4`, Pandas `2.1.4`, Scikit-learn `1.2.2`, and Matplotlib `3.8.0` (for visualization, if needed). 

Two `.py ` for Pcc estimations are provided. The first one, `Pcc estimation in method 1 ` provides a method to estimate Pcc with paired MAP and CO (PP*Hr in our study) for every 3 hours (e.g., H1-H2-H3, H2-H3-H4,…). The results included k_co, b_co, and rsquared_co, which represent the slope, intercept, and r squared of the fitting line, with intercept being Pcc value.
The second file one ` Pcc estimation in method 2`, provides another method to estimate Pcc. The method estimates the hourly Pcc with paired MAP and CO for every 5 minutes. Therefore, a total of 13 points are used for estimation. The results included k_co, b_co, and rsquared_co, which represent the slope, intercept, and r squared of the fitting line, with intercept being Pcc value.


