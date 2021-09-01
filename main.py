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
            if date.strftime("%A") in ('Friday', 'Saturday'):
                return True
            elif tomorrow.day == date_obj.day:
                return holiday['holiday_name']
            elif date.strftime("%A") == 'Sunday':
                return False

    def progress(self, percent=0, widht=25):
        left = widht * percent // 100
        right = widht - left
        return '▓' * left + '░' * right + f' {percent:.0f}%'

    def _get_year_percentage(self):
        epoch_year = date.today().year
        year_start = date(epoch_year, 1, 1)
        year_end = date(epoch_year, 12, 31)

        current_date = date.today() - year_start
        total_days = year_end - year_start
        return round(current_date.days / total_days.days * 100)

    def __init__(self):
        bar = self.progress(self._get_year_percentage())
        f = open(f'/home/{os.getlogin()}/.cache/holidays.json', "r")
        holidays = json.loads(f.read())
        if self._is_day_after_tomorrow_off(holidays):
            print(f'{bar} | Lusa Libur!!')

        is_off = self._is_tomorrow_off(holidays)
        if type(is_off) == str:
            print('Besok Libur! |', is_off, year_percent)
        elif type(is_off) ==  bool:
            print(f'{bar} | Besok Libur! Happy Weekend!')
        else:
            print(f'{bar} | あの子のために')

        self._get_weather()

hello()