# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 14:26
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : demo_v1.py
# @Software: PyCharm Community Edition

# 写这个demo才发现控件之间的通信真的是一个大问题
# 这样，拿button来打比方，本控件的内容更改利用onclick来解决
#         全局的内容更改利用buttonListener的onchange来解决

# 唉，有点乱，再仔细想想吧

from resource import *
import pygame


class MyButton(Button):
    def __init__(self, upimage, inimage, downimage, position, size):
        super(MyButton, self).__init__(upimage, inimage, downimage, position, size)
        # some special fundtion here

    def onClick(self):
        pass
    def change_image_ind(self,image_list_obj):
        image_list_obj.next_image()

class myButton_listener(ButtonListener):
    def mouse_down(self):
        super(myButton_listener, self).mouse_down()

    def __init__(self, button,image_list):
        super(myButton_listener, self).__init__(button)
        self.image_list=image_list


if __name__ == '__main__':
    #init
    pygame.init()
    screen = pygame.display.set_mode((800, 800), 0, 32)
    pygame.display.set_caption("测试demo")

    event_manager = EventManager()

    while True:
        event = pygame.event.wait()
        screen.fill((200, 200, 200))
        event_manager.eventManage(event)
        pygame.display.update()
