# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 20:13
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : Listener.py
# @Software: PyCharm Community Edition
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
