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
    def do(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        print('[%s] Time spent %.2f seconds.' % (func.__name__, end - start))
    return do


@sleep_later()
def open_app_detail(package):
    print ('Open application detail setting: %s' % package)
    # adb shell am start -a ACTION -d DATA
    intent_action = 'android.settings.APPLICATION_DETAILS_SETTINGS'
    intent_data = 'package:%s' % package

    run('shell am start -a %s -d %s' % (intent_action, intent_data))


def dump_layout():
    print ('Dump window layouts')
    # adb shell uiautomator dump <FILE>
    run('shell uiautomator dump %s' % dump_file)


def parse_bounds(text):
    # adb shell cat /sdcard/window_dump.xml
    dumps = run('shell cat %s' % dump_file)
    
    tree = etree.fromstring(dumps)
    
    print("------")
    print(type(tree))
    print(tree)
    print("------")
    neighbor = tree.iter(tag='node')
    for x in neighbor :
        
        if x.get('text') == text:
            print("------")
            print(x.get('bounds'))
            print(type(x.get('bounds')))
            print("---11111---")
            return x.get('bounds')
        
    #x = nodes.iterfind(u'//node[@text="%s"]/@bounds' % (text))[0]
    
    
def point_in_bounds(bounds):
    """
    '[42,1023][126,1080]'
    bounds_pattern = re.compile(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]')
    """
    print("---000---")
    print(bounds)
    print(type(bounds))
    points = bounds_pattern.match(bounds).groups()
    
    print("---2222---")
    print(points)
    print(type(points))
    
    print("---3333---")
    #points = map(int, points)    
    #return (points[0] + points[2]) / 2, (points[1] + points[3]) / 2
    
    return (int(points[0]) + int(points[2])) / 2, (int(points[1]) + int(points[3]))/ 2

@sleep_later()
def click_with_keyword(keyword, dump=True, **kwargs):
    if dump:
        dump_layout()
    bounds = parse_bounds(keyword)
    
    point = point_in_bounds(bounds)

    print ('Click "%s" (%d, %d)' % (keyword, point[0], point[1]))
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
    print(run('devices'))
    


if __name__ == '__main__':
    main()