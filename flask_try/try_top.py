# coding=utf-8
'''
Created on Feb 21, 2017

@author: Administrator
'''

import re
import subprocess
#import sys
import time

import xml.etree.ElementTree as etree


target_package = 'com.veclink.microcomm.healthy'
launcher_activity = 'com.veclink.microcomm.healthy/.main.activity.SplashActivity'

dump_file = '/sdcard/window_dump.xml'

# '[42,1023][126,1080]'
bounds_pattern = re.compile(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]')


def run(cmd):
    # adb <CMD>
    '''subprocess.check_output语法: 
      subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
                        语义:
                             运行args定义的命令，并返回一个字符串表示的输出值。
                             如果返回码为非零，则抛出 CalledProcessError异常。
                             如果要捕捉结果中的标准错误，使用 stderr=subprocess.STDOUT参数'''
    
    return subprocess.check_output(('adb %s' % cmd).split(' '),stderr=subprocess.STDOUT)


def sleep_later(duration=0.5):
    def wrapper(func):
        def do(*args, **kwargs):
            func(*args, **kwargs)
            if 'duration' in kwargs.keys():
                time.sleep(kwargs['duration'])
            else:
                time.sleep(duration)

        return do

    return wrapper


def timeit(func):
    '''该装饰器记录函数运行时间，也可用于接口测试时记录时间用于评估性能'''
    def do(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        print('[%s] Time spent %.2f seconds.' % (func.__name__, end - start))
    return do


@sleep_later()
def open_app_detail(package):
    '''进入指定app的系统设置界面'''
    print ('Open application detail setting: %s' % package)
    # adb shell am start -a ACTION -d DATA
    intent_action = 'android.settings.APPLICATION_DETAILS_SETTINGS'
    intent_data = 'package:%s' % package

    run('shell am start -a %s -d %s' % (intent_action, intent_data))


def dump_layout():
    print ('Dump window layouts')
    # adb shell uiautomator dump <FILE>
    run('shell uiautomator dump %s' % dump_file)


def parse_bounds(value_text,tag_text):
    # adb shell cat /sdcard/window_dump.xml
    dumps = run('shell cat %s' % dump_file)
    tree = etree.fromstring(dumps)
    get_node = tree.iter(tag='node')
    for x in get_node :
        
        if x.get(tag_text) == value_text:
            print("------")
            print(x)
            print(x.get('bounds'))
            print(type(x.get('bounds')))
            print("---11111---")
            return x.get('bounds')
        
    #x = nodes.iterfind(u'//node[@text="%s"]/@bounds' % (text))[0]
    
    


def point_in_bounds(bounds):
    """
    '[42,1023][126,1080]'
    """
    points = bounds_pattern.match(bounds).groups()
    #points = map(int, points)
    return (int(points[0]) + int(points[2])) / 2, (int(points[1]) + int(points[3]))/ 2


@sleep_later()
def click_with_keyword(tag_vlue,tag_key='text', dump=True, **kwargs):
    if dump:
        dump_layout()
    bounds = parse_bounds(tag_vlue,tag_key)
    point = point_in_bounds(bounds)

    print ('Click "%s" (%d, %d)' % (tag_vlue, point[0], point[1]))
    # adb shell input tap <x> <y>
    run('shell input tap %d %d' % point)


@sleep_later()
def force_stop(package):
    print ('Force stop %s' % package)
    # adb shell am force-stop <package>
    run('shell am force-stop %s' % package)


@sleep_later(0.5)
def start_activity(activity):
    print ('Start activity %s' % activity)
    # adb shell am start -n <activity>
    run('shell am start -n %s' % activity)


@sleep_later(0.5)
def clear_data(package):
    print ('Clear app data: %s' % package)
    # adb shell pm clear <package>
    run('shell pm clear %s' % package)


@sleep_later()
def keyboard_input(text):
    # adb shell input text <string>
    run('shell input text %s' % text)


@sleep_later()
def keyboard_back():
    # adb shell input keyevent 4
    run('shell input keyevent 4')


@timeit
def main():
    username, password = 'qq@qq.com','123456'
    # 停止应用
    force_stop(target_package)
    # 清除数据
    clear_data(target_package)
    # 启动应用设置页
    #open_app_detail(target_package)
    # 进入权限页
    #click_with_keyword(u'权限')
    # 打开「存储控件权限」
    #click_with_keyword(u'存储')
    # 按一下返回
    #keyboard_back()
    # 启动 app
    start_activity(launcher_activity)
    # 欢迎页跳过
    click_with_keyword(u'跳过')
    # 选中「帐号」输入框
    click_with_keyword(u'请输入账号', duration=0)
    # 输入帐号
    keyboard_input(username)
    # 按一下返回
    #keyboard_back()
    # 选中「密码」输入框
    click_with_keyword(u'com.veclink.microcomm.healthy:id/login_password',tag_key='resource-id', dump=False, duration=0)
    # 输入密码
    keyboard_input(password)
    # 按一下返回
    keyboard_back()
    # 点一下登录按钮
    click_with_keyword(u'登录', dump=False)


if __name__ == '__main__':
    main()