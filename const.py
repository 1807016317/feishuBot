#!/usr/bin/python
# -*- coding: UTF-8 -*-

# # /*
#  * @Author: 惊仙 
#  * @Date: 2021-03-14 21:57:56 
#  * @Last Modified by:   惊仙 
#  * @Last Modified time: 2021-03-14 21:57:56 
#  */
# 常量

class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind const instance attribute (%s)" % name

        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()