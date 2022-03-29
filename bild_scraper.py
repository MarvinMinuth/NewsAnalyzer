from bs4 import BeautifulSoup
import requests
from datetime import date

def bild_titles(search_term):
    url = f"https://www.bild.de/suche.bild.html?type=article&query={search_term}&resultsStart=0&resultsPerPage=1000"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    article_list = {}

    articles = doc.find_all(class_='headline')

    for article in articles:
        try:
            title = article.text
            datum = article.parent.parent.find("time")['datetime'].split("-")
            year = int(datum[0])
            month = int(datum[1])
            day = int(datum[2].split("T")[0])
            converted_date = date(year, month, day)
            article_list[title] = converted_date
            print(title)
        except:
            pass

    return article_list





