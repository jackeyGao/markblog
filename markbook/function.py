# -*- coding: utf-8 -*-
'''
File Name: markbook/function.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: Tue Apr 28 21:20:21 2015
'''
import re

def is_mobile(user_agent):
    detects = "iPod|iPhone|Android|Opera Mini|BlackBerry| \
            webOS|UCWEB|Blazer|PSP|IEMobile"
    return re.search(detects, user_agent)
