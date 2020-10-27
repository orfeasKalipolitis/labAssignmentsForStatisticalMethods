import numpy as np
import matplotlib.pyplot as plt
import dataGetter as data

# get men & women count
men = 0
women = 0
for person in data.gender:
    if person == 1:
        men = men + 1
    elif person == 2:
        women = women + 1
    else:
        print('Someone was not registered as a man or woman. #dataGathering')

# Create charts
labels = ['Gender']
x = np.arange(len(labels))
width = 0.4

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, men, width, label='Men')
rects2 = ax.bar(x + width, women, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of people')
ax.set_title('Gender of employees')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

def show():
    plt.show()
