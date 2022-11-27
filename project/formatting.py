#aedan wells
#11/13/2022
#finds the features for the given datasets
import pandas as pd
import datetime

monthly = ["monthly-al-ga.csv", "monthly-hi-md.csv", "monthly-ma-nj.csv", "monthly-nm-sc.csv", "monthly-sd-wy.csv"]

us_states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']

#columns for each 50 states, will be like each month
length = [0]*50

data = {"state": us_states, "mean-m1": length, "mean-m2": length, "mean-m3": length, "mean-m4": length, "mean-m5": length, "mean-m6": length, "mean-m7": length, "mean-m8": length, "mean-m9": length, "mean-m10": length, "mean-m11": length, "mean-m12": length}
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
data = {"state": us_states, "press-m1": length, "press-m2": length, "press-m3": length, "press-m4": length, "press-m5": length, "press-m6": length, "press-m7": length, "press-m8": length, "press-m9": length, "press-m10": length, "press-m11": length, "press-m12": length}
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
data = {"state": us_states, "precip-m1": length, "precip-m2": length, "precip-m3": length, "precip-m4": length, "precip-m5": length, "precip-m6": length, "precip-m7": length, "precip-m8": length, "precip-m9": length, "precip-m10": length, "precip-m11": length, "precip-m12": length}
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
data = {"state": us_states, "max-m1": length, "max-m2": length, "max-m3": length, "max-m4": length, "max-m5": length, "max-m6": length, "max-m7": length, "max-m8": length, "max-m9": length, "max-m10": length, "max-m11": length, "max-m12": length}
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
data = {"state": us_states, "min-m1": length, "min-m2": length, "min-m3": length, "min-m4": length, "min-m5": length, "min-m6": length, "min-m7": length, "min-m8": length, "min-m9": length, "min-m10": length, "min-m11": length, "min-m12": length}
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

#total snowfall
data = {"state": us_states, "snow-m1": length, "snow-m2": length, "snow-m3": length, "snow-m4": length, "snow-m5": length, "snow-m6": length, "snow-m7": length, "snow-m8": length, "snow-m9": length, "snow-m10": length, "snow-m11": length, "snow-m12": length}
precip = pd.DataFrame(data)
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        row['MonthlyTotalSnowfall'] = str(row['MonthlyTotalSnowfall']).replace("T", "0")
        precip.loc[precip.index[precip['state'] == row['state']], "m"+str(dt_object.month)] = float(row['MonthlyTotalSnowfall'])
precip = precip.fillna(float(0))
precip.to_csv("data/monthly-total-snowfall.csv")
