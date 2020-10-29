import numpy as np
from scipy import stats as spStats
import dataGetter as data

# default confidence level
confidenceLevel = 0.95

def confidenceInterval(quantitativeVar, confidence=confidenceLevel):
    ciSatisfaction = spStats.t.interval(confidence, len(quantitativeVar) - 1, loc=np.mean(quantitativeVar), scale=spStats.sem(quantitativeVar))
    print('The confidence interval for your quantitative variable is:')
    print(ciSatisfaction)

def confidenceIntervalDifference(quantitativeVar1, quantitativeVar2, confidence=confidenceLevel):
    diffSatisfaction = np.abs(np.array(quantitativeVar1) - np.array(quantitativeVar2))
    ciSatisfaction = spStats.t.interval(confidence, len(diffSatisfaction) - 1, loc=np.mean(diffSatisfaction), scale=spStats.sem(diffSatisfaction))
    print()
    print('The confidence interval for the difference of your two variables is:')
    print(ciSatisfaction)
    print()
    anovaTest(quantitativeVar1, quantitativeVar2)

def anovaTest(var1, var2):
    anova = spStats.f_oneway(var1, var2)
    print('In order to compare them further, we are also performing an ANOVA analysis:')
    print('If the p-value is less than or equal to your significance level,')
    print('you should reject the null hypothesis and conclude that not all of population means are equal.')
    print(anova)
