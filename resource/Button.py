# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 11:34
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : Button.py
# @Software: PyCharm Community Edition
# 我第一个实现的部件，就是这个按钮，基本功能都已经实现
# 现在还需要完成按钮的文字显示功能

import pygame
import os
from Listener import *
from Component import *
from pygame.locals import *
from TextManager import *
from CanvasManager import *
from TextManager import Font_Brush


class Button(Component):
    def __init__(self, upimage, inimage, downimage, position, size):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageIn = pygame.image.load(inimage).convert_alpha()
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.imageUp = pygame.transform.scale(self.imageUp, size)
        self.imageIn = pygame.transform.scale(self.imageIn, size)
        self.imageDown = pygame.transform.scale(self.imageDown, size)
        self.positionX, self.positionY = position
        self.imageWidth, self.imageHeight = self.imageUp.get_size()
        self.draw_position = (self.positionX - self.imageWidth / 2, self.positionY - self.imageHeight / 2)
        self.draw_image = self.imageUp
        self.text_obj = []

    def set_text(self, textObj):
        self.text_obj = textObj

    def set_text(self, text):  # 默认字体
        self.text_obj = Font_Brush()
        self.text_obj.setText(text)
        self.text_obj.font_color = (0, 0, 255)
        self.text_obj.setFontsize(20)
        text_rec = self.text_obj.text_fmt.get_rect()
        text_rec.center = (self.imageWidth / 2, self.imageHeight / 2)
        self.text_obj.position = text_rec
        # 突然想起来你重新设置字体大小，就要重新更改字的位置，因为是根据中央写字的

    def set_text_size(self, text_size):
        self.text_obj.setFontsize(text_size)
        text_rec = self.text_obj.text_fmt.get_rect()
        text_rec.center = (self.imageWidth / 2, self.imageHeight / 2)
        self.text_obj.position = text_rec

    def is_Overlap(self):
        point_x, point_y = pygame.mouse.get_pos()
        in_x = self.positionX - self.imageWidth / 2 < point_x < self.positionX + self.imageWidth / 2
        in_y = self.positionY - self.imageHeight / 2 < point_y < self.positionY + self.imageHeight / 2
        return in_x and in_y

    def mouse_In(self):
        self.draw_image = self.imageIn

    def mouse_Down(self):
        self.draw_image = self.imageDown

    def mouse_Up(self):
        self.draw_image = self.imageUp

    def Update(self, screen):
        self.text_obj.Update(self.draw_image)
        screen.blit(self.draw_image, self.draw_position)

    def onClick(self):
        pass


class ButtonListener(Listener):
    def __init__(self, button):
        self.button = button

    def onChange(self, event):
        if event.type == MOUSEMOTION:
            if self.button.is_Overlap():
                self.button.mouse_In()
                self.mouse_in()
            else:
                self.button.mouse_Up()
        elif event.type == MOUSEBUTTONDOWN:  # left mouse down
            if self.button.is_Overlap():
                self.button.mouse_Down()
                self.button.onClick()
                self.mouse_down()
            else:
                self.button.mouse_Up()
        elif event.type == MOUSEBUTTONUP:
            self.button.mouse_Up()
            self.mouse_up()

    def mouse_in(self):
        pass

    def mouse_down(self):
        pass

    def mouse_up(self):
        pass


if __name__ == "__main__":
    # get button images
    project_file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    upImageFilename = project_file_dir + '/assets/button/button1_up.png'
    downImageFilename = project_file_dir + '/assets/button/button1_down.png'
    inImageFilename = project_file_dir + '/assets/button/button1_in.png'

    pygame.init()
    screen = pygame.display.set_mode((400, 400), 0, 32)
    pygame.display.set_caption("Button test")

    class MyButton(Button):
        def __init__(self, upimage, inimage, downimage, position, size):
            super(MyButton, self).__init__(upimage, inimage, downimage, position, size)
            # some special fundtion here

        def onClick(self):
            print '按了MyButton一下'

    button = MyButton(upImageFilename, inImageFilename,
                      downImageFilename, (150, 100), (100, 50))
    button.set_text('test button')
    button2 = MyButton(upImageFilename, inImageFilename,
                      downImageFilename, (250, 200), (100, 50))
    button2.set_text('A')
    button2.set_text_size(50)
    myButtonListener1 = ButtonListener(button)
    myButtonListener2 = ButtonListener(button2)
    eventManager = EventManager()
    eventManager.addListener(myButtonListener1)
    eventManager.addListener(myButtonListener2)
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill((200, 200, 200))
        #  button.render(screen)
        eventManager.eventManage(event)
        button.Update(screen)
        button2.Update(screen)
        pygame.display.update()
