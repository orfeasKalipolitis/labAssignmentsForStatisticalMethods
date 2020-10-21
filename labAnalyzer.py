import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as spStats
import dataGetter as data
import barplot, pieChart, boxplot, histogram, scatterplot, simpleRegression, multipleRegression

# Ex 1a. Barplot
barplot.show()


# Ex 1a. Pie chart, where the slices will be ordered and plotted counter-clockwise:
pieChart.show()


# Ex 1b. Box plot
boxplot.show()


# Ex 1.c: mean and Standard Deviation of Income
incomeMean = np.mean(data.income)
incomeStandardDeviation = np.std(data.income)

print('Income mean: ', incomeMean)
print('Income Standard Deviation: ', incomeStandardDeviation)

# the histogram of the data
input('Press Enter to continue: ')
histogram.show()


# Ex 2
input('Press Enter to continue: ')
scatterplot.show()

# Find the simple regression model where income is the dependent variable and rated quality is the independent
# What is the determination coefficient?
simpleRegression.show()


# Ex 3. Multiple Regression Model. 
# dependent: satis
# independent: commit, autonom, income, skill, rated quality, age, years 
# Following Lecture 11, Multiple Regression
multipleRegression.show()


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