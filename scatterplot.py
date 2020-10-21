import matplotlib.pyplot as plt
import dataGetter as data

def prepare():
    x = data.income
    y = data.quality

    plt.scatter(x, y, c="g", label="Relationship between Income & Rated Quality")
    plt.xlabel("Income")
    plt.ylabel("Rated Quality")
    plt.legend(loc='upper left')

def show():
    prepare()
    plt.show()