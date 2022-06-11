from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from page_function.page_bathroom.bathroom_function import Bathroom_Func
from page_function.page_bath_position.bath_position_function import Bath_position_Func
from base_global.base_page import BasePage
from page_function.page_charging_pile.charging_pile_function import Charging_pile_Func
from page_function.page_dryer.dryer_function import Dryer_Func
from page_function.page_global_receipt.global_receipt_function import Global_receipt_Func
from page_function.page_shop.shop_function import Shop_Func
from page_function.page_washingmanage.wash_function import Wash_Func
from base_global.base_log import log


class BaseroomManagement(BasePage):
    bathposition_management = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("浴位管理")')
    bathroom_management = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("浴室管理")')
    washing_management = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("洗衣机管理")')
    shop_management = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("店铺管理")')
    global_receipt_management = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("通用小票管理")')
    charging_pile_management = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("充电桩管理")')
    dryer_management = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("烘干机管理")')

    def into_bathposition_management(self):
        lp = BasePage(self.driver)
        """进入浴位管理"""
        log.info("点击'浴位管理'")
        lp.find(self.bathposition_management).click()
        return Bath_position_Func(self.driver)

    def into_bathroom_management(self):
        lp = BasePage(self.driver)
        """进入浴室管理"""
        log.info("点击'浴室管理'")
        lp.find(self.bathroom_management).click()
        return Bathroom_Func(self.driver)

    def into_washing_management(self):
        lp = BasePage(self.driver)
        """进入洗衣机管理"""
        log.info("点击'洗衣机管理'")
        lp.find(self.washing_management).click()
        return Wash_Func(self.driver)

    def into_shop_management(self):
        lp = BasePage(self.driver)
        """进入店铺管理"""
        log.info("点击'店铺管理'")
        lp.find(self.shop_management).click()
        return Shop_Func(self.driver)

    def into_global_receipt_management(self):
        lp = BasePage(self.driver)
        """进入通用小票管理"""
        log.info("点击'通用小票管理'")
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.1
                          )
        lp.find(self.global_receipt_management).click()
        return Global_receipt_Func(self.driver)

    def into_charging_pile_management(self):
        lp = BasePage(self.driver)
        """进入充电桩管理"""
        log.info("点击'充电桩管理'")
        lp.find(self.charging_pile_management).click()
        return Charging_pile_Func(self.driver)

    def into_dryer_management(self):
        """进入烘干机管理页面"""
        lp = BasePage(self.driver)
        log.info("点击'烘干机管理'")
        lp.find(self.dryer_management).click()
        return Dryer_Func(self.driver)





