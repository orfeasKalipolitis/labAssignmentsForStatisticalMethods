import numpy as np
from p2ex5 import doTTests

defaultConfidenceLevel = 0.95

def regressionAnalysis(dependentVar, *independentVars, confidence=defaultConfidenceLevel):
    print(len(independentVars))
    print('Performing Multiple Regression Analysis between your dependent and independent variables.')
    # Figuring out which variables to drop
    pvalues = doTTests(dependentVar, *independentVars)
    risk = 1 - confidence
    prunedIndependentVars = []
    for i in range(0, len(pvalues)):
        if pvalues[i] > risk:
            print()
            print('Independent variable #', str(i + 1), 'has a p-value of:', pvalues[i])
            print('which means it should be discarded.')
        else:
            prunedIndependentVars.append(independentVars[i])
    print()

    # Create a formula
    Y = dependentVar
    XT = np.array([np.ones(len(Y)), *prunedIndependentVars]) # X transpose
    X = XT.transpose()

    XTX = XT.dot(X)
    XTY = XT.dot(Y)

    B = np.linalg.inv(XTX).dot(XTY)
    print('The weights for the remaining independent variables should be:')
    print(B)

# test with data
# regressionAnalysis(data.satisfaction, data.absence, data.age, data.attendance, data.autonomy, data.commitment, data.income, data.skills, data.years, confidence=0.90)