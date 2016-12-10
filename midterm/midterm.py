
# coding: utf-8

# In[5]:

import requests
import json
r1 = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&tagged=pandas&site=stackoverflow')
r1.json()
with open('question_pandas.json','w') as q1:
    json.dump(r.json(),q1)


# In[6]:

import requests
import json
r2 = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&tagged=pandas&site=stackoverflow')
r2.json()
with open('user.json','w') as q2:
    json.dump(r2.json(),q2)


# In[7]:

import requests
import json
r3 = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&tagged=python&site=stackoverflow')
r3.json()
with open('question_python.json','w') as q3:
    json.dump(r3.json(),q3)


# In[33]:

questions = []
user_id = []
with open('question_python.json') as a1:
    data = json.load(a1)
for i in data['items']:
    j = i['owner']
    m = j['user_id']
    n = i ['title']
    user_id.append(m)
    questions.append(n)
print(user_id)
print(questions)


# In[48]:

import requests
import json
user_dic = {}
for i in user_id:
    url = 'https://api.stackexchange.com/2.2/users/'
    url = url + str(i) 
    url = url + '?order=desc&sort=reputation&site=stackoverflow'
    r4 = requests.get(url)
    jsonname = r4.json()
    user_dic[str(i)] = jsonname['items'][0]['badge_counts']['bronze'] + jsonname['items'][0]['badge_counts']['silver'] + jsonname['items'][0]['badge_counts']['gold']
print(user_dic)


# In[53]:

import requests
import json
user_dic = {}
for i in user_id:
    url = 'https://api.stackexchange.com/2.2/users/'
    url = url + str(i) 
    url = url + '/tags?order=desc&sort=popular&site=stackoverflow'
    r5 = requests.get(url)
    jsonname = r5.json()
    user_list = []
    for j in jsonname['items']:
        if j['name'] not in user_list:
            user_list.append(j['name'])
    user_dic[str(i)] = user_list
print(user_dic)


# In[61]:

r6 = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')
jsonname = r6.json()
questions_dic = {}
for i in jsonname['items']:
    name = i['title']
    taglist =  []
    for j in i['tags']:       
        taglist.append(j)
    questions_dic[name] = taglist
print(questions_dic)


# In[62]:

r7 = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')
jsonname = r7.json()
n = 0
user_id = 0
question = ''
for i in jsonname['items']:
    if i['view_count'] > n:
        n = i['view_count']
        user_id = i['owner']['user_id']
        question = i['title']
print('the most view question is')
print(question)
print(user_id)
print('the count of it is')
print(n)


# In[ ]:



