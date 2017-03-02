#coding=utf8
from uiautomator import device

from time import sleep 

'''
Created on Jan 13, 2017

@author: Administrator
'''

d = device()
print(u"get devices") 
print(d.info)

if d.screen =="off":
    d.wakeup()
    sleep(1)
    print(u"已唤醒屏幕，等待解锁")  
    d.swipe('804','670','56','691',steps=10)      
    #d(className="android.widget.FrameLayout",index=0).swipe('804','670','56','691',steps=10)
    
    print(u"已解锁,等待启动app") 
sleep(1)
print(u"开始启动app") 
d(className="com.veclink.microcomm.healthy/.main.activity.SplashActivity",index="18").click()
print(u"启动app ok") 
sleep(2)
d(className="com.veclink.microcomm.healthy/.main.activity.SplashActivity",text=u"登 录").click()
sleep(1)

