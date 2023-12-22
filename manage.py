#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Modify: 薄荷你玩
# Date: 2023/12/22

from bin.main import main


if __name__ == '__main__':
    """
    环境: python3 + pygame
    running 起来就可以打飞机了O(∩_∩)O~.
    """
    main()


"""
PlayPlane/
|-- bin/
|   |-- main.py         程序运行主体程序
|-- config/
|   |-- settings.py     程序配置(例如: 游戏背景音乐的加载等)
|-- material            程序素材放置(打飞机游戏素材放置)
    |-- ...
|-- src/                程序主体模块存放
|   |-- __init__.py 
|   |-- bullet.py       我方飞机发射子弹实现代码存放
|   |-- enemy.py        敌方飞机实现代码存放
|   |-- plane.py        我方飞机实现代码存放
|-- manage.py           程序启动文件   
"""


# 2023/12/22：
# 1、修复游戏中窗口无法关闭的问题
# 2、为我方飞机添加血量显示
# 3、加入游戏结束提示
# 4、游戏结束2s后自动初始化游戏（重新开始）
