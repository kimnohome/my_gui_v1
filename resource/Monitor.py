# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 00:00
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : Button.py
# @Software: PyCharm Community Edition
# component for the GUI to show images and do some things to the image
# 主要用于实现Monitor控件，用于在GUI中显示图片并且向下实现对图像的操作
# 后期拟实现用来显示动画等

import pygame
from Listener import *
from Component import *
from pygame.locals import *

class Monitor(Component):
    def __init__(self):
        pass

    def is_Overlap(self):
        super(Monitor, self).is_Overlap()

    def Update(self):
        super(Monitor, self).Update()

class MonitorListener(Listener):
    def __init__(self):
        super(MonitorListener, self).__init__()

    def onChange(self, event):
        super(MonitorListener, self).onChange(event)