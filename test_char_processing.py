# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 15:45
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : test_char_processing.py
# @Software: PyCharm Community Edition
from math import floor,ceil
from resource.lib import String_handle
def wrap_text_str(text):
    width = 100  # 文本框宽度
    font_size=16
    max_num_char = int(floor(float(width) / (font_size / 2)))  # 单行最多字母数
    #list_text = String_handle.string2List(text)
    list_text = list(text)
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
    return result_textlist



if __name__ == '__main__':
    str=u'123456789罗罗123'
    str=u'You know — one loves the sunset， when one is so sad\n---the little prince'
    a=wrap_text_str(str)
    for i in range(a.__len__()):
        print a[i]

