import os
from time import sleep
import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy
from xlrd import open_workbook
from base_global.base_page import BasePage
from base_global.base_log import log



class Dryer_Func(BasePage):
    # 新增按钮
    add_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_add")')
    # 选择"新增设备"
    add_device = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新增设备")')
    # 设备类型名称
    dryer_type = (MobileBy.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_name" and @text="LG13KG-RV1329A7S(企鹅模块专用)"]')
    # "同意"按钮
    iv_select = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_select")')
    # 下一步按钮/提交按钮
    tv_next = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_next")')
    # 新增烘干机设备名称输入框
    et_device_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_device_name")')
    # 所属店铺框
    tv_shop = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_shop")')
    # 新增-NQT
    tv_nqt = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_nqt")')
    # "相册"按钮（进入相册选择二维码）
    tv_photo = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_photo")')
    # 在相册中选中照片后右下方出现的"确定1"按钮
    confirm1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定(1)")')
    # 新增-IMEI
    tv_device_sn = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_device_sn")')
    # 烘干模式-新增
    ll_cd_model = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/ll_cd_model")')
    # 功能设置
    ll_function = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/ll_function")')
    # 新增烘干机设备名称
    # device_name_after_add = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("企鹅烘干机")')
    device_name_after_add = (MobileBy.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_device_name" and @text="企鹅烘干机"]')
    # 详情-启动按钮
    start_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("启动")')
    # 中温烘干
    middle_dry = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("中温烘干")')
    # 详情-复位按钮
    reset_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("复位")')
    # 具体启动功能模式(中温烘干)
    func_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("中温烘干")')
    # 功能模式页面启动按钮
    func_start_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tvStart")')
    # 确定按钮
    confirm_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")')
    # 确认按钮
    confirm_button1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确认")')
    # 返回按钮
    tv_back = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_back")')
    # 更换NQT选择框
    NQT_change = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更换NQT")')
    # 更换IMEI选择框
    IMEI_change = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更换IMEI")')
    # 修改功能参数选择框
    func_paragram_change = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("修改功能参数")')
    # 中温烘干-修改原价
    tv_edit_price = (MobileBy.XPATH, '//*[@text="中温烘干"]/../../..//*[@resource-id="com.qekj.merchant:id/tv_edit_price"]')
    # 修改单位时间内价格
    tvPrice = (MobileBy.XPATH, '//*[@text="价格(元/分钟)"]/..//*[@resource-id="com.qekj.merchant:id/tv_price"]')
    # 修改-价格输入框
    et_input = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_input")')
    # 价格修改后对应的中温烘干价格
    tv_time_price = (MobileBy.XPATH, '//*[@text="中温烘干"]/../../..//*[@resource-id="com.qekj.merchant:id/tv_time"]')
    # 基础信息-详情页
    base_info = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rlBasic")')
    # 烘干模式-详情页
    rlHgMode = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rlHgMode")')
    # 功能设置下拉箭头-详情页
    iv_set = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_set")')
    # 设备转移
    device_belong_transfer = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("设备转移")')
    # "测试洗衣机店铺2"定位-用于设备转移
    shop_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试洗衣机店铺2")')
    # 确认转移按钮
    transfer_confirm = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tvTransfer")')
    # 删除设备入口按钮
    iv_menu = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_menu")')
    # 删除设备按钮
    delete_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("删除设备")')
    # "我知道了"弹窗按钮
    i_know = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我知道了")')


    def into_add_dryer_page(self):
        """点击右上角“新增”按钮进入新增烘干机界面"""
        lp = BasePage(self.driver)
        log.info("点击'+'号进入新增烘干机页面")
        lp.find(self.add_button).click()
        lp.find(self.add_device).click()
        return self

    def complete_message_add(self):
        """
        :完善新增烘干机信息
        """
        lp = BasePage(self.driver)
        log.info("新增完善烘干机资料")
        lp.find(self.dryer_type).click()
        lp.find(self.iv_select).click()
        lp.find(self.tv_next).click()
        lp.find(self.et_device_name).send_keys("企鹅烘干机")
        lp.find(self.tv_shop).click()
        lp.find(self.confirm_button).click()
        lp.find(self.tv_nqt).click()
        lp.find(self.tv_photo).click()
        # 此NQT二维码坐标只适用于HUAWEI nova3手机，其他机型需要重新适配
        self.driver.tap([(208, 268), (352, 412)])
        lp.find(self.confirm1).click()
        lp.find(self.tv_device_sn).click()
        lp.find(self.tv_photo).click()
        # 此IMEI二维码坐标只适用于HUAWEI nova3手机，其他机型需要重新适配
        self.driver.tap([(572, 268), (716, 412)])
        lp.find(self.confirm1).click()
        lp.find(self.ll_cd_model).click()
        lp.find(self.tv_next).click()
        lp.find(self.ll_function).click()
        lp.find(self.tv_next).click()
        lp.find(self.tv_next).click()
        lp.find(self.i_know).click()
        return self

    def into_device_detail_information(self):
        """进入烘干机详情页面"""
        lp = BasePage(self.driver)
        log.info("进入烘干机详情")
        lp.find(self.device_name_after_add).click()
        return self

    def show_base_infomation(self):
        """点击展示基础信息"""
        lp = BasePage(self.driver)
        log.info("点击展示详情页-基础信息")
        lp.find(self.base_info).click()
        return self

    def show_dry_mode(self):
        """点击展示烘干模式"""
        lp = BasePage(self.driver)
        log.info("点击展示详情页-烘干模式信息")
        lp.find(self.rlHgMode).click()
        return self

    def show_func_setting(self):
        """点击展示功能设置"""
        lp = BasePage(self.driver)
        log.info("点击展示详情页-功能设置信息")
        lp.find(self.iv_set).click()
        return self

    def edit_NQT(self):
        """更换NQT"""
        lp = BasePage(self.driver)
        log.info("更换NQT")
        lp.find(self.NQT_change).click()
        lp.find(self.tv_photo).click()
        # 此NQT二维码坐标只适用于HUAWEI nova3手机，其他机型需要重新适配(待新模块适配)
        self.driver.tap([(936, 268), (1080, 412)])
        lp.find(self.confirm1).click()
        return self

    def edit_IMEI(self):
        """更换IMEI"""
        lp = BasePage(self.driver)
        log.info("更换IMEI")
        lp.find(self.IMEI_change).click()
        lp.find(self.tv_photo).click()
        # 此IMEI二维码坐标只适用于HUAWEI nova3手机，其他机型需要重新适配(待新模块适配)
        self.driver.tap([(208, 632), (352, 776)])
        lp.find(self.confirm1).click()
        return self

    def change_fun_paragram(self):
        """修改功能参数"""
        lp = BasePage(self.driver)
        log.info("修改功能参数")
        lp.find(self.func_paragram_change).click()
        lp.find(self.tv_edit_price).click()
        lp.find(self.tvPrice).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        lp.find(self.et_input).send_keys("0.03")
        lp.find(self.confirm_button).click()
        lp.find(self.tv_next).click()
        lp.find(self.tv_next).click()
        return self

    def edit_device_belong(self):
        """设备转移"""
        lp = BasePage(self.driver)
        log.info("设备转移")
        lp.find(self.device_belong_transfer).click()
        lp.find(self.shop_name).click()
        lp.find(self.transfer_confirm).click()
        return self

    def start_dryer(self):
        """启动烘干机"""
        lp = BasePage(self.driver)
        log.info("启动烘干机")
        lp.find(self.start_button).click()
        lp.find(self.middle_dry).click()
        lp.find(self.func_start_button).click()
        lp.find(self.confirm_button).click()
        return self

    def reset_dryer(self):
        """复位烘干机"""
        lp = BasePage(self.driver)
        log.info("复位烘干机")
        lp.find(self.reset_button).click()
        return self

    def back_list(self):
        """返回设备列表"""
        lp = BasePage(self.driver)
        log.info("点击'返回'返回设备列表")
        lp.find(self.tv_back).click()
        return self

    def delete_device(self):
        """删除设备"""
        lp = BasePage(self.driver)
        log.info("删除设备")
        lp.find(self.iv_menu).click()
        lp.find(self.delete_button).click()
        lp.find(self.confirm_button1).click()
        lp.find(self.i_know).click()
        return self













