#!/usr/bin/env python
# -*- coding: utf-8 -*-

def string_to_dict(string):
    d = {}
    for kv in string.split("|"):
        k,v = kv.split(":")
        if v.isdigit():
            v=int(v)
        d[k]=v
    return d

print(string_to_dict("k1:1|k2:2|k3:3"))