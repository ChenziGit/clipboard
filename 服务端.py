import pyperclip
from flask import Flask, request

# 设置剪贴板历史记录文件的名称
CLIPBOARD_HISTORY_FILE = 'clipboard_history.txt'

# 初始化 Flask 应用程序
app = Flask(__name__)
clipboard_contents = ''

# 定义路由处理程序
@app.route('/', methods=['POST'])
def update_clipboard():
    # 从请求中获取剪贴板内容
    global clipboard_contents
    clipboard_contents = request.form.get('contents', '')
    pyperclip.copy(clipboard_contents)

    # 将剪贴板内容写入历史记录文件
    with open(CLIPBOARD_HISTORY_FILE, 'a') as f:
        f.write(clipboard_contents + '\n')

    # 返回成功响应
    return 'OK'

# 启动 Flask 应用程序

if __name__ == '__main__':

    # 监听所有地址的 8000 端口
    app.run(host='0.0.0.0', port=8000,debug=True)