import requests
import time
import pyperclip
from threading import Thread
from flask import Flask, request

# 设置 API 服务器地址，需要根据实际情况进行修改
API_SERVER_URL = 'http://xxxxxxxxxxxx:8000'

# 全局变量，用于存储剪贴板内容
clipboard_contents = ''

def sync_clipboard():
    """同步剪贴板内容"""
    global clipboard_contents
    # 循环读取剪贴板内容并将其发送到 API 服务器
    while True:
        contents = pyperclip.paste()
        if contents != clipboard_contents:
            clipboard_contents = contents
            print(f'clipboard_contents: {clipboard_contents}')
            requests.post(API_SERVER_URL, data=clipboard_contents.encode('utf-8'))
        time.sleep(0.1)

# 启动剪贴板同步线程
Thread(target=sync_clipboard).start()

# Flask 应用程序对象
app = Flask(__name__)

@app.route('/', methods=['POST'])
def update_clipboard():
    """接收来自其他设备的剪贴板内容，并更新本地剪贴板"""
    global clipboard_contents
    clipboard_contents = request.form.get('contents', '')
    pyperclip.copy(clipboard_contents)
    return 'OK'

if __name__ == '__main__':
    app.run()