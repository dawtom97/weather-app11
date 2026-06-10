from services.openweather_api import get_weather
from services.excel_files import save_to_excel, read_from_excel
import time
from config import Config
from services.render_dashboard import render_dashboard

# x = read_from_excel(Config.EXCEL_PATH)
# z = read_from_excel("sciezka.xlsx")

render_dashboard("lisbon_weather_450.csv")

# while True:
#     weather = get_weather()
#     # save_to_excel([weather])
#     print("Udało się pobrać dane")
#     time.sleep(10)






