from tqdm import tqdm
import requests
from tkinter import filedialog
import tkinter.filedialog


def 获取文件大小():
    responsehead = requests.head(url, headers=headers)
    # 文件大小，以 B 为单位
    return int(responsehead.headers.get('Content-Length'))


def 开始下载(file_size, file_name):
    global seek
    headers['Range'] = f'bytes={start}-{end}'
    print("文件大小",file_size/1000000000)
    response = requests.get(url=url, headers=headers, proxies=proxies, params=params, timeout=5, stream=True)
    # 一块文件的大小
    bar = tqdm(total=(min(end,file_size)-start)/1000000, desc=f'下载文件 {file_name}')
    with open(file_name, mode='ab') as f:
        # 写入分块文件
        for chunk in response.iter_content(chunk_size=chunk_size):
            _seek = min(seek + chunk_size, end)
            seek = _seek
            f.write(chunk)
            bar.update(chunk_size/1000000)
    # 关闭进度条
    bar.close()


def 文件合成():
    filename = tkinter.filedialog.askopenfilename()  # 获得完整文件地址
    print(filename)
    with open("测试文件", mode='ab') as f:
        with open(filename, mode="rb") as r:
            while True:
                chunk = r.read(10000)
                if not chunk:
                    return
                f.write(chunk)


url = '''https://mirrors.aliyun.com/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-2207-02.iso'''
headers = {"user-agent": "NSPlayer/12.00.22621.2428 WMFSDK/12.00.22621.2428", }
params = {}  # "abc":123路径参数,例如http://www.baidu.com?abc=123
proxies = {"http": None, "https": None}  # proxies代理给他关了
# 待下载部分的文件起始位置和终止位置.单位GB(非GiB)
start = 4
end = 5
start = start * 1000000000
end = end * 1000000000 - 1
# 每次读取的大小
chunk_size = 128
# 记录下载的位置
seek = start



开始下载(获取文件大小(), "测试文件")
# 文件合成()
