# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 8:35
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : CanvasManager.py
# @Software: PyCharm Community Edition
# 这个主要是一个部件更新类，
# 用来在处理完部件显示图像以后调用所有部件的Update()方法进行screen的更新

class CanversManager(object):
    def __init__(self):
        self.componentList = [] #use component

    def addComponent(self,component):
        self.componentList.append(component)

    def removeComponent(self,component):
        self.componentList.remove(component)

    def UpdateComponent(self,screen):
        for component in self.componentList:
            component.Update(screen)
