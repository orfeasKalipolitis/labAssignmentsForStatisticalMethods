import numpy as np
import dataGetter as data

Y = data.satisfaction
XT = np.array([np.ones(len(Y)), data.commitment, data.autonomy, data.income, data.skills, data.quality, data.age, data.years]) # X transpose
X = XT.transpose()

XTX = XT.dot(X)
XTY = XT.dot(Y)

B1 = np.linalg.inv(XTX).dot(XTY)


YEst = X.dot(B1)
SSE = np.sum(np.power(Y - YEst, 2))


# Dropping income and years
XT = np.array([np.ones(len(Y)), data.commitment, data.autonomy, data.skills, data.quality, data.age]) # X transpose
X = XT.transpose()

XTX = XT.dot(X)
XTY = XT.dot(Y)

B2 = np.linalg.inv(XTX).dot(XTY)
YEst = X.dot(B2)
SSE2 = np.sum(np.power(Y - YEst, 2))
# They are off by ~1% one from the other, so dropping those definitely is for the better


def show():
    print('Variable weights:')
    print(B1)
    print()
    print('This gives an error sum of squares equal to: ', SSE)
    print()
    print('Income and years seems to have the lowest significance at weights of ~0.04 and less than 0.02 respectively.')
    print('Dropping the income and years as independent variables.')
    print('This gives a new set of weights:')
    print(B2)
    print()
    print('This gives an error sum of squares equal to: ', SSE2)

show()
