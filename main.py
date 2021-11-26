import tweepy
from textblob import TextBlob
import csv
import time
import os
from tqdm import tqdm, trange
import time
import nltk
from wordcloud import WordCloud, STOPWORDS 
from PIL import Image
import numpy as np

def getCommit(query, path, date):
    query = query
    file_name = str(path) + '/id/tweetsID_' + str(date) + '.txt'
    date = int(date) % 100
    progress = tqdm(total=4800)

    
    for hr in range(0,24):
        if (hr<10):
            startTime = '2021-11-' + str(date) + 'T0' + str(hr) + ':00:00Z'
            endTime = '2021-11-' + str(int(date)+1) + 'T0' + str(hr) + ':59:59Z'
        else:
            startTime = '2021-11-' + str(date) + 'T' + str(hr) + ':00:00Z'
            endTime = '2021-11-' + str(int(date)+1) + 'T' + str(hr) + ':59:59Z'

        with open(file_name, 'a+') as filehandle:
            for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, start_time=startTime, end_time=endTime,
                                        tweet_fields=['context_annotations', 'created_at'], max_results=10).flatten(limit=200):
                filehandle.write('%s\n' % tweet.id)
                progress.update(1)
                time.sleep(0.5)

def Extraction(path, date):
    file = str(path) + '/id/tweetsID_' + str(date) + '.txt'
    tweetID = []
    with open(file) as f:
        tweetID = [s.rstrip('\n') for s in list(f)]
    # dataID = [tweetID[index] for index in range(100)]
    # IDList = [",".join(str(id) for id in dataID)]

    outputpath = str(path) + '/data/output_' + str(date) + '.txt'
    with open(outputpath, 'a+', encoding='UTF-8') as f:
        # int(len(tweetID)/100)
    
        for ids in trange(int(len(tweetID)/100)):
            dataID = [tweetID[index] for index in range(ids*100,(ids+1)*100)]
            IDList = ",".join(str(id) for id in dataID)

            tweets = client.get_tweets(ids=IDList)
            
            output = [tweets.data[index]['text'] for index in range(95)]
            output = "\n".join(output)
            # print(output)
            # print(tweets.data['text'])
            f.write('%s\n' % output)
            time.sleep(0.5)
    
      

def wordCloud(path, date):
    # datapath = str(path) + 'covid/data/output_' + str(date) + '.txt'
    datapath = str(path) + '/data/total.txt'
    data = open(datapath, 'r', encoding='utf-8').read()
    data = ' '.join(nltk.word_tokenize(data))

    mask = np.array(Image.open('twitter.png')) #文字雲形狀

    stopwords = set(STOPWORDS)  
    stopwords.add("t")
    stopwords.add("co")
    stopwords.add("de")
    stopwords.add("la")
    stopwords.add("s")
    stopwords.add("que")
    stopwords.add("le")
    stopwords.add("en")
    stopwords.add("el")
    stopwords.add("les")
    stopwords.add("lo")
    stopwords.add("RT")
    stopwords.add("y")
    stopwords.add("e")
    stopwords.add("amp")
    stopwords.add("n't")
    stopwords.add("w")
    stopwords.add("u")
    stopwords.add("se")
    stopwords.add("re")
    stopwords.add("o")
    stopwords.add("del")
    stopwords.add("due")
    stopwords.add("m")

    ### stopword for bitcoin ###
    if (path == 'bitcoin'):
        stopwords.add("https") 
        stopwords.add("bitcoin")

    ### stop word for covid ###
    if (path == 'covid'):
        stopwords.add("https") 
        stopwords.add("covid")
        

    # photopath = str(path) + '/photo/wordcloud' + str(date) + '.png'
    photopath = str(path) + '/photo/wordcloud_total.png'
    cloud = WordCloud(stopwords=stopwords,background_color='white',mask=mask).generate(data)
    cloud.to_file(photopath)

if __name__ == '__main__':
    consumer_key = 'PYVDbrq9iLuKrhOHFIghJ8X2v'
    consumer_secret='kyKF11dnLv1HB95pV7ZWtNE6U0qy7y7ZJKoiXe2zzA5PF5jizn'
    access_token='1459457686035398659-Qkl28oU2w2VKbtI3oHiKQ4LMeN8nIX'
    access_token_secret='Y123MJ3alqC9wdh9p6YWL32fePk1SItHxGTxuqoZ7R1Wu'
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAAONoVwEAAAAA95%2BZhcLwZW5VM48mzQ7da2LA%2Bso%3DyX60MdcTK9Lfj4acwkJEfnUsDB4XhrzWuqiPvsicAEk4IFyBWD'

    client = tweepy.Client(bearer_token)

    # Step 1. 
    # query = "bitcoin -is:retweet"
    # path = 'bitcoin'
    # query = "covid -is:retweet"
    query = "covid"
    path = 'covid'
    # https://mobile.twitter.com/user/status/ID
    day = ['1123'] # '1118','1119','1120','1121','1122','1123'
    for date in day:
        # Step 1. 
        # getCommit(query, path, date)

        # Step 2.
        # Extraction(path, date)
        # time.sleep(5)

        # Step 3.
        wordCloud(path, date)


    # Step 2.
    # Extraction(path, date)
    
    # print(tweets)
    # Step 3.
    # wordCloud(path, date)


    