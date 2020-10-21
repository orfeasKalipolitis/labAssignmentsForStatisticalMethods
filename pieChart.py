from collections import Counter
import dataGetter as data
import matplotlib.pyplot as plt

labels = ['White', 'Asian', 'West Indian', 'African', 'other']
ethnicGroups = Counter(data.ethnic)
sizes = [ethnicGroups[1], ethnicGroups[2], ethnicGroups[3], ethnicGroups[4], ethnicGroups[5]]
explode = (0.1, 0.2, 0.3, 0.4, 0.5)  # "explode" each slice a different amount

fig2, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

def show():
    plt.show()