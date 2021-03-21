#!/usr/bin/python
# -*- coding: UTF-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
import json
from urllib import request, parse
from net_event_id import NetEvents
from net_call import NetCall


APP_ID = "cli_a0cf66c4dbb9500d"
APP_SECRET = "1ahp6HKcmxuLfBhPWRfe4bmaRPCB6J4d"
APP_VERIFICATION_TOKEN = "i1SVjjEw1leB9jsxhHEIUbbC0GHvDQcK"

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 解析请求 body
        print('第一步: 获取 post')

        req_body = self.rfile.read(int(self.headers['content-length']))
        obj = json.loads(req_body.decode("utf-8"))
        print('req_body: ', req_body)

        # 校验 verification token 是否匹配，token 不匹配说明该回调并非来自开发平台
        token = obj.get("token", "")
        if token != APP_VERIFICATION_TOKEN:
            print("verification token not match, token =", token)
            self.response("")
            return

        self.handle_request_by_type(obj)

        return


    def handle_request_by_type(self, obj):
        # 根据 type 处理不同类型事件
        type = obj.get("type", "")
        if NetEvents['URL_VERIFICATION'] == type:
            # 验证请求 URL 是否有效
            self.handle_request_url_verify(obj)
        elif NetEvents['EVENT_CALLBACK'] == type:  # 事件回调
            # 获取事件内容和类型，并进行相应处理，此处只关注给机器人推送的消息事件
            event = obj.get("event")
            NetCall.call(NetEvents['EVENT_MESSAGE'], event)
            # if event.get("type", "") == NetEvents['EVENT_MESSAGE']:
            #     self.handle_message(event)
            #     return


    def handle_request_url_verify(self, post_obj):
        # 原样返回 challenge 字段内容
        challenge = post_obj.get("challenge", "")
        rsp = {'challenge': challenge}
        self.response(json.dumps(rsp))
        return

    # def handle_message(self, event):
    #     # 此处只处理 text 类型消息，其他类型消息忽略
    #     msg_type = event.get("msg_type", "")
    #     if msg_type != "text":
    #         print("unknown msg_type =", msg_type)
    #         self.response("")
    #         return

    #     # 调用发消息 API 之前，先要获取 API 调用凭证：tenant_access_token
    #     access_token = self.get_tenant_access_token()
    #     if access_token == "":
    #         self.response("")s
    #         return




    def response(self, body):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(body.encode())





def run():
    port = 8000 # 机器人端口号
    server_address = ('172.17.0.9', port)
    httpServer = HTTPServer(server_address, RequestHandler)
    print("start listen.....")
    httpServer.serve_forever()


def getServer():
    return httpServer

if __name__ == '__main__':
    run()