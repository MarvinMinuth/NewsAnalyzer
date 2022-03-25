from bs4 import BeautifulSoup
import requests
from datetime import date


def zeit_titles(search_term, search_date):
    url = f"https://www.zeit.de/suche/index?q={search_term}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    page_text = doc.find(class_="pager__pages")
    max_pages = int(page_text.find_all("li")[-1].find("a").text)

    article_list = {}

    for current_page in range(1, max_pages+1):
        url = f"https://www.zeit.de/suche/index?q={search_term}&p={current_page}"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")

        body = doc.find(class_="main main--centerpage")
        articles = body.find_all('article')

        for article in articles:
            try:
                title = article.find("a").text
                datum = article.find("time")['datetime'].split("-")
                year = int(datum[0])
                month = int(datum[1])
                day = int(datum[2].split("T")[0])
                converted_date = date(year, month, day)
                if converted_date < search_date:
                    break
                article_list[title] = converted_date
                print(title, converted_date)
            except:
                pass
        else:
            continue
        break
    return article_list


