
import matplotlib.pyplot as plt
from collections import Counter
from scipy import stats as spStats
import dataGetter as data
import barplot

# Ex 1a. Barplot
barplot.show()


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['White', 'Asian', 'West Indian', 'African', 'other']
ethnicGroups = Counter(data.ethnic)
sizes = [ethnicGroups[1], ethnicGroups[2], ethnicGroups[3], ethnicGroups[4], ethnicGroups[5]]
explode = (0.1, 0.2, 0.3, 0.4, 0.5)  # "explode" each slice a different amount

fig2, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# Box plot
ageMax = np.max(data.age)
ageMin = np.min(data.age)
ageMedian = np.median(data.age)
ageQ1 = np.quantile(data.age, 0.25)
ageQ3 = np.quantile(data.age, 0.75)
print('Q1: ', ageQ1)
print('Q2: ', ageQ3)

boxData = [data.age]
fig3, ax3 = plt.subplots()
ax3.set_title('max, min, median, the first and third quartile box plot of Age')
ax3.boxplot(boxData, showmeans=True)
plt.xlabel('Age')
plt.show()


# Ex 1.c: mean and Standard Deviation of Income
incomeMean = np.mean(data.income)
incomeStandardDeviation = np.std(data.income)

print('Income mean: ', incomeMean)
print('Income Standard Deviation: ', incomeStandardDeviation)

# the histogram of the data
n, bins, patches = plt.hist(data.income, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Gross Annual Income in 1000s of GBP')
plt.ylabel('Probability')
plt.title('Histogram of Income')
plt.xlim(np.min(data.income) + 5, np.max(data.income) + 5)
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
print('Mann-Whitney-Wilcoxon test to see if there is any significance in skill between men and women:')
print(mwwTest)


# Ex 6. Kruskal-Wallis  test  to  see  if  there  is  any  significance  in  absence  among  ethnic group

# Prepare ethnic group data for absence
whiteAbsence = []
asianAbsence = []
westIndianAbsence = []
africanAbsence = []

for i in range(0, len(absence)):
    # White
    if(ethnic[i] == 1):
        whiteAbsence.append(absence[i])
    # Asian
    elif(ethnic[i] == 2):
        asianAbsence.append(absence[i])
    # West Indian
    elif(ethnic[i] == 3):
        westIndianAbsence.append(absence[i])
    # African
    elif(ethnic[i] == 4):
        africanAbsence.append(absence[i])

# Do the Kruskal-Wallis test and output the results
kwTest = spStats.kruskal(whiteAbsence, asianAbsence, westIndianAbsence, africanAbsence)
print('Kruskal-Wallis test to see if there is any significance in absence among ethnic groups:')
print(kwTest)

# If one-way ANOVA reports a P value of <0.05, 
# you reject the null hypothesis that all the data 
# are sampled from populations with the same mean.

# Do the One-Way Anova test and output the results
anovaTest = spStats.f_oneway(whiteAbsence, asianAbsence, westIndianAbsence, africanAbsence)
print('One-Way Anova test to see if there is any significance in absence among ethnic groups:')
print(anovaTest)


# Ex 7. Income class and its relationship with skill

# Create 3 separate income groups: low, middle and high
incomeQ = np.quantile(income, [0.25, 0.75])
lowIncome = []
skillLowIncome = []
middleIncome = []
skillMiddleIncome = []
highIncome = []
skillHighIncome = []

for i in range(0, len(income)):
    # [min, Q1]
    if income[i] <= incomeQ[0]:
        lowIncome.append(income[i])
        skillLowIncome.append(skills[i])
    # (Q1, Q3]
    elif income[i] <= incomeQ[1]:
        middleIncome.append(income[i])
        skillMiddleIncome.append(skills[i])
    # (Q3, max]
    else:
        highIncome.append(income[i])
        skillHighIncome.append(skills[i])

# Print out the mean skill of each income group
print('Mean low income skill:', np.mean(skillLowIncome))
print('Mean middle income skill:', np.mean(skillMiddleIncome))
print('Mean high income skill:', np.mean(skillHighIncome))

# Use the One-Way Anova test to see if there is significant different in the income groups' mean skill
anovaTest = spStats.f_oneway(skillLowIncome, skillMiddleIncome, skillHighIncome)
print('One-Way Anova test to see if there is significant different in the income groups\' mean skill:')
print(anovaTest)