#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Feb 9, 2017

@author: Administrator
'''
import unittest
import requests
import json
import time


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def getAcc_token(self):
        '''刷新会话token'''
        acc_data = {"pwd":"4aeaa0633ad509dccb22ef3eb4a18bd9","uid":"qq@qq.com"}    
        r = requests.get("https://api.sns.movnow.com/sns/access_token",params=acc_data,verify=False)
        print("请求access_token的url为：%s"%r.url)
        print(r.text)
        #返回json数据，解析获取token值
        acc_json = json.loads(r.text)   #{"error_code":0,"access_token":"8ed68627e443be07d2f3f5d05b855d2e"}
        access_token=acc_json["access_token"]
        
        print("获取access_token的值为：%s"%access_token)
        return access_token
    
    def movnow_login(self,login_par):
        '''登录接口实现'''
        #https 有SSL验证，默认是开启的，但是部分服务器未设置有效证书，所以此处通过verify=False 忽略SSL验证或者使用http方式访问（要看服务器是否支持HTTP方式）
        lr = requests.get("https://web.sns.movnow.com/movnow/login",params=login_par,verify=False)
        #lr = requests.get("http://web.sns.movnow.com/movnow/login",params=login_par)
        print("请求login的url为：%s"%lr.url)
        print("login的返回信息为：%s"%lr.text) 
        login_json = json.loads(lr.text)
        print("---------逐个参数校验-------------")
        print("login的返回error_code信息为：%s"%login_json["error_code"])
        print("login的返回user_id信息为：%s"%login_json["user_id"])
        print("login的返回error_text信息为：%s"%login_json["error_text"])
        print("login的返回config信息为：%s"%login_json["config"])
        #print("login的返回error_code信息为：%s"%login_json["error_code"])
        return login_json["user_id"]
    
    def get_userinfo(self,acc_token,uid):
        '''调用info_get接口获取用户头像URl
        '''
        user_par = {"access_token":acc_token,"user_id":uid}
        gr = requests.get("http://webapi.snstest.movnow.com/movnow/info_get",params=user_par)
        print("请求userinfo的url为：%s"%gr.url)
        print("get_userinfo的返回信息为：%s"%gr.text) 
        u_json = json.loads(gr.text)
        print("---------逐个参数校验-------------")
        print("get_userinfo的返回error_code信息为：%s"%u_json["error_code"])
        print("get_userinfo的返回user信息为：%s"%u_json["user"])        
        print("get_userinfo的返回email信息为：%s"%u_json["email"])
        
        return u_json["user"]["icon"] #user用户信息， 对应的是字典类型的数据，单独获取用户头像访问URL
    
    def testforlogin(self):
        
        r_access_token = self.getAcc_token() #获取token作为登录接口的参数
        #模拟登录https://web.sns.movnow.com/movnow/login?password=e10adc3949ba59abbe56e057f20f883e&access_token=8ed68627e443be07d2f3f5d05b855d2e&os=android&user_id=qq@qq.com&mac=02:00:00:00:00:00 HTTP/1.1
        
        login_par = {"password":"e10adc3949ba59abbe56e057f20f883e",
                    "access_token":r_access_token,
                    "os":"android",
                    "user_id":"qq@qq.com",
                    "mac":"02:00:00:00:00:00"}
        
        login_uid = self.movnow_login(login_par) #登录成功并截取uid备用
        print("登录获取的UID=%s"%login_uid)
        
        
        
        #上传用户头像old3.jpg
        #p_icon={'file': with open('old3.jpg', 'rb') } 
        p_data={"uid":login_uid,"access_token":r_access_token}
        with open('old3.jpg', 'rb') as f:   #此处需要以with方式，否则会出现文件未正常关闭的警告
            re_icon = requests.post("http://webapi.snstest.movnow.com/movnow/upload_icon.php",data=p_data,files={'filename':f})
                
        time.sleep(5)
        
        #获取登录账户的信息http://webapi.snstest.movnow.com/movnow/info_get?access_token=8ed68627e443be07d2f3f5d05b855d2e&user_id=200147
        url_info = self.get_userinfo(r_access_token, login_uid)
        print("----------------------")
        #获取用户头像并保存在当前目录下
        icom_down = requests.get(url_info, stream=True)
        #创建或者打开本地文件用于保存接收的数据
        with open("bili.jpg", "wb") as f:
            for chunk in icom_down.iter_content(chunk_size=1024):  
                if chunk: # filter out keep-alive new chunks  
                    f.write(chunk)  
                    f.flush()  
        f.close()
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testforlogin']
    unittest.main()