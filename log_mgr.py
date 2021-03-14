# /*
#  * @Author: 惊仙
#  * @Date: 2021-03-14 20:34:37
#  * @Last Modified by: 惊仙
#  * @Last Modified time: 2021-03-14 20:35:58
#  */
# 日志管理

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import time
import json
from os import path
 
current_work_dir = path.dirname(__file__)  # 当前文件所在的目录

class log_mgr:
    def __init__(self, *args):
        pass


    @ staticmethod
    def export_log_file(log_content):
        log_time = time.localtime()
        time_str = ''
        time_range = len(log_time) - 1
        for index in range(time_range):
            time_str += (str(log_time[index]) + '-')

        log_file_name = time_str + 'log.log'
        file_path = path.join(current_work_dir, log_file_name)  # 再加上它的相对路径，这样可以动态生成绝对路径
        print('file_path: ', file_path)
        with open(file_path, 'w+', encoding = 'utf-8') as log_f:
            jsonStr = json.dumps(
                            log_content, ensure_ascii = False, indent = 2)
            log_f.write(jsonStr)

        print("log write", log_f.closed)
