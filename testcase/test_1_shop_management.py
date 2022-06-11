import os
from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy
from base_global.app import App
from base_global.base_page import BasePage
from page_function.page_bathroom.bathroom_function import Bathroom_Func
from base_global.base_log import log
from hamcrest import *


@allure.feature("店铺管理模块")
class Test_Shop:
    shop_name = (MobileBy.XPATH, '//*[@text="店铺名称"]/..//*[@resource-id="com.qekj.merchant:id/tv_shop_name"]')
    shop_type = (MobileBy.XPATH, '//*[@text="店铺类型"]/..//*[@resource-id="com.qekj.merchant:id/tv_shop_type_name"]')
    shop_address = (MobileBy.XPATH, '//*[@text="店铺地址"]/..//*[@resource-id="com.qekj.merchant:id/tv_address"]')
    shop_pay_way = (MobileBy.XPATH, '//*[@text="强制免密支付"]/..//*[@resource-id="com.qekj.merchant:id/tv_mianmi"]')

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()
        # self.main = self.app.start().main()

    @allure.story("新增店铺")
    def test_add_position(self):
        bm = BasePage(self.app.driver)
        log.info("------'新增店铺'测试用例执行------")
        self.main. \
            goto_all_management(). \
            into_shop_management().\
            add_button_click(). \
            complete_shop_name(). \
            complete_shop_type(). \
            choose_shop_area(). \
            choose_shop_address(). \
            choose_shop_open_hours(). \
            fillout_phone_number(). \
            submit_information().\
            into_shop3_detail()
        bm.assertest("测试店铺3", self.shop_name)
        bm.assertest("浙江省杭州市西湖区联合大厦A座1005室", self.shop_address)
        bm.assertest("开启", self.shop_pay_way)

    @allure.story("编辑店铺")
    def test_edit_position(self):
        bm = BasePage(self.app.driver)
        log.info("------'编辑店铺'测试用例执行------")
        self.app.main_shop_page().\
            into_edit_page().\
            edit_shop_name().\
            edit_shop_type().\
            edit_shop_open_time().\
            edit_shop_phone().\
            edit_shop_pay_way().\
            submit_information().\
            into_shop4_detail()
        bm.assertest("测试店铺4", self.shop_name)
        bm.assertest("学校", self.shop_type)
        bm.assertest("开启", self.shop_pay_way)

    @allure.story("删除店铺")
    def test_delete_position(self):
        bm = BasePage(self.app.driver)
        log.info("------'删除店铺'测试用例执行------")
        self.app.main_shop_page().delete_shop()
        shop_delete_as = bm.is_exist_element("测试店铺4")
        assert not shop_delete_as
        self.app.driver.quit()
