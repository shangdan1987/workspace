#coding=utf8
'''
Created on Jan 12, 2017

@author: Administrator
'''
from appium import webdriver
from time import sleep
import unittest


class login(unittest.TestCase):
    '''test_bak class'''
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'PLK-UL00'        
        desired_caps['appPackage'] = 'com.veclink.microcomm.healthy'
        desired_caps['appActivity'] = 'com.veclink.microcomm.healthy.main.activity.SplashActivity'
        desired_caps['waitappActivity'] ='com.veclink.microcomm.healthy/.main.activity.SplashActivity'
        desired_caps['unicodeKeyboard'] ='True'
        desired_caps['resetKeyboard'] ='True'
        self.r = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)
        print(u"1111")

    def tearDown(self):
        self.r.close_app()
        self.r.quit()
    
    def test_loginpass(self):
        '''test_bak login'''
        sleep(3)
        print(self.r.current_activity)
        print(u"333") 
        print(self.r.contexts)
        print(u"1111") 
        # sleep(3)
        # self.r.find_element_by_id('com.veclink.microcomm.healthy:id/login_username').send_keys(u"qqq@qq.com")
        # print(u"已输入账户")
        # self.r.find_element_by_id('com.veclink.microcomm.healthy:id/login_password').send_keys(u"123456")
        # print(u"已输入密码")
        # self.r.press_keycode("4")
        # sleep(2)
        # self.r.find_element_by_class_name("android.widget.Button").click()
        # print(u"已点击登录")
        # sleep(5)
        self.r.find_element_by_id('com.veclink.microcomm.healthy:id/tran_title_img_left').click()
        print(u"已点击头像") 
        sleep(1)
        self.r.find_element_by_id('com.veclink.microcomm.healthy:id/item_mine_rela').click()
        print(u"已点击目标") 
        sleep(1)
        self.r.find_element_by_id('com.veclink.microcomm.healthy:id/dialog_editext').clear()
        print(u"已清空预置数据") 
        self.r.find_element_by_id('com.veclink.microcomm.healthy:id/dialog_editext').send_keys(u"5050")
        print(u"已输入新值5050") 
        sleep(1)
        self.r.find_element_by_id('com.veclink.microcomm.healthy:id/dialog_tem_btn_yes').click()
        print(u"已点击确定，保存新增") 
        sleep(2)
        self.r.find_element_by_id('com.veclink.microcomm.healthy:id/tran_title_img_right').click()
        sleep(1)
        
        self.r.find_element_by_id('com.veclink.microcomm.healthy:id/setting_exit').click()
        print(u"已点击退出") 
        sleep(1)
        self.r.find_element_by_id('com.veclink.microcomm.healthy:id/dialog_single_tem_btn_yes').click()
        print(u"已点击确定") 
        sleep(1)
        
if __name__ == "__main__":
    unittest.main()


