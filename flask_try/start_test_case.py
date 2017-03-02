#coding=utf-8

import sys
sys.path.append("\test_case")
from test_case import test_bak,test2  

import unittest
import HTMLTestRunner
import time

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(test2.Test))
suite.addTest(unittest.makeSuite(test_bak.login))

now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename='F:\\workspace\\'+now+"test_all.html"

fp=open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'web自动化测试报告',description=u'测试用例结果')
runner.run(suite)
fp.close()