login_requests_post
1、r = requests.get和r = requests.post 对应http参数的字段不一样，get使用params=acc_data；post使用data=p_data
2、resp.text返回的是Unicode型的数据。 也就是说，如果你想取文本，可以通过r.text。 
使用resp.content返回的是bytes型的数据。 如果想取图片，文件，则可以通过r.content。
3、r.text 转换为json格式时内容顺序与r.text不一致，获取指定key值不受影响.
4、数据转换为json时需要import json，然后json.loads(r.text) 
5、https请求时有SSL验证，默认是开启的，但是部分服务器未设置有效证书，通过verify=False 忽略SSL验证或者使用http方式访问（要看服务器是否支持HTTP方式）
6、通过post上传带参数的图片（文件）时建议通过如下方式，避免出现文件未正常关闭的警告
with open('old3.jpg', 'rb') as f:   #此处需要以with方式，否则会出现文件未正常关闭的警告
            re_icon = requests.post(url,data=p_data,files={'filename':f})

7、获取服务器图片（文件）建议通过如下方式
icom_down = requests.get(url_info, stream=True)
        #创建或者打开本地文件用于保存接收的数据
        with open("bili.jpg", "wb") as f:
            for chunk in icom_down.iter_content(chunk_size=1024):  
                if chunk: # filter out keep-alive new chunks  
                    f.write(chunk)  
                    f.flush()  
        f.close()        