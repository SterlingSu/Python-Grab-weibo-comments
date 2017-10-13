#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from weibo import APIClient

import webbrowser

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

APP_KEY = '2401928872'
APP_SECRET = 'a2c6813e42cdcc1f9b762e4eeaf496dc'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print url
webbrowser.open_new(url)

# 获取code=后面的内容
print '输入url中code后面的内容后按回车键：'
code = raw_input()
r = client.request_access_token(code)
access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in  # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4

# 设置得到的access_token
client.set_access_token(access_token, expires_in)

# 调用API爬单条微博
r = client.comments.show.get(id=4160547165300149, count=200, page=1)

for st in r.comments:
    text = st.text
    print text
