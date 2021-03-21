# /*
#  * @Author: 惊仙
#  * @Date: 2021-03-20 23:09:27
#  * @Last Modified by:   惊仙
#  * @Last Modified time: 2021-03-20 23:09:27
#  */
# 网络消息回复

class net_sender:
    def send_handle(self, content):
            # 调用发消息 API 之前，先要获取 API 调用凭证：tenant_access_token
        access_token = self.get_tenant_access_token()
        if access_token == "":
            self.response("")
            return
        
        # 机器人回复消息
        self.send_message(access_token, event.get("open_id"), content)
        self.response("")
        return


    def get_tenant_access_token(self):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
        headers = {
            "Content-Type" : "application/json"
        }
        req_body = {
            "app_id": APP_ID,
            "app_secret": APP_SECRET
        }

        data = bytes(json.dumps(req_body), encoding='utf8')
        req = request.Request(url=url, data=data, headers=headers, method='POST')
        try:
            response = request.urlopen(req)
        except Exception as e:
            print('decode: ', e.read().decode())
            return ""

        rsp_body = response.read().decode('utf-8')
        rsp_dict = json.loads(rsp_body)
        code = rsp_dict.get("code", -1)
        if code != 0:
            print("get tenant_access_token error, code =", code)
            return ""
        return rsp_dict.get("tenant_access_token", "")



    def send_message(self, token, open_id, text):
        url = "https://open.feishu.cn/open-apis/message/v4/send/"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        req_body = {
            "open_id": open_id,
            "msg_type": "text",
            "content": {
                "text": text
            }
        }

        data = bytes(json.dumps(req_body), encoding='utf8')
        req = request.Request(url=url, data=data,
                              headers=headers, method='POST')
        try:
            response = request.urlopen(req)
        except Exception as e:
            print('decode2: ', e.read().decode())
            return

        rsp_body = response.read().decode('utf-8')
        rsp_dict = json.loads(rsp_body)
        code = rsp_dict.get("code", -1)
        if code != 0:
            print("send message error, code = ", code,
                ", msg =", rsp_dict.get("msg", ""))
