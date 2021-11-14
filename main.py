import tweepy
from textblob import TextBlob
import csv
import time
import os
from tqdm import tqdm, trange
import time
import nltk
from wordcloud import WordCloud, STOPWORDS 

def getCommit(query, path):
    query = query
    file_name = str(path) + '/tweetsID.txt'

    with open(file_name, 'a+') as filehandle:
        for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                                    tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=100000):
            filehandle.write('%s\n' % tweet.id)

def Extraction(path):
    file = str(path) + '/tweetsID.txt'
    tweetID = []
    with open(file) as f:
        tweetID = [s.rstrip('\n') for s in list(f)]

    outputpath = str(path) + '/output.txt'
    with open(outputpath, 'a+', encoding='UTF-8') as f:
        for ids in trange(int(len(tweetID)/100)):
        
            tweets = client.get_tweets(ids=tweetID[ids*100:(ids+1)*100])
            output = [tweets.data[index]['text'] for index in range(len(tweets))]
            output = "\n".join(output)
            # print(output)
            # print(tweets.data['text'])
            f.write('%s\n' % output)
            time.sleep(0.1)

def wordCloud(path):
    datapath = str(path) + '/output.txt'
    data = open(datapath, 'r', encoding='utf-8').read()
    data = ' '.join(nltk.word_tokenize(data))
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

    ### stopword for bitcoin ###
    if (path == 'bitcoin'):
        stopwords.add("https") 
        stopwords.add("bitcoin")

    ### stop word for covid ###
    if (path == 'covid'):
        stopwords.add("https") 
        stopwords.add("covid")
        

    photopath = str(path) + '/wordcloud.png'
    cloud = WordCloud(stopwords=stopwords).generate(data)
    cloud.to_file(photopath)

if __name__ == '__main__':
    consumer_key = '9rbWU8mEwuurbPx1Dw1x86jIL'
    consumer_secret='pdNzxzpThDjn0vblI3MS5Ogl4ZXZgDooV36aq4pkb2vAMgdyvG'
    access_token='1459457686035398659-NfovUnuVSZ5cjc7hBNwHUHf6FAy5lm'
    access_token_secret='8xiBMW89ssNvSieaIGEHxW4pjVHsdWXK1vOPxZvLk23DY'
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAADr%2BVgEAAAAAPckb3AgEkdLO2tq5r2xKto%2F8A70%3DseSdQfTYngK50TDV54authG6SEck1N9pV1dYRNgP6hEUr4Ugse'

    client = tweepy.Client(bearer_token)

    # Step 1. 
    query = "bitcoin -is:retweet"
    path = 'bitcoin'
    # query = "covid -is:retweet"
    # path = 'covid'
    getCommit(query, path)

    # Step 2.
    Extraction(path)

    # Step 3.
    wordCloud(path)


    