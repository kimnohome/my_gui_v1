# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 13:20
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : TextView.py
# @Software: PyCharm Community Edition
# 仿照android的文字框控件用来展示文字
# 想想需要什么属性来支撑这个控件：
# 1）文字内容----------》可以实现,文字大小，位置，颜色等
#          整个文本框，暂定上下左右各空出15点吧
# 2）文本框大小--------》可以实现
# 3）文本框换行--------》可以实现
# 4）文本框换行进度条--》需要额外实现进度条控件,进度条应该只用控制显示位置的up-down偏置就好了

from Component import *
from Listener import *
from CanvasManager import *
import pygame
from lib import String_handle
from TextManager import Font_Brush
from math import ceil,floor  # 计算取整行数

class TextView(Component):
    def __init__(self, text='', size=(300, 100), position=(0, 0)):
        project_file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        bg_image = project_file_dir + '/assets/TextView/TextBlock1.png'
        bg_image_obj = pygame.image.load(bg_image).convert_alpha()
        self.bg_image = pygame.transform.scale(bg_image_obj, size)
        self.block_size = size
        self.block_position = position

        self.text_bias = (15, 15, 15, 15)  # up, left, down, right
        self.text_row_space = 3  # 行间距
        self.text = text
        self.text_position = (0+self.text_bias[0], 0 + self.text_bias[1])
        self.text_list = [text]  # wrap text
        self.text_list_position = [self.text_position]  # wraped text position
        self.auto_wrap = True
        self.font_brush = Font_Brush(self.bg_image)

        self.font_brush.setText_color((0, 0, 0))
        self.font_brush.setFontsize(16)
        self.__text_process()

    def __text_process(self):
        # 实现文字处理，如果需要换行的话，就转换为list来分行处理
        # 其中换行时，需要考虑文本框宽度和字体大小的关系
        # 输入是self.text  输出在self.text_list,使得每行的长度适合于文本框长度
        # 文字的高度为字体大小加1 ,英文宽度为字体大小的一半，中文为字体大小
        if self.auto_wrap:
            self.__wrap_text_str()
            self.__wrap_text_position()
        else:
            pass

    def __wrap_text_str(self):  # 实现自动换行
        width = self.block_size[0] - self.text_bias[1] - self.text_bias[3]  # 文本框宽度
        max_num_char = int(floor(float(width) / (self.font_brush.font_size / 2)))  # 单行最多字母数
        list_text = list(self.text)
        list_chinese_char = [String_handle.is_chinese_2(temp_c) for temp_c in list_text]
        result_textlist = []
        i_num_char = 0
        temp = 0
        for i in range(list_text.__len__()):
            if temp == max_num_char:
                temp = 0
                result_textlist.append(String_handle.list2string(list_text[i_num_char:i]))
                i_num_char = i
            elif temp > max_num_char:
                temp = 0
                result_textlist.append(String_handle.list2string(list_text[i_num_char:i - 1]))
                i_num_char = i - 1
            temp += list_chinese_char[i]
        if i_num_char < list_text.__len__():
            result_textlist.append(String_handle.list2string(list_text[i_num_char:list_text.__len__()]))
        self.text_list = result_textlist

    def __wrap_text_position(self):  # use after wrap text
        list_position = []
        # 文字的高度为字体大小加1 ,英文宽度为字体大小的一半，中文为字体大小
        list_position.append((0 + self.text_bias[0], 0 + self.text_bias[1]))
        for i in range(1, self.text_list.__len__()):
            temp = list_position[-1]
            list_position.append((0 + self.text_bias[0],
                                  temp[1] + self.font_brush.font_size + 1 + self.text_row_space))
        self.text_list_position=list_position

    def Update(self, screen):
        if self.auto_wrap:
            for i in range(self.text_list.__len__()):
                self.font_brush.position=self.text_list_position[i]
                self.font_brush.setText(self.text_list[i])
                self.font_brush.Update()
        else:
            self.font_brush.position = self.text_position
            self.font_brush.setText(self.text)
            self.font_brush.Update()
        screen.blit(self.bg_image, self.block_position)




if __name__ == '__main__':
    print '测试'
    import os
    pygame.init()
    screen = pygame.display.set_mode((600, 600), 0, 32)
    pygame.display.set_caption("TextView test")  # 实现demo
    # 需要实例化TextView的一个子类
    txt = TextView(u'You know — one loves the sunset， when one is so sad---the little prince')
    #txt = TextView(u'我要那天，再遮不住我眼')
    project_file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    #font_path = project_file_dir + '/assets/font/shaeryingbiti.ttf'
    #font_path = project_file_dir + '/assets/font/fangzheng_youmaozai.ttf'
    font_path = project_file_dir + '/assets/font/qiufu_kaiti.ttf'
    txt.font_brush.setFont(font_path)
    # 需要实例化对应listener
    # 需要实例化eventmanager
    # 需要实例化CanvasManager
    eventManager = EventManager()
    canvasManager = CanversManager()
    canvasManager.addComponent(txt)
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill((255, 255, 255))
        canvasManager.UpdateComponent(screen)
        pygame.display.update()