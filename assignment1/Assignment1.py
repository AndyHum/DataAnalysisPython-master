
# coding: utf-8

# # Question 1 

# In[12]:

L =[]
for num in range(1,501):
    if num % 3 == 0:
        if num % 7 ==0:
            L = L + [num]
print(L)


# In[38]:

i = len(L)
L1 = []
print("The mean is {}".format(sum(L)/len(L)))
L1.append(L[i//4])
L1.append(L[i//2])
L1.append(L[i//4*3])
print(L1)


# # Question 2

# In[3]:

lines = []
with open('ques2.txt','rb') as f:
    lines = f.readlines()
input_line = lines[0].decode('utf-8')
stringnum = len(input_line.split())
print(stringnum)


# In[37]:

from statistics import mode
words = input_line.split()
average = sum(len(word) for word in words)/len(words)
print(average)
charnum = list()
for word in words:
    charnum.append(len(word))
charnum.sort()
length = len(charnum) // 2 + 1
print(charnum[length])
modenum = mode(charnum)
print(modenum)


# In[3]:

import sys
sys.getdefaultencoding()


# # Question 3

# In[79]:

import os
import json

path = 'jsons'
n = 0
for filename in os.listdir(path):
    if(filename[-5:] == ".json"):
        with open("jsons/"+filename) as f:
            if(json.load(f).get('name') == 'User Not Found'):
                n += 1
print(n)


# In[39]:

import os
import json
import random
path = 'jsons'
num = 0
D = dict()
for filename in os.listdir(path):
    if(filename[-5:] == ".json"):
        with open("jsons/"+filename) as f:
            name = filename[:-5]
            num1 = 0 
            if(json.load(f).get('name') == 'User Not Found'): 
                num1 = num1 + 1
            D[name] = num1
for i in range(5):
    key = random.choice(list(D.keys()))
    value = D.get(key)
    print((key,value))


# # Question 4

# In[48]:

import os
import json
import random
path = os.listdir("jsons")
D1 = dict()
for filename in path:
    userID = filename[:-5]
    if(filename[-5:] == ".json"):
        with open("jsons/" + filename) as f:
            i = 0
            j = 0
            D = json.load(f)
            if(D.get('name') == 'User Not Found'): 
                D1[userID]  = {'first' : 0, 'third' :0}
            else:
                stringlist = D['retargetingSegments']
                for elt in stringlist:
                    if(elt['segmentUid'].startswith('0')):
                        a += 1
                    elif(elt['segmentUid'].startswith('1')):
                        b += 1
                D1[userID] = {'first': a, 'third': b}
print(len(D1))
#print(json.dumps(result,sort_keys=True, indent=4))
for i in range(10):
    key = random.choice(list(result.keys()))
    value = result.get(key)
    print({key:value})


# In[ ]:



