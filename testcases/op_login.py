#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/5/24 17:16
 @功能模块:
 @模块备注:台州开放域测试环境
"""
import requests
import pytest
def op_login():
    url = "http://dfh-user-facade.tz-dev.kfy.xip.io/sso/login"
    params = {
        "account":"admin",
        "password":"szzj123456",
        "service":"http://api-inner-gateway.tz-dev.kfy.xip.io/ops"
    }
    r1 = requests.post(url, data=params)
    print(r1.text)
    print(r1.json())
    print(r1.json()['data'])
    return r1.cookies
    assert r1.json()['success'] == True
    assert r1.status_code == 200
    assert 4==4

    # if r1.status_code == 200:
    #    print(r1.cookies)
    # loginCookies1=''
    # for cookie in r1.cookies:
    #     print(str(cookie.name)+"="+str(cookie.value))
    #     loginCookies1 = loginCookies1+str(cookie.name)+"="+str(cookie.value)+';'
    #     print('=======================================================================')
    #     print(cookie)
    # print(loginCookies1)
    # # return loginCookies
    # print(r1.cookies)

# def op_login_01(){
#
# }

if __name__ == '__main__':
     pytest.main()