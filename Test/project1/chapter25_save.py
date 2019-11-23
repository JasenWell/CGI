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
    #print('Content-type: text/html\n')
    #重定向未解决
    print("Location:、 http://127.0.0.1:9092/Python-chapter25/cgi-bin/redirect_save.py?from=http://127.0.0.1:9092"
          "/Python-chapter25/cgi-bin/chapter25_save.py\n")
    BASE_DIR = abspath('data')
    timeFormat = '%Y-%m-%d %H:%M:%S'
    form = cgi.FieldStorage()
    filename = form.getvalue('filename')
    username = form.getvalue('username')
    text = form.getvalue('text')
    lasttext = form.getvalue('lasttext')
    password = form.getvalue('password')
    if not (filename and text and password):
        print('Invalid paramters')
        sys.exit()
    if sha1(password.encode()).hexdigest() != '7c4a8d09ca3762af61e59520943dc26494f8941b':
        print('Invalid password')
        sys.exit()

    f = open(join(BASE_DIR, filename), 'w')
    f.write(text)
    f.close()

    if text == lasttext:
        logging.info(time.strftime(timeFormat, time.localtime()) + " ==> same file,don't save history")
    elif lasttext:  # 首次非空判断
        HISTORY_DIR = abspath('history')
        if not os.path.isdir(HISTORY_DIR):
            os.makedirs(HISTORY_DIR, True)
            logging.info(time.strftime(timeFormat, time.localtime()) + ' ==> makedirs: ' + HISTORY_DIR)
        lastFileName = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime())
        with open(join(HISTORY_DIR, lastFileName + '.txt'), 'w') as f:
            f.write(lasttext)
            logging.info(time.strftime(timeFormat, time.localtime()) + " ==> save history")
    print('The file has been saved.')
    #重定向Location:、空格和url
    if 0:
        print("""Location:、 http://127.0.0.1:9092/Python-chapter25/cgi-bin/redirect_save.py
        
            <html>
                <head>
                    <title>test</title>
                </head>
                <body>
                
                </body>
            </html>
        
        """)


run()
