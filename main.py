from datetime import date
from zeit_scraper import zeit_titles
from hanta import title_hanta

search_term = "ukraine"
search_date = date(2022, 2, 24)

zeit_liste = zeit_titles(search_term, search_date)
title_hanta(zeit_liste)




