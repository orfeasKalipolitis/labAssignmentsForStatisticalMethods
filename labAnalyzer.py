
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from scipy import stats as spStats

dataFilename = "jss13_ht20.xlsx"
# empty cells have been replaced with 0s

# Get data from xlsl file
dataFrame = pd.read_excel(dataFilename, sheet_name=None)
dataMatrix = dataFrame['Sheet1']

# get each column of data
gender = dataMatrix['gender']
income = dataMatrix['income']
productivity = dataMatrix['prody']
skills = dataMatrix['skill']
ethnic = dataMatrix['ethnicgp']
quality = dataMatrix['qual']
satisfaction = dataMatrix['satis']
commitment = dataMatrix['commit']
autonomy = dataMatrix['autonom']
age = dataMatrix['age']
years = dataMatrix['years']
routine = dataMatrix['routine']
attendance = dataMatrix['attend']
absence = dataMatrix['absence']

# Prapare gendered data
femaleIncome = []
maleIncome = []
femaleSkills = []
maleSkills = []
femaleProductivity = []
maleProductivity = []
femaleSatisfaction = []
maleSatisfaction = []

# Distinguish female from male data
iterator = 0
for person in gender:
    if person == 1:
        maleIncome.append(income[iterator])
        maleProductivity.append(productivity[iterator])
        maleSkills.append(skills[iterator])
        maleSatisfaction.append(satisfaction[iterator])
    else:
        femaleIncome.append(income[iterator])
        femaleProductivity.append(productivity[iterator])
        femaleSkills.append(skills[iterator])
        femaleSatisfaction.append(satisfaction[iterator])
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


# Box plot
ageMax = np.max(age)
ageMin = np.min(age)
ageMedian = np.median(age)
ageQ1 = np.quantile(age, 0.25)
ageQ3 = np.quantile(age, 0.75)
print('Q1: ', ageQ1)
print('Q2: ', ageQ3)

boxData = [age]
fig3, ax3 = plt.subplots()
ax3.set_title('max, min, median, the first and third quartile box plot of Age')
ax3.boxplot(boxData, showmeans=True)
plt.xlabel('Age')
plt.show()


# Ex 1.c: mean and Standard Deviation of Income
incomeMean = np.mean(income)
incomeStandardDeviation = np.std(income)

print('Income mean: ', incomeMean)
print('Income Standard Deviation: ', incomeStandardDeviation)

# the histogram of the data
n, bins, patches = plt.hist(income, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Gross Annual Income in 1000s of GBP')
plt.ylabel('Probability')
plt.title('Histogram of Income')
plt.xlim(np.min(income) + 5, np.max(income) + 5)
#plt.ylim(0, 0.03)
plt.grid(True)
plt.show()


# Ex 2
x = income
y = quality

plt.scatter(x, y, c="g", label="Relationship between Income & Rated Quality")
plt.xlabel("Income")
plt.ylabel("Rated Quality")
plt.legend(loc='upper left')
plt.show()

# Find the simple regression model where income is the dependent variable and rated quality is the independent
# What is the determination coefficient?

# Library solution
x = quality
y = income

correlation_matrix = np.corrcoef(x, y)
correlation_xy = correlation_matrix[0,1]
detCoeff = correlation_xy ** 2
print('Library (numpy) solution: Our calculated determination coefficient is: ', detCoeff) 


# DIY solution Following Lecture 11 Simple Regression

x = np.array(quality) # independent
y = np.array(income)  # dependent

xMean = np.mean(x)
yMean = np.mean(y)

b1 = np.sum((x - xMean) * (y - yMean) / np.sum(np.power(x - xMean, 2)))
b0 = yMean - (b1 * xMean)

yEst = b0 + (b1 * x)

sign = '+' if b1 > 0 else ''
print('Estimated regression equation: yEst = ', b0, sign, b1, '* x')

# calculate the error sum squares (SSE) and the total corrected sum squares (SST)
SSE = np.sum(np.power(y - yEst, 2))
SST = np.sum(np.power(y - yMean, 2))

# calculate the determination coefficient R^2
R2 = 1 - (SSE / SST)
print('DIY: Our calculated determination coefficient is: ', R2) 


# Ex 3. Multiple Regression Model. 
# dependent: satis
# independent: commit, autonom, income, skill, rated quality, age, years 
# Following Lecture 11, Multiple Regression

Y = satisfaction
XT = np.array([np.ones(len(Y)), commitment, autonomy, income, skills, quality, age, years]) # X transpose
X = XT.transpose()

XTX = XT.dot(X)
XTY = XT.dot(Y)

B = np.linalg.inv(XTX).dot(XTY)
print('Variable weights:')
print(B)
print('Income and years seem to have the lowest significance at weights of ~0.04 and ~-0.02 respectively.')

YEst = X.dot(B)
SSE = np.sum(np.power(Y - YEst, 2))
print('This gives an error sum of squares equal to: ', SSE)

# Dropping income and years
print('Dropping the income and years as independent variables.')
XT = np.array([np.ones(len(Y)), commitment, autonomy, skills, quality, age]) # X transpose
X = XT.transpose()

XTX = XT.dot(X)
XTY = XT.dot(Y)

B = np.linalg.inv(XTX).dot(XTY)
YEst = X.dot(B)
SSE = np.sum(np.power(Y - YEst, 2))
print('This gives an error sum of squares equal to: ', SSE)
# They are off by ~1% one from the other, so dropping those definitely is for the better


# Ex 4. Find confidence interval of job satisfaction
confidenceLevel = 0.95
ciSatisfaction = spStats.t.interval(confidenceLevel, len(satisfaction) - 1, loc=np.mean(satisfaction), scale=spStats.sem(satisfaction))
print('The confidence interval of job satisfaction for all genders was: ', end='')
print(ciSatisfaction)

# Find confidence interval of difference in job satisfaction between men and women

# Clean satisfaction data, as both female and male data need to have same length
# Create local copies to mess with
tmpMaleSatisfaction = maleSatisfaction.copy()
tmpFemaleSatisfaction = femaleSatisfaction.copy()
nMale = len(tmpMaleSatisfaction)
nFemale = len(tmpFemaleSatisfaction)

# Python dataToClean to be a reference to either of the two NOT a copy of the values
dataToClean = tmpFemaleSatisfaction if nFemale > nMale else tmpMaleSatisfaction
nDataToClean = len(dataToClean)

# Get rid of the first elements of the biggest array and replace on original array
dataToClean.sort()
dataToClean = np.delete(dataToClean, range(0, abs(nFemale - nMale)))
if nFemale > nMale:
    tmpFemaleSatisfaction = dataToClean.copy()
else:
    tmpMaleSatisfaction = dataToClean.copy()

# Get the diff and output the answer
diffSatisfaction = np.abs(np.array(tmpFemaleSatisfaction) - np.array(tmpMaleSatisfaction))
ciSatisfaction = spStats.t.interval(confidenceLevel, len(diffSatisfaction) - 1, loc=np.mean(diffSatisfaction), scale=spStats.sem(diffSatisfaction))
print('The confidence interval of difference in job satisfaction between men and women was: ', end='')
print(ciSatisfaction)


# Ex 5. Mann-Whitney-Wilcoxon test to see if there is any significant difference in skill between men and women
mwwTest = spStats.mannwhitneyu(femaleSkills, maleSkills)
print('Mann-Whitney-Wilcoxon test to see if there is any significant difference in skill between men and women')
print(mwwTest)