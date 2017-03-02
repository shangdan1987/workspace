#coding=utf8
'''
Created on Feb 5, 2017

@author: Administrator
'''
import requests

import unittest
import json

class Test(unittest.TestCase):
    '''test2 class'''

    def setUp(self):
        # 创建一个socket:
        pass

    def tearDown(self):
        # 关闭连接:
        pass
           
  
    def testName(self):
        '''test2 testname'''
        # 发送数据:curl "http://q.movnow.com/firmware/list.do" 
        #r = requests.get("http://q.movnow.com/firmware/list.do")
        
        p_data = {
            'method':'firmware.list',
            'v':'2.0.0',
            'app_key':'stest'
        }
        r = requests.post("http://q.movnow.com/rest",data=p_data)
        print(r.url)
        print("-----1-------")
        print(r.text)
        jd = json.loads(r.text)
        for x in jd:
            
            if x["mId"] == 327:
                print("-----5-------")
                print(x["firmwareVer"]) 
         
        
        print("-----2-------")
        print(r.json())     
        print("-----3-------")
         
        print(r.cookies)
        print("-----4-------")
        print(r.status_code)
        print("-----5-------")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()