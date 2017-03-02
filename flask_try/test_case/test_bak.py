#-*-coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pyquery import PyQuery
import unittest
import time
from time import sleep

class login(unittest.TestCase):
    '''test_bak class'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
    
    def test_loginpass(self):
        '''test_bak login'''
        driver = self.driver
        driver.get(self.base_url)
        
        driver.find_element_by_xpath(".//*[@id='u1']/a[8]").click()                
        #js = 'document.findElement(By.xpath(".//*[@id=\'wrapper\']/div[6]")).style.display="block";'
        #js_r = driver.execute_script('$(".bdpfmenu").css({"display":"block"})')
        #js_r = driver.execute_script('$(".bdpfmenu").style.display="block"')
        
        #sleep(1)
        #print(js_r)
        
        sleep(1)
        driver.find_element_by_xpath(".//*[@id='wrapper']/div[6]/a[1]").click()
        sleep(1)
        #driver.find_element_by_css_selector(".setpref").click()
        m=driver.find_element_by_name("NR")
        try:
            m.find_element_by_xpath(".//*[@id='nr']").click()
        except:
            driver.get_screenshot_as_file("D:/screenshots/dd.png")#如果没有找到上面的元素就截取当前页面。
            time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()
        driver.switch_to_alert().accept()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    unittest.main()