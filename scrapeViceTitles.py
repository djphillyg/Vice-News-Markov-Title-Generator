import requests
import time
import xml.etree.ElementTree as ET
from datetime import datetime
import pymongo
import pprint
import random
import nltk
import markovify
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def scrapeOnePage():
    client = pymongo.MongoClient('localhost', 27017)
    db = client['mySuperDB']
    collection = db["articles"]
    headers = {'Content-Type': 'application/xml'}
    vice_url = "https://www.vice.com/rss"
    xmlData = requests.get(headers=headers, url=vice_url, verify=False)
    tree = ET.fromstring(xmlData.text)
    for child in tree[0].findall('item'):
        title = child.find('title').text
        pubDate = child.find('pubDate').text
        nDate = datetime.strptime("%s" % pubDate,
                                  "%a, %d %b %Y %H:%M:%S %z")
        realTime = time.mktime(datetime.utctimetuple(nDate))
        print("%s \t %s" % (title, realTime))
        createDBobj = {"title": title, "ts": realTime}
        if not collection.find_one({"ts": realTime}):
            objID = collection.insert_one(createDBobj).inserted_id
            print("%s\n" % objID)
    for posts in collection.find():
        pprint.pprint(posts)


def scrapeWayBack():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    lines = [line.rstrip('\n') for line in open('RSSList.txt')]
    client = pymongo.MongoClient('localhost',27017)
    db = client['mySuperDB']
    collection = db['articles']
    headers = {'Content-Type': 'application/xml'}
    articlesprocessed=0
    for line in lines:
        try:
            xmlData = requests.get(headers=headers, url=line, verify=False)
        except requests.ConnectionError as e:
            continue
        articlesprocessed+=1
        print("%d articles processed"%articlesprocessed)
        tree = ET.fromstring(xmlData.text)
        for child in tree[0].findall('item'):
            title = child.find('title').text
            pubDate = child.find('pubDate').text
            nDate = datetime.strptime("%s" % pubDate, "%a, %d %b %Y %H:%M:%S %z")
            realTime = time.mktime(datetime.utctimetuple(nDate))
            createDBobj = {"title": title, "ts": realTime}
            if not collection.find_one({"ts": realTime}):
                collection.insert_one(createDBobj).inserted_id
    print("completed!")



def tryMongoDB():
    client = pymongo.MongoClient('localhost', 27017)
    db = client["mySuperDB"]
    collection = db["articles"]
    f = open("viceTitles",'w')
    for posts in collection.find():
        f.write("%s\n"%posts["title"])
    f.close()

def generate_markov():
    with open("viceTitles") as f:
        text = f.read()
    text_model = markovify.NewlineText(text)

    for i in range(10):
        print(text_model.make_short_sentence(140))

scrapeWayBack()
generate_markov()
