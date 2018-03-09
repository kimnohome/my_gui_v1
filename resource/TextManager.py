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

#  要避免一个问题就是：先把文字画在一个图上面，图画到屏幕上以后，又再次画一遍文字
import pygame
from Component import *

# 暂时不要用这个类
class TextManager(Component):  # no use,后面打算把TextManager弄成和CanvasManager一样
    def __init__(self, font="arial", height=16, anti=True, font_color=(0, 0, 0),
                 bg_color=(255, 255, 255)):  # 暂时不管自定义ttf字体
        super(TextManager, self).__init__()
        self.anti = anti
        self.font_color = font_color
        self.bg_color = bg_color
        self.font = pygame.font.SysFont(font, height)
        self.text_surface = self.font.render("hello", anti, font_color, bg_color)

    def Update(self, surface, text, position):
        if self.bg_color == 'no':
            text_surface = self.font.render(text, self.anti, self.font_color)
        else:
            text_surface = self.font.render(text, self.anti, self.font_color, self.bg_color)
        textRectObj = text_surface.get_rect()
        textRectObj.center = position
        surface.blit(text_surface, textRectObj)

    def is_Overlap(self):
        pass

# 这个类写得有点乱我给你说，大致思路理一下：
# 首先设置font（字体类型，大小）得到一个font类型的变量
# 然后调用font的render函数输入文字内容，颜色抗锯齿等等得到文字surface
# 最后blit把这个surface画上去，显示出文字
# 所以整个设置内容应该是：
# 1）更改文字属性（文字内容，颜色，抗锯齿等等），要更新text_fmt变量
# 2）更改文字类型，大小要更新font变量，然后还要更新text_fmt才能更新显示出去的内容
# 打算更改针对两个变量的方法按照不同的名字来定，我得重新改方法名字，到时候又是要花点功夫
class Font_Brush(Component):  # used to define font instance
    def __init__(self, surface_handle=[]):  # 这里出错了，如何多态初始化，好像并不能有多个初始化函数python
        self.__surface_handle = surface_handle
        # print type(self.__surface_handle)

        self.font_bold = False           # ->>>>self.font
        self.font_italic = False         # ->>>>self.font
        self.font_size = 16              # ->>>>self.font
        self.font_type = 'arial'         # ->>>>self.font
        self.is_sys_font = True          # ->>>>self.font
        self.text = 'Love U Forever'          # ->>>>self.text_fmt
        self.text_color = (255, 0, 0)         # ->>>>self.text_fmt
        self.text_bg_color = 'no'             # ->>>>self.text_fmt
        self.text_anti = True                      # ->>>>self.text_fmt

        self.position = (0, 0)  # ->>>>draw text surface
        self.font = pygame.font.SysFont('arial', 16)
        self.text_fmt = self.font.render(self.text, self.text_anti, self.text_color)  # no font bg

    def setText(self, text):
        self.text = text
        self.__update_text_fmt()

    def setText_color(self, color):
        self.text_color = color
        self.__update_text_fmt()

    def setSysFont(self, font_type):
        self.is_sys_font = True
        self.font_type = font_type
        self.__update_font()

    def setText_bg_color(self, color):
        self.text_bg_color = color
        self.__update_text_fmt()

    def setText_anti(self, anti):
        self.text_bg_color = color
        self.__update_text_fmt()

    def setFont(self, font_type):
        self.is_sys_font = False
        self.font_type = font_type
        self.__update_font()

    def setFontsize(self, font_size):
        self.font_size = font_size
        self.__update_font()

    def setSurface(self, surface):
        self.__surface_handle = surface

    def font_set_bold(self, font_bold):
        self.font_bold = font_bold  # 是否粗体
        self.__update_font()

    def font_set_italic(self, italic):
        self.font_italic = italic  # 是否粗体
        self.__update_font()

    def __update_font(self):
        if self.is_sys_font:
            self.font = pygame.font.SysFont(self.font_type, self.font_size)
        else:
            self.font = pygame.font.Font(self.font_type, self.font_size)
        self.font.set_italic(self.font_italic)
        self.font.set_bold(self.font_bold)
        self.__update_text_fmt()

    def __update_text_fmt(self):
        if self.text_bg_color != tuple:
            self.text_fmt = self.font.render(self.text,  # no font bg
                                             self.text_anti, self.text_color)
        else:
            self.text_fmt = self.font.render(self.text,  # set font bg
                                             self.text_anti, self.text_color, self.text_bg_color)

    def Update(self, surface_handle=[]):
        #print type(surface_handle)
        if type(surface_handle) == pygame.Surface:
            if self.text_bg_color == 'no':
                text_fmt = self.font.render(self.text, self.text_anti, self.text_color)  # no font bg
            else:
                text_fmt = self.font.render(self.text, self.text_anti, self.text_color,
                                            self.text_bg_color)  # set font bg
                #  绘制文字
            surface_handle.blit(text_fmt, self.position)
        else:
            self.__surface_handle.blit(self.text_fmt, self.position)


if __name__ == '__main__':
    import os
    print '测试'
    pygame.init()
    screen = pygame.display.set_mode((400, 400), 0, 32)
    pygame.display.set_caption("font test")

    project_file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    image = project_file_dir + '/assets/button/button1_in.png'
    imageObj = pygame.image.load(image).convert_alpha()
    text_1 = Font_Brush(imageObj)
    text_2 = Font_Brush(screen)
    text_2.font_color = (0, 255, 0)
    text_2.setText('Come On')
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill((200, 200, 200))
        text_1.Update()
        text_2.Update()
        screen.blit(imageObj, (100, 50))
        pygame.display.update()
