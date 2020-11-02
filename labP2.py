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