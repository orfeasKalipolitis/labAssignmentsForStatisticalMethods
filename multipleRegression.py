import numpy as np
import dataGetter as data
from scipy import stats as spStats

Y = data.satisfaction
XT = np.array([np.ones(len(Y)), data.commitment, data.autonomy, data.income, data.skills, data.quality, data.age, data.years]) # X transpose
variableNames = ['commitment', 'autonomy', 'income', 'skills', 'quality', 'age', 'years']
X = XT.transpose()

XTX = XT.dot(X)
XTY = XT.dot(Y)

B1 = np.linalg.inv(XTX).dot(XTY)


YEst = X.dot(B1)
SSE = np.sum(np.power(Y - YEst, 2))


# Dropping income and years
XT2 = np.array([np.ones(len(Y)), data.commitment, data.autonomy, data.income, data.skills, data.quality, data.age]) # X transpose
X2 = XT2.transpose()

XTX2 = XT2.dot(X2)
XTY2 = XT2.dot(Y)

B2 = np.linalg.inv(XTX2).dot(XTY2)
YEst2 = X2.dot(B2)
SSE2 = np.sum(np.power(Y - YEst2, 2))
# They are off by ~1% one from the other, so dropping those definitely is for the better

# Individual t-Tests for Variable Screening
def doTTests():
    for i in range(1, len(X[0])):
        print(variableNames[i - 1], ':', spStats.ttest_ind(Y, X[:, i], equal_var = False))

def show():
    print('Variable weights:')
    print(B1)
    #print()
    print('This gives an error sum of squares equal to: ', SSE)
    print()
    print('Now running Individual t-Tests for Variable Screening, to see if we can drop any variables.')
    print()
    doTTests()
    print()
    print('This gives a new set of weights:')
    print(B2)
    print()
    print('This gives an error sum of squares equal to: ', SSE2)
