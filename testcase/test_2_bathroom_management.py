import os
from time import sleep
# import allure
from appium.webdriver.common.mobileby import MobileBy
from base_global.app import App
from base_global.base_page import BasePage
from page_function.page_bathroom.bathroom_function import Bathroom_Func
from hamcrest import *
from base_global.base_log import log


# @allure.feature("浴室管理模块")
class Test_add_bathroom:
    bathroom_name = (MobileBy.XPATH, '//*[@text="浴室名称"]/..//*[@resource-id="com.qekj.merchant:id/tv_device_name"]')
    bathroom_belong = (MobileBy.XPATH, '//*[@text="所属店铺"]/..//*[@resource-id="com.qekj.merchant:id/tv_belong_store"]')

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    # @allure.story("新增浴室")
    def test_add_bathroom(self):
        """新增浴室"""
        bm = Bathroom_Func(self.app.driver)
        log.info("------'新增浴室'测试用例执行------")
        self.main.\
            goto_all_management().\
            into_bathroom_management().\
            into_add_bathroom_page().\
            add_bathroom_message_complete().\
            submit_bathroom_message().\
            into_bathroom_detail_page()
        bm.assertest("测试浴室1", self.bathroom_name)
        bm.assertest("测试浴室店铺1", self.bathroom_belong)

    # @allure.story("编辑新增浴室")
    def test_edit_bathroom(self):
        """编辑浴室"""
        bm = Bathroom_Func(self.app.driver)
        log.info("------'编辑浴室'测试用例执行------")
        self.app.\
            main_bathroom_page().\
            into_edit_page().\
            edit_bathroom_name().\
            edit_bathroom_blong().\
            edit_bathroom_state().\
            submit_bathroom_message()
        bm.assertest("测试用浴室1", self.bathroom_name)
        bm.assertest("测试浴室店铺", self.bathroom_belong)

    # @allure.story("删除浴室")
    def test_delete_bathroom(self):
        """删除浴室"""
        bm = BasePage(self.app.driver)
        log.info("------'删除浴室'测试用例执行------")
        self.app.\
            main_bathroom_page().\
            delete_bathroom()
        sleep(1)
        shop_as = bm.is_exist_element("测试用浴室1")
        sleep(1)
        assert not shop_as
        self.app.driver.quit()




