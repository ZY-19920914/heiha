#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/06/28
# @Author  : zy
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from base_global.base_page import BasePage
from base_global.base_log import log


class Bath_position_Func(BasePage):
    # 新增按钮
    iv_add = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_add")')
    add_device = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新增设备")')
    qe_device = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("企鹅自研集中淋浴水控（带流量计）")')
    # 确认弹框
    iv_select = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_select")')
    # 下一步按钮
    tv_next = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_next")')
    # 所属店铺
    shop_belong = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("所属店铺")')
    # 确认按钮
    confirm_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")')
    # 所属浴室
    washroom_belong = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("所属浴室")')
    # 脉冲数填写框
    et_maichong = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_maichong")')
    # 单价填写框
    et_price = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_price")')
    # 浴位编号填写
    et_yw_no = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_yw_no")')
    # 设备编号填写框（点击唤起扫码IMEI）
    tv_sb_no = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_sb_no")')
    # 扫码页面中的"选取相册"按钮
    tv_photo = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_photo")')
    # 相册中选中后显示的"确定"按钮
    confirm_button1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定(1)")')
    # "提交"按钮
    submit_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("提交")')
    # 更换设备编号
    change_number = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更换设备编号")')
    # 修改价格
    change_price = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("修改价格")')
    # 修改单价输入框
    etContent = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/etContent")')
    # 修改单脉冲流量
    change_pulse = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("修改单脉冲流量")')
    # 修改浴位编号
    change_position_number = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("编辑浴位编号")')
    # "高级参数设置"按钮
    advanced_setting_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("高级参数设置")')
    # 流量超时时长
    flow_et_centent = (MobileBy.XPATH, '//*[@text="无流量超时时长(秒)"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 最大允许出水时间
    time_et_centent = (MobileBy.XPATH, '//*[@text="最大允许出水时间(秒)"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 网络参数设置
    tv_report = (MobileBy.XPATH, '//*[@text="网络参数设置"]/..//*[@resource-id="com.qekj.merchant:id/tv_report"]')
    et_centent = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_centent")')
    # 清除故障对应的提交
    clear_submit = (MobileBy.XPATH, '//*[@text="清除故障"]/..//*[@text="提交"]')
    # 搜索按钮
    iv_search = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_search")')
    # 搜索输入框
    et_search_shop = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_search_shop")')
    # 点击此按钮显示"删除设备按钮"
    iv_search_single = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_search_single")')
    # "删除"按钮
    delete = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("删除设备")')
    # "我知道了"按钮
    i_know = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我知道了")')
    # 设备编号
    position_number = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0001")')
    # "返回"按钮
    back_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("返回")')
    # "基础信息"
    base_information_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("基础信息")')
    # 基础信息——单脉冲流量
    monopulse_flow = (MobileBy.XPATH, '//*[@text="单脉冲流量(ml)"]/..//*[@resource-id="com.qekj.merchant:id/tv_maichang"]')
    # 基础信息——浴位单价
    unit_price = (MobileBy.XPATH, '//*[@text="单价(元/L)"]/..//*[@resource-id="com.qekj.merchant:id/tv_price"]')
    # 基础信息——设备名称
    device_name = (MobileBy.XPATH, '//*[@text="设备名称"]/..//*[@resource-id="com.qekj.merchant:id/tv_yw_no"]')

    def into_add_button_page(self):
        lp = BasePage(self.driver)
        """
        1、点击右上角“新增”按钮
        2、点击新增按钮后选择“新增设备”
        :return:
        """
        log.info("点击'+'号按钮")
        lp.find(self.iv_add).click()
        log.info("选择'新增设备'")
        lp.find(self.add_device).click()
        return self

    def add_bath_position_message_complete(self):
        lp = BasePage(self.driver)
        """
        1、选择设备
        2、点击确认上述操作选择框
        3、点击"下一步"按钮
        4、完善资料，包括如下选项
            #所属店铺
            #所属浴室
            #单脉冲流量
            #单价
            #浴位编号
            #设备SN号
        :return:
        """
        log.info("点击'企鹅自研集中淋浴水控（带流量计）设备'")
        lp.find(self.qe_device).click()
        # 点击确认小确认框
        log.info("点击'确认'")
        lp.find(self.iv_select).click()
        # 点击下一步按钮
        log.info("点击'下一步'")
        lp.find(self.tv_next).click()
        # 设备资料完善
        log.info("点击选择'所属店铺'")
        lp.find(self.shop_belong).click()
        log.info("向上滑动选择店铺")
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.85
                          )
        lp.find(self.confirm_button).click()
        log.info("点击选择'所属浴室'")
        lp.find(self.washroom_belong).click()
        lp.find(self.confirm_button).click()
        log.info("填写脉冲数")
        lp.find(self.et_maichong).send_keys("500")
        log.info("填写单价")
        lp.find(self.et_price).send_keys("0.01")
        lp.find(self.tv_next).click()
        log.info("填写浴位编号")
        lp.find(self.et_yw_no).send_keys("0001")
        log.info("点击设备编号")
        lp.find(self.tv_sb_no).click()
        log.info("扫码页面点击右上角'相册'按钮")
        lp.find(self.tv_photo).click()
        # 此坐标只适用于redmi note7手机，其他机型需要重新适配
        log.info("选取对应相册中的浴位IMEI码")
        self.driver.tap([(584, 609), (716, 741)])
        lp.find(self.confirm_button1).click()
        lp.find(self.submit_button).click()
        sleep(2)
        return self

    def into_edit_page(self):
        """
        :进入编辑页面（若此步骤在新增浴位后操作需要连续返回两次页面后操作进入编辑页）
        """
        lp = BasePage(self.driver)
        # for i in range(2):
        #     self.driver.swipe(self.width*0.5,
        #                       self.height*0.4,
        #                       self.width*0.5,
        #                       self.height*0.8
        #                       )
        log.info("点击设备号，进入设备编辑页面")
        lp.find(self.position_number).click()
        return self

    def edit_device_number(self):
        """
        :更改设备编号
        """
        lp = BasePage(self.driver)
        log.info("点击'更换设备编号'选项")
        lp.find(self.change_number).click()
        log.info("从相册选取")
        lp.find(self.tv_photo).click()
        # 此坐标只适用于redmi note7手机，其他机型需要重新适配
        self.driver.tap([(948, 609), (1080, 741)])
        lp.find(self.confirm_button1).click()
        log.info("确认更换设备编号")
        lp.find(self.submit_button).click()
        return self

    def edit_device_price(self):
        """
        修改设备单价
        """
        lp = BasePage(self.driver)
        log.info("点击'修改价格'选项")
        lp.find(self.change_price).click()
        log.info("将原价格删除")
        ele = lp.find(self.etContent)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        log.info("价格修改成'0.1'")
        ele.send_keys("0.1")
        log.info("确认修改价格")
        lp.find(self.confirm_button).click()
        return self

    def edit_device_flow(self):
        """
        修改单脉冲流量
        """
        lp = BasePage(self.driver)
        log.info("点击'修改单脉冲流量'选项")
        lp.find(self.change_pulse).click()
        log.info("将原单脉冲流量参数删除")
        ele = lp.find(self.etContent)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        log.info("将单脉冲流量修改成1000ml")
        ele.send_keys("1000")
        lp.find(self.confirm_button).click()
        return self

    def edit_position_number(self):
        """
        修改浴位编号
        """
        lp = BasePage(self.driver)
        log.info("点击'修改浴位编号'选项")
        lp.find(self.change_position_number).click()
        log.info("删除原浴位编号")
        ele = lp.find(self.etContent)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        log.info("将浴位编号修改为'0101'")
        ele.send_keys("0101")
        lp.find(self.confirm_button).click()
        return self

    def base_information(self):
        """
        基础信息展示
        """
        lp = BasePage(self.driver)
        log.info("点击'基础信息'展示")
        lp.find(self.base_information_button).click()
        return self

    def edit_advanced_setting_network(self):
        """
        高级参数设置-网络参数设置
        """
        lp = BasePage(self.driver)
        lp.find(self.advanced_setting_button).click()
        lp.find(self.flow_et_centent).send_keys("3600")
        lp.find(self.time_et_centent).send_keys("3600")
        lp.find(self.tv_report).click()
        return self

    def edit_advanced_setting_malfunction(self):
        """
        高级参数设置-清除故障
        """
        lp = BasePage(self.driver)
        lp.find(self.advanced_setting_button).click()
        lp.find(self.et_centent).send_keys("1")
        lp.find(self.clear_submit).click()
        return self

    def search_device_by_number(self):
        """
        根据输入浴位编号搜索设备
        """
        lp = BasePage(self.driver)
        lp.find(self.iv_search).click()
        # 此处为模糊查找
        lp.find(self.et_search_shop).send_keys("04")
        return self

    def delete_device_after_edit(self):
        """
        编辑设备后再删除新增浴位设备
        """
        lp = BasePage(self.driver)
        lp.find(self.iv_search_single).click()
        lp.find(self.delete).click()
        lp.find(self.confirm_button).click()
        lp.find(self.i_know).click()
        return self

    def delete_device_after_add(self):
        """
        新增设备后直接删除新增浴位设备（需要点击返回按钮进入设备列表页再执行删除）
        """
        lp = BasePage(self.driver)
        lp.find(self.position_number).click()
        lp.find(self.iv_search_single).click()
        lp.find(self.delete).click()
        lp.find(self.confirm_button).click()
        lp.find(self.i_know).click()
        return self

    def return_home_page(self):
        lp = BasePage(self.driver)
        """
        删除设备后返回首页准备进行下一条用例执行
        """
        for i in range(2):
            lp.find(self.back_button).click()
        return self






