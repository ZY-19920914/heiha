#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/06/28
# @Author  : zy

import os
import time
from time import sleep
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from xlrd import open_workbook
from selenium.webdriver.support import expected_conditions as ec
from appium import webdriver
from base_global.base_screenshot import Screenshots
from hamcrest import *


class BasePage(Screenshots):

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def  is_exist_element(self, ele_attr):
        '''
        判断元素是否存在
        ele_attr: 元素的属性值
        '''
        sleep(3)
        source = self.driver.page_source
        if ele_attr in source:
            return True
        else:
            return False

    def is_toast_exist(self, text, timeout=20, poll_frequency=0.1):
        '''
        判断toast是否存在，是则返回True，否则返回False
        :param driver: driver实例对象
        :param text: toast文本
        :param timeout: 定位超时时间
        :param poll_frequency: 查询频率
        :return: True or False
        '''
        try:
            toast_loc = (MobileBy.XPATH, ".//*[contains(@text, %s)]" % text)
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                ec.presence_of_element_located(toast_loc)
            )
            return True
        except:
            return False

    def get_toast_text(self, timeout=20, poll_frequency=0.1):
        '''
        定位toast元素，获取text属性
        '''
        toast_loc = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        try:
            toast = WebDriverWait(self.driver, timeout, poll_frequency).until(
                ec.presence_of_element_located(toast_loc)
            )
            toast_text = toast.get_attribute('text')
            return toast_text
        except Exception as e:
            return e

    def assertest(self, expect_value, locatorself):
        """
        :断言封装
        """
        ele_locator = self.find(locatorself)
        text_locator = ele_locator.get_attribute("name")
        return assert_that(expect_value, equal_to(text_locator))

    @property
    def width(self):
        """
        :获取屏幕宽度
        """
        return self.driver.get_window_size().get('width', 0)

    @property
    def height(self):
        """
        :获取屏幕高度
        """
        return self.driver.get_window_size().get('height', 0)

    def data_acquire(self):
        """
        :解析excel表格中的测试数据
        """
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        openExcelFile = open_workbook(path + "/base_global/config/data.xlsx")
        # 获取工作表
        getSheet = openExcelFile.sheet_by_name("Sheet1")
        # 获取行数
        rowNumber = getSheet.nrows
        # 数据List
        dataList = []
        # 从第二行开始遍历每一行
        for i in range(1, rowNumber):
            # 把每个单元格的数值存放到dataLis
            dataList.append(getSheet.row_values(i))
        return dataList

    def find(self, locator, timeout=20, value: str = None):
        lp = Screenshots()
        '''
        获取可视元素
        param loctor: By方法定位元素，如(By.XPATH, "//*[@text='照片']")
        return：返回可见元素
        '''
        try:
            return WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
        except Exception as e:
            # 截图、日志
            print("失败，原因是：{}".format(e))

            self.driver.get_screenshot_as_file(lp.screenshot_filepath())



