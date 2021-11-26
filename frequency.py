import nltk
import collections
import plotly
import plotly.graph_objs as go
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords

date = 1118
# file = './covid/data/output_' + str(date) + '.txt'
file = './covid/data/total.txt'
# text = ''
with open(file, encoding='UTF-8') as f:
    text = f.read()

en_stopws = stopwords.words('english')  
stopwords = [
    'covid','rt','de','19','la','en','que','el','le','amp','un','se','1',
    'les','los','por','2','e','000','des','il','et','get','del','à','es',
    'las','5','di','3','est','10','pas','one','du','n','6','non','dr','da',
    'new','covid_19','l','vaccines','c','u','si','je','al','qui','q','per',
    'got','11','4','still','many','2021'
]
en_stopws += stopwords
text = text.lower()
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)

tokens = [token for token in tokens if token not in en_stopws]  # filter stopwords
fdist = FreqDist(tokens)
common = fdist.most_common(50)
print(common)
# print(common[0][0])

"""
# plotly.offline.init_notebook_mode(connected=False)
keywords=[item[0] for item in common]
weights=[item[1] for item in common]
# print(keywords)

# title = 'Covid-19詞頻分佈：' + str(date)
title = 'Covid-19詞頻分佈' 
plotly.offline.iplot({
    "data": [go.Scatter(x=keywords, y=weights)],
    "layout": go.Layout(title=title)
})
"""
