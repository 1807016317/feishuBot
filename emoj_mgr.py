#!/usr/bin/python
# -*- coding: UTF-8 -*-

# /*
#  * @Author: 惊仙
#  * @Date: 2021-03-14 20:36:14
#  * @Last Modified by:   惊仙
#  * @Last Modified time: 2021-03-14 20:36:14
#  */
# 表情包处理

from urllib import request, parse
import re
import os
import sys
import log_mgr
import threading
import random
# reload(sys)
# sys.setdefaultencoding('utf8')

home_url = 'https://fabiaoqing.com'  # 首页
search_temp = '/search/bqb/keyword/want_find/type/bq/page/url_page.html'
reg_content = r'want_find'  # 查询内容替换正则
reg_page = r'url_page'  # 查询结果第几页替换正则
reg_img = '<img class.*?/>'  # 查询结果网页解析正则
img_info_list = []


class emoj_mgr:
    _instance_lock = threading.Lock()


    def __init__(self):
        # self.start()
        pass


    def __new__(cls, *args, **kwargs):
        if not hasattr(emoj_mgr, "_instance"):
            with emoj_mgr._instance_lock:
                if not hasattr(emoj_mgr, "_instance"):
                    emoj_mgr._instance = object.__new__(cls)  
        return emoj_mgr._instance


    def splic_search_url(self):
        # 拼接出搜索结果页的链接
        # https://fabiaoqing.com/search/bqb/keyword/你过来啊/type/bq/page/1.html
        total_url = home_url + search_temp
        search_url = total_url.replace(reg_content, self.search_content_encode)
        search_url = search_url.replace(reg_page, self.url_page)
        print("goto: ", search_url)
        return search_url


    def req_emoj_search(self):
        # 向搜索结果链接发起请求
        search_url = self.splic_search_url()
        url_content = request.urlopen(search_url)
        print(url_content)

        html_utf8 = url_content.read().decode('utf-8')
        img_div_list = re.findall(reg_img, html_utf8)
        img_id = 0

        for img_div in img_div_list:
            img_info_tuple = re.findall(r"(original|title)=(\".*?\")", img_div)
            key = "img_%d" % (img_id)
            img_info_dict = {key: {}}
            for info_dict in img_info_tuple:
                img_info_value = re.sub(r'\"', "", info_dict[1])
                img_info_dict[key][info_dict[0]] = img_info_value

            img_info_list.append(img_info_dict)
            img_id += 1

        log_mgr.log_mgr.export_log_file(img_info_list, 'bot_log')
        if len(img_info_list) == 0:
            print('not find any emoj.')
            return False
            
        return True


    def get_emoj_url(self):
        # 获取最终表情包链接
        maxOrder = len(img_info_list) - 1
        orderNum = random.randint(0, maxOrder)
        img_info_dict = img_info_list[orderNum]
        img_url = img_info_dict['img_%d' % (orderNum)]['original']
        return img_url


emojMgr = emoj_mgr


def start(search_str, page_num = 1):
    print('start search emoj...')
    # emoj_mgr = emoj_mgr("你过来啊")
    global emojMgr
    emojMgr = emoj_mgr()
    emojMgr.search_content_encode = parse.quote_plus(search_str)  # 查询内容
    emojMgr.url_page = str(page_num)  # 查询结果第几页
    search_result = emojMgr.req_emoj_search()
    return search_result


def get_emoj():
    return emojMgr.get_emoj_url()