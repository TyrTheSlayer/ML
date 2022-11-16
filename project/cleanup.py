#aedan wells
#11/13/2022
#cleanup file
import pandas as pd

filelist = ['al-ga.csv', 'hi-md.csv', 'ma-nj.csv', 'nm-sc.csv', 'sd-wy.csv']
hourly_num = 0
daily_num = 0
monthly_num = 0

#df1.insert(0, 'ID', df1.index)
#df1.loc[df1['Abstract'].isnull(, 'Abstract'] = ''
for file in filelist:
    df = pd.read_csv("data/"+file, low_memory=False)
    df = df.drop(["BackupDirection","BackupDistance","BackupDistanceUnit","BackupElements","BackupElevation","BackupElevationUnit","BackupEquipment","BackupLatitude","BackupLongitude","BackupName", "WindEquipmentChangeDate"], axis=1)

    #set states
    df.insert(0, 'state', '')
    df.loc[df['STATION'] == 72323003856, 'state'] = 'alabama'
    df.loc[df['STATION'] == 70273026451, 'state'] = 'alaska'
    df.loc[df['STATION'] == 72278023183, 'state'] = 'arizona'
    df.loc[df['STATION'] == 72340003952, 'state'] = 'arkansas'
    df.loc[df['STATION'] == 72295023174, 'state'] = 'california'
    df.loc[df['STATION'] == 72565003017, 'state'] = 'colorado'
    df.loc[df['STATION'] == 72508014740, 'state'] = 'connecticut'
    df.loc[df['STATION'] == 72409313764, 'state'] = 'delaware'
    df.loc[df['STATION'] == 72202012839, 'state'] = 'florida'
    df.loc[df['STATION'] == 72219013874, 'state'] = 'georgia'
    df.loc[df['STATION'] == 91182022521, 'state'] = 'hawaii'
    df.loc[df['STATION'] == 72681024131, 'state'] = 'idaho'
    df.loc[df['STATION'] == 72530094846, 'state'] = 'illinois'
    df.loc[df['STATION'] == 72438093819, 'state'] = 'indiana'
    df.loc[df['STATION'] == 74455094982, 'state'] = 'iowa'
    df.loc[df['STATION'] == 72450003928, 'state'] = 'kansas'
    df.loc[df['STATION'] == 72423093821, 'state'] = 'kentucky'
    df.loc[df['STATION'] == 74754093915, 'state'] = 'louisiana'
    df.loc[df['STATION'] == 72607014606, 'state'] = 'maine'
    df.loc[df['STATION'] == 72406093721, 'state'] = 'maryland'
    df.loc[df['STATION'] == 72509014739, 'state'] = 'massachusetts'
    df.loc[df['STATION'] == 72537094847, 'state'] = 'michigan'
    df.loc[df['STATION'] == 72747694961, 'state'] = 'minnesota'
    df.loc[df['STATION'] == 72235003940, 'state'] = 'mississippi'
    df.loc[df['STATION'] == 72446003947, 'state'] = 'missouri'
    df.loc[df['STATION'] == 72677024033, 'state'] = 'montana'
    df.loc[df['STATION'] == 72550014942, 'state'] = 'nebraska'
    df.loc[df['STATION'] == 72484653123, 'state'] = 'nevada'
    df.loc[df['STATION'] == 74394514710, 'state'] = 'new hampshire'
    df.loc[df['STATION'] == 72407093730, 'state'] = 'new jersey'
    df.loc[df['STATION'] == 72365023050, 'state'] = 'new mexico'
    df.loc[df['STATION'] == 74486094789, 'state'] = 'new york'
    df.loc[df['STATION'] == 72306013722, 'state'] = 'north carolina'
    df.loc[df['STATION'] == 72753014914, 'state'] = 'north dakota'
    df.loc[df['STATION'] == 72429793812, 'state'] = 'ohio'
    df.loc[df['STATION'] == 72353013967, 'state'] = 'oklahoma'
    df.loc[df['STATION'] == 72698024229, 'state'] = 'oregon'
    df.loc[df['STATION'] == 72408013739, 'state'] = 'pennsylvania'
    df.loc[df['STATION'] == 99999954797, 'state'] = 'rhode island'
    df.loc[df['STATION'] == 72310013883, 'state'] = 'south carolina'
    df.loc[df['STATION'] == 72651014944, 'state'] = 'south dakota'
    df.loc[df['STATION'] == 72334013893, 'state'] = 'tennessee'
    df.loc[df['STATION'] == 72254013904, 'state'] = 'texas'
    df.loc[df['STATION'] == 72572024127, 'state'] = 'utah'
    df.loc[df['STATION'] == 72617014742, 'state'] = 'vermont'
    df.loc[df['STATION'] == 72308013737, 'state'] = 'virginia'
    df.loc[df['STATION'] == 72793024233, 'state'] = 'washington'
    df.loc[df['STATION'] == 72414013866, 'state'] = 'west virginia'
    df.loc[df['STATION'] == 72640014839, 'state'] = 'wisconsin'
    df.loc[df['STATION'] == 72564024018, 'state'] = 'wyoming'
    df.fillna(0)

    #grab labels
    labels = pd.DataFrame()
    labels = labels.append(df.iloc[0], ignore_index=True)

    #grab daily
    daily = df[df["DailyAverageDryBulbTemperature"].notnull()]
    value, features = daily.shape
    daily_num += value
    labels = labels.append(daily, ignore_index=True)
    labels.to_csv("data/daily-"+file)
    labels = pd.DataFrame()
    labels = labels.append(df.iloc[0], ignore_index=True)

    #grab monthly
    monthly = df[df["MonthlyMeanTemperature"].notnull()]
    value, features = monthly.shape
    monthly_num += value
    labels = labels.append(monthly, ignore_index=True)
    labels.to_csv("data/monthly-"+file)
    labels = pd.DataFrame()
    labels = labels.append(df.iloc[0], ignore_index=True)

    #grab hourly
    hourly = df[df["HourlyDryBulbTemperature"].notnull()]
    value, features = hourly.shape
    hourly_num += value
    labels = labels.append(hourly, ignore_index=True)
    labels.to_csv("data/hourly-"+file)

print("Daily: ", daily_num)
print("monthly: ", monthly_num)
print("hourly: ", hourly_num)