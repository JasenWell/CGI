#!E:\Python\Anaconda3\python.exe
# coding=utf-8

import cgi, cgitb
from os.path import join, abspath
import sys, os, logging, time

cgitb.enable()


def test():
    directory = "./dir"
    os.chdir(directory)  # 切换到directory目录
    cwd = os.getcwd()  # 获取当前目录即dir目录下


def deleteBySize(minSize):
    """删除小于minSize的文件（单位：K）"""
    files = os.listdir(os.getcwd())  # 列出目录下的文件
    for file in files:
        if os.path.getsize(file) < minSize * 1000:
            os.remove(file)  # 删除文件
            print(file + " deleted")
    return


def deleteNullFile():
    '''删除所有大小为0的文件'''
    files = os.listdir(os.getcwd())
    for file in files:
        if os.path.getsize(file) == 0:  # 获取文件大小
            os.remove(file)
            print(file + " deleted.")
    return


def create():
    '''根据本地时间创建新文件，如果已存在则不创建'''
    import time
    t = time.strftime('%Y-%m-%d', time.localtime())  # 将指定格式的当前时间以字符串输出
    suffix = ".docx"
    newfile = t + suffix
    if not os.path.exists(newfile):
        f = open(newfile, 'w')
        f.close()
        print(newfile + " created.")
    else:
        print(newfile + " already existed.")
    return


def run():
    print('Content-type: text/html\n')
    timeFormat = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(level=logging.INFO, filename='cgi_log.log', filemode='a+')
    form = cgi.FieldStorage()
    filename = form.getvalue('filename')
    username = form.getvalue('username')
    if not filename:
        print('Please enter a file name')
        sys.exit()
    if not username:
        print('Please enter your name')
        sys.exit()

    BASE_DIR = abspath('data')
    if not os.path.isdir(BASE_DIR):
        os.makedirs(BASE_DIR, True)
        logging.info(time.strftime(timeFormat, time.localtime())+ ' ==> makedirs: '+ BASE_DIR)
    path = join(BASE_DIR, filename)
    if not os.path.exists(path):# os.path.isfile() 也可以判断
        with open(path, 'w') as f:  # 不存在文件就创建
            logging.info(time.strftime(timeFormat, time.localtime())+' ==> makefile: '+path)

    with open(path) as f:
        text = f.read()

    print("""
    <html>
        <head>
            <title>Editing...</title>
        </head>
        <body>
            <form action='chapter25_save.py' method='POST'>
                <b>File:</b>{}<br/>
                <input type='hidden' value='{}' name='filename'/>
                <input type='hidden' value='{}' name='lasttext'/>
                <input type='hidden' value='{}' name='username'/>
                <b>Password:</b><br/>
                <input type='password' name='password'/><br/>
                <b>Text:</b><br/>
                <textarea cols='40' rows='20' name='text'>{}</textarea><br/>
                <input type='submit' value='Save'/>
            </form>
        </body>
    </html>
    """.format(filename, filename, text,username,text))


run()
