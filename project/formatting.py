#aedan wells
#11/13/2022
#finds the features for the given datasets
import pandas as pd
import datetime

monthly = ["monthly-al-ga.csv", "monthly-hi-md.csv", "monthly-ma-nj.csv", "monthly-nm-sc.csv", "monthly-sd-wy.csv"]

us_states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']

#columns for each 50 states, will be like each month
length = [0]*50

data1 = {"state": us_states, "mean1": length, "mean2": length, "mean3": length, "mean4": length, "mean5": length, "mean6": length, "mean7": length, "mean8": length, "mean9": length, "mean10": length, "mean11": length, "mean12": length}
df1 = pd.DataFrame(data1)


str_format = "%Y-%m-%dT%H:%M:%S"
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        df1.loc[df1.index[df1['state'] == row['state']], "mean"+str(dt_object.month)] = row['MonthlyMeanTemperature']
df1.to_csv("data/monthly-mean-temp.csv")

#create mean pressure
#! Pressure for Rhode Island and arkansas is all 0, 0 for some small ones (m6 for wyoming,
#! m3 for oregon, m3 for north carolina, m9 for minnisota, and m4 for california)
data2 = {"state": us_states, "press1": length, "press2": length, "press3": length, "press4": length, "press5": length, "press6": length, "press7": length, "press8": length, "press9": length, "press10": length, "press11": length, "press12": length}
pressure = pd.DataFrame(data2)
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        pressure.loc[pressure.index[pressure['state'] == row['state']], "press"+str(dt_object.month)] = row['MonthlyStationPressure']
pressure = pressure.fillna(0)
pressure.to_csv("data/monthly-station-pressure.csv")

#Monthly Greatest Predipitation
#!rhode island is missing precipitation
data3 = {"state": us_states, "precip1": length, "precip2": length, "precip3": length, "precip4": length, "precip5": length, "precip6": length, "precip7": length, "precip8": length, "precip9": length, "precip10": length, "precip11": length, "precip12": length}
precip = pd.DataFrame(data3)
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        row['MonthlyGreatestPrecip'] = str(row['MonthlyGreatestPrecip']).replace("s", "")
        row['MonthlyGreatestPrecip'] = str(row['MonthlyGreatestPrecip']).replace("T", "0.00")
        precip.loc[precip.index[precip['state'] == row['state']], "precip"+str(dt_object.month)] = float(row['MonthlyGreatestPrecip'])
precip = precip.fillna(0)
precip.to_csv("data/monthly-greatest-precip.csv")

#maximum tempearture
data4 = {"state": us_states, "max1": length, "max2": length, "max3": length, "max4": length, "max5": length, "max6": length, "max7": length, "max8": length, "max9": length, "max10": length, "max11": length, "max12": length}
precip = pd.DataFrame(data4)
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        row['MonthlyMaximumTemperature'] = str(row['MonthlyMaximumTemperature']).replace("s", "")
        precip.loc[precip.index[precip['state'] == row['state']], "max"+str(dt_object.month)] = float(row['MonthlyMaximumTemperature'])
precip = precip.fillna(0)
precip.to_csv("data/monthly-max-temp.csv")

#min tempearture
data5 = {"state": us_states, "min1": length, "min2": length, "min3": length, "min4": length, "min5": length, "min6": length, "min7": length, "min8": length, "min9": length, "min10": length, "min11": length, "min12": length}
precip = pd.DataFrame(data5)
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        row['MonthlyMinimumTemperature'] = str(row['MonthlyMinimumTemperature']).replace("s", "")
        precip.loc[precip.index[precip['state'] == row['state']], "min"+str(dt_object.month)] = float(row['MonthlyMinimumTemperature'])
precip = precip.fillna(0)
precip.to_csv("data/monthly-min-temp.csv")

#total snowfall
data6 = {"state": us_states, "snow1": length, "snow2": length, "snow3": length, "snow4": length, "snow5": length, "snow6": length, "snow7": length, "snow8": length, "snow9": length, "snow10": length, "snow11": length, "snow12": length}
precip = pd.DataFrame(data6)
#create mean temp here
for file in monthly:
    df2 = pd.read_csv("data/"+file, low_memory=False)
    for index, row in df2.iloc[1: , :].iterrows():
        dt_object = datetime.datetime.strptime(row['DATE'], str_format)
        row['MonthlyTotalSnowfall'] = str(row['MonthlyTotalSnowfall']).replace("T", "0")
        precip.loc[precip.index[precip['state'] == row['state']], "snow"+str(dt_object.month)] = float(row['MonthlyTotalSnowfall'])
precip = precip.fillna(float(0))
precip.to_csv("data/monthly-total-snowfall.csv")
