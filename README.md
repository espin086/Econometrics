# Econometrics
A set of command line tools to perform econometric analysis.

## Difference in Difference Model

**Background on Model**
[wikipedia](https://en.wikipedia.org/wiki/Difference_in_differences)

**Documentation**
```
usage: diff_in_diff.py [-h] data_file treatment post outcome_variable [confounding_variables ...]

Run difference-in-differences analysis

positional arguments:
  data_file             Path to the data file
  treatment             Treatment variable
  post                  Post variable
  outcome_variable      Outcome variable
  confounding_variables
                        List of confounding variables

options:
  -h, --help            show this help message and exit
```

**Example**
```
 python diff_in_diff.py 'data/kielmc_clean.xlsx' "nearinc" "y81" "lprice" "rooms" "age" "land" "area"
```
**Output**
```
  OLS Regression Results                            
==============================================================================
Dep. Variable:                 lprice   R-squared:                       0.751
Model:                            OLS   Adj. R-squared:                  0.746
Method:                 Least Squares   F-statistic:                     134.6
Date:                Thu, 11 Apr 2024   Prob (F-statistic):           2.52e-90
Time:                        12:10:41   Log-Likelihood:                 32.968
No. Observations:                 320   AIC:                            -49.94
Df Residuals:                     312   BIC:                            -19.79
Df Model:                           7                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
const             10.0705      0.105     96.053      0.000       9.864      10.277
nearinc           -0.0692      0.041     -1.697      0.091      -0.149       0.011
y81                0.3861      0.031     12.548      0.000       0.326       0.447
treatment_post    -0.0817      0.055     -1.478      0.140      -0.190       0.027
rooms              0.0989      0.017      5.709      0.000       0.065       0.133
age               -0.0038      0.000     -9.349      0.000      -0.005      -0.003
land            8.964e-07   3.33e-07      2.691      0.008    2.41e-07    1.55e-06
area               0.0003   2.18e-05     11.989      0.000       0.000       0.000
==============================================================================
Omnibus:                       53.069   Durbin-Watson:                   1.731
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              189.391
Skew:                          -0.668   Prob(JB):                     7.49e-42
Kurtosis:                       6.524   Cond. No.                     4.92e+05
==============================================================================
```