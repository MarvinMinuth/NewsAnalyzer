import math
from datetime import date
from tagesschau_scraper import tagesschau_titles
from bild_scraper import bild_titles
from zeit_scraper import zeit_titles
from hanta import title_hanta
from wordclouder import cloud_it
import matplotlib.pyplot as plt

search_term = "ukraine"
search_date = date(2022, 2, 24)

cloud_list = {}

tagesschau_liste = tagesschau_titles(search_term, search_date)
tagesschau_words = title_hanta(tagesschau_liste)
tagesschau_cloud = cloud_it(tagesschau_words)
cloud_list['Tagesschau'] = tagesschau_cloud

zeit_liste = zeit_titles(search_term, search_date)
zeit_words = title_hanta(zeit_liste)
zeit_cloud = cloud_it(zeit_words)
cloud_list['Zeit'] = zeit_cloud

bild_liste = bild_titles(search_term)
bild_words = title_hanta(bild_liste)
bild_cloud = cloud_it(bild_words)
cloud_list['Bild'] = bild_cloud

fig = plt.figure(figsize=(10, 7))
rows = math.ceil(len(cloud_list)/3)
colums = 3
counter = 1

for key, value in cloud_list.items():
    fig.add_subplot(rows, colums, counter)
    counter += 1
    plt.imshow(value, interpolation="bilinear")
    plt.title(key)
    plt.axis("off")

plt.show()
