# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 8:23
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : TextManager.py
# @Software: PyCharm Community Edition
# 这个主要是一个文字管理类，拟实现文字处理功能可以用在部件内部文字显示
# 也可以用来直接显示文字
# 实例化这个类的话，就是建立一个字体模版

# 拟学习python的可变参数输入，建立默认字体模版
# 并且在控件内部需要实现文字显示的控件中实现默认字体管理类，如手动传入字体类
#    则更改字体类相关属性：font color 抗锯齿等，同时根据控件大小自适应改变字体大小
import pygame
from Component import *
class TextManager(Component):
    def __init__(self):
        super(TextManager, self).__init__()


    def Update(self):
        super(TextManager, self).Update()

    def is_Overlap(self):
        super(TextManager, self).is_Overlap()


if __name__ == '__main__':
    print '测试'