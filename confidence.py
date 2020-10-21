import numpy as np
import dataGetter as data
from scipy import stats as spStats

confidenceLevel = 0.95
ciSatisfaction = spStats.t.interval(confidenceLevel, len(data.satisfaction) - 1, loc=np.mean(data.satisfaction), scale=spStats.sem(data.satisfaction))


# Find confidence interval of difference in job satisfaction between men and women

# Clean satisfaction data, as both female and male data need to have same length
# Create local copies to mess with
tmpMaleSatisfaction = data.maleSatisfaction.copy()
tmpFemaleSatisfaction = data.femaleSatisfaction.copy()
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
ciSatisfaction2 = spStats.t.interval(confidenceLevel, len(diffSatisfaction) - 1, loc=np.mean(diffSatisfaction), scale=spStats.sem(diffSatisfaction))


def show():
    print('The confidence interval of job satisfaction for all genders was: ', end='')
    print(ciSatisfaction)
    print('The confidence interval of difference in job satisfaction between men and women was: ', end='')
    print(ciSatisfaction2)