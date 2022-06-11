from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from base_global.base_page import BasePage


class Login(BasePage):
    # 清空登录账号框按钮
    clear_count_button = 'com.qekj.merchant:id/iv_clear_account'
    clear_count_button_va = 'new UiSelector().resourceId("com.qekj.merchant:id/iv_clear_account")'
    # 清空登录密码框按钮
    clear_psw_button = 'com.qekj.merchant:id/iv_clear_password'
    # 登录页面账号输入框
    account_input = 'com.qekj.merchant:id/et_account'
    account_input_va = 'new UiSelector().resourceId("com.qekj.merchant:id/et_account")'
    # 登录页面密码输入框
    password_input = 'com.qekj.merchant:id/et_password'
    password_input_va = 'new UiSelector().resourceId("com.qekj.merchant:id/et_password")'
    # 登录页面"同意"按钮
    agree_button = 'com.qekj.merchant:id/iv_select'
    agree_button_va = 'new UiSelector().resourceId("com.qekj.merchant:id/iv_select")'
    # 登录页面"登录"按钮
    login_button = 'com.qekj.merchant:id/rl_login'
    login_button_va = 'new UiSelector().resourceId("com.qekj.merchant:id/rl_login")'
    # 未清除缓存时输入原号码选中框
    cache_phone = "//*[@resource-id='com.qekj.merchant:id/rv_phone']/android.widget.RelativeLayout"

    def into_login_page(self):
        """进入登录页面"""
        lp = BasePage(self.driver)
        try:
            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().text("我的")').click()
            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId("com.qekj.merchant:id/iv_add")').click()
        except Exception as e:
            print("'进入退出登录页面'失败，原因是：{}".format(e))
            self.driver.get_screenshot_as_file(lp.screenshot_filepath())
        return self

    def quit_login(self):
        """退出登录"""
        lp = BasePage(self.driver)
        try:
            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().text("退出登录")').click()
        except Exception as e:
            print("'退出登录'失败，原因是：{}".format(e))
            self.driver.get_screenshot_as_file(lp.screenshot_filepath())
        return self

    def login_correct(self):
        """正确账号密码登录"""
        lp = BasePage(self.driver)
        try:
            self.driver.find_element_by_android_uiautomator(self.account_input_va).send_keys("18814810220")
            sleep(1)
            self.driver.find_element(MobileBy.XPATH, self.cache_phone).click()
            self.driver.find_element_by_android_uiautomator(self.password_input_va).send_keys("888666")
            self.driver.find_element_by_android_uiautomator(self.login_button_va).click()
        except Exception as e:
            print("'正常账号登录'失败，原因是：{}".format(e))
            self.driver.get_screenshot_as_file(lp.screenshot_filepath())
        return self

    def login_wrong(self):
        """错误账号密码登录"""
        lp = BasePage(self.driver)
        try:
            self.driver.find_element_by_android_uiautomator(self.account_input_va).send_keys("18814810220")
            sleep(1)
            self.driver.find_element(MobileBy.XPATH, self.cache_phone).click()
            self.driver.find_element_by_android_uiautomator(self.password_input_va).send_keys("88866")
            self.driver.find_element_by_android_uiautomator(self.login_button_va).click()
        except Exception as e:
            print("'错误账号密码登录'失败，原因是：{}".format(e))
            self.driver.get_screenshot_as_file(lp.screenshot_filepath())
        return self
