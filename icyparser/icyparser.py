#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Documentation on ICY in Icecast streams:
## http://www.smackfu.com/stuff/programming/shoutcast.html

import os
import re
import sys
import urllib.parse
import urllib.request

class IcyParser():
    def __init__(self, url):
        self.url = url

    def getIcyInformation(self):
        ## request the metadata headers: otherwise we won't get them.
        extra_headers = {"Icy-MetaData":1}

        try:
            rq  = urllib.request.Request(url=self.url, headers=extra_headers)
        except ValueError:
            print("Faulty URL. Please check URL and run again.")
            sys.exit(1)
        rsp = urllib.request.urlopen(rq)

        rsp_headers = rsp.getheaders()
        headers_dict = dict(rsp_headers)

        metaint = int(headers_dict["icy-metaint"])
        
        ## read the metaint amount of bytes so that our 'cursor'
        ## is at the right offset
        rsp.read(metaint)

        ## read the length specifier: this will tell us the length of
        ## the StreamTitle string
        length_specifier = int(ord(rsp.read(1)))*16

        ## finally, read the necessary amount of bytes and make it
        ## human-readable
        streamtitle = rsp.read(length_specifier).decode("utf-8", "ignore")
        streamtitle = re.findall("(?<=StreamTitle=').*(?=';)", streamtitle)[0]

        headers_dict["icy-streamtitle"] = streamtitle

        return(headers_dict)




        ## Some old code, this may come in handy if I decide to 
        ## create a blocking interface later on
        """
        while True:

            rsp.read(16000)
            b = rsp.read(1)
            print(b)
            length_specifier = int(ord(b))*16
             
            if length_specifier != 0:
                print("l: {}".format(length_specifier))

            msg = rsp.read(length_specifier)
            if msg != b"":
                print(msg)


        print(rsp.read(20))
        """


def entry_point():
    try:
        url = sys.argv[1]
    except IndexError:
        print("Usage: icyparser URL")
        sys.exit(1)
    ip = IcyParser(url)
    headers_dict = ip.getIcyInformation()
    
    for k in sorted(headers_dict.keys()):
        print(k + ": " + headers_dict[k])
