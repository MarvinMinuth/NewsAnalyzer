from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np


def cloud_it(article_list):
    text = ''
    for title in article_list:
        text = text + title + ' '

    x, y = np.ogrid[:1000, :1000]

    mask = (x - 500) ** 2 + (y - 500) ** 2 > 400 ** 2
    mask = 255 * mask.astype(int)

    wordcloud = WordCloud(background_color="white",width=1920, height=1080, mask=mask).generate(text)

    return wordcloud

    # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()
