#aedan wells
#11/13/2022
#finds the features for the given datasets
import pandas as pd

df = pd.read_csv("data/daily-al-ga.csv", low_memory=False)
print(df.columns.values)