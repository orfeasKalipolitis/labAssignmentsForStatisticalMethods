import numpy as np
from scipy import stats as spStats
import dataGetter as data
import barplot, pieChart, boxplot, histogram, scatterplot
import confidence, simpleRegression, multipleRegression

print()
# Ex 1a. Barplot
barplot.show()


print()
# Ex 1a. Pie chart, where the slices will be ordered and plotted counter-clockwise:
pieChart.show()


print()
# Ex 1b. Box plot
boxplot.show()


print()
# Ex 1.c: mean and Standard Deviation of Income
incomeMean = np.mean(data.income)
incomeStandardDeviation = np.std(data.income)

print('Income mean: ', incomeMean)
print('Income Standard Deviation: ', incomeStandardDeviation)


print()
# the histogram of the data
input('Press Enter to continue: ')
histogram.show()


print()
# Ex 2
input('Press Enter to continue: ')
scatterplot.show()


print()
# Find the simple regression model where income is the dependent variable and rated quality is the independent
# What is the determination coefficient?
simpleRegression.show()


print()
# Ex 3. Multiple Regression Model. 
# dependent: satis
# independent: commit, autonom, income, skill, rated quality, age, years 
# Following Lecture 11, Multiple Regression
multipleRegression.show()


print()
# Ex 4. Find confidence interval of job satisfaction
confidence.show()


print()
# Ex 5. Mann-Whitney-Wilcoxon test to see if there is any significant difference in skill between men and women
mwwTest = spStats.mannwhitneyu(data.femaleSkills, data.maleSkills)
print('Mann-Whitney-Wilcoxon test to see if there is any significance in skill between men and women:')
print(mwwTest)


print()
# Ex 6. Kruskal-Wallis  test  to  see  if  there  is  any  significance  in  absence  among  ethnic group

# Do the Kruskal-Wallis test and output the results
kwTest = spStats.kruskal(data.whiteAbsence, data.asianAbsence, data.westIndianAbsence, data.africanAbsence)
print('Kruskal-Wallis test to see if there is any significance in absence among ethnic groups:')
print(kwTest)

# If one-way ANOVA reports a P value of <0.05, 
# you reject the null hypothesis that all the data 
# are sampled from populations with the same mean.

# Do the One-Way Anova test and output the results
anovaTest = spStats.f_oneway(data.whiteAbsence, data.asianAbsence, data.westIndianAbsence, data.africanAbsence)
print('One-Way Anova test to see if there is any significance in absence among ethnic groups:')
print(anovaTest)


print()
# Ex 7. Income class and its relationship with skill

# Print out the mean skill of each income group
print('Mean low income skill:', np.mean(data.skillLowIncome))
print('Mean middle income skill:', np.mean(data.skillMiddleIncome))
print('Mean high income skill:', np.mean(data.skillHighIncome))

# Use the One-Way Anova test to see if there is significant different in the income groups' mean skill
anovaTest = spStats.f_oneway(data.skillLowIncome, data.skillMiddleIncome, data.skillHighIncome)
print('One-Way Anova test to see if there is significant different in the income groups\' mean skill:')
print(anovaTest)