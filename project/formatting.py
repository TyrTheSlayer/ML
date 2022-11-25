#aedan wells
#11/13/2022
#finds the features for the given datasets
import pandas as pd
import datetime

monthly = ["monthly-al-ga.csv", "monthly-hi-md.csv", "monthly-ma-nj.csv", "monthly-nm-sc.csv", "monthly-sd-wy.csv"]

us_states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']

#columns for each 50 states, will be like each month
length = [0]*50

data = {"state": us_states, "m1": length, "m2": length, "m3": length, "m4": length, "m5": length, "m6": length, "m7": length, "m8": length, "m9": length, "m10": length, "m11": length, "m12": length}
df1 = pd.DataFrame(data)


str_format = "%Y-%m-%dT%H:%M:%S"
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        df1.loc[df1.index[df1['state'] == row['state']], "m"+str(dt_object.month)] = row['MonthlyMeanTemperature']
df1.to_csv("data/monthly-mean-temp.csv")

#create mean pressure
#! Pressure for Rhode Island and arkansas is all 0, 0 for some small ones (m6 for wyoming,
#! m3 for oregon, m3 for north carolina, m9 for minnisota, and m4 for california)
data = {"state": us_states, "m1": length, "m2": length, "m3": length, "m4": length, "m5": length, "m6": length, "m7": length, "m8": length, "m9": length, "m10": length, "m11": length, "m12": length}
pressure = pd.DataFrame(data)
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        pressure.loc[pressure.index[pressure['state'] == row['state']], "m"+str(dt_object.month)] = row['MonthlyStationPressure']
pressure = pressure.fillna(0)
pressure.to_csv("data/monthly-station-pressure.csv")

#Monthly Greatest Predipitation
#!rhode island is missing precipitation
data = {"state": us_states, "m1": length, "m2": length, "m3": length, "m4": length, "m5": length, "m6": length, "m7": length, "m8": length, "m9": length, "m10": length, "m11": length, "m12": length}
precip = pd.DataFrame(data)
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        row['MonthlyGreatestPrecip'] = str(row['MonthlyGreatestPrecip']).replace("s", "")
        row['MonthlyGreatestPrecip'] = str(row['MonthlyGreatestPrecip']).replace("T", "0.00")
        precip.loc[precip.index[precip['state'] == row['state']], "m"+str(dt_object.month)] = float(row['MonthlyGreatestPrecip'])
precip = precip.fillna(0)
precip.to_csv("data/monthly-greatest-precip.csv")

#maximum tempearture
data = {"state": us_states, "m1": length, "m2": length, "m3": length, "m4": length, "m5": length, "m6": length, "m7": length, "m8": length, "m9": length, "m10": length, "m11": length, "m12": length}
precip = pd.DataFrame(data)
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        row['MonthlyMaximumTemperature'] = str(row['MonthlyMaximumTemperature']).replace("s", "")
        precip.loc[precip.index[precip['state'] == row['state']], "m"+str(dt_object.month)] = float(row['MonthlyMaximumTemperature'])
precip = precip.fillna(0)
precip.to_csv("data/monthly-max-temp.csv")

#min tempearture
data = {"state": us_states, "m1": length, "m2": length, "m3": length, "m4": length, "m5": length, "m6": length, "m7": length, "m8": length, "m9": length, "m10": length, "m11": length, "m12": length}
precip = pd.DataFrame(data)
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        row['MonthlyMinimumTemperature'] = str(row['MonthlyMinimumTemperature']).replace("s", "")
        precip.loc[precip.index[precip['state'] == row['state']], "m"+str(dt_object.month)] = float(row['MonthlyMinimumTemperature'])
precip = precip.fillna(0)
precip.to_csv("data/monthly-min-temp.csv")
