import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from base_global.base_page import BasePage
from base_global.main import Main
from time import sleep
from page_function.page_bath_position.bath_position_function import Bath_position_Func
from page_function.page_bathroom.bathroom_function import Bathroom_Func
from page_function.page_charging_pile.charging_pile_function import Charging_pile_Func
from page_function.page_dryer.dryer_function import Dryer_Func
from page_function.page_global_receipt.global_receipt_function import Global_receipt_Func
from page_function.page_shop.shop_function import Shop_Func
from page_function.page_washingmanage.wash_function import Wash_Func
from base_global.base_log import log


class App(BasePage):
    # 启动欢迎页"同意"按钮
    agree_loc = 'com.qekj.merchant:id/tv_know'
    agree_loc_va = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_know")')
    # "立即进入"按钮
    open_loc = 'com.qekj.merchant:id/btn_open'
    open_loc_va = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/btn_open")')
    # 首页更新弹窗中"同意更新"按钮
    update_alter = 'com.qekj.merchant:id/ll_update'
    update_alter_va = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/ll_update")')
    # app首页更新弹窗的取消按钮
    update_cancel = 'com.qekj.merchant:id/iv_cancel'
    update_cancel_va = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_cancel")')
    # 清空登录账号框按钮
    clear_count_button = 'com.qekj.merchant:id/iv_clear_account'
    clear_count_button_va = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_clear_account")')
    # 清空登录密码框按钮
    clear_psw_button = 'com.qekj.merchant:id/iv_clear_password'
    # 登录页面账号输入框
    account_input = 'com.qekj.merchant:id/et_account'
    account_input_va = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_account")')
    # 登录页面密码输入框
    password_input = 'com.qekj.merchant:id/et_password'
    password_input_va = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_password")')
    # 登录页面"同意"按钮
    agree_button = 'com.qekj.merchant:id/iv_select'
    agree_button_va = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_select")')
    # 登录页面"登录"按钮
    login_button = 'com.qekj.merchant:id/rl_login'
    login_button_va = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_login")')
    # 未清除缓存时输入原号码选中框
    cache_phone = (MobileBy.XPATH, "//*[@resource-id='com.qekj.merchant:id/rv_phone']/android.widget.RelativeLayout")
    # 首页"收益统计"元素
    shouyi = "com.qekj.merchant:id/tv_today_revenue_final"

    def start(self):
        #if self.driver == None:
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        # desired_caps['deviceName'] = 'UQG5T20629006835'
        # desired_caps['deviceName'] = 'emulator-5554'
        # desired_caps['deviceName'] = '551ed6e4'
        # desired_caps['deviceName'] = 'ibw865ina6y5fyfy'
        #desired_caps['deviceName'] = 'FJH5T18728058867'
        desired_caps['deviceName'] = 'ad533d9d'
        desired_caps['appPackage'] = 'com.qekj.merchant'
        desired_caps['appActivity'] = 'com.qekj.merchant.ui.activity.SplashActivity'
        #desired_caps['platformVersion'] = '9'
        desired_caps['platformVersion'] = '10'
        # desired_caps['platformVersion'] = '6'
        desired_caps['skipDeviceInitializatio'] = 'true'
        desired_caps['uicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['noReset'] = 'true'
        # desired_caps['newCommandTimeout'] = '3600'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # else:
        #     self.driver.launch_app()
        self.driver.implicitly_wait(15)
        return self

    def stop(self):
        pass

    def restart(self):
        pass
        return self

    def main(self):
        lp = BasePage(self.driver)
        """
        1、先判断是否在首页（是否包含收益元素）
        2、是否在首页且被"更新"弹窗覆盖
        3、是否app刚下载打开状态
        4、是否在登录页面
        """
        if lp.is_exist_element(self.shouyi):
            pass
        elif lp.is_exist_element(self.update_cancel) is True:
            log.info("取消设备服务费弹窗/取消更新")
            lp.find(self.update_cancel_va).click()
            if lp.is_exist_element(self.update_cancel) is True:
                log.info("取消更新")
                lp.find(self.update_cancel_va).click()
            else:
                pass
        elif lp.is_exist_element(self.update_alter) is True:
            log.info("更新版本")
            lp.find(self.update_alter_va).click()
        elif lp.is_exist_element(self.agree_loc):
            log.info("执行首次下载app登录操作")
            log.info("点击'同意'按钮")
            lp.find(self.agree_loc_va).click()
            sleep(1)
            log.info("左滑3次banner")
            for i in range(2):
                self.driver.swipe(self.width*0.9,
                                  self.height*0.5,
                                  self.width*0.1,
                                  self.height*0.5
                                  )
            sleep(1)
            log.info("点击启动页'立即进入'按钮")
            lp.find(self.open_loc_va).click()
            # 执行首次登录操作
            log.info("输入电话号码")
            lp.find(self.account_input_va).send_keys("18814810220")
            sleep(1)
            log.info("输入密码")
            lp.find(self.password_input_va).send_keys("888666")
            log.info("点击'我已阅读'")
            lp.find(self.agree_button_va).click()
            log.info("点击登录")
            lp.find(self.login_button_va).click()

            if lp.is_exist_element(self.update_cancel):
                log.info("取消更新")
                lp.find(self.update_cancel_va).click()
            elif lp.is_exist_element(self.update_alter):
                log.info("更新版本")
                lp.find(self.update_alter_va).click()
            else:
                pass
            # sleep(5)

        elif lp.is_exist_element(self.login_button) is True:
            if lp.is_exist_element(self.clear_count_button) is True:
                log.info("执行缓存登录")
                log.info("点击清除账号按钮")
                # 缓存登录
                lp.find(self.clear_count_button_va).click()
                log.info("输入电话号码")
                lp.find(self.account_input_va).send_keys("18814810220")
                sleep(1)
                log.info("选择缓存电话号码")
                lp.find(self.cache_phone).click()
                log.info("输入密码")
                lp.find(self.password_input_va).send_keys("888666")
                log.info("点击'登录'按钮")
                lp.find(self.login_button_va).click()

                if lp.is_exist_element(self.update_cancel):
                    log.info("取消更新")
                    lp.find(self.update_cancel_va).click()
                elif lp.is_exist_element(self.update_alter):
                    log.info("更新版本")
                    lp.find(self.update_alter_va).click()
                else:
                    pass
            else:
                log.info("执行非缓存登录")
                log.info("输入电话号码")
                lp.find(self.account_input_va).send_keys("18814810220")
                sleep(1)
                # lp.find(self.cache_phone).click()
                log.info("输入密码")
                lp.find(self.password_input_va).send_keys("888666")
                log.info("点击'登录'按钮")
                lp.find(self.login_button_va).click()

                if lp.is_exist_element(self.update_cancel):
                    log.info("取消更新")
                    lp.find(self.update_cancel_va).click()
                elif lp.is_exist_element(self.update_alter):
                    log.info("取消更新")
                    lp.find(self.update_alter_va).click()
                else:
                    pass
        else:
            pass

        return Main(self.driver)

    def home_page(self):
        pass
        return Main(self.driver)

    # def home_page_with_update(self):
    #     lp = BasePage(self.driver)
    #     if lp.is_exist_element(self.update_cancel):
    #         lp.find(self.update_cancel_va).click()
    #     elif lp.is_exist_element(self.update_alter):
    #         lp.find(self.update_alter_va).click()
    #     else:
    #         pass
    #     return Main(self.driver)

    def main_bathroom_page(self):
        pass
        return Bathroom_Func(self.driver)

    def main_shop_page(self):
        pass
        return Shop_Func(self.driver)

    def main_bath_position_page(self):
        pass
        return Bath_position_Func(self.driver)

    def main_wash_page(self):
        pass
        return Wash_Func(self.driver)

    def main_charging_pile_page(self):
        pass
        return Charging_pile_Func(self.driver)

    def main_login(self):
        pass
        return self

    def main_global_receipt_page(self):
        pass
        return Global_receipt_Func(self.driver)

    def main_dryer_page(self):
        pass
        return Dryer_Func(self.driver)
