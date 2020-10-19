
import pandas as pd

dataFilename = "jss13_ht20.xlsx"

dataFrame = pd.read_excel(dataFilename, sheet_name=None)

print(dataFrame)