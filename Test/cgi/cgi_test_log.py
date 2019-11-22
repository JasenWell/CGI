#!D:\Service\Python\python3\python.exe
# coding=utf-8
"""

cgitb 脚本异常管理
用途：如发生未捕获异常，将展示格式化输出报告。包括源代码每一层回溯，及当前执行程序参数和局部变量。
import cgitb
函数：
cgitb.encable(display=1, logdir=None, context=5, format="html")
用途：报告显示在浏览器或文件；加到你的浏览器头部
参数：display：1发送至浏览器；0不发送 
logdir：如果有的话，写到该目录下
context： 显示错误代码周围的代码行数
format： 显示HTML，除'html'之外所有值都会显示为纯文本‘text’
cgitb.text（info，context = 5 ）
用途：处理info描述的异常将其回溯格式化为文本并将结果作为字符串返回。
参数：上下文是在回溯中围绕当前源代码行显示的上下文行数;默认5
 
cgitb.html（info，context = 5 ）
用途：处理info描述的异常（包含结果3元组sys.exc_info()），将其回溯格式化为HTML并将结果作为字符串返回
cgitb.handle(info=None)
用途：用cgitb处理异常（在浏览器中显示报告，不记录到文件）
参数：info 是含有异常类型、异常值和traceback三元组；如无则从sys.exc_info中获取
————————————————
版权声明：本文为CSDN博主「tcy23456」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/tcy23456/article/details/94355037

"""

import cgitb, sys, traceback


def func(a, b):
    return a / b


def my_exception_handler(exc_type, exc_value, exc_tb):
    print("1.1.Err type=", exc_type)
    print("1.2.Err value=", exc_value)
    while exc_tb:
        print("2.Line No:", exc_tb.tb_lineno)
        print("3.Frame locals:", exc_tb.tb_frame.f_locals)
        exc_tb = exc_tb.tb_next


cgitb.enable(format='text')

sys.excepthook = my_exception_handler


def test(Mode=0):
    if Mode == 0:
        func(1, 0)
    elif Mode == 1:
        try:
            func(1, 0)
        except:
            info = sys.exc_info()
            print('4.info=', cgitb.text(info))
    elif Mode == 2:
        cgitb.handler()
        func(1, 0)
    elif Mode == 3:
        cgitb.enable(display=0, logdir='./cgi_log', context=5, format='text')
        cgitb.handler()
        func(1, 0)


if __name__ == '__main__':
    test(3)
