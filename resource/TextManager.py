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

# 这里似乎应该用装饰器模式把具体font外包出去，而TextManager则只管理font>>>想想还是算了
# 》》想想还是需要用装饰器，把具体文字内容，位置全部外包出去，然后一个字形的manager就管那个字形的所有文字

import pygame
from Component import *
class TextManager(Component):
    def __init__(self,font="arial", height=16,anti=True,font_color=(0,0,0),bg_color=(255,255,255)): # 暂时不管自定义ttf字体
        super(TextManager, self).__init__()
        self.anti=anti
        self.font_color=font_color
        self.bg_color=bg_color
        self.font = pygame.font.SysFont(font, height)
        self.text_surface = self.font.render("hello", anti, font_color, bg_color)

    def Update(self, surface,text,position):
        if self.bg_color == 'no':
            text_surface = self.font.render(text, self.anti, self.font_color)
        else:
            text_surface = self.font.render(text, self.anti, self.font_color, self.bg_color)
        textRectObj= text_surface.get_rect()
        textRectObj.center = (position)
        surface.blit(text_surface, textRectObj)
    def is_Overlap(self):
        pass



class Font_No_Use(object):  #no use
    def __init__(self):
        pass
    def getText(self):
        pass

if __name__ == '__main__':
    import os
    print '测试'
    pygame.init()
    screen = pygame.display.set_mode((400,400),0,32)
    pygame.display.set_caption("font test")
    text_m=TextManager(font_color=(255,0,0),bg_color='no')
    project_file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    image = project_file_dir+'/assets/button/button1_in.png'
    imageObj = pygame.image.load(image).convert_alpha()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill((200, 200, 200))
        text_m.Update(imageObj,u'Come On',(20,20))
        text_m.Update(screen, u'I Love U', (200, 250))
        screen.blit(imageObj,(100,50))
        pygame.display.update()
