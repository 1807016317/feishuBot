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
from net_call import NetCall
from net_event_id import NetEvents

const.TEXT_MSG = 'text' # 文本类型消息
const.EMOJ_REG = 'e-'

response_content = ''

class message_ctrl:
    def __init__(self):
        pass


    def register_listen(self):
        """
        注册事件监听
        """
        NetCall.addListen(NetEvents.EVENT_MESSAGE, self.handle_event)
        pass
        
    
    def handle_event(self, event):
        self.event = event
        # 处理消息事件类型，分发到各函数
        msg_type = self.event.get("msg_type", "")
        if msg_type == const.TEXT_MSG:
            self.handle_text_msg()
        else:
            print("unknown msg_type =", msg_type)
            # self.response("")
            return


    def handle_text_msg(self):
        # 此处只处理 text 类型消息
        msg_text_content = self.event.get("text")
        response_content = msg_text_content
        
        is_emoj_req = re.match(const.EMOJ_REG, msg_text_content)
        if is_emoj_req == None:
            
        elif is_emoj_req != None:
            search_content = re.sub(const.EMOJ_REG, '', msg_text_content)
            emojMgr = emoj_mgr.emoj_mgr(search_content)
            search_result = emojMgr.start()
            if search_result:
                response_content = emojMgr.get_emoj_url()
        

        