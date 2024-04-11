# Econometrics
A set of command line tools to perform econometric analysis.

## Difference in Difference Model


**Documentation**

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


**Example**

python diff_in_diff.py 'data/kielmc_clean.xlsx' "nearinc" "y81" "lprice"