#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Documentation on ICY in Icecast streams:
## http://www.smackfu.com/stuff/programming/shoutcast.html

import sys
import urllib.parse
import urllib.request

url = sys.argv[1]

extra_headers = {"Icy-MetaData":1}

rq  = urllib.request.Request(url=url, headers=extra_headers)
rsp = urllib.request.urlopen(rq)

rsp_headers = rsp.getheaders()
clean_dict = dict(rsp_headers)

for k in sorted(clean_dict.keys()):
    print(k + ": " + clean_dict[k])


