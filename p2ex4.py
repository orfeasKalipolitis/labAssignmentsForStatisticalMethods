from scipy import stats as spStats
from p2ex2_3 import anovaTest

# x and y should be 1-D arrays they do not need to have the same size
# array length for both x and y should be bigger than 0 for the results to be dependable
def mannWhitneyWilcoxonTest(x, y):
    mwwTest = spStats.mannwhitneyu(x, y)
    print()
    print('Mann-Whitney-Wilcoxon test to see if there is any significant difference between your 2 variables:')
    print('If the p-value is less than or equal to your significance level,')
    print('you should reject the null hypothesis and conclude that at least one significant difference can be assumed.')
    print(mwwTest)
    print()
    anovaTest(x, y)
