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
        # 初始化的时候载入空间的边框图片，用ppt制作一个边框保存为png存在assets/monitor文件夹内（demo用）
        # 调用aseets/image里面的一张图片展示在monitor里面作为demo展示图片

    def is_Overlap(self):
        super(Monitor, self).is_Overlap()
        # 用来判断鼠标是否在目前控件内部

    def Update(self, screen):
        super(Monitor, self).Update()

class MonitorListener(Listener):
    def __init__(self):
        super(MonitorListener, self).__init__()

    def onChange(self, event):
        super(MonitorListener, self).onChange(event)
        # 实现判断鼠标在本空间内部
        # 鼠标点击的时候获取鼠标的位置以及鼠标松开的位置，记录在空间内的一个属性内以便获取截图 最好也print出来

if __name__ ==  '__main__':
    print '测试monitor'
    pygame.init()
    screen = pygame.display.set_mode((400, 400), 0, 32)
    pygame.display.set_caption("Button test")
    # 实现demo
    # 需要背景图片一张用来展示在monitor里面
    # 需要实例化monitor的一个子类
    # 需要实例化对应listener
    # 需要实例化eventmanager
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill((200, 200, 200))
