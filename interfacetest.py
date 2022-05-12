# -*- coding=utf-8 -*-
# @Time: 2022/5/12 21:55
# @Author: John
# @File: interfacetest.py
# @Software: PyCharm
import requests as requests



class TestApi:
    access_token=""
    def test_get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        data={
            "corpid":"wwef4be8e3973e3c69",
            "corpsecret":"BJyyn3HjJv8ufPXf7Q3GZA2D16zPwke6j9S41WmD1Y4"
        }
        res=requests.get(url,params=data).json()
        TestApi.access_token = res["access_token"]
        print(res["access_token"])

    def test_get_tags(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tags/get"
        data = {
            "access_token": TestApi.access_token

        }
        res1 = requests.get(url, params=data)
        print(res1.json())




if __name__ == '__main__':
   TestApi().test_get_token()
   TestApi().test_get_tags()

