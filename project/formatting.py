#aedan wells
#11/13/2022
#finds the features for the given datasets
import pandas as pd

df = pd.read_csv("data/monthly-al-ga.csv", low_memory=False)
#print(df['MonthlyMeanTemperature'].to_string(index=False))
#al-ga starts with a NaN but rest is good
df = pd.read_csv("data/monthly-hi-md.csv", low_memory=False)
#print(df['MonthlyMeanTemperature'].to_string(index=False))
#hi-md has 2 NaNs, one at the beginning and one in the middle
df = pd.read_csv("data/monthly-ma-nj.csv", low_memory=False)
print(df['MonthlyMeanTemperature'].to_string(index=False))