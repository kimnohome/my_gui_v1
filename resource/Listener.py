# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 20:13
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : Listener.py
# @Software: PyCharm Community Edition

# 包含 监听器类 和 事件管理类
# 监听器类主要向下实现onChange接口用于给事件管理类统一管理事件
# 事件管理类主要管理所有监听器并且统一管理事件

import pygame

class Listener(object):
    def __init__(self):
        pass
    def onChange(self,event):
        pass

class EventManager(object):
    def __init__(self):
        self.listenerList = [] #use list

    def addListener(self,listener):
        self.listenerList.append(listener)

    def removeListener(self,listener):
        self.listenerList.remove(listener)

    def eventManage(self,event):
        for listener in self.listenerList:
            listener.onChange(event)
