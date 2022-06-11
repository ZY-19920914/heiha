import os
from time import sleep
import pytest
from base_global.base_log import log
import threading


def system_out():
    """
    ：打印logcat
    """
    os.system("adb logcat *:E >/Users/zhanzhoumin/Downloads/logcat.txt")


def run_test():
    """
    ：执行testcase
    """
    # mac中要让appiumserver在后台启动运行的话需要在命令前面加nohub和在末尾加"&"
    os.system("nohup appium -a 127.0.0.1 -p 4723 &")
    sleep(1)
    log.info("========初始化测试环境========")
    pytest.main(["-v", "testcase/"])
    log.info("========测试完成========")


def start_thread():
    """
    ：thread1:定义打印logcat线程
    ：thread2:定义执行testcase线程
    ：start方法设置thread1和thread2两个线程同时执行
    """
    thread1 = threading.Thread(target=system_out, name="logcat_out")
    thread2 = threading.Thread(target=run_test, name="run_testcase")
    thread2.start()
    thread1.start()


if __name__ == '__main__':
    start_thread()
