
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

dataFilename = "jss13_ht20.xlsx"
# empty cells have been replaced with 0s

# Get data from xlsl file
dataFrame = pd.read_excel(dataFilename, sheet_name=None)
dataMatrix = dataFrame['Sheet1']

gender = dataMatrix['gender']
income = dataMatrix['income']
productivity = dataMatrix['prody']
skills = dataMatrix['skill']
ethnic = dataMatrix['ethnicgp']

# Prapare gendered data
femaleIncome = []
maleIncome = []
femaleSkills = []
maleSkills = []
femaleProductivity = []
maleProductivity = []

# Distinguish female from male data
iterator = 0
for person in gender:
    if person == 1:
        maleIncome.append(income[iterator])
        maleProductivity.append(productivity[iterator])
        maleSkills.append(skills[iterator])
    else:
        femaleIncome.append(income[iterator])
        femaleProductivity.append(productivity[iterator])
        femaleSkills.append(skills[iterator])
    iterator = iterator + 1

# Barplot

# Get mean values
femaleAvgIncome = np.mean(femaleIncome)
maleAvgIncome = np.mean(maleIncome)
femaleAvgProductivity = np.mean(femaleProductivity)
maleAvgProductivity = np.mean(maleProductivity)
femaleAvgSkills = np.mean(femaleSkills)
maleAvgSkills = np.mean(maleSkills)

menMeans = [
    np.round(maleAvgIncome, 2), 
    np.round(maleAvgProductivity, 2), 
    np.round(maleAvgSkills, 2)
]
womenMeans = [
    np.round(femaleAvgIncome, 2), 
    np.round(femaleAvgProductivity, 2), 
    np.round(femaleAvgSkills, 2)
]

# Create charts
labels = ['Income', 'Skills', 'Productivity']
x = np.arange(len(labels))
width = 0.4

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, menMeans, width, label='Men')
rects2 = ax.bar(x + width/2, womenMeans, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Income, Productivity / Skill level')
ax.set_title('Income, Productivity and Skill level by gender')
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

plt.show()


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['White', 'Asian', 'West Indian', 'African', 'other']
ethnicGroups = Counter(ethnic)
sizes = [ethnicGroups[1], ethnicGroups[2], ethnicGroups[3], ethnicGroups[4], ethnicGroups[5]]
explode = (0.1, 0.2, 0.3, 0.4, 0.5)  # "explode" each slice a different amount

fig2, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()