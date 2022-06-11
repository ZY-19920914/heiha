#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/06/28
# @Author  : zy
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webelement import WebElement
from base_global.base_page import BasePage
from base_global.base_log import log


class Shop_Func(BasePage):
    # 新增按钮
    add_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_add")')
    # 新增店铺名称输入框
    shop_name_input_box = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_shop_name")')
    # 选择店铺类型
    shop_type = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_store_type")')
    # 确认按钮
    confirm_button= (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")')
    # 选择店铺所属地区
    shop_area = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_area")')
    # 浙江省
    zjs = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("浙江省")')
    # 杭州市
    hz = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("杭州市")')
    # 西湖区
    xh = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("西湖区")')
    # 详细地址-小区/大厦学校
    shop_detail_area = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_shop_detail_area")')
    # 详细地址-搜索
    ll_search = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/ll_search")')
    # 详细地址-搜索
    et_search = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_search")')
    # class属性定位
    class_name = (MobileBy.CLASS_NAME, "android.widget.RelativeLayout")
    # 详细地址填写
    et_search_detail_address = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_search_detail_address")')
    # 店铺营业时间
    rl_time = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_time")')
    # 客服电话填写框
    et_service_phone = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_service_phone")')
    # 提交按钮
    rl_submit = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_submit")')
    # 测试店铺4对应店铺详情
    shop4_detail = (MobileBy.XPATH, '//*[@text="测试店铺4"]/..//*[@text="店铺详情"]')
    # 店铺删除按钮
    delete_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_delete")')
    # 测试店铺3对应店铺详情
    shop3_detail = (MobileBy.XPATH, '//*[@text="测试店铺3"]/..//*[@text="店铺详情"]')
    # 编辑按钮
    edit_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_edit")')
    # 编辑店铺名称
    et_shop_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_shop_name")')
    # 更改店铺类型
    rl_store_type = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_store_type")')
    # 选择店铺以"学校"类型
    rl_school = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_school")')
    # 点击模糊搜索后搜索结果—浙江旅游职业学院千岛湖校区
    after_dim_search_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("浙江旅游职业学院千岛湖校区")')
    # 填写具体地址
    et_floor = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_floor")')
    # 更改店铺营业时间
    rl_school_time = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/rl_school_time")')
    # 填写学校店铺客服电话
    et_school_service_phone = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_school_service_phone")')
    # 更改支付方式按钮（免密与非免密）
    sc_school_force = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/sc_school_force")')
    # 搜索店铺按钮
    iv_search = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_search")')
    # 搜索框
    et_search_shop = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_search_shop")')
    # 搜索浴室
    search_shop = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试浴室店铺")')
    # 联合大厦A座定位
    area_detail_location = (MobileBy.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_address" and @text="联合大厦A座"]')

    def add_button_click(self):
        """点击右上角"新增"按钮"""
        lp = BasePage(self.driver)
        log.info("点击'+'号进入新增店铺页面")
        lp.find(self.add_button).click()
        return self

    def complete_shop_name(self):
        """填写店铺名称"""
        lp = BasePage(self.driver)
        log.info("填写新增店铺名称")
        lp.find(self.shop_name_input_box).send_keys("测试店铺3")
        return self

    def complete_shop_type(self):
        """选择店铺类型"""
        lp = BasePage(self.driver)
        log.info("向上滑动选择店铺类型")
        lp.find(self.shop_type).click()
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.79
                          )
        lp.find(self.confirm_button).click()
        return self

    def choose_shop_area(self):
        """选择店铺所属地区"""
        lp = BasePage(self.driver)
        log.info("向上滑动选择店铺所在地区")
        lp.find(self.shop_area).click()
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.8
                          )
        lp.find(self.zjs).click()
        lp.find(self.hz).click()
        lp.find(self.xh).click()
        return self

    def choose_shop_address(self):
        """选择详细地址"""
        lp = BasePage(self.driver)
        log.info("填充新增店铺详细地址")
        lp.find(self.shop_detail_area).click()
        lp.find(self.ll_search).click()
        lp.find(self.et_search).send_keys("联合大厦A座")
        # ele = lp.find(self.class_name)
        # ele[0].click()
        lp.find(self.area_detail_location).click()
        lp.find(self.et_search_detail_address).send_keys("1005室")
        return self

    def choose_shop_open_hours(self):
        """
        1、选择店铺营业时间（默认）
        2、点击确定
        """
        lp = BasePage(self.driver)
        log.info("选择新增店铺营业时间")
        lp.find(self.rl_time).click()
        lp.find(self.confirm_button).click()
        return self

    def fillout_phone_number(self):
        """填写客服电话"""
        lp = BasePage(self.driver)
        log.info("填写新增店铺客服电话")
        lp.find(self.et_service_phone).send_keys("10000")
        return self

    def submit_information(self):
        """点击"提交"按钮"""
        lp = BasePage(self.driver)
        log.info("提交新增店铺")
        lp.find(self.rl_submit).click()
        return self

    def into_shop3_detail(self):
        """进入店铺详情"""
        lp = BasePage(self.driver)
        log.info("点击'测试店铺3'详情按钮")
        lp.find(self.shop3_detail).click()
        return self

    def into_shop4_detail(self):
        """进入店铺详情"""
        lp = BasePage(self.driver)
        log.info("点击'测试店铺4'详情按钮")
        lp.find(self.shop4_detail).click()
        return self

    def delete_shop(self):
        """
        1、新增店铺后再次点击"店铺详情"
        2、点击底部"删除"按钮
        3、点击删除确认弹框中的"确定"按钮
        """
        lp = BasePage(self.driver)
        # log.info("点击'测试店铺4'详情按钮")
        # lp.find(self.shop4_detail).click()
        log.info("点击删除店铺按钮")
        lp.find(self.delete_button).click()
        log.info("点击确认删除")
        lp.find(self.confirm_button).click()
        return self

    def into_edit_page(self):
        """
        1、新增店铺后再次点击"店铺详情"
        2、点击底部"编辑"按钮
        """
        lp = BasePage(self.driver)
        # log.info("点击'测试店铺3'详情按钮")
        # lp.find(self.shop3_detail).click()
        log.info("点击编辑店铺按钮")
        lp.find(self.edit_button).click()
        return self

    def edit_shop_name(self):
        """
        1、获取店铺编辑页面店铺名称text
        2、点击店铺编辑页面店铺名称输入框
        3、将输入光标移动到末尾（123代表光标移动到末尾键）
        4、删除原有店铺名（67代号表示退格回删）
        5、输入新的店铺名称
        """
        lp = BasePage(self.driver)
        log.info("删除旧的店铺名称，填写新的店铺名")
        ele = lp.find(self.et_shop_name)
        ele_text = ele.get_attribute("text")
        ele.click()
        self.driver.keyevent(123)
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("测试店铺4")
        return self

    def edit_shop_type(self):
        """
        1、编辑更改店铺类型
        2、选择学校
        3、选择学校所在地区（选择学校后自动填充）
        4、学校的详细地址（选择学校后自动填充）
        5、设备所在学校的楼栋及楼层
        """
        lp = BasePage(self.driver)
        log.info("更改店铺类型为学校")
        lp.find(self.rl_store_type).click()
        sleep(1)
        self.driver.swipe(self.width*0.5,
                          self.height*0.86,
                          self.width*0.5,
                          self.height*0.99
                          )
        lp.find(self.confirm_button).click()
        lp.find(self.rl_school).click()
        lp.find(self.et_search).send_keys("浙江旅游职业学院千岛湖")
        lp.find(self.after_dim_search_name).click()
        lp.find(self.et_floor).send_keys("男生寝室2号楼一楼")
        return self

    def edit_shop_open_time(self):
        """更改学校店铺营业时间"""
        lp = BasePage(self.driver)
        log.info("更改店铺营业时间")
        lp.find(self.rl_school_time).click()
        lp.find(self.confirm_button).click()
        return self

    def edit_shop_phone(self):
        """填写学校店铺客服电话"""
        lp = BasePage(self.driver)
        lp.find(self.et_school_service_phone).send_keys("10000")
        return self

    def edit_shop_pay_way(self):
        """更改支付方式（免密与非免密）"""
        lp = BasePage(self.driver)
        lp.find(self.sc_school_force).click()
        return self

    def serch_shop(self):
        """搜索店铺"""
        lp = BasePage(self.driver)
        log.info("模糊查询搜索店铺")
        lp.find(self.iv_search).click()
        # 此处为模糊查找
        lp.find(self.et_search_shop).send_keys("测试浴室")
        lp.find(self.search_shop).click()
        return self












