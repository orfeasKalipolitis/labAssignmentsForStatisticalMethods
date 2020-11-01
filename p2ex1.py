import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def prepareChartData(xLabelsForChart, yLabelForChart, aVar, bVar, dataLabelA, dataLabelB, titleForChart, axis):
    labels = xLabelsForChart
    a = aVar
    b = bVar

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    rects1 = axis.bar(x - width/2, a, width, label=dataLabelA)
    rects2 = axis.bar(x + width/2, b, width, label=dataLabelB)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    axis.set_ylabel(yLabelForChart)
    axis.set_title(titleForChart)
    axis.set_xticks(x)
    axis.set_xticklabels(labels)
    axis.legend()

# Works for comparing any 2 sets of data points that have been made into n-pairs
# each pair-group is represented as 2 bar plots one next to each other for comparison
#
# Parameters:
# groupLabels: an array of string labels. one string for each group on the x-axis
# yLabel: the label for the y-axis
# dataA: the vector of one of the data points
# dataB: the vector of of the another data point
# labelDataA: a string for what dataA represents
# labelDataB: a string for what dataB represents
# title: a string for the title of the chart
#
# Notes:
# the vectors groupLabels, dataA and dataB should all have the same length
def comparativeBarChart(groupLabels, yLabel, dataA, dataB, labelDataA, labelDataB, title):
    fig, ax = plt.subplots()
    prepareChartData(groupLabels, yLabel, dataA, dataB, labelDataA, labelDataB, title, ax)
    plt.show()

comparativeBarChart()
