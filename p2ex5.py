from scipy import stats as spStats
import numpy as np

# Individual t-tests for Variable Screening
# dependentVar is the Y vector of the dependent variable
# independentVars are the variables in the X matrix of Y = X * B
# you can add as many independent variables as you want
# returns the p-values for all independent variables
def doTTests(dependentVar, *independentVars):
    print()
    print('Performing t-tests of each independent variable against the dependent variable:')
    print('Assuming a confidence level of 95%')
    print('If we observe a large p-value larger than 0.05, then we cannot reject the null hypothesis of identical average scores.')
    print('And so you should conclude that variable is insignificant.')

    XT = np.array([np.ones(len(dependentVar)), *independentVars])
    X = XT.transpose()
    count = 1
    minPValue = 1
    minIndex = -1
    pvalues = []
    for i in range(1, len(X[0])):
        print('Dependent variable #:', count)
        ttest = spStats.ttest_ind(dependentVar, X[:, i], equal_var = False)
        print(ttest)

        if ttest[1] < minPValue:
            minPValue = ttest[1]
            minIndex = count
        pvalues.append(ttest[1])
        count = count + 1

    print()
    print('We observe the strongest correlation between the dependent variable and independent variable #', minIndex)
    print('with a p-value of: ', minPValue)
    return pvalues
