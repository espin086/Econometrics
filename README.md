# Econometrics
A set of command line tools to perform econometric analysis.

## Difference in Difference Model

**Background on Model**
[wikipedia](https://en.wikipedia.org/wiki/Difference_in_differences)

**Documentation**
```
python diff_in_diff.py --help                                           
usage: diff_in_diff.py [-h] data_file treatment post outcome_variable

Run difference-in-differences analysis

positional arguments:
  data_file         Path to the data file
  treatment         Treatment variable
  post              Post variable
  outcome_variable  Outcome variable

options:
  -h, --help        show this help message and exit
```

**Example**
```
python diff_in_diff.py 'data/kielmc_clean.xlsx' "nearinc" "y81" "lprice"
```
**Output**
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 lprice   R-squared:                       0.408
Model:                            OLS   Adj. R-squared:                  0.402
Method:                 Least Squares   F-statistic:                     72.52
Date:                Thu, 11 Apr 2024   Prob (F-statistic):           1.03e-35
Time:                        09:44:55   Log-Likelihood:                -105.83
No. Observations:                 320   AIC:                             219.7
Df Residuals:                     316   BIC:                             234.7
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
const             11.2854      0.031    369.271      0.000      11.225      11.346
nearinc           -0.3410      0.055     -6.201      0.000      -0.449      -0.233
y81                0.4570      0.045     10.068      0.000       0.368       0.546
treatment_post    -0.0616      0.084     -0.735      0.463      -0.226       0.103
==============================================================================
Omnibus:                       29.375   Durbin-Watson:                   1.565
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               83.642
Skew:                           0.372   Prob(JB):                     6.88e-19
Kurtosis:                       5.392   Cond. No.                         6.06
==============================================================================
```