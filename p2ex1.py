import dataGetterCOVID as data
import numpy as np
import matplotlib.pyplot as plt

# Create charts
labels = ['Day 147', 'Day 148']
x = np.arange(len(labels))
width = 0.4

fig, ax = plt.subplots()

# Working on day 0
indexGreece = 0
indexItaly = 0
countries = []
confirmed = []
for i in range(0, len(data.dataFrames)):
    confirmed.append(data.dataFrames[i]['Confirmed'])
    countries.append(data.dataFrames[i]['Country_Region'])

greeceFound = False
italyFound = False
for country in countries[0]:
    
    if country.lower() == 'Greece'.lower():
        greeceFound = True
    elif country.lower() == 'Italy'.lower():
        italyFound = True
    
    if not greeceFound:
        indexGreece = indexGreece + 1
    if not italyFound:
        indexItaly = indexItaly + 1
    
    if greeceFound and italyFound:
        break

if indexGreece >= len(countries):
    print('Greece not found')

if indexItaly >= len(countries):
    print('Italy not found')


rects1 = ax.bar(x - width, [confirmed[0][indexGreece], confirmed[1][indexGreece]], width, label=countries[0][indexGreece])
rects2 = ax.bar(x + width, [confirmed[0][indexItaly], confirmed[1][indexItaly]], width, label=countries[0][indexItaly])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of confirmed cases')
ax.set_title('Cases of COVID-19 in different countries')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

def show():
    plt.show()

show()