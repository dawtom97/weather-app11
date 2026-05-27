from services.openweather_api import get_weather
import time

print(123)

while True:
    weather = get_weather()
    print(weather)
    time.sleep(10)




