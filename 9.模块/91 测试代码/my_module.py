#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'kivet'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('无传参，只有一个默认的参数，为当前文件的文件名：', args[0])
    elif len(args)==2:
        print('执行时传入了一个额外的参数，参数名为：%s，传入额外参数为：%s' % (args[0], args[1]))
    else:
        print('传入可超过一个的参数')

if __name__ == '__main__':
    test()
