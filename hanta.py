import nltk
import codecs
import matplotlib
from HanTa import HanoverTagger as ht
from pprint import pprint


def title_hanta(article_list):
    # nltk.download('punkt')
    text = ''
    for title in article_list:
        text = text + title + ' '

    sentences = nltk.sent_tokenize(text, language='german')

    tagger = ht.HanoverTagger('morphmodel_ger.pgz')

    nouns = []
    sentences_tok = [nltk.tokenize.word_tokenize(sent) for sent in sentences]
    for sent in sentences_tok:
        tags = tagger.tag_sent(sent)
        nouns_from_sent = [lemma for (word, lemma, pos) in tags if pos == "NN" or pos == "NE"]
        nouns.extend(nouns_from_sent)

    fdist = nltk.FreqDist(nouns)

    pprint(fdist.most_common(10))
    return(nouns)
    # fdist.plot(75, cumulative=False)
