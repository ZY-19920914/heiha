from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from base_global.app import App
from base_global.base_page import BasePage
import allure
from base_global.base_log import log


@allure.feature("通用小票管理")
class Test_global_receipt:
    # 开通小票店铺名
    global_shop_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_shop_name")')
    # 强制通用小票开关状态值
    cc_value = (MobileBy.XPATH, '//*[@text="强制通用小票消费:"]/..//*[@resource-id="com.qekj.merchant:id/tvValue"]')
    # 允许退款开关对应的值
    refund_value = (MobileBy.XPATH, '//*[@text="允许退款:"]/..//*[@resource-id="com.qekj.merchant:id/tvValue"]')

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    @allure.story("新增通用小票")
    def test_add_global_receipt(self):
        bm = BasePage(self.app.driver)
        log.info("------'新增通用小票'测试用例执行------")
        self.main.\
            goto_all_management(). \
            into_global_receipt_management(). \
            into_add_global_receipt_page(). \
            add_globao_receipt_message_complete().\
            global_receipt_submit()
        bm.assertest("测试洗衣店铺", self.global_shop_name)

    @allure.story("编辑通用小票")
    def test_edit_global_receipt(self):
        bm = BasePage(self.app.driver)
        log.info("------'编辑通用小票'测试用例执行------")
        self.app.main_global_receipt_page().\
            into_edit_global_receipt_page().\
            edit_global_receipt_compel_use().\
            edit_global_receipt_compel_refund(). \
            edit_global_receipt_price().\
            global_receipt_submit()
        bm.assertest("开启", self.cc_value)
        bm.assertest("开启", self.refund_value)
        self.app.driver.quit()

    # @allure.story("充值通用小票")
    # def test_top_up_global_receipt(self):
        

    # @allure.story("删除通用小票")
    # def test_delete_global_receipt(self):
    #     bm = BasePage(self.app.driver)
    #     self.app.\
    #         main_global_receipt_page().\
    #         delete_global_receipt()
    #     ele_as = bm.is_exist_element("测试洗衣店铺")
    #     sleep(5)
    #     assert not ele_as
    #     self.app.driver.quit()
