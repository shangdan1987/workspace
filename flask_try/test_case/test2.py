#coding=utf8
'''
Created on Dec 26, 2016

@author: Administrator
'''
import unittest

from selenium import webdriver
from time import sleep


class Test(unittest.TestCase):
    '''test2 class'''

    def setUp(self):
        self.x  = webdriver.Firefox()
        self.x.implicitly_wait(20)
        self.x.get("http://web.sns.movnow.com/ht/login.php")

    def tearDown(self):
        
        self.x.quit()    
  
    def testName(self):
        '''test2 testname'''
        self.x.find_element_by_name("username").send_keys("admin")
        self.x.find_element_by_name("password").send_keys("1234")
        sleep(1)
        self.x.find_element_by_id("btn-login").click()
        sleep(1)
        try:
            b = self.x.switch_to.alert
            print(b.text)
            print("login for test is err err")
        except:
            print("login for test get exception")
          
        self.x.save_screenshot("test2.png")
        self.x.get_screenshot_as_file('F:/workspace/python.hello/test.png')
        sleep(2)
        b.accept()
        sleep(2)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()