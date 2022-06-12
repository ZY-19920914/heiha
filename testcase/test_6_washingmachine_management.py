from time import sleep

# import allure
from appium.webdriver.common.mobileby import MobileBy
from base_global.app import App
from base_global.base_page import BasePage
from hamcrest import *
from base_global.base_log import log


# @allure.feature("洗衣机管理")
class Test_washing:
    # 设备"空闲"状态定位
    status_free_device = (MobileBy.XPATH, '//*[@resource-id="com.qekj.merchant:id/v_circle"]/../../..//*[@text="空闲"]')
    # 设备"运行"状态定位
    status_run_device = (MobileBy.XPATH, '//*[@resource-id="com.qekj.merchant:id/v_circle"]/../../..//*[@text="运行"]')
    # 列表-洗衣机设备名称
    device_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_device_name")')
    # 列表-洗衣机所属店铺
    device_shop_belong = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_shop_name")')
    # 功能详情-功能名称
    func_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_name")')
    # 功能详情-功能价格
    func_price = (MobileBy.XPATH, '//*[@text="单脱水"]/../..//*[@resource-id="com.qekj.merchant:id/tv_time"]')

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    # @allure.story("新增洗衣机")
    def test_add_device(self):
        """
        测试添加洗衣机设备
        步骤1：判断是否在app首页
        步骤2：进入洗衣机管理
        步骤3：点击"新增设备"按钮，选择"新增设备"
        步骤4：完善新增洗衣机设备信息
        步骤5：点击"提交"按钮
        """
        bm = BasePage(self.app.driver)
        log.info("------'新增洗衣机设备'测试用例执行------")
        self.main.\
            goto_all_management(). \
            into_washing_management(). \
            into_add_device_page(). \
            add_wash_message_complete(). \
            submit_add_after()
        bm.assertest("测试洗衣机1", self.device_name)
        bm.assertest("测试洗衣店铺", self.device_shop_belong)

    # @allure.story("编辑洗衣机")
    def test_edit_device(self):
        """
        测试编辑洗衣机设备信息
        步骤1：点击设备名进入编辑页面
        步骤2：更换NQT
        步骤3：更换IMEI
        步骤4：修改功能参数（包括修改单脱水功能名称、价格）
        步骤5：点击"提交"按钮
        """
        bm = BasePage(self.app.driver)
        log.info("------'编辑洗衣机设备'测试用例执行------")
        self.app.\
            main_wash_page().\
            into_edit_page().\
            into_edit_func_parameter_page().\
            edit_only_dry_name().\
            edit_only_dry_price().\
            submit_edit_after().\
            base_information()
        bm.assertest("耗时10分钟  价格0.02元", self.func_price)

    # @allure.story("启动洗衣机")
    def test_start_device(self):
        """
        测试启动洗衣机
        步骤1：进入设备详情页
        步骤2：点击"启动"按钮
        步骤3：选择具体的功能点击"启动"
        步骤4：返回check设备状态是否已运行
        """
        bm = BasePage(self.app.driver)
        log.info("------'启动洗衣机设备'测试用例执行------")
        self.app.\
            main_wash_page().\
            base_information().\
            start_device()
        sleep(3)
        bm.assertest("运行", self.status_run_device)

    # @allure.story("复位洗衣机")
    def test_reset_device(self):
        """
        复位运行中的洗衣机
        步骤1：进入设备详情页
        步骤2：点击"复位"按钮
        步骤3：返回设备列表页判断设备状态是否恢复"空闲"
        """
        bm = BasePage(self.app.driver)
        log.info("------'复位洗衣机设备'测试用例执行------")
        self.app. \
            main_wash_page(). \
            into_edit_page(). \
            rest_device()
        bm.assertest("空闲", self.status_free_device)

    # @allure.story("删除洗衣机")
    def test_delete_devide(self):
        bm = BasePage(self.app.driver)
        log.info("------'删除洗衣机设备'测试用例执行------")
        self.app.\
            main_wash_page().\
            into_edit_page().\
            delete_device()
        sleep(1)
        washing_as = bm.is_exist_element("测试洗衣机1")
        sleep(1)
        assert not washing_as
        self.app.driver.quit()


