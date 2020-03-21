# @File: get_authorization_code_by_client_id
# @Author: Kevin Huo
# @LastUpdate: 3/21/2020 12:16 AM

import json
import requests


def _load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        app_json = json.load(f)
    return app_json


def get_authorization_code_by_client_id(app_json_path):
    """
    https://docs.microsoft.com/en-us/graph/auth-v2-user
    该函数是 OAuth 的第一步 - 用 client id 向 https://login.microsoftonline.com 发起请求.
    如果请求成功, 会返回一个 authorization_code.

    PS: 网络中 %2F %3A 等特殊字符的转码:
    https://blog.csdn.net/pcyph/article/details/45010609

    示例请求Url:
    https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=917c36c2-efd2-40c1-bcc9-b2602449f494&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Flogin&response_mode=query&scope=offline_access%20user.read%20mail.read&state=12345

    https://login.microsoftonline.com/common/OAuth2/v2.0/authorize?client_id=917c36c2-efd2-40c1-bcc9-b2602449f494&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Freceive_authZ_code_and_request_access_token&response_mode=query&scope=offline_access%20user.read%20mail.read&state=12345


    这个请求, 会将响应返回到以下url:
    http://localhost:5000/login?code=OAQABAAIAAABeAFzDwllzTYGDLh_qYbH8qvqJgjRzHbFCu2HmuqnoIj1gIDHJiurbxJsUuUqh6XJFvKuDJOzENcz_fMzCUV8VEuYhZCs0RqDmgo8EH9vpbp35nbQzcf7wUJ1tQEzZJIte1tExNk0-TYXeaNnHx05Y_OB1aHQeHayClibBkO3EInpT62w6wZSawOZg-BVQPCjF--HbEt2rcMxcYXDJHD2TAxIkXkl34JHgK74fGHnBAzi-KTBGZcmvfUysqLz2ykcZMIXALdBMI2_IwLLGIv9RbAyXBaAZXwCQwuHRrzcWCusAknK10c0m3FcotRvo0b-rdE4xHnRS31SkW-rEMSu92z6jXkSOv5RQuGExND0nJX-QEKbwJP1JX8TOF1qAE_aeyHJMYBA6Xo1CBKmyx98cCS0k5fv0I4xFlH34A269LG4pz6wSdtQsD-dZxdMMqthKP2cZEiu95lXLBzI7rn4jwZ5v25Ce-yWZV6zJfViqF0ngSYuIqxwPfDM-4oayTXrMF3A25kLO7dk_yPvVF3PUBq69VuKzRzDlGMLDEZ5SqZdnwETr3t1QQFCzhZM8kcBAmqtdjaZPejkxRjWoqsHZfzipxnepaqmfleZuX3V6nKcFvzMYV6jl0OXmHhxiDzggAA&state=12345&session_state=f7c4c589-27f6-4000-9f47-2948169e4e15#
    """
    # 读取 azure_app.json 文件
    app_json = _load_json(app_json_path)

    # 构造 GET 请求
    req_host = "https://login.microsoftonline.com/"
    tenant_name = "common/"
    base = "oauth2/v2.0/authorize"
    query_string = {"client_id": app_json["client_id"],
                    "response_type": app_json["response_type"],
                    "redirect_uri": app_json["raw_redirect_uri"],
                    "response_mode": app_json["response_mode"],
                    "scope": app_json["scope"],
                    "state": app_json["state"]}

    req_url = req_host + tenant_name

    resp = requests.get(req_url, query_string)


def main():
    json_path = "../azure_app.json"
    get_authorization_code_by_client_id(json_path)


if __name__ == '__main__':
    main()
