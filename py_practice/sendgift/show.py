#!/usr/bin/evn python 
# -*- coding: utf-8 -*-


# from gift import have_gift
import gift
# 展示礼物的方法
def show():
    # if have_gift == True:
    if gift.have_gift == True:
        print("收到礼物")
    else:
        print("没有礼物")
