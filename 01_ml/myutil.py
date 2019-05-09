#!/usr/bin/env python
# coding: utf-8

# In[1]:


# this is my util


# In[9]:


from contextlib import contextmanager
import time
import json
import requests
import socket
import sys
import os


# In[14]:


os.system('jupyter nbconvert --to script myutil.ipynb')


# In[12]:


get_ipython().system('jupyter nbconvert\u200a--to script util.ipynb')


# # my context

# In[3]:


@contextmanager
def gc2():
    gc.enable()
    yield
    gc.collect()


# In[4]:


@contextmanager
def timer(title='do'):
    t0 = time.time()
    yield
    print("{} - done in {:.4f}s".format(title, time.time() - t0))


# # messange

# In[5]:


token = "130fe712252513ab163f9453dbe9bdc9efca01eb3a7f1def85a5f6d89dc7c358"
phones = [17621684529]
# def bot(message, phones=phones, token=token):
def ding(message):
    url = 'https://oapi.dingtalk.com/robot/send'
    params = { 'access_token': token }
    headers = { 'Content-Type': 'application/json' }
    data = json.dumps({
        "msgtype": "text",
        "text": {
            "content": message + "\n" +
                       time.strftime('%Y/%m/%d %H:%M:%S') + "\n" +
                       socket.gethostname()},
        "at": {"atMobiles": phones},
    })
    return requests.post(url, headers=headers, params=params, data=data)


# In[7]:


# ding('ok')


# In[ ]:




