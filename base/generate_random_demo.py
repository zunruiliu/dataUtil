# -*- coding:utf-8 -*-
import time


def generate_random(lenth):
    date = str(time.time()).split(".")
    lstr = str(date[0]) + str(date[1])
    return lstr[(len(lstr)-lenth):]