#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from weibo import APIClient
import webbrowser

APP_KEY = '2401928872'
APP_SECRET = 'a2c6813e42cdcc1f9b762e4eeaf496dc'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'

# 利用官方微博SDK
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

# 得到授权页面的url，利用webbrowser打开这个url
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

# 可以打印下看看里面都有什么东西
statuses = client.statuses__friends_timeline()['statuses']  # 获取当前登录用户以及所关注用户（已授权）的微博

length = len(statuses)

print length

for i in range(0, length):
    print u'昵称：' + statuses[i]['user']['screen_name']
    print u'简介：' + statuses[i]['user']['description']
    print u'位置：' + statuses[i]['user']['location']
    print u'微博：' + statuses[i]['text']
