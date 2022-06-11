from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from base_global.base_page import BasePage
from base_global.base_log import log


class Global_receipt_Func(BasePage):
    role_setting = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("规则配置")')
    iv_search = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_search")')
    # shop_detail = (MobileBy.XPATH, '//*[@text="测试洗衣店铺"]/../..//*[@resource-id="com.qekj.merchant:id/llDetail"]')
    shop_detail = (MobileBy.XPATH, '//*[@text="测试洗衣店铺"]/../..//*[@text="详情"]')
    edit_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("编辑")')
    tv_shop_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_shop_name")')
    shop_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试洗衣店铺")')
    confirm_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")')
    delete_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("删除")')
    ll_submit = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/ll_submit")')
    tv_force = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_force")')
    tv_allow = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/ll_allow")')
    # et_chongzhi = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_chongzhi")')
    et_chongzhi = (MobileBy.XPATH, '//*[@resource-id="com.qekj.merchant:id/et_chongzhi" and @text="6"]')

    def into_add_global_receipt_page(self):
        """进入新增通用小票编辑界面"""
        lp = BasePage(self.driver)
        log.info("点击店铺通用小票规则配置")
        lp.find(self.role_setting).click()
        lp.find(self.iv_search).click()
        return self

    def into_edit_global_receipt_page(self):
        """进入编辑对应店铺通用小票页面"""
        lp = BasePage(self.driver)
        log.info("进入通用小票编辑页面")
        lp.find(self.shop_detail).click()
        sleep(1)
        lp.find(self.edit_button).click()
        return self

    def add_globao_receipt_message_complete(self):
        """通用小票新增详情完善"""
        lp = BasePage(self.driver)
        log.info("新增通用小票信息完善")
        lp.find(self.tv_shop_name).click()
        lp.find(self.shop_name).click()
        lp.find(self.confirm_button).click()
        return self

    def global_receipt_submit(self):
        """新增通用小票提交按钮"""
        lp = BasePage(self.driver)
        log.info("新增/修改通用小票后的提交按钮")
        lp.find(self.ll_submit).click()
        return self

    def edit_global_receipt_compel_use(self):
        """打开/关闭通用小票强制使用开关"""
        lp = BasePage(self.driver)
        log.info("打开/关闭通用小票强制使用开关")
        lp.find(self.tv_force).click()
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.7
                          )
        lp.find(self.confirm_button).click()
        return self

    def edit_global_receipt_compel_refund(self):
        """打开/关闭通用小票允许退款开关"""
        lp = BasePage(self.driver)
        log.info("打开/关闭通用小票允许退款开关")
        lp.find(self.tv_allow).click()
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.7
                          )
        lp.find(self.confirm_button).click()
        return self

    def edit_global_receipt_price(self):
        """编辑更改通用小票方案"""
        lp = BasePage(self.driver)
        # 此坐标只适用于redmi note7手机，其他机型需要重新适配
        # self.driver.tap([(999, 1538), (1045, 1584)])
        # self.driver.tap([(999, 1409), (1045, 1455)])
        # self.driver.tap([(999, 1280), (1045, 1326)])
        # self.driver.tap([(999, 1151), (1045, 1197)])
        # self.driver.tap([(999, 1022), (1045, 1068)])
        ele = lp.find(self.et_chongzhi)
        ele_text = ele.get_attribute("text")
        ele.click()
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("6")
        return self

    def delete_global_receipt(self):
        """删除通用小票"""
        lp = BasePage(self.driver)
        log.info("删除通用小票")
        lp.find(self.delete_button).click()
        lp.find(self.confirm_button).click()
        return self



