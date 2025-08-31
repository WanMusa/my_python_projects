#html test file 2
import json
import requests
import pandas as pd

url = 'https://api.aladhan.com/v1/calendarByAddress/2025/8?address=Auckaland%2C+New+Zealand&method=3&month=08&year=2025&latitudeAdjustmentMethod=3&tune=0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0&school=0&annual=false&adjustment=1&_=1756509619790'
r = requests.get(url)
data = r.json()['data']

def get_dates(data):
    dates = []
    for item in data:
        dates.append({'date' : (item['date']['gregorian']['date'])})
    return dates
#    print(dates)

def get_prayer_times(data):
    prayer_times = []
    for item in data:
        times = item['timings']
        prayer_times.append(times)
#    print (prayer_times) 
    return prayer_times


def add_dates_list (dates, prayer_times):
    combined = []
    for d, pt in zip(dates, prayer_times):
        combined.append({**d, **pt}) 
    return combined
#    print(combined)


#get_prayer_times(data)
#get_dates(data)
extracted = add_dates_list(get_dates(data), get_prayer_times(data))

df = pd.DataFrame(extracted)
#cleaned_df = df.replace(to_replace='\(NZST\)', value= '', regex=True, inplace=True)
df = df.applymap(lambda x: x.replace('(NZST)', '').replace(' ', '') if isinstance(x, str) else x)
print (df)