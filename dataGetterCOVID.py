import pandas as pd
import numpy as np
from pathlib import Path

dataFolder = Path("csse_covid_19_daily_reports/")
year = 2020
ext = '.csv'
dataFrames = []
debug = True

# Trying to open 1 csv file for each day of the year
# Catching exceptions for days that we either don't have data for,
# haven't happened yet, or don't exist
for month in range(1, 12):
    for day in range(1, 31):
        fileToOpen = str(month).zfill(2) + '-' + str(day).zfill(2) + '-' + str(year) + ext
        fileToOpenRelativePath = dataFolder / fileToOpen
        try:
            dataFrame = pd.read_csv(fileToOpenRelativePath)
            dataFrames.append(dataFrame)
        except Exception as e:
            if debug:
                print(e)
            else:
                print(end='')

print()

# We choose to keep only part of the data, so we have all the possible data points
dataFrames = dataFrames[126:][:]
startingDate = 127
