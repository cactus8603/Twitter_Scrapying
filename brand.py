import nltk
import collections
import plotly
import plotly.graph_objs as go
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import re

date = 1123
# file = './covid/data/output_' + str(date) + '.txt'
file = './covid/data/total.txt'
# text = ''
with open(file, encoding='UTF-8') as f:
    text = f.read()

en_stopws = stopwords.words('english')  

bnt = ['biontech','pfizer','bnt']
az = ['oxford','astrazeneca','az']
mo = ['moderna']
ja = ['johnson&johnson','janssen']
no = ['novavax']
mvc = ['medigen','mvc']

count = [
    ['bnt',0],['az',0],['mo',0],['ja',0],['no',0],['mvc',0]
]


text = text.lower()

print(len(re.findall(bnt[0], text)))
print(len(re.findall(bnt[1], text)))
print(len(re.findall(bnt[2], text)))

for brand in range(len(bnt)):
    count[0][1] += len(re.findall(bnt[brand], text))

for brand in range(len(az)):
    count[1][1] += len(re.findall(az[brand], text))

for brand in range(len(mo)):
    count[2][1] += len(re.findall(mo[brand], text))

for brand in range(len(ja)):
    count[3][1] += len(re.findall(ja[brand], text))

for brand in range(len(no)):
    count[4][1] += len(re.findall(no[brand], text))

for brand in range(len(mvc)):
    count[5][1] += len(re.findall(mvc[brand], text))

print(count)

# fdist = FreqDist(count)
# common = fdist.most_common()
# print(common)
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
