import numpy as np
import dataGetter as data

Y = data.satisfaction
XT = np.array([np.ones(len(Y)), data.commitment, data.autonomy, data.income, data.skills, data.quality, data.age, data.years]) # X transpose
X = XT.transpose()

XTX = XT.dot(X)
XTY = XT.dot(Y)

B = np.linalg.inv(XTX).dot(XTY)


YEst = X.dot(B)
SSE = np.sum(np.power(Y - YEst, 2))


# Dropping income and years
XT = np.array([np.ones(len(Y)), data.commitment, data.autonomy, data.skills, data.quality, data.age]) # X transpose
X = XT.transpose()

XTX = XT.dot(X)
XTY = XT.dot(Y)

B = np.linalg.inv(XTX).dot(XTY)
YEst = X.dot(B)
SSE2 = np.sum(np.power(Y - YEst, 2))
# They are off by ~1% one from the other, so dropping those definitely is for the better


def show():
    print('Variable weights:')
    print(B)
    print()
    print('This gives an error sum of squares equal to: ', SSE)
    print()
    print('Income and years seems to have the lowest significance at weights of ~0.04 and less than 0.02 respectively.')
    print('Dropping the income and years as independent variables.')
    print()
    print('This gives an error sum of squares equal to: ', SSE2)
