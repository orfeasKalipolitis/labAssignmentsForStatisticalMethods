import pandas as pd
import numpy as np

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