#coding=utf8
'''
Created on Dec 26, 2016

@author: Administrator
'''
import unittest
from ddt import ddt,data,unpack
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

@ddt
class Test(unittest.TestCase):


    def setUp(self):
        self.x  = webdriver.Firefox()
        self.x.implicitly_wait(20)
        self.x.get("http://web.sns.movnow.com/ht/login.php")

    def tearDown(self):
        
        self.x.quit()
        
    def contrast(self,n,n1):
        
        if int(n[8:-2]) == int(n1[8:-2])-1 :
            print("Add record OK")
        else:
            print("Add record failed") 
    @data(("fw","888888",1),("admin","1234qwer",0))
    @unpack
    def testName(self,v_name,v_pwd,v_path):
        self.x.find_element_by_name("username").send_keys(v_name)
        self.x.find_element_by_name("password").send_keys(v_pwd)
        sleep(1)
        self.x.find_element_by_id("btn-login").click()
        print("used :{0} and {1} login ".format(v_name, v_pwd))
        '''try:
            b = x.switch_to.alert
            print(b.text)
            
            b.accept()
            sleep(2)
            print("login for test is err err")
        except:
            print("login for test get exception")'''
                 
        try :
            self.x.find_element_by_id("loginOut")
            print("login for test is ok")
        except :
            print("login for test is err")
        
        if v_path==1 :
            fw = self.x.find_element_by_xpath(".//*[@id='accordion']/div/div[2]/ul/li/div/a")  
        else:
            #先定位到父节点并点击,否则找不到子节点
            xx= self.x.find_element_by_xpath(".//*[@id='accordion']/div[8]/div[1]/div[1]")
            xx.click()
            sleep(1) 
            fw = self.x.find_element_by_xpath(".//*[@id='accordion']/div[8]/div[2]/ul/li[2]/div/a")
            
        fw.click()
        print("used xpath={0} to click".format(v_path))
        sleep(1)
        #切换到新的frame窗口，
        fname = self.x.find_element_by_name("mainFrame")
        self.x.switch_to.frame(fname)
        #检查校验上传前总记录数
        r = self.x.find_element_by_xpath(".//*[@id='divMainDataGrid']/div/div/div[3]/div[1]")
        ru = r.text
        print(ru)
        #定位到‘新增’并点击操作
        self.x.find_element_by_xpath(".//*[@id='addButton']/span").click()
    
        sleep(1)
        #输入添加固件版本需要的参数
        fw_name=self.x.find_element_by_id("FW_NO")
        fw_name.send_keys("2")  
        
        self.x.find_element_by_id("FW_TYPE").send_keys("C001H")
        self.x.find_element_by_id("FW_NAME").send_keys("C002H")
        
        #选择下拉框选项
        fw_s= self.x.find_element_by_name("FLAG")
        fw_s_value=Select(fw_s)
        fw_s_value.select_by_visible_text("生效")
        #设置上传文件所在路径
        uploadf = self.x.find_element_by_name("file")
        uploadf.send_keys("H:\C066A\C066A_V012_B20161219(1).cyacd")      
        sleep(2)
        #点击上传按钮
        self.x.find_element_by_xpath(".//*[@id='uploadIMG']").click()
        #等待文件上传成功
        sleep(5)
        #上传成功的弹出框，获取提示信息并点击确认
        b = self.x.switch_to.alert
        print(b.text)            
        b.accept()
        
        sleep(1)        
        #固件上传成功提示框，点击确认
        self.x.find_element_by_xpath(".//*[@id='dlg-buttons']/a[1]/span/span[1]").click()
        sleep(1) 
        #检查校验上传结果，通过匹配总记录数
        r1 = self.x.find_element_by_xpath(".//*[@id='divMainDataGrid']/div/div/div[3]/div[1]")
        ru1 = r1.text
        print(ru1)
        
        self.contrast(ru,ru1)
        #切回到上一级的主窗口，然后确认固件上传成功的提示框
        self.x.switch_to.default_content()
        c = self.x.switch_to.alert
        print(c.text)            
        c.accept()
        sleep(1)
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()