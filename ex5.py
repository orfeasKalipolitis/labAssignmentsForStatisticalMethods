import numpy as np
import dataGetter as data
from scipy import stats as spStats

# do the mann whitney test
mwwTest = spStats.mannwhitneyu(data.femaleSkills, data.maleSkills)

localFemSkills = np.array(data.femaleSkills.copy())
localMaleSkills = np.array(data.maleSkills.copy())

# Shuffle the male skills and get rid of the excess ones
np.random.shuffle(localMaleSkills)
localMaleSkills = (localMaleSkills[np.abs(len(localFemSkills) - len(localMaleSkills)):])

diffSkills = np.abs(localMaleSkills - localFemSkills)

# get the confidence intervan of the difference in skill
confidenceLevel = 0.95
ciSkillDifference = spStats.t.interval(confidenceLevel, len(diffSkills) - 1, loc=np.mean(diffSkills), scale=spStats.sem(diffSkills))

def show():
    print('Mann-Whitney-Wilcoxon test to see if there is any significance in skill between men and women:')
    print(mwwTest)
    print('')
    print(ciSkillDifference)
