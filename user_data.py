# /*
#  * @Author: 惊仙 
#  * @Date: 2021-03-15 16:14:27 
#  * @Last Modified by:   惊仙 
#  * @Last Modified time: 2021-03-15 16:14:27 
#  */
# 用户数据

import threading


class user_data:
    class user(object):
        def __init__(self, open_id, name, employee_id):
            self.__open_id = open_id
            self.__name = name
            self.__employee_id = employee_id

        
        def get_open_id(self):
            return self.__open_id


        def get_name(self):
            return self.__name


        def get_employee_id(self):
            return self.__employee_id

    _instance_lock = threading.Lock()
    __user_list = []

    def __new__(cls, *args, **kwargs):
        if not hasattr(user_data, "_instance"):
            with user_data._instance_lock:
                if not hasattr(user_data, "_instance"):
                    user_data._instance = object.__new__(cls)  
        return user_data._instance


    def update_user(self, open_id, name, employee_id):
        user_info = user_data.user(open_id, name, employee_id)
        self.__user_list.append(user_info)
        pass


    def get_user(self):
        self.__user_list.pop()
        pass

    


userData = user_data()