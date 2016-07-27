#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Author:          Gijs Timmers: https://github.com/GijsTimmers

from icyparser import icyparser
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    icyparser(url)
