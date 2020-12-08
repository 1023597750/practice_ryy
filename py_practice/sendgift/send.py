#!/usr/bin/evn python 
# -*- coding: utf-8 -*-
# 如果导入失败，需要设置根目录，包右键-mark directory as>sources Root


# 区别：
# 复制一份变量到本地，在本地修改没有实际修改
# 引用模块的地址
# from gift import have_gift
import gift

# 发礼物的方法
def send():
    print("发礼物啦")
    # have_gift = True
    gift.have_gift = True