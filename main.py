import threading
import time
from services.openweather_api import get_weather
from services.mysql_db import save_weather_record
from services.render_dashboard import render_dashboard

def collector():
    while True:
        weather = get_weather()
        save_weather_record(weather)
        time.sleep(10)


threading.Thread(target=collector, daemon=True).start()

render_dashboard()