import pandas as pd
import glob

path = '/bigdata/data/airline-on-time-performance/inflated/On_Time_On_Time_Performance_*.csv'
filelist = glob.glob(path)
depart_delay = pd.DataFrame()

for file in filelist:
    d = pd.read_csv(file, usecols=['DepDelayMinutes'])
    depart_delay = pd.concat([depart_delay, d], axis=0)

depart_delay = depart_delay['DepDelayMinutes'].mean(axis=0)
print(depart_delay_mean)