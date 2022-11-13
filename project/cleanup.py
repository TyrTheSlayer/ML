#aedan wells
#11/13/2022
#cleanup file
import pandas as pd

filelist = ['al-ga.csv', 'hi-md.csv', 'ma-nj.csv', 'nm-sc.csv', 'sd-wy.csv']


for file in filelist:
    df = pd.read_csv("data/"+file, low_memory=False)
    df = df.drop(["BackupDirection","BackupDistance","BackupDistanceUnit","BackupElements","BackupElevation","BackupElevationUnit","BackupEquipment","BackupLatitude","BackupLongitude","BackupName", "WindEquipmentChangeDate"], axis=1)
    #grab labels
    labels = pd.DataFrame()
    labels = labels.append(df.iloc[0], ignore_index=True)

    #grab daily
    daily = df[df["DailyAverageDryBulbTemperature"].notnull()]
    labels = labels.append(daily, ignore_index=True)
    labels.to_csv("data/daily-"+file)
    labels = pd.DataFrame()
    labels = labels.append(df.iloc[0], ignore_index=True)

    #grab monthly
    monthly = df[df["MonthlyMeanTemperature"].notnull()]
    labels = labels.append(monthly, ignore_index=True)
    labels.to_csv("data/monthly-"+file)
    labels = pd.DataFrame()
    labels = labels.append(df.iloc[0], ignore_index=True)

    #grab hourly
    hourly = df[df["HourlyDryBulbTemperature"].notnull()]
    labels = labels.append(hourly, ignore_index=True)
    labels.to_csv("data/hourly-"+file)