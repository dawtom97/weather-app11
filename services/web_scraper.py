from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--disable-notifications")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--no-sandbox") # ważne na linuxie!!

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(
    service=service,
    options=options
)

def scrap_news():
    try:
        driver.get("https://www.onet.pl/")

        articles = driver.find_elements(By.TAG_NAME, "article")

        data = []
        for article in articles:
            title = article.find_elements(By.TAG_NAME, "h3")
            image = article.find_elements(By.TAG_NAME, "img")
            link = article.find_elements(By.TAG_NAME, "a")

            if not image or not title or not link:
                continue

            title_text = title[0].get_attribute("textContent")
            image_src = image[0].get_attribute("src")
            link_href = link[0].get_attribute("href")

            post = {
                "title": title_text,
                "image": image_src,
                "link": link_href,
            }
            data.append(post)

        return data

    except Exception as e:
        print(e)


def create_file(data):
    df = pd.DataFrame(data)
    df.to_excel("onet_news.xlsx")
    df.to_csv("onet_news.csv")


news = scrap_news()
create_file(news)
