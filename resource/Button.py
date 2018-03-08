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
class Button(Component):
  def __init__(self, upimage, inimage, downimage,position,size):
      self.imageUp = pygame.image.load(upimage).convert_alpha()
      self.imageIn = pygame.image.load(inimage).convert_alpha()
      self.imageDown = pygame.image.load(downimage).convert_alpha()

      self.imageUp = pygame.transform.scale(self.imageUp, size)
      self.imageIn = pygame.transform.scale(self.imageIn, size)
      self.imageDown = pygame.transform.scale(self.imageDown, size)

      self.positionX, self.positionY = position
      self.imageWidth, self.imageHeight = self.imageUp.get_size()
      self.draw_position = (self.positionX - self.imageWidth / 2, self.positionY - self.imageHeight / 2)
      self.draw_image=self.imageUp

  def is_Overlap(self):
      point_x,point_y = pygame.mouse.get_pos()
      in_x = self.positionX - self.imageWidth/2 < point_x < self.positionX + self.imageWidth/2
      in_y = self.positionY - self.imageHeight/2 < point_y < self.positionY + self.imageHeight/2
      return in_x and in_y

  def mouse_In(self):
      self.draw_image=self.imageIn

  def mouse_Down(self):
      self.draw_image = self.imageDown

  def mouse_Up(self):
      self.draw_image = self.imageUp

  def Update(self,screen):
      screen.blit(self.draw_image, self.draw_position)

  def onClick(self):
      pass

class ButtonListener(Listener):
    def __init__(self, button):
        self.button = button
    def onChange(self,event):
        if event.type == MOUSEMOTION:
            if self.button.is_Overlap():
                self.button.mouse_In()
            else:
                self.button.mouse_Up()
        elif event.type == MOUSEBUTTONDOWN:#left mouse down
            if self.button.is_Overlap():
                self.button.mouse_Down()
                self.button.onClick()
            else:
                self.button.mouse_Up()
        elif event.type == MOUSEBUTTONUP:
            self.button.mouse_Up()

if __name__ == "__main__":
    #get button images
    project_file_dir= os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    upImageFilename = project_file_dir+'/assets/button/button1_up.png'
    downImageFilename = project_file_dir+'/assets/button/button1_down.png'
    inImageFilename = project_file_dir+'/assets/button/button1_in.png'

    pygame.init()
    screen = pygame.display.set_mode((400,400),0,32)
    pygame.display.set_caption("Button test")
    class MyButton(Button):
        def __init__(self, upimage, inimage, downimage,position,size):
            super(MyButton, self).__init__(upimage, inimage, downimage,position,size)
            # some special fundtion here
        def onClick(self):
            print '按了MyButton一下'
    button = MyButton(upImageFilename, inImageFilename, downImageFilename, (150, 100),(200,50))
    myButtonListener=ButtonListener(button)
    eventManager=EventManager()
    eventManager.addListener(myButtonListener)
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill((200, 200, 200))
      #  button.render(screen)
        eventManager.eventManage(event)
        button.Update(screen)
        pygame.display.update()