---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
# this is my util
```

```python
from contextlib import contextmanager
import time
import json
import requests
import socket
import sys
import os
```

```python
# os.system('jupyter nbconvert --to script myutil.ipynb')
```

# my context

```python
@contextmanager
def gc2():
    gc.enable()
    yield
    gc.collect()
```

```python
@contextmanager
def timer(title='do'):
    t0 = time.time()
    yield
    print("{} - done in {:.4f}s".format(title, time.time() - t0))
```

# messange

```python
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
```

```python

```
