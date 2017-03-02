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
            #�ȶ�λ�����ڵ㲢���,�����Ҳ����ӽڵ�
            xx= self.x.find_element_by_xpath(".//*[@id='accordion']/div[8]/div[1]/div[1]")
            xx.click()
            sleep(1) 
            fw = self.x.find_element_by_xpath(".//*[@id='accordion']/div[8]/div[2]/ul/li[2]/div/a")
            
        fw.click()
        print("used xpath={0} to click".format(v_path))
        sleep(1)
        #�л����µ�frame���ڣ�
        fname = self.x.find_element_by_name("mainFrame")
        self.x.switch_to.frame(fname)
        #���У���ϴ�ǰ�ܼ�¼��
        r = self.x.find_element_by_xpath(".//*[@id='divMainDataGrid']/div/div/div[3]/div[1]")
        ru = r.text
        print(ru)
        #��λ�������������������
        self.x.find_element_by_xpath(".//*[@id='addButton']/span").click()
    
        sleep(1)
        #������ӹ̼��汾��Ҫ�Ĳ���
        fw_name=self.x.find_element_by_id("FW_NO")
        fw_name.send_keys("2")  
        
        self.x.find_element_by_id("FW_TYPE").send_keys("C001H")
        self.x.find_element_by_id("FW_NAME").send_keys("C002H")
        
        #ѡ��������ѡ��
        fw_s= self.x.find_element_by_name("FLAG")
        fw_s_value=Select(fw_s)
        fw_s_value.select_by_visible_text("��Ч")
        #�����ϴ��ļ�����·��
        uploadf = self.x.find_element_by_name("file")
        uploadf.send_keys("H:\C066A\C066A_V012_B20161219(1).cyacd")      
        sleep(2)
        #����ϴ���ť
        self.x.find_element_by_xpath(".//*[@id='uploadIMG']").click()
        #�ȴ��ļ��ϴ��ɹ�
        sleep(5)
        #�ϴ��ɹ��ĵ����򣬻�ȡ��ʾ��Ϣ�����ȷ��
        b = self.x.switch_to.alert
        print(b.text)            
        b.accept()
        
        sleep(1)        
        #�̼��ϴ��ɹ���ʾ�򣬵��ȷ��
        self.x.find_element_by_xpath(".//*[@id='dlg-buttons']/a[1]/span/span[1]").click()
        sleep(1) 
        #���У���ϴ������ͨ��ƥ���ܼ�¼��
        r1 = self.x.find_element_by_xpath(".//*[@id='divMainDataGrid']/div/div/div[3]/div[1]")
        ru1 = r1.text
        print(ru1)
        
        self.contrast(ru,ru1)
        #�лص���һ���������ڣ�Ȼ��ȷ�Ϲ̼��ϴ��ɹ�����ʾ��
        self.x.switch_to.default_content()
        c = self.x.switch_to.alert
        print(c.text)            
        c.accept()
        sleep(1)
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()