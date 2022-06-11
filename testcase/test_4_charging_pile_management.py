from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy
from base_global.app import App
from base_global.base_page import BasePage
from base_global.base_log import log


@allure.feature("充电桩管理")
class Test_charging_pile:
    device_name = (MobileBy.XPATH, '//*[@text="设备名称"]/..//*[@resource-id="com.qekj.merchant:id/tv_yw_no"]')
    shop_belong = (MobileBy.XPATH, '//*[@text="所属店铺"]/..//*[@resource-id="com.qekj.merchant:id/tv_shop"]')

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    @allure.story("新增充电桩")
    def test_add_charging_pile(self):
        bm = BasePage(self.app.driver)
        log.info("------'新增充电桩'测试用例执行------")
        self.main.\
            goto_all_management(). \
            into_charging_pile_management(). \
            into_add_charging_pile_page(). \
            add_charging_message_complete().\
            submit().\
            into_detail_charging_pile_page().\
            click_base_information()
        bm.assertest("测试充电桩", self.device_name)
        bm.assertest("测试洗衣店铺", self.shop_belong)

    @allure.story("编辑充电桩")
    def test_edit_charging_pile(self):
        bm = BasePage(self.app.driver)
        log.info("------'编辑充电桩'测试用例执行------")
        self.app. \
            main_charging_pile_page().\
            click_base_information().\
            edit_change_nqt().\
            edit_change_imei().\
            edit_price().\
            edit_change_charging_port().\
            edit_charging_pile_name().\
            edit_charging_pile_belong().\
            click_base_information()
        sleep(1)
        bm.assertest("测试充电桩1", self.device_name)
        bm.assertest("测试充电桩店铺", self.shop_belong)

    @allure.story("删除充电桩")
    def test_delete_device(self):
        bm = BasePage(self.app.driver)
        log.info("------'删除充电桩'测试用例执行------")
        self.app.\
            main_charging_pile_page().\
            delete_device()
        ele_as = bm.is_exist_element("测试充电桩1")
        assert not ele_as
        self.app.driver.quit()
