# /*
#  * @Author: 惊仙 
#  * @Date: 2021-03-15 13:31:31 
#  * @Last Modified by:   惊仙 
#  * @Last Modified time: 2021-03-15 13:31:31 
#  */
# 网络消息通知

import threading
import util

class net_call:
    _instance_lock = threading.Lock()
    __callback_dict = {}
    """
    网络消息通知
    """
    def __init__(self):
        pass


    def __new__(cls, *args, **kwargs):
        if not hasattr(net_call, "_instance"):
            with net_call._instance_lock:
                if not hasattr(net_call, "_instance"):
                    net_call._instance = object.__new__(cls)  
        return net_call._instance


    def addListen(self, key, callback):
        if self.__callback_dict[key] == None:
            self.__callback_dict[key] = []
        
        self.__callback_dict[key].append(callback)
        

    def call(self, key, *param):
        if self.__callback_dict[key] != None:
            for callback in self.__callback_dict[key]:
                util.safeCallback(callback, *param)
        


NetCall = net_call()