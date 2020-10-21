import numpy as np
import matplotlib.pyplot as plt
import dataGetter as data

ageMax = np.max(data.age)
ageMin = np.min(data.age)
ageMedian = np.median(data.age)
ageQ1 = np.quantile(data.age, 0.25)
ageQ3 = np.quantile(data.age, 0.75)

boxData = [data.age]
fig3, ax3 = plt.subplots()
ax3.set_title('max, min, median, the first and third quartile box plot of Age')
ax3.boxplot(boxData, showmeans=True)
plt.xlabel('Age')

def show():
    print('Q1: ', ageQ1)
    print('Q2: ', ageQ3)
    plt.show()