login_requests_post
1��r = requests.get��r = requests.post ��Ӧhttp�������ֶβ�һ����getʹ��params=acc_data��postʹ��data=p_data
2��resp.text���ص���Unicode�͵����ݡ� Ҳ����˵���������ȡ�ı�������ͨ��r.text�� 
ʹ��resp.content���ص���bytes�͵����ݡ� �����ȡͼƬ���ļ��������ͨ��r.content��
3��r.text ת��Ϊjson��ʽʱ����˳����r.text��һ�£���ȡָ��keyֵ����Ӱ��.
4������ת��Ϊjsonʱ��Ҫimport json��Ȼ��json.loads(r.text) 
5��https����ʱ��SSL��֤��Ĭ���ǿ����ģ����ǲ��ַ�����δ������Ч֤�飬ͨ��verify=False ����SSL��֤����ʹ��http��ʽ���ʣ�Ҫ���������Ƿ�֧��HTTP��ʽ��
6��ͨ��post�ϴ���������ͼƬ���ļ���ʱ����ͨ�����·�ʽ����������ļ�δ�����رյľ���
with open('old3.jpg', 'rb') as f:   #�˴���Ҫ��with��ʽ�����������ļ�δ�����رյľ���
            re_icon = requests.post(url,data=p_data,files={'filename':f})

7����ȡ������ͼƬ���ļ�������ͨ�����·�ʽ
icom_down = requests.get(url_info, stream=True)
        #�������ߴ򿪱����ļ����ڱ�����յ�����
        with open("bili.jpg", "wb") as f:
            for chunk in icom_down.iter_content(chunk_size=1024):  
                if chunk: # filter out keep-alive new chunks  
                    f.write(chunk)  
                    f.flush()  
        f.close()        