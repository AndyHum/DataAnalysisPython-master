
# coding: utf-8

# In[259]:

import oauth2 as oauth
import tweepy
from tweepy import OAuthHandler
import argparse, time, datetime, requests, os, json
from heapq import *
from requests_oauthlib import OAuth1
import pytz
from datetime import datetime
import operator
 
consumer_key = 'w2bBUontza2zpX1cnQ3LV8JY5'
consumer_secret = 'aF3dMOJesvAFOKoazAODP0zqnUN7XEDJvDY8HsbVIc5sEUQ9Sg'
access_token = '3162877560-bL9ILWTxtSFt1zqES5m8de8EXHDKpyvGwZi3xFY'
access_secret = '0XrxV9njXgyRBIhKgjxgj74gGZ4U7MIrNb2ejLCfKpmc9'
 
consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_token = oauth.Token(key=access_token, secret=access_secret)
client = oauth.Client(consumer, access_token)


# In[54]:

import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('string', metavar='N', type=int, 
                    nargs='+',help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
parser.parse_args(['--sum', '7', '-1', '42'])


# In[66]:

import os
def checkexist():
    if not os.path.exists("/assignment1"):
        os.makedirs("/assignment1")


# In[67]:

import os
import time
def checkexistwithdate():
    now = time.strftime("%d/%m/%Y-%H:%M:%S")
    folder = "/" + now
    if not os.path.exists(folder):
        os.makedirs(folder)


# In[103]:

user_input = input('search')
date = input('date')
search_term = {'q': user_input, 'since': date, 'count': 100, 'result_type': 'mixed'}


# In[262]:

def authenticate_and_search():
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
    verification_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    requests.get(verification_url, auth=auth)

    url = 'https://api.twitter.com/1.1/search/tweets.json'
    results = requests.get(url, params=search_term, auth=auth)
    return results.json()
data = authenticate_and_search()


# In[263]:

def dump_data():
    with open(sub_folder + "\\" +'data.json', 'w') as outfile:
        json.dump(data, outfile)
dump_data()


# In[ ]:




# In[264]:

def Analysis_One():
    friends_sum = 0
    count = 0
    for i in range(int(count)):
        jsonData = tweets["statuses"][i]["user"]
    # print(tweets["statuses"][0]["user"].keys())
    # for item in jsonData:
        friends_count = jsonData["friends_count"]
        id = jsonData["id"]
        friends_sum += int(friends_count)
        print("User id is: {}".format(id), "  User friends_count is: {}".format(friends_count))
    friends_avg = friends_sum/int(count)
    print("Users' average friends count is: {}".format(friends_avg))


# In[154]:

def Analysis_Two():
    dic = {'Foreign': '0', 'Alien': '0', 'Alabama': '0', 'Alaska': '0', 'American Samoa': '0', 'Arizona': '0',
           'Arkansas': '0', 'California': '0', 'Colorado': '0', 'Connecticut': '0', 'Delaware': '0',
           'Washington, D.C.': '0', 'Florida': '0', 'Georgia': '0', 'Guam': '0', 'Hawaii': '0', 'Idaho': '0',
           'Illinois': '0', 'Indiana': '0', 'Kansas': '0', 'Iowa': '0', 'Kentucky': '0', 'Louisiana': '0', 'Maine': '0',
           'Maryland': '0', 'Marshall Islands': '0', 'Massachusetts': '0', 'Michigan': '0', 'Micronesia': '0',
           'Minnesota': '0', 'Mississippi': '0', 'Montana': '0', 'Nebraska': '0', 'Nevada': '0', 'New Hampshire': '0',
           'New Jersey': '0', 'New Mexico': '0', 'New York': '0', 'North Carolina': '0', 'North Dakota': '0',
           'Northern Marianas': '0', 'Ohio': '0', 'Oklahoma': '0', 'Oregon': '0', 'Palau': '0', 'Pennsylvania': '0',
           'Puerto Rico': '0', 'Rhode Island': '0', 'Missouri': '0', 'South Carolina': '0', 'South Dakota': '0',
           'Tennessee': '0', 'Texas': '0', 'Utah': '0', 'Vermont': '0', 'Virginia': '0', 'Virgin Islands': '0',
           'Washington': '0', 'West Virginia': '0', 'Wisconsin': '0', 'Wyoming': '0'}
    dic = dic.fromkeys(dic.keys(), 0)

    for i in range(int(count) - 1):
        jsonData = tweets["statuses"][i]["user"]
        user_location = jsonData["location"]
        id = jsonData["id"]

        url = "http://api.geonames.org/searchJSON?formatted=true&q=" + user_location + "&maxRows=10&lang=en&username=limuzi0609&style=full"
        data = json.dumps({"name": "test_repo", "description": "test"})
        r = requests.post(url, data)
        print(user_location)
        if r.json()["totalResultsCount"] == 0:
            dic['Alien'] += 1
        elif r.json()["geonames"][0]["countryCode"] == "US" and r.json()["geonames"][0]["adminName1"] is not '':
            state = r.json()["geonames"][0]["adminName1"]
            dic[state] += 1
        else:
            dic['Foreign'] += 1

    dic = {k: v for (k, v) in dic.items() if v > 0}
    print(dic.items())
    # visualisation
    wordlist=[]
    for key,val in dic.items():
        wordlist.append((key,val))
    matplotlib.pyplot.figure(figsize=(9, 6))
    wordlist.sort()
    keylist=[key for key,val in wordlist]
    vallist=[val for key,val in wordlist]
    barwidth=0.3
    xVal=np.arange(len(keylist))
    pylab.xticks(xVal+barwidth/2.0,keylist,rotation=45)
    pylab.bar(xVal,vallist,width=barwidth,color='lightskyblue',edgecolor = 'white')

    pylab.title(u"Bar Chart of Users' States" )
    pylab.show()


# In[172]:

def Analysis_Three():
    matplotlib.pyplot.figure(figsize=(9,6))

    followers_num = []
    retweet_num = []

    for i in range(int(count)):
        followers_count = tweets["statuses"][i]["user"]["followers_count"]
        retweet_count = tweets["statuses"][i]["retweet_count"]
        followers_num.append(followers_count)
        retweet_num.append(retweet_count)
        print("Tweets retweet number is: {}".format(retweet_count), " User's followers number is: {}".format(followers_count))

    T = np.arctan2(followers_num,retweet_num)
    matplotlib.pyplot.scatter(followers_num,retweet_num,c=T,s=25,alpha=0.4,marker='o')
    matplotlib.pyplot.xlabel("User's follower number")
    matplotlib.pyplot.ylabel("User's this tweet's retweet number")
    matplotlib.pyplot.show()


# In[192]:

def Analysis_Four():
    user_mentioned = 0
    for i in range(int(count)):
        mentioned_count = len(tweets["statuses"][i]["entities"]["user_mentions"])
        id = tweets["statuses"][i]["user"]["id"]
        user_mentioned += mentioned_count
        print("User id is: {}".format(id), "  User mentioned people number is: {}".format(mentioned_count))
    mentioned_avg = user_mentioned/int(count)
    print("Users' average friends count is: {}".format(mentioned_avg))


# In[236]:

def Analysis_Five():
    term_1 = input("What do you want to search?")
    if choose_time == 1:
        # global search_1
        integra_search = "%20since%3A" + date_0 + '&count=' + count
        search_2 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_1 + integra_search
    if choose_time == 2:
        # global search_1
        integra_search = "%20until%3A" + date_0 + '&count=' + count
        search_2 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_1 + integra_search
    else:
        search_2 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_1 + "%20until%3A" + date_0 + '&count=' + count
        print("Your input is wrong, please input again")

    response_1, data_1 = client.request(search_2)

    str_response_1 = data_1.decode('utf-8')
    tweets_1 = json.loads(str_response_1)

    dic = {'Foreign': '0', 'Alien': '0', 'Alabama': '0', 'Alaska': '0', 'American Samoa': '0', 'Arizona': '0',
           'Arkansas': '0', 'California': '0', 'Colorado': '0', 'Connecticut': '0', 'Delaware': '0',
           'Washington, D.C.': '0', 'Florida': '0', 'Georgia': '0', 'Guam': '0', 'Hawaii': '0', 'Idaho': '0',
           'Illinois': '0', 'Indiana': '0', 'Kansas': '0', 'Iowa': '0', 'Kentucky': '0', 'Louisiana': '0', 'Maine': '0',
           'Maryland': '0', 'Marshall Islands': '0', 'Massachusetts': '0', 'Michigan': '0', 'Micronesia': '0',
           'Minnesota': '0', 'Mississippi': '0', 'Montana': '0', 'Nebraska': '0', 'Nevada': '0', 'New Hampshire': '0',
           'New Jersey': '0', 'New Mexico': '0', 'New York': '0', 'North Carolina': '0', 'North Dakota': '0',
           'Northern Marianas': '0', 'Ohio': '0', 'Oklahoma': '0', 'Oregon': '0', 'Palau': '0', 'Pennsylvania': '0',
           'Puerto Rico': '0', 'Rhode Island': '0', 'Missouri': '0', 'South Carolina': '0', 'South Dakota': '0',
           'Tennessee': '0', 'Texas': '0', 'Utah': '0', 'Vermont': '0', 'Virginia': '0', 'Virgin Islands': '0',
           'Washington': '0', 'West Virginia': '0', 'Wisconsin': '0', 'Wyoming': '0'}
    dic_1 = {'Foreign': '0', 'Alien': '0', 'Alabama': '0', 'Alaska': '0', 'American Samoa': '0', 'Arizona': '0',
           'Arkansas': '0', 'California': '0', 'Colorado': '0', 'Connecticut': '0', 'Delaware': '0',
           'Washington, D.C.': '0', 'Florida': '0', 'Georgia': '0', 'Guam': '0', 'Hawaii': '0', 'Idaho': '0',
           'Illinois': '0', 'Indiana': '0', 'Kansas': '0', 'Iowa': '0', 'Kentucky': '0', 'Louisiana': '0', 'Maine': '0',
           'Maryland': '0', 'Marshall Islands': '0', 'Massachusetts': '0', 'Michigan': '0', 'Micronesia': '0',
           'Minnesota': '0', 'Mississippi': '0', 'Montana': '0', 'Nebraska': '0', 'Nevada': '0', 'New Hampshire': '0',
           'New Jersey': '0', 'New Mexico': '0', 'New York': '0', 'North Carolina': '0', 'North Dakota': '0',
           'Northern Marianas': '0', 'Ohio': '0', 'Oklahoma': '0', 'Oregon': '0', 'Palau': '0', 'Pennsylvania': '0',
           'Puerto Rico': '0', 'Rhode Island': '0', 'Missouri': '0', 'South Carolina': '0', 'South Dakota': '0',
           'Tennessee': '0', 'Texas': '0', 'Utah': '0', 'Vermont': '0', 'Virginia': '0', 'Virgin Islands': '0',
           'Washington': '0', 'West Virginia': '0', 'Wisconsin': '0', 'Wyoming': '0'}
    dic = dic.fromkeys(dic.keys(), 0)
    dic_1 = dic_1.fromkeys(dic_1.keys(), 0)

    for i in range(int(count) - 1):
        jsonData = tweets["statuses"][i]["user"]
        jsonData_1 = tweets_1["statuses"][i]["user"]
        user_location = jsonData["location"]
        user_location_1 = jsonData_1["location"]
        id = jsonData["id"]
        id_1 = jsonData_1["id"]

        url = "http://api.geonames.org/searchJSON?formatted=true&q=" + user_location + "&maxRows=10&lang=en&username=limuzi0609&style=full"
        url_1 = "http://api.geonames.org/searchJSON?formatted=true&q=" + user_location_1 + "&maxRows=10&lang=en&username=limuzi0609&style=full"
        data = json.dumps({"name": "test_repo", "description": "test"})
        data_1 = json.dumps({"name": "test_repo", "description": "test"})
        r = requests.post(url, data)
        r_1 = requests.post(url_1, data_1)
        print(user_location)
        print(user_location_1)
        if r.json()["totalResultsCount"] == 0:
            dic['Alien'] += 1
        elif r.json()["geonames"][0]["countryCode"] == "US" and r.json()["geonames"][0]["adminName1"] is not '':
            state = r.json()["geonames"][0]["adminName1"]
            dic[state] += 1
        else:
            dic['Foreign'] += 1

        if r_1.json()["totalResultsCount"] == 0:
            dic_1['Alien'] += 1
        elif r_1.json()["geonames"][0]["countryCode"] == "US" and r_1.json()["geonames"][0]["adminName1"] is not '':
            state_1 = r_1.json()["geonames"][0]["adminName1"]
            dic_1[state_1] += 1
        else:
            dic_1['Foreign'] += 1

    #dic = {k: v for (k, v) in dic.items() if v > 0}
    print(dic.items())
    #dic_1 = {k: v for (k, v) in dic_1.items() if v > 0}
    print(dic_1.items())
    # visualisation
    wordlist = []
    wordlist_1 = []
    for key, val in dic.items():
        wordlist.append((key, val))
    matplotlib.pyplot.figure(figsize=(9, 6))
    wordlist.sort()
    keylist = [key for key, val in wordlist]
    vallist = [val for key, val in wordlist]

    for key_1, val_1 in dic_1.items():
        wordlist_1.append((key_1, val_1))
    wordlist_1.sort()
    keylist_1 = [key_1 for key_1, val_1 in wordlist_1]
    vallist_1 = [val_1 for key_1, val_1 in wordlist_1]

    barwidth = 0.35
    xVal = np.arange(len(keylist))+1
    pylab.xticks((xVal*2 + barwidth) / 2.0, keylist, rotation=45)
    pylab.bar(xVal, vallist, width=barwidth, color='lightskyblue', edgecolor='white')
    pylab.bar(xVal+0.35, vallist_1, width=barwidth, color='yellowgreen', edgecolor='white')

    pylab.title(u"Lightskyblue for Trump, Yellowgreen for Clinton")
    pylab.show()



# In[265]:

num = input("NumberFrom 1-5:")
if num == "1":
    print("Analysis One")
    Analysis_One()
if num == 2:
    Analysis_Two()
if num == 3:
    Analysis_Three()
if num == 4:
    Analysis_four()
if num == 5:
    Analysis_Five()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



