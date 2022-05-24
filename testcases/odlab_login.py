#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/5/7 11:05
 @功能模块:
 @模块备注:
"""
import pytest
import requests
from requests.cookies import RequestsCookieJar
def odlab_login():
    url = "http://user-gateway.tz-dev.kfy.xip.io/odlab/sub/account/login"
    jsonData = {"loginName":"11010119900307723X","password":"07723X"}
    r = requests.post(url=url, json=jsonData)
    if r.status_code ==200:
       print(r.cookies)
    loginCookies=''
    for cookie in r.cookies:
        print(str(cookie.name)+"="+str(cookie.value))
        loginCookies = loginCookies+str(cookie.name)+"="+str(cookie.value)+';'
        print('=======================================================================')
        print(cookie)
    print(loginCookies)
    # return loginCookies
    print(r.cookies)
    return r.cookies
        # print(r)
        # print('=============================')
        # print(r.json())
        # print('=============================')
        # print(r.status_code)
        # print('=============================')
        # print(r.content)
        # print('-----------------------------------------------------------------------------------------')
        # print(r.headers)
        # print('--------------------==================================================================')
        # print(r.headers.get('Set-Cookie'))

if __name__ == '__main__':
    odlab_login()