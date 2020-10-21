import numpy as np
import dataGetter as data

# Library solution
x = data.quality
y = data.income

correlation_matrix = np.corrcoef(x, y)
correlation_xy = correlation_matrix[0,1]
detCoeff = correlation_xy ** 2


# DIY solution Following Lecture 11 Simple Regression

x = np.array(data.quality) # independent
y = np.array(data.income)  # dependent

xMean = np.mean(x)
yMean = np.mean(y)

b1 = np.sum((x - xMean) * (y - yMean) / np.sum(np.power(x - xMean, 2)))
b0 = yMean - (b1 * xMean)

yEst = b0 + (b1 * x)

sign = '+' if b1 > 0 else ''


# calculate the error sum squares (SSE) and the total corrected sum squares (SST)
SSE = np.sum(np.power(y - yEst, 2))
SST = np.sum(np.power(y - yMean, 2))

# calculate the determination coefficient R^2
R2 = 1 - (SSE / SST)
 

def show():
    print('Library (numpy) solution: Our calculated determination coefficient is: ', detCoeff)
    print('DIY: Our calculated determination coefficient is: ', R2)
    print('Estimated regression equation: yEst = ', b0, sign, b1, '* x')
    