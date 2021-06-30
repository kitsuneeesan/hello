import json
import os
from datetime import date, datetime, timedelta

class hello():
    current_datetime = datetime.now()
    def _get_weather(self):
        f = open(f'/home/{os.getlogin()}/.cache/weather.json', "r")
        data = json.loads(f.read())
        main = data['main']
        temp = str(main['temp']) + '°C'
        humidity = str(main['humidity']) + '%'
        feels_like = str(main['feels_like']) + '°C'
        wind_speed = str(data['wind']['speed']) + 'm/s'
        print('temp :', temp, '|','humidity :', humidity, '|','feels_like :', feels_like, '|','wind_speed :', wind_speed, '\n')

    def _is_day_after_tomorrow_off(self, holidays, date=current_datetime):
        future_day = date + timedelta(days=2)
        for holiday in holidays:
            date_obj = datetime.strptime(holiday['holiday_date'], '%Y-%m-%d')
            if future_day == date_obj.day:
                return True

    def _is_tomorrow_off(self, holidays, date=current_datetime):
        tomorrow = date + timedelta(days=1)
        
        for holiday in holidays:
            date_obj = datetime.strptime(holiday['holiday_date'], '%Y-%m-%d')
            if date.strftime("%A") in ('Friday', 'Saturday') or tomorrow == date_obj.day:
                return True
            elif date.strftime("%A") == 'Sunday':
                return False

    def _get_year_percentage(self):
        epoch_year = date.today().year
        year_start = date(epoch_year, 1, 1)
        year_end = date(epoch_year, 12, 31)

        current_date = date.today() - year_start
        total_days = year_end - year_start

        persen = round(current_date.days / total_days.days * 100)
        return f'| year progress : {persen}%'

    def __init__(self):
        year_percent = self._get_year_percentage()
        f = open(f'/home/{os.getlogin()}/.cache/holidays.json', "r")
        holidays = json.loads(f.read())
        if self._is_day_after_tomorrow_off(holidays):
            print(f'Lusa Libur!! {year_percent}')
        print(f'Besok Libur! {year_percent}' if self._is_tomorrow_off(holidays) else f'あの子のために {year_percent}')
        self._get_weather()

hello()