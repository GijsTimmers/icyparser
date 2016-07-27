#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Author:          Gijs Timmers: https://github.com/GijsTimmers

from icyparser import IcyParser
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    ip = IcyParser(url)
    headers_dict = ip.getIcyInformation()

    for k in sorted(headers_dict.keys()):
        print(k + ": " + headers_dict[k])


