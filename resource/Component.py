# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 00:01
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : Component.py
# @Software: PyCharm Community Edition
# super class for all the component in GUI
# 所有控件的基本类
# is_Overlap方法表示判断鼠标是否在空间内部
# Update是必须实现的用来最终在screen上更新画面的方法
class Component(object):
    def __init__(self):  # init
        pass

    def is_Overlap(self):  # judge that mouse in the component
        pass

    def Update(self, screen):  # method to update the image of the component
        pass
