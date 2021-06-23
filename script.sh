#!/bin/bash

api_key=7a5c8d7374c83319c33e3e0819d4edde
city_id=1642911
weather="api.openweathermap.org/data/2.5/weather?id=${city_id}&appid=${api_key}&cnt=5&units=metric&lang=en"
curl ${weather} -s -o ~/.cache/weather.json

month=$(date -d "$D" '+%m')
holidays="https://api-harilibur.vercel.app/api?month=${month}"
curl ${holidays} -s -o ~/.cache/holidays.json
