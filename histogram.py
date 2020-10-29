import numpy as np
import matplotlib.pyplot as plt
import dataGetter as data
from matplotlib.ticker import PercentFormatter

def prepare():
    n, bins, patches = plt.hist(data.income, 50, density=True, facecolor='g', alpha=0.75)

    plt.xlabel('Gross Annual Income [1000s of GBP]')
    plt.ylabel('Probability [percentage]')
    plt.title('Histogram of Income')
    plt.xlim(np.min(data.income) + 5, np.max(data.income) + 5)
    #plt.ylim(0, 0.03)
    plt.grid(True)

def show():
    prepare()
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()
