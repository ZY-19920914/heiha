from time import sleep

# import allure
from appium.webdriver.common.mobileby import MobileBy
from base_global.app import App
from base_global.base_page import BasePage
from base_global.base_log import log


# @allure.feature("烘干机管理模块")
class Test_dryer:
    # 价格修改后对应的中温烘干价格
    tv_time_price = (MobileBy.XPATH, '//*[@text="中温烘干"]/../..//*[@resource-id="com.qekj.merchant:id/tv_time"]')
    # 烘干机名称（基础信息下拉展示中）
    device_name = (MobileBy.XPATH, '//*[@text="设备名称"]/..//*[@resource-id="com.qekj.merchant:id/tv_value"]')
    # 烘干机所属店铺（基础信息下拉展示中）
    shop_belong = (MobileBy.XPATH, '//*[@text="所属店铺"]/..//*[@resource-id="com.qekj.merchant:id/tv_value"]')
    # 烘干机状态
    device_status = (MobileBy.XPATH, '//*[@text="企鹅烘干机"]/..//*[@resource-id="com.qekj.merchant:id/tv_device_status"]')

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    # @allure.story("新增烘干机")
    def test_add_dryer(self):
        bm = BasePage(self.app.driver)
        log.info("------'新增充电桩'测试用例执行------")
        self.main.\
            goto_all_management().\
            into_dryer_management().\
            into_add_dryer_page().\
            complete_message_add().\
            into_device_detail_information().\
            show_base_infomation()
        bm.assertest("企鹅烘干机", self.device_name)
        bm.assertest("测试浴室店铺1", self.shop_belong)

    # @allure.story("编辑烘干机")
    def test_edit_dryer(self):
        bm = BasePage(self.app.driver)
        log.info("------'编辑充电桩'测试用例执行------")
        self.app.\
            main_dryer_page().\
            show_base_infomation().\
            change_fun_paragram().\
            show_func_setting()
        bm.assertest("耗时1分钟  原价0.03元/分钟", self.tv_time_price)

    # @allure.story("启动烘干机")
    def test_start_dryer(self):
        bm = BasePage(self.app.driver)
        log.info("------'启动充电桩'测试用例执行------")
        self.app.\
            main_dryer_page().\
            show_func_setting().\
            start_dryer().\
            back_list()
        bm.assertest("运行", self.device_status)

    # @allure.story("复位烘干机")
    def test_reset_dryer(self):
        bm = BasePage(self.app.driver)
        log.info("------'复位充电桩'测试用例执行------")
        self.app.\
            main_dryer_page().\
            into_device_detail_information().\
            reset_dryer().\
            back_list()
        bm.assertest("空闲", self.device_status)
        self.app.driver.quit()

    # @allure.story("删除烘干机")
    def test_delete_dryer(self):
        bm = BasePage(self.app.driver)
        log.info("------'删除充电桩'测试用例执行------")
        self.app.\
            main_dryer_page().\
            into_device_detail_information().\
            delete_device()
        sleep(1)
        dryer_as = bm.is_exist_element("企鹅烘干机")
        sleep(1)
        assert not dryer_as
        self.app.driver.quit()
