import urllib.request,urllib.parse
import json

content= input("say something:")

url='http://fanyi.baidu.com/v2transapi'

ua='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

udata={'query':content,
       'from':'en',
        'to':'zh',
        'transtype':'realtime',
        'simple_means_flag':len(content)}

udata1=urllib.parse.urlencode(udata).encode('utf-8') #按照要求编码成默认的格式
req=urllib.request.Request(url,udata1)#组装拼接请求消息
req.add_header('User-Agent',ua) #添加自定义的消息头,伪装为浏览器

#访问之前可以设置代理方式访问
proxy_=urllib.request.ProxyHandler({'http':'60.13.143.99:8080'})#设置代理参数，字典类型
opener = urllib.request.build_opener(proxy_)#定制一个代理，可以定制head
opener.addheaders=[('User-Agent',ua)] #添加自定义的消息头
#安装一个代理到系统中，之后的所有请求均通过代理访问，如果不安装的话可以通过直接
#调用的方式实现，例如opener.oprn(url)
urllib.request.install_opener(opener)
#以上为设置代理实现

resp = urllib.request.urlopen(req)#执行请求
ht=resp.read().decode('utf-8') #返回的内容解码为utf-8

j_ht=json.loads(ht)#返回内容解析为json
print('------2-----------')
print(j_ht)
print('------3-----------')
a =  j_ht['trans_result']['data'][0]['result'][0][1]
print(a)
print('------1-----------')
#print()