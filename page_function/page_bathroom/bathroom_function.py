import os
from time import sleep
import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy
from base_global.base_page import BasePage
from base_global.base_log import log


class Bathroom_Func(BasePage):

    # 新增按钮
    add_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_add")')
    # 浴室名称填写框
    shop_name_box = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_device_name")')
    # 选择店铺所在拦（用于点击显示店铺列表）定位
    shop_choice = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_store_name")')
    # 确定按钮
    confirm_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")')
    # 性别选择所在选项拦（用于点击显示性别列表）定位
    sexy_choice = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_sex")')
    # 提交按钮
    submit_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_submit")')
    # 新增浴室后的浴室名称（用于编辑浴室时定位使用）
    new_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试浴室1")')
    # 编辑按钮
    edit_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_edit")')
    # 浴室名称填写框（编辑界面）
    edit_name_box = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_device_name")')
    # 浴室所属店铺
    edit_shop_belong = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_store_name")')
    # 浴室预约功能按钮
    appointment_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/switch_device_type")')
    # 修改预约时长
    edit_appointment_time = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_time")')
    # 违约惩罚开关
    punishment_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/sc_weiyue_switch")')
    # 更改浴室营业状态
    edit_open_status = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_status")')
    # 搜索按钮
    search_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_search")')
    # 搜索输入框
    search_box = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_search_shop")')
    # 模糊搜索文案
    search_text = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试用浴室")')
    # 页面"返回"按钮
    back_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("返回")')
    # 编辑后浴室名称
    edit_after_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试用浴室1")')
    # 删除按钮
    delete_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("删除")')

    def into_add_bathroom_page(self):
        """点击右上角“新增”按钮进入新增浴室界面"""
        lp = BasePage(self.driver)
        log.info("点击'+'号进入新增浴室页面")
        lp.find(self.add_button).click()
        return self

    def into_bathroom_detail_page(self):
        """进入浴室详情页面"""
        lp = BasePage(self.driver)
        lp.find(self.new_name).click()
        # return self

    def add_bathroom_message_complete(self):
        """新增设备时的信息完善"""
        lp = BasePage(self.driver)
        sleep(1)
        log.info("新增浴室名称—测试浴室1")
        lp.find(self.shop_name_box).send_keys("测试浴室1")
        log.info("选择'测试用店铺'为所属店铺")
        lp.find(self.shop_choice).click()
        sleep(1)
        lp.find(self.confirm_button).click()
        sleep(1)
        log.info("选择浴室'适用性别'")
        lp.find(self.sexy_choice).click()
        lp.find(self.confirm_button).click()
        return self

    def submit_bathroom_message(self):
        lp = BasePage(self.driver)
        log.info("点击'提交'按钮新增浴室")
        lp.find(self.submit_button).click()
        return self

    def into_edit_page(self):
        lp = BasePage(self.driver)
        """进入编辑浴室页面"""
        sleep(1)
        log.info("点击'编辑'按钮信息编辑页面")
        lp.find(self.edit_button).click()
        return self

    def edit_bathroom_name(self):
        lp = BasePage(self.driver)
        """修改浴室名称"""
        log.info("删除原浴室名称")
        ele = lp.find(self.edit_name_box)
        ele_text = ele.get_attribute("text")
        ele.click()
        self.driver.keyevent(123)
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        log.info("修改浴室名称为'测试用浴室1'")
        ele.send_keys("测试用浴室1")
        return self

    def edit_bathroom_blong(self):
        lp = BasePage(self.driver)
        """更改浴室所属"""
        log.info("修改成'测试浴室店铺'为所属店铺")
        lp.find(self.edit_shop_belong).click()
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.85
                          )
        lp.find(self.confirm_button).click()
        return self

    def edit_bathroom_appointment_switch(self):
        lp = BasePage(self.driver)
        """打开/关闭店铺预约按钮"""
        lp.find(self.appointment_button).click()
        # return self

    def edit_appointment_appointment_time(self):
        lp = BasePage(self.driver)
        """修改预约时长"""
        ele_text = lp.find(self.edit_appointment_time).get_attribute("text")
        self.driver.keyevent(123)
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        lp.find(self.edit_appointment_time).send_keys("5")
        return self

    def edit_bathroom_sex(self):
        lp = BasePage(self.driver)
        """修改适用性别"""
        lp.find(self.sexy_choice).click()
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.8
                          )
        lp.find(self.confirm_button).click()
        # return self

    def edit_bathroom_punishment(self):
        lp = BasePage(self.driver)
        """打开/关闭违约惩罚开关"""
        lp.find(self.punishment_button).click()
        return self

    def edit_bathroom_open_time(self):
        pass

    def edit_bathroom_state(self):
        lp = BasePage(self.driver)
        """更改浴室营业状态"""
        lp.find(self.edit_open_status).click()
        log.info("修改成'浴室营业状态'为暂停营业")
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.8
                          )
        lp.find(self.confirm_button).click()
        return self

    def search_device_by_number(self):
        """根据输入浴室编号搜索设备"""
        lp = BasePage(self.driver)
        lp.find(self.search_button).click()
        # 此处为模糊查找
        lp.find(self.search_box).send_keys("测试用")
        lp.find(self.search_text).click()
        return self

    def delete_bathroom(self):
        """删除新增浴室(此步骤排在编辑步骤后需要先点击返回按钮进入浴室列表页面)"""
        lp = BasePage(self.driver)
        sleep(1)
        lp.find(self.delete_button).click()
        lp.find(self.confirm_button).click()
        sleep(1)
        return self



















