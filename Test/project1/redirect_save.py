#!E:\Python\Anaconda3\python.exe
# coding=utf-8

import cgi, cgitb
from os.path import join, abspath
from hashlib import sha1  # 安全散列算法
import sys, logging, time, os

# print(sha1(b'123456').hexdigest())
cgitb.enable()
logging.basicConfig(level=logging.INFO, filename='cgi_log.log', filemode='a+')


def run():
    logging.info('redirect_save')
    print('Content-type: text/html\n')
    print("""
        <html>
            <head>
                <title>test2</title>
            </head>
            <body>
                <h1>保存成功</h1>
            </body>
        </html>
    
    """)


run()
