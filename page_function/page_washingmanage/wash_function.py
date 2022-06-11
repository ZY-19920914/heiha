#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/06/28
# @Author  : zy

from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from base_global.base_page import BasePage
from base_global.base_log import log


class Wash_Func(BasePage):
    # 新增按钮
    add_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_add")')
    # 选择新增设备
    add_device = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新增设备")')
    # 新增设备时，选择"企鹅洗衣机"型号
    qe_machine = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("企鹅洗衣机")')
    # 选择型号后的"同意"小按钮
    iv_select = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_select")')
    # "下一步"按钮
    tv_next = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_next")')
    # 新增设备时填写name
    et_device_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_device_name")')
    # 新增设备时选择所属"店铺"
    tv_shop = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_shop")')
    # "确定"按钮
    confirm_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")')
    # 新增设备时点击扫码"NQT"
    tv_nqt = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_nqt")')
    # "相册"按钮（进入相册选择二维码）
    tv_photo = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_photo")')
    # 在相册中选中照片后右下方出现的"确定1"按钮
    confirm1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定(1)")')
    # 新增设备时点击扫码"IMEI"
    tv_device_sn = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_device_sn")')
    # 新增设备后"提交"按钮
    submit_after_add = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_next")')
    # 新增设备提交后弹出的"我知道了"弹窗
    i_know = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我知道了")')
    # 点击新增的"测试洗衣机1"设备
    device1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试洗衣机1")')
    # 编辑界面-更换NQT栏
    change_nqt = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更换NQT")')
    # 编辑界面-更换IMEI栏
    change_imei = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更换IMEI")')
    # 生成付款码按钮
    pay_code = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("生成付款码")')
    # 点击生成付款码弹窗后点击的"保存"按钮
    save_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_save")')
    # 修改功能参数
    change_func_param = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("修改功能参数")')
    # 修改"普通混合（标准）-名称"
    change_normal_name = (MobileBy.XPATH, '//*[@text="普通混合（标准）"]/../../..//*[@text="修改名称"]')
    # 修改名字输入框
    et_input = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_input")')
    # 修改普通混合功能—标准洗衣中的价格
    change_price = (MobileBy.XPATH, '//*[@text="标准洗衣"]/../../..//*[@text="修改原价"]')
    # 改普通混合功能—标准洗衣中的耗时
    change_standard_time = (MobileBy.XPATH, '//*[@text="标准洗衣"]/../../..//*[@text="修改耗时"]')
    # 关闭/开启普通混合模式功能
    normal_open_close_button = (MobileBy.XPATH, '//*[@text="标准洗衣"]/../../..//*[@text="关闭"]')
    # 修改单脱功能——名称
    change_only_name = (MobileBy.XPATH, '//*[@text="单脱水"]/../../..//*[@text="修改名称"]')
    # 修改单脱功能——单价
    change_only_price = (MobileBy.XPATH, '//*[@text="单脱水"]/../../..//*[@text="修改原价"]')
    # 修改单脱功能——耗时
    change_only_time = (MobileBy.XPATH, '//*[@text="单脱水"]/../../..//*[@text="修改耗时"]')
    # 关闭/开启单脱模式功能
    only_open_close_button = (MobileBy.XPATH, '//*[@text="单脱水"]/../../..//*[@text="关闭"]')
    # 修改快洗功能——名称
    express_func_name = (MobileBy.XPATH, '//*[@text="快洗"]/../../..//*[@text="修改名称"]')
    # 修改精洗功能——原价
    change_careful_price = (MobileBy.XPATH, '//*[@text="精洗"]/../../..//*[@text="修改原价"]')
    # 修改精洗功能——耗时
    change_careful_time = (MobileBy.XPATH, '//*[@text="精洗"]/../../..//*[@text="修改耗时"]')
    # 修改精洗功能关闭/开启按钮
    careful_open_close_button = (MobileBy.XPATH, '//*[@text="精洗"]/../../..//*[@text="关闭"]')
    # 修改超净洗功能——名称（改成"随意洗"）
    change_super_clean_clean = (MobileBy.XPATH, '//*[@text="超净洗"]/../../..//*[@text="修改名称"]')
    # 修改超净洗功能——原价
    change_super_clean_price = (MobileBy.XPATH, '//*[@text="随意洗"]/../../..//*[@text="修改原价"]')
    # 修改超净洗功能——耗时
    change_super_clean_time = (MobileBy.XPATH, '//*[@text="随意洗"]/../../..//*[@text="修改耗时"]')
    # 修改超净洗功能关闭/开启按钮
    super_open_close_button = (MobileBy.XPATH, '//*[@text="随意洗"]/../../..//*[@text="关闭"]')
    # 修改桶自洁功能——名称
    change_clean_self_name = (MobileBy.XPATH, '//*[@text="桶自洁"]/../../..//*[@text="修改名称"]')
    # 修改桶自洁功能——原价
    change_clean_self_price = (MobileBy.XPATH, '//*[@text="人工洁"]/../../..//*[@text="修改原价"]')
    # 修改桶自洁功能——耗时
    change_clean_self_time = (MobileBy.XPATH, '//*[@text="人工洁"]/../../..//*[@text="修改耗时"]')
    #  修改桶自洁功能关闭/开启按钮
    clean_self_open_close_button = (MobileBy.XPATH, '//*[@text="人工洁"]/../../..//*[@text="关闭"]')
    # 编辑修改设备名称
    edit_de_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("编辑设备名")')
    # 设备名填写框
    etContent = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/etContent")')
    # 设备转移选项
    move_device = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("设备转移")')
    # 所属店铺
    shop_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试洗衣机店铺2")')
    # 确定转移按钮
    tvTransfer = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tvTransfer")')
    # 范围35-43
    area1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("范围35-43")')
    # 范围20-32
    area2 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("范围20-32")')
    # 范围45-53
    area3 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("范围45-53")')
    # 范围5-9
    area4 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("范围5-9")')
    # 时间设置对应的"提交"按钮
    time_submit = (MobileBy.XPATH, '//*[@text="时间设置"]/..//*[@text="提交"]')
    # 掉电记忆功能
    tv_centent1 = (MobileBy.XPATH, '//*[@text="掉电记忆功能"]/..//*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    # 全程半程保护功能
    tv_centent2 = (MobileBy.XPATH, '//*[@text="全程半程保护功能"]/..//*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    # 加热功能
    tv_centent3 = (MobileBy.XPATH, '//*[@text="加热功能"]/..//*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    # 桶清洁功能
    tv_centent4 = (MobileBy.XPATH, '//*[@text="桶清洁功能"]/..//*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    # 按键使能
    tv_centent5 = (MobileBy.XPATH, '//*[@text="按键使能"]/..//*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    # 投币使能
    tv_centent6 = (MobileBy.XPATH, '//*[@text="投币使能"]/..//*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    # 设置快速洗水位
    tv_centent7 = (MobileBy.XPATH, '//*[@text="设置快速洗水位"]/..//*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    # 设置标准洗水位
    tv_centent8 = (MobileBy.XPATH, '//*[@text="设置标准洗水位"]/..//*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    # 设置大物洗水位
    tv_centent9 = (MobileBy.XPATH, '//*[@text="设置大物洗水位"]/..//*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    # 批量启动
    start_with_batch = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("批量启动")')
    # 批量启动选择店铺
    start_shop_batch = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试洗衣店铺")')
    # 批量启动—结束功能
    finish = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("结束")')
    # 批量启动—立即启动
    start_now = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("立即启动")')
    # 确认按钮
    sure_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确认")')
    # "知道了"按钮
    know = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("知道了")')
    # 单脱水
    only_dry = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("单脱水")')
    # 桶自洁
    clean_self = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("桶自洁")')
    # 搜索按钮
    iv_search = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_search")')
    # 搜索输入框
    et_search_shop = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_search_shop")')
    # 861037051054997
    search_result = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("861037051054997")')
    # 搜索框中的二维码扫描功能按钮
    iv_scan = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_scan")')
    # 设备详情中"删除设备"入口定位
    iv_menu = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_menu")')
    # 删除设备
    delete_device_icon = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("删除设备")')
    # 一级页面启动按钮
    start_device_button1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("启动")')
    # "标准洗衣"功能启动按钮
    start_device_button2 =(MobileBy.XPATH, '//*[@text="单脱水"]/../../..//*[@text="启动"]')
    # "复位"按钮
    reset_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("复位")')
    # 设备"空闲"状态定位
    status_free_device = (MobileBy.XPATH, '//*[@resource-id="com.qekj.merchant:id/v_circle"]/../../..//*[@text="空闲"]')
    # 设备"运行"状态定位
    status_run_device = (MobileBy.XPATH, '//*[@resource-id="com.qekj.merchant:id/v_circle"]/../../..//*[@text="运行"]')
    # "返回"按钮
    come_back_button = (MobileBy.XPATH, '//*[@text="设备详情"]/../../..//*[@text="返回"]')
    # "基础信息的下拉按钮"
    function_setting_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_set")')


    def into_add_device_page(self):
        """点击右上角"新增"按钮，选择"新增设备" """
        lp = BasePage(self.driver)
        log.info("点击新增设备进入新增洗衣机页面")
        lp.find(self.add_button).click()
        lp.find(self.add_device).click()
        return self

    def add_wash_message_complete(self):
        """
        1、选择企鹅洗衣机
        2、完善设备名称、所属店铺、设备NQT、设备IMEI号信息
        3、点击提交
        """
        lp = BasePage(self.driver)
        log.info("新增洗衣机信息完善")
        lp.find(self.qe_machine).click()
        lp.find(self.iv_select).click()
        lp.find(self.tv_next).click()
        lp.find(self.et_device_name).send_keys("测试洗衣机1")
        lp.find(self.tv_shop).click()
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.1
                          )
        lp.find(self.confirm_button).click()
        lp.find(self.tv_nqt).click()
        lp.find(self.tv_photo).click()
        sleep(2)
        # 此NQT二维码坐标只适用于redmi note7手机，其他机型需要重新适配
        self.driver.tap([(208, 268), (352, 412)])
        lp.find(self.confirm1).click()
        lp.find(self.tv_device_sn).click()
        lp.find(self.tv_photo).click()
        # 此IMEI二维码坐标只适用于redmi note7手机，其他机型需要重新适配
        self.driver.tap([(572, 268), (716, 412)])
        lp.find(self.confirm1).click()
        return self

    def submit_add_after(self):
        """新增设备完善资料后提交按钮"""
        lp = BasePage(self.driver)
        log.info("提交新增洗衣机")
        lp.find(self.submit_after_add).click()
        lp.find(self.i_know).click()
        sleep(2)
        self.driver.swipe(self.width*0.5,
                          self.height*0.4,
                          self.width*0.5,
                          self.height*0.7
                          )
        return self

    def submit_edit_after(self):
        """修改功能参数后提交按钮"""
        lp = BasePage(self.driver)
        log.info("提交修改")
        lp.find(self.submit_after_add).click()
        return self

    def into_edit_page(self):
        """进入编辑设备页面"""
        lp = BasePage(self.driver)
        log.info("进入编辑洗衣机页面")
        lp.find(self.device1).click()
        return self

    def edit_nqt(self):
        """更换NQT号"""
        lp = BasePage(self.driver)
        log.info("更换NQT号")
        lp.find(self.change_nqt).click()
        lp.find(self.tv_photo).click()
        # 此NQT二维码坐标只适用于HUAWEI nova3手机，其他机型需要重新适配
        self.driver.tap([(936, 268), (1080, 412)])
        lp.find(self.confirm1).click()
        return self

    def edit_imei(self):
        """更换IMEI号"""
        lp = BasePage(self.driver)
        log.info("更换IMEI号")
        lp.find(self.change_imei).click()
        lp.find(self.tv_photo).click()
        # 此IMEI二维码坐标只适用于HUAWEI nova3手机，其他机型需要重新适配
        self.driver.tap([(208, 632), (352, 776)])
        lp.find(self.confirm1).click()
        lp.find(self.confirm_button).click()
        return self

    def edit_pay_QR(self):
        """生成付款吗"""
        lp = BasePage(self.driver)
        log.info("生成付款码")
        lp.find(self.pay_code).click()
        lp.find(self.save_button).click()
        # 点击保存到相册后提示"保存成功"，另外二维码的定位id="com.qekj.merchant:id/iv_scan"，可以以此判断成功与否
        return self

    def into_edit_func_parameter_page(self):
        """进入修改功能参数页面"""
        lp = BasePage(self.driver)
        lp.find(self.change_func_param).click()
        return self

    def edit_normal_mixture_name(self):
        """修改"普通混合-名称"参数"""
        lp = BasePage(self.driver)
        lp.find(self.change_normal_name).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        lp.find(self.et_input).send_keys("标准洗衣")
        lp.find(self.confirm_button).click()
        return self

    def edit_normal_mixture_price(self):
        """修改普通混合功能价格"""
        lp = BasePage(self.driver)
        lp.find(self.change_price).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("0.02")
        lp.find(self.confirm_button).click()
        return self

    def edit_normal_micture_time(self):
        """修改普通混合功能耗时"""
        lp = BasePage(self.driver)
        lp.find(self.change_standard_time).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("30")
        lp.find(self.confirm_button).click()
        return self

    def edit_normal_micture_close(self):
        """关闭/开启普通混合模式功能"""
        lp = BasePage(self.driver)
        lp.find(self.normal_open_close_button).click()
        return self

    def edit_only_dry_name(self):
        """修改单脱功能名称"""
        lp = BasePage(self.driver)
        log.info("修改'单脱'功能模式")
        sleep(2)
        lp.find(self.change_only_name).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("单脱水")
        lp.find(self.confirm_button).click()
        return self

    def edit_only_dry_price(self):
        """修改单脱功能原价"""
        lp = BasePage(self.driver)
        log.info("修改'单脱'功能单价")
        lp.find(self.change_only_price).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("0.02")
        lp.find(self.confirm_button).click()
        return self

    def edit_only_dry_time(self):
        """修改单脱功能耗时"""
        lp = BasePage(self.driver)
        lp.find(self.change_only_time).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("30")
        lp.find(self.confirm_button).click()
        return self

    def edit_only_dry_close(self):
        """关闭/开启单脱模式功能"""
        lp = BasePage(self.driver)
        lp.find(self.only_open_close_button).click()
        return self

    def edit_express_wash_name(self):
        """修改快洗功能名称"""
        lp = BasePage(self.driver)
        lp.find(self.express_func_name).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("精洗")
        lp.find(self.confirm_button).click()
        return self

    def edit_express_wash_price(self):
        """修改快洗功能原价"""
        lp = BasePage(self.driver)
        lp.find(self.change_careful_price).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("0.02")
        lp.find(self.confirm_button).click()
        return self

    def edit_express_wash_time(self):
        """修改快洗功能耗时"""
        lp = BasePage(self.driver)
        lp.find(self.change_careful_time).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("30")
        lp.find(self.confirm_button).click()
        return self

    def edit_express_wash_close(self):
        """关闭/开启快洗模式功能"""
        lp = BasePage(self.driver)
        lp.find(self.careful_open_close_button).click()
        return self

    def edit_super_clean_name(self):
        """修改超净洗功能名称"""
        lp = BasePage(self.driver)
        lp.find(self.change_super_clean_clean).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("随意洗")
        return self

    def edit_super_clean_price(self):
        """修改超净洗功能原价"""
        lp = BasePage(self.driver)
        lp.find(self.change_super_clean_price).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("0.02")
        lp.find(self.confirm_button).click()
        return self

    def edit_super_clean_time(self):
        """修改超净洗功能耗时"""
        lp = BasePage(self.driver)
        lp.find(self.change_super_clean_time).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("30")
        lp.find(self.confirm_button).click()
        return self

    def edit_super_clean_close(self):
        """关闭/开启超净洗模式功能"""
        lp = BasePage(self.driver)
        lp.find(self.super_open_close_button).click()
        return self

    def edit_self_clean_name(self):
        """修改桶自洁功能名称"""
        lp = BasePage(self.driver)
        lp.find(self.change_clean_self_name).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("人工洁")
        lp.find(self.confirm_button).click()
        return self

    def edit_self_clean_price(self):
        """修改桶自洁功能原价"""
        lp = BasePage(self.driver)
        lp.find(self.change_clean_self_price).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("0.02")
        lp.find(self.confirm_button).click()
        return self

    def edit_self_clean_time(self):
        """修改桶自洁功能耗时"""
        lp = BasePage(self.driver)
        lp.find(self.change_clean_self_time).click()
        ele = lp.find(self.et_input)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("30")
        lp.find(self.confirm_button).click()
        return self

    def edit_self_clean_close(self):
        """关闭/开启桶自洁模式功能"""
        lp = BasePage(self.driver)
        lp.find(self.clean_self_open_close_button).click()
        return self

    def edit_device_name(self):
        """编辑修改设备名称"""
        lp = BasePage(self.driver)
        lp.find(self.edit_de_name).click()
        ele = lp.find(self.etContent)
        ele_text = ele.get_attribute("text")
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("测试洗衣机2")
        lp.find(self.confirm_button).click()
        return self

    def edit_device_transfer(self):
        """设备转移"""
        lp = BasePage(self.driver)
        lp.find(self.move_device).click()
        lp.find(self.shop_name).click()
        lp.find(self.tvTransfer).click()
        return self

    def edit_advanced_setting_time(self):
        """高级参数设置-时间设置"""
        lp = BasePage(self.driver)
        lp.find(self.area1).send_keys("35")
        lp.find(self.area2).send_keys("35")
        lp.find(self.area3).send_keys("35")
        lp.find(self.area4).send_keys("35")
        lp.find(self.time_submit).click()
        return self

    def edit_advanced_setting_special1(self):
        """特殊功能设置1"""
        lp = BasePage(self.driver)
        lp.find(self.tv_centent1).click()
        lp.find(self.confirm_button).click()
        lp.find(self.tv_centent2).click()
        lp.find(self.confirm_button).click()
        lp.find(self.tv_centent3).click()
        lp.find(self.confirm_button).click()
        lp.find(self.tv_centent4).click()
        lp.find(self.confirm_button).click()
        lp.find(self.tv_centent5).click()
        lp.find(self.confirm_button).click()
        lp.find(self.tv_centent6).click()
        lp.find(self.confirm_button).click()
        # 此提交按钮坐标仅使用于redmi note7手机，其他机型需要重新适配
        self.driver.tap([(957, 706), (1037, 760)])
        return self

    def edit_advanced_setting_special2(self):
        """特殊功能设置2"""
        lp = BasePage(self.driver)
        lp.find(self.tv_centent7).click()
        lp.find(self.confirm_button).click()
        lp.find(self.tv_centent8).click()
        lp.find(self.confirm_button).click()
        lp.find(self.tv_centent9).click()
        lp.find(self.confirm_button).click()
        # 此提交按钮坐标仅使用于redmi note7手机，其他机型需要重新适配
        self.driver.tap([(957, 1610), (1037, 1664)])
        return self


    def into_start_batch_page(self):
        """点击新增按钮后选择“批量启动”"""
        lp = BasePage(self.driver)
        lp.find(self.start_with_batch).click()
        return self

    def choose_shop(self):
        """
        1、选择商铺并点击
        2、跳转至商铺设备功能项，选择并点击
        3、点击"立即启动"按钮
        4、断言是否启动成功
        """
        lp = BasePage(self.driver)
        lp.find(self.start_shop_batch).click()
        return self

    def func_end(self):
        """结束功能"""
        lp = BasePage(self.driver)
        lp.find(self.finish).click()
        lp.find(self.start_now).click()
        lp.find(self.sure_button).click()
        sleep(11)
        lp.find(self.know).click()
        sleep(3)
        return self

    def func_dry(self):
        """单脱水功能"""
        lp = BasePage(self.driver)
        lp.find(self.only_dry).click()
        lp.find(self.start_now).click()
        lp.find(self.sure_button).click()
        sleep(11)
        lp.find(self.know).click()
        sleep(3)
        return self


    def func_clearself(self):
        """桶自洁功能"""
        lp = BasePage(self.driver)
        lp.find(self.clean_self).click()
        lp.find(self.start_now).click()
        lp.find(self.sure_button).click()
        sleep(11)
        lp.find(self.know).click()
        sleep(3)
        return self

    def base_information(self):
        """基础信息展示"""
        lp = BasePage(self.driver)
        log.info("点击'功能设置'")
        lp.find(self.function_setting_button).click()
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.4
                          )
        return self

    def search_device_by_number(self):
        """根据填充IMEI号搜索设备"""
        lp = BasePage(self.driver)
        lp.find(self.iv_search).click()
        # 此处设置为模糊查找
        lp.find(self.et_search_shop).send_keys("861037051054")
        lp.find(self.search_result).click()
        return self

    def search_device_by_QR(self):
        """根据扫相册二维码搜索设备"""
        lp = BasePage(self.driver)
        lp.find(self.iv_scan).click()
        lp.find(self.tv_photo).click()
        # 具体二维码图片坐标等补充至相册后再补充相关代码
        return self

    def start_device(self):
        """启动设备"""
        lp = BasePage(self.driver)
        log.info("点击洗衣机详情页-'启动'按钮")
        lp.find(self.start_device_button1).click()
        log.info("选择具体的'单脱水'功能进行启动")
        lp.find(self.start_device_button2).click()
        lp.find(self.confirm_button).click()
        sleep(6)
        log.info("点击'返回'按钮返回洗衣机设备列表展示页")
        lp.find(self.come_back_button).click()
        return self

    def rest_device(self):
        """复位设备"""
        lp = BasePage(self.driver)
        log.info("点击洗衣机详情页-'复位'按钮")
        lp.find(self.reset_button).click()
        lp.find(self.come_back_button).click()
        return self

    def delete_device(self):
        """删除新增洗衣机"""
        lp = BasePage(self.driver)
        log.info("删除洗衣机")
        lp.find(self.iv_menu).click()
        lp.find(self.delete_device_icon).click()
        lp.find(self.sure_button).click()
        lp.find(self.i_know).click()
        return self

    # def return_home_page(self):
    #     """删除设备后返回首页准备进行下一条用例执行"""
    #     lp = BasePage(self.driver)
    #     try:
    #         for i in range(2):
    #             self.driver.find_element_by_android_uiautomator(
    #                 'new UiSelector().text("返回")').click()
    #     except Exception as e:
    #         print("点击'返回'失败，原因是：{}".format(e))
    #         self.driver.get_screenshot_as_file(lp.screenshot_filepath())
    #     return self