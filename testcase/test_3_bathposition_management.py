import os
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from base_global.app import App
from base_global.base_page import BasePage
import requests
from hamcrest import *
from base_global.base_log import log


class Testdemo:
    bath_device_name = (MobileBy.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_device_name"]/..//*[@text="0001"]')
    belong_bathroom = (MobileBy.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_shop_name"]/..//*[@text="测试用浴室"]')
    # 基础信息——单脉冲流量
    monopulse_flow = (MobileBy.XPATH, '//*[@text="单脉冲流量(ml)"]/..//*[@resource-id="com.qekj.merchant:id/tv_maichang"]')
    # 基础信息——浴位单价
    unit_price = (MobileBy.XPATH, '//*[@text="单价(元/L)"]/..//*[@resource-id="com.qekj.merchant:id/tv_price"]')
    # 基础信息——设备名称
    device_name = (MobileBy.XPATH, '//*[@text="设备名称"]/..//*[@resource-id="com.qekj.merchant:id/tv_yw_no"]')

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_add_position(self):
        # bm = BasePage(self.app.driver)
        # log.info("------'新增浴位'测试用例执行------")
        # self.main.\
        #     goto_all_management(). \
        #     into_bathposition_management(). \
        #     into_add_button_page(). \
        #     add_bath_position_message_complete()
        # bm.assertest("0001", self.bath_device_name)
        # bm.assertest("测试用浴室", self.belong_bathroom)
        pass

    # def test_edit_position(self):
    #     bm = BasePage(self.app.driver)
    #     log.info("------'编辑浴位'测试用例执行------")
    #     self.app.\
    #         main_bath_position_page().\
    #         into_edit_page().\
    #         edit_device_price().\
    #         edit_device_flow().\
    #         edit_position_number().\
    #         base_information()
    #     bm.assertest("1000", self.monopulse_flow)
    #     bm.assertest("0.1", self.unit_price)
    #     bm.assertest("0101", self.device_name)
    #     pass


    def test_delete_position(self):
        # bm = BasePage(self.app.driver)
        # log.info("------'删除浴位'测试用例执行------")
        # self.app.main_bath_position_page().delete_device_after_edit()
        # ele_as = bm.is_exist_element("0101")
        # assert ele_as
        pass
        self.app.driver.quit()



