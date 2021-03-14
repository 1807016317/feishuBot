#!/usr/bin/python
# -*- coding: UTF-8 -*-

# /*
#  * @Author: 惊仙 
#  * @Date: 2021-03-14 21:51:32 
#  * @Last Modified by:   惊仙 
#  * @Last Modified time: 2021-03-14 21:51:32 
#  */
# 机器人消息事件处理

import const
import re
import emoj_mgr

const.TEXT_MSG = 'text' # 文本类型消息
const.EMOJ_REG = 'emoj:'

response_content = ''

class message_handle:
    def __init__(self, event):
        self.event = event

    
    def handle_event(self):
        # 处理消息事件类型，分发到各函数
        msg_type = self.event.get("msg_type", "")
        if msg_type == const.TEXT_MSG:
            self.handle_text_msg(msg_text_content)
        else:
            print("unknown msg_type =", msg_type)
            # self.response("")
            return


    def handle_text_msg(self):
        # 此处只处理 text 类型消息
        # 调用发消息 API 之前，先要获取 API 调用凭证：tenant_access_token
        access_token = self.get_tenant_access_token()
        if access_token == "":
            self.response("")
            return

        msg_text_content = self.event.get("text")
        response_content = msg_text_content
        
        is_emoj_req = re.match(const.EMOJ_REG, msg_text_content)
        if is_emoj_req != None:
            search_content = re.sub(const.EMOJ_REG, '', msg_text_content)
            emojMgr = emoj_mgr.emoj_mgr(search_content)
            search_result = emojMgr.start()
            if search_result:
                response_content = emojMgr.get_emoj_url()
            

        # 机器人 echo 收到的消息
        self.send_message(access_token, event.get("open_id"), response_content)
        self.response("")
        return

        