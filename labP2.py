import dataGetterCOVID as data
import p2ex1 as ex1

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