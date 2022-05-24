'''
@编写人：冯爱军
@开发时间：2021/12/24 10:31
'''
import requests
import os
import sys
import testcases.odlab_login
def odlab_pageQuery():
    url01 = "http://user-gateway.tz-dev.kfy.xip.io/odlab/data/resource/application/pageQuery"
    jsonData01 = {"appType":0,"authorizedOperatorId":"8","currentPage":1}
    headers = {
      'Content-Type': 'application/json;charset=UTF-8'
    }

    print(testcases.odlab_login.odlab_login())
    print("==============================================================================================================")
    r1 =requests.post(url=url01,json=jsonData01,headers = headers,cookies =testcases.odlab_login.odlab_login())
    print(r1.json())
        # if r1.status_code ==200:
        #     print(r1.cookies)
        #     return r1.cookies

if __name__ == '__main__':
    odlab_pageQuery()






