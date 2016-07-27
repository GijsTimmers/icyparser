#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Documentation on ICY in Icecast streams:
## http://www.smackfu.com/stuff/programming/shoutcast.html

import sys
import urllib.parse
import urllib.request


def icyparser(url):
    extra_headers = {"Icy-MetaData":1}

    rq  = urllib.request.Request(url=url, headers=extra_headers)
    rsp = urllib.request.urlopen(rq)

    rsp_headers = rsp.getheaders()
    clean_dict = dict(rsp_headers)

    for k in sorted(clean_dict.keys()):
        print(k + ": " + clean_dict[k])

    #chunksize = 1024
    chunksize = 16000

    count = 0
    lengte_metadata = 0
    metadata = ""
    
    while True:
        stream = rsp.read(1)
        count += 1

        if count == 16001:
            lengte_metadata = int(ord(stream))*16
            print(lengte_metadata)

        if lengte_metadata != 0:
            if count >= 16002 and count <= 16001 + lengte_metadata:
                #print(stream)
                print(stream.decode("utf-8", "ignore"), end="")

        if count >= 16500:
            break

def entry_point():
    url = sys.argv[1]
    icyparser(url)
