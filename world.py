import nltk
import collections
import plotly
import plotly.graph_objs as go
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import re

date = 1123
file = './covid/data/output_' + str(date) + '.txt'
# file = './covid/data/total.txt'
# text = ''
with open(file, encoding='UTF-8') as f:
    text = f.read()

en_stopws = stopwords.words('english')  

country = []
with open("./covid/au/country.txt") as f:
    for line in range(196):
        data = str(f.readline()).rstrip('\n').lower()
        country.append(data)
# print(country)
text = text.lower()
# print(country[21])
# print(len(re.findall(country[21], text)))
# print(text)
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)

tokens = [token for token in tokens if token in country]  # filter stopwords
# print(tokens)
fdist = FreqDist(tokens)
common = fdist.most_common()
print(common)
# print(common[0][0])

"""
# plotly.offline.init_notebook_mode(connected=False)
keywords=[item[0] for item in common]
weights=[item[1] for item in common]
# print(keywords)

# title = 'Covid-19詞頻分佈：' + str(date)
title = 'Covid-19詞頻分佈(國家)：' + str(date)
plotly.offline.iplot({
    "data": [go.Scatter(x=keywords, y=weights)],
    "layout": go.Layout(title=title)
})
"""
