from bs4 import BeautifulSoup
import requests
from datetime import date


def tagesschau_titles(search_term, search_date):
    url = f"https://www.zeit.de/suche/index?q={search_term}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    page_text = doc.find(class_="pager__pages")
    max_pages = int(page_text.find_all("li")[-1].find("a").text)

    article_list = {}

    for current_page in range(1, 100):
        url = f"https://www.tagesschau.de/suche2.html?page_number={current_page}&query={search_term}&sort_by=date&dnav_type=story"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")

        articles = doc.find_all(class_='teaser')

        for article in articles:
            try:
                title = article.find(class_="headline").find("a").text
                datum = article.find(class_="dachzeile").find("a").text.split(".")
                day = int(datum[0].split(' ')[2])
                month = int(datum[1])
                year = int(datum[2].split(" ")[0])
                converted_date = date(year, month, day)
                if converted_date < search_date:
                    break
                article_list[title] = converted_date
                print(title)
            except:
                pass
        else:
            continue
        break
    return article_list


