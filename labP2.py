import dataGetterCOVID as data
import p2ex1 as ex1
import p2ex2_3 as ex2_3
import p2ex4 as ex4
import p2ex5 as ex5
import p2ex6 as ex6

print('Lab assignment - Part 2')
print()
print('Exercise 1: Descriptive statistics analysis for at least two qualitative and quantitative variables')

# Create the data as needed
# Get the first 25 days of data
days = data.dataFrames[:25][:].copy()
labels = []

# Check confirmed in Abbeville and Acadia
# Sample every 5 days
abbevilleConfirmed = []
acadiaConfirmed = []

for dayOff in range(0, len(days), 5):
    abbevilleConfirmed.append(days[dayOff]['Confirmed'][0])
    acadiaConfirmed.append(days[dayOff]['Confirmed'][1])
    labels.append('Day ' + str(data.startingDate + dayOff))
    
# Print a comparative bar chart between the two
ex1.comparativeBarChart(labels, 'Confirmed Cases', abbevilleConfirmed, acadiaConfirmed, 'Abbeville', 'Acadia', 'Confirmed cases in Abbeville and Acadia')

# Prepare data for bar chart
# We will be looking at the first day as well as 30 days later

day0 = data.dataFrames[0]
day30 = data.dataFrames[29]

# We will be using the first 10 counties
confirmed0 = []
confirmed30 = []
deaths0 = []
deaths30 = []
pieLabels = []
pieKeys = []
for town in range(4):
    pieLabels.append(day0['Admin2'][town])
    pieKeys.append(town)
    [confirmed0.append(town) for case in range(day0['Confirmed'][town])]
    [confirmed30.append(town) for case in range(day30['Confirmed'][town])]
    [deaths0.append(town) for case in range(day0['Deaths'][town])]
    [deaths30.append(town) for case in range(day30['Deaths'][town])]

# Pie plots for confirmed cases
ex1.pieChart(pieLabels, confirmed0, pieKeys)
ex1.pieChart(pieLabels, confirmed30, pieKeys)

# Pie plots for confirmed deaths as a result of the virus
ex1.pieChart(pieLabels, deaths0, pieKeys)
ex1.pieChart(pieLabels, deaths30, pieKeys)

print()
print('Exercise 2: Confidence interval for one quantitative variable; Confidence interval for difference')

print()
print('Quantitative variable: Deaths on the first 1000 US counties. On the Day', data.startingDate)
ex2_3.confidenceInterval(days[0]['Deaths'][1:1000])

print()
print('Quantitative variable: Deaths globally. On the Day', data.startingDate)
ex2_3.confidenceInterval(days[0]['Deaths'])

print()
print('Quantitative variable: Deaths on the first 1000 US counties. On the Day', data.startingDate + 30)
ex2_3.confidenceInterval(data.dataFrames[29]['Deaths'][1:1000])

print()
print('Quantitative variable: Deaths globally. On the Day', data.startingDate + 30)
ex2_3.confidenceInterval(data.dataFrames[29]['Deaths'])

print()
print('Quantitative variable: Incidence rate on the first 1000 US counties. On the Day', data.startingDate)
ex2_3.confidenceInterval(data.dataFrames[0]['Incidence_Rate'].fillna(0)[1:1000])

print()
print('Quantitative variable: Incidence rate on the first 1000 US counties. On the Day', data.startingDate + 30)
ex2_3.confidenceInterval(data.dataFrames[29]['Incidence_Rate'].fillna(0)[1:1000])

print()
print('Exercise 3: ANOVA')

print()
print('Quantitative variable1: Deaths on the first 1000 US counties. On the Day', data.startingDate)
print('Quantitative variable2: Incidence rate on the first 1000 US counties. On the Day', data.startingDate)
ex2_3.confidenceIntervalDifference(data.dataFrames[0]['Deaths'][1:1000], data.dataFrames[0]['Incidence_Rate'].fillna(0)[1:1000])

print()
print('Quantitative variable1: Deaths on the first 1000 US counties. On the Day', data.startingDate + 30)
print('Quantitative variable2: Incidence rate on the first 1000 US counties. On the Day', data.startingDate + 30)
ex2_3.confidenceIntervalDifference(data.dataFrames[29]['Deaths'][1:1000], data.dataFrames[29]['Incidence_Rate'].fillna(0)[1:1000])

print()
print('Exercise 4: Non-parametric test for some of your variables and even compare the conclusion(s) with ANOVA')

print()
print('Quantitative variable1: Deaths on the first 1000 US counties. On the Day', data.startingDate)
print('Quantitative variable2: Incidence rate on the first 1000 US counties. On the Day', data.startingDate)
ex4.mannWhitneyWilcoxonTest(data.dataFrames[0]['Deaths'][1:1000], data.dataFrames[0]['Incidence_Rate'].fillna(0)[1:1000])

print()
print('Quantitative variable1: Deaths on the first 1000 US counties. On the Day', data.startingDate + 30)
print('Quantitative variable2: Incidence rate on the first 1000 US counties. On the Day', data.startingDate + 30)
ex4.mannWhitneyWilcoxonTest(data.dataFrames[29]['Deaths'][1:1000], data.dataFrames[29]['Incidence_Rate'].fillna(0)[1:1000])

print()
print('Exercise 5: Correlation analysis, specially the strongest correlation and statistically not significant relation(s)')

print()
ex5.doTTests(data.dataFrames[0]['Confirmed'][1:1000], data.dataFrames[0]['Deaths'][1:1000], data.dataFrames[0]['Active'][1:1000], data.dataFrames[0]['Incidence_Rate'].fillna(0)[1:1000])

print()
ex5.doTTests(data.dataFrames[29]['Confirmed'][1:1000], data.dataFrames[29]['Deaths'][1:1000], data.dataFrames[29]['Active'][1:1000], data.dataFrames[29]['Incidence_Rate'].fillna(0)[1:1000])

print()
print('Exercise 6: Regression Analysis')

print()
ex6.regressionAnalysis(data.dataFrames[0]['Confirmed'][1:1000], data.dataFrames[0]['Deaths'][1:1000], data.dataFrames[0]['Active'][1:1000], data.dataFrames[0]['Incidence_Rate'].fillna(0)[1:1000], confidence=0.9)

print()