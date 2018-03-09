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
import os
from math import floor,ceil

class Monitor(Component):
    def __init__(self,size=(500,500),position=(10,10)):
        pass
        # 初始化的时候载入空间的边框图片，用ppt制作一个边框保存为png存在assets/monitor文件夹内（demo用）
        # 调用aseets/image里面的一张图片展示在monitor里面作为demo展示图片
        project_file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        bg_image = project_file_dir + '/assets/monitor/monitor_bg_1.png'
        bg_image_obj = pygame.image.load(bg_image).convert_alpha()
        self.bg_image = pygame.transform.scale(bg_image_obj, size)
        self.block_size = size
        self.block_position = position
        self.monitor_bias = (5,5)
        self.monitor_offset=(self.block_position[0]+self.monitor_bias[0],self.block_position[1]+self.monitor_bias[1])  #展示图片在屏幕坐标的偏置，方便获取鼠标位置
        self.monitor_size=(self.block_size[0]-self.monitor_bias[0]*2,self.block_size[1]-self.monitor_bias[1]*2)
        self.image_path=project_file_dir+'/assets/image/arcade.jpg'
        self.image_scale = 1
        self.image = []
        self.image_after_scale=[]
        self.__update_show_image_obj()

    def is_Overlap(self):
        super(Monitor, self).is_Overlap()
        # 用来判断鼠标是否在目前控件内部

    def Update(self, screen):
        screen.blit(self.image_after_scale,self.block_position)

    def __update_show_image_obj(self):
        self.image = pygame.image.load(self.image_path).convert_alpha()
        image_size=self.image.get_size()  #图像大小，要判断是否需要缩放
        scale= [float(image_size[0])/self.monitor_size[0],float(image_size[0])/self.monitor_size[0]]
        max_scale=max(scale)
        ind_scale=scale.index(max_scale)
        # 需要计算图像缩放后的大小
        if max_scale >1.0:
            self.image_scale=1/max_scale
            image_size_re =(int(floor(float(image_size[0])*self.image_scale)),int(floor(float(image_size[1])*self.image_scale)))
            self.image_after_scale = pygame.transform.scale(self.image, image_size_re)
        else:
            self.image_scale=1.0
            image_size_re=(image_size[0],image_size[1])
            self.image_after_scale = self.image
        self.bg_image.blit(self.image_after_scale,self.monitor_bias)

    def set_image_path(self,image_path):
        self.image_path = image_path
        self.__update_show_image_obj()

class MonitorListener(Listener):
    def __init__(self):
        super(MonitorListener, self).__init__()

    def onChange(self, event):
        super(MonitorListener, self).onChange(event)
        # 实现判断鼠标在本空间内部
        # 鼠标点击的时候获取鼠标的位置以及鼠标松开的位置，记录在空间内的一个属性内以便获取截图 最好也print出来

if __name__ ==  '__main__':
    print '测试monitor'
    import os
    from CanvasManager import *
    pygame.init()
    screen = pygame.display.set_mode((700, 700), 0, 32)
    pygame.display.set_caption("TextView test")  # 实现demo
    # 需要实例化Monitor或者一个其子类
    mnt=Monitor()
    # 需要实例化对应listener，暂时不要
    # 需要实例化eventmanager，暂时不要
    # 需要实例化CanvasManager
    eventManager = EventManager()
    canvasManager = CanversManager()
    canvasManager.addComponent(mnt)
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill((255, 255, 255))
        canvasManager.UpdateComponent(screen)
        pygame.display.update()
