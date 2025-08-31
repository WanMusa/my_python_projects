#html test file
import requests
import pandas as pd

class PrayerTimes:
    def __init__(self, date, fajr, dhuhr, asr, maghrib, isha):
        self.date = date
        self.fajr = fajr
        self.dhuhr = dhuhr
        self.asr = asr
        self.maghrib = maghrib
        self.isha = isha

def api_call(self):
    url = 'https://api.aladhan.com/v1/calendarByAddress/2025/8?address=Auckaland%2C+New+Zealand&method=3&month=08&year=2025&latitudeAdjustmentMethod=3&tune=0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0&school=0&annual=false&adjustment=1&_=1756509619790'
    r = requests.get(url)
    #dates = (r.json(['data']['date']['gregorian']['date'] )for r in r.json()['data'])
    data = r.json()['data']

def get_dates(data):
    for day in data:
        print(day['date']['gregorian']['date'])

api_call(PrayerTimes)


# def pr(list_dict):
#     keys=list_dict[0].keys()
#     out_dict={key:[] for key in keys}
#     for dict_ in list_dict:
#         for key, value in dict_.items():
#             out_dict[key].append(value)
#     return out_dict


#prayer_times = pr(r.json())
#df=pd.DataFrame(prayer_times)
#print(df.head())
