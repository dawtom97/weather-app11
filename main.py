from services.openweather_api import get_weather
import time


while True:
    weather = get_weather()
    print(weather)
    time.sleep(10)


# git commit -m "initial commit"

new_var = 123




