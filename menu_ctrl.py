#!/usr/bin/python
# -*- coding: UTF-8 -*-
# /*
#  * @Author: 惊仙 
#  * @Date: 2021-03-24 20:24:03 
#  * @Last Modified by:   惊仙 
#  * @Last Modified time: 2021-03-24 20:24:03 
#  */
# 菜单管理
import threading
import cfg.zn as ZN

class menu_ctrl:
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(menu_ctrl, "_instance"):
            with menu_ctrl._instance_lock:
                if not hasattr(menu_ctrl, "_instance"):
                    menu_ctrl._instance = object.__new__(cls)  
        return menu_ctrl._instance

    
    def show_menu(self):
        # 展示菜单
        menu_text = ZN.MENU_EMOJ + '\n' + ZN.MENU_TABLE
        pass