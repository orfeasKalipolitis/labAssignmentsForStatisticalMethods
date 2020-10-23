import numpy as np
import matplotlib.pyplot as plt
import dataGetter as data

# Make a copy of the Age array
localAge = np.array(data.age.copy())

# Remove 0s as they are obviously incorrect data points
localAge = np.delete(localAge, np.argwhere(localAge == 0))

ageMax = np.max(localAge)
ageMin = np.min(localAge)
ageMedian = np.median(localAge)
ageQ1 = np.quantile(localAge, 0.25)
ageQ3 = np.quantile(localAge, 0.75)

boxData = [localAge]
fig3, ax3 = plt.subplots()
ax3.set_title('max, min, median, the first and third quartile box plot of Age')
ax3.boxplot(boxData, showmeans=True)
plt.xlabel('Age')

def show():
    print('Age max:', ageMax)
    print('Age min:', ageMin)
    print('Age median:', ageMedian)
    print('Age Q1:', ageQ1)
    print('Age Q3:', ageQ3)
    plt.show()
    