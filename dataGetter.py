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