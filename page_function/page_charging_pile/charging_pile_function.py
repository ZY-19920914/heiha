from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from base_global.base_page import BasePage
from base_global.base_log import log


class Charging_pile_Func(BasePage):
    # 新增按钮
    add_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_add")')
    # 选择新增设备
    add_device = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新增设备")')
    # 选择需要编辑的充电桩
    device_name_after_add = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试充电桩")')
    # "高级参数设置"按钮
    advanced_setting_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("高级参数设置")')
    # 选择新增设备型号
    device_type = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("XY-10")')
    # 设备型号选择后的确认小圆框
    confirm_select = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_select")')
    # 设备型号选择后的"下一步"确认按钮/"提交按钮"
    next_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_next")')
    # 设备名称填写框
    device_name_box = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_device_name")')
    # 选择所属商铺栏
    shop_belong = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_shop")')
    # 确定按钮
    confirm_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")')
    # 确认按钮
    confirm_button1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确认")')
    # 新增功率按钮
    add_power_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新增功率")')
    # 添加NQT
    NQT_select = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_nqt")')
    # "相册"按钮（从相册选择二维码）
    photo_select = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_photo")')
    # 添加"SN"号
    sn_select = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_device_sn")')
    # 相册选择二维码后出现的确定按钮
    confirm_button_after_photo = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定(1)")')
    # 充电口
    charging_mouth = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("充电口")')
    # 价格设置
    price_setting = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("价格设置")')
    # 充电模式
    charging_mode = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("充电模式")')
    # charging_mode = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/ll_jf_model")')

    # 提交按钮
    submit_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("提交")')
    # "我知道了"按钮（在点击提交后还会有一个确认框，点击"我知道了"消失）
    i_know_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/tv_know")')
    # 编辑更换NQT
    change_nqt = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更换NQT")')
    # 更换IMEI
    change_imei = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更换IMEI")')
    # 修改价格
    change_price = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("修改价格")')
    # 修改原价按钮
    edit_price_button = (MobileBy.XPATH, '//*[@text="0 ~ 200"]/..//*[@resource-id="com.qekj.merchant:id/tv_price"]')
    # 价格输入框
    price_input_box = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/et_price")')
    # 修改充电口
    change_charging_mouth = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("修改充电口")')
    # 进入选择充电口
    charging_mouth_select = (MobileBy.XPATH, '//*[@text="10号口"]/..//*[@resource-id="com.qekj.merchant:id/sc_check"]')
    # 编辑设备名
    edit_device_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("编辑设备名")')
    # 编辑设备名输入框
    edit_device_name_input = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/etContent")')
    # 设备转移选项
    device_transfer = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("设备转移")')
    # 选择充电桩店铺
    shop_select = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试充电桩店铺")')
    # 确认转移
    transfer_confirm = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确认转移")')
    # 更改自停开关
    edit_stop_switch = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_right")')
    # 充满自停开关"提交"按钮
    advanced_setting_stop_submit = (MobileBy.XPATH, '//*[@text="充满自停开关"]/..//*[@text="提交"]')
    # 更改单路最大功率
    advanced_mix_power = (MobileBy.XPATH, '//*[@text="单路最大功率"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 更改充满自停时间
    advanced_stop_time = (MobileBy.XPATH, '//*[@text="充满自停时间"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 更改自停功率
    advanced_stop_power = (MobileBy.XPATH, '//*[@text="充满自停功率"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 充满自停参数"提交"按钮
    advanced_setting_param_submit = (MobileBy.XPATH, '//*[@text="充满自停参数"]/..//*[@text="提交"]')
    # 高级参数设置-空载断电时间
    advanced_setting_break_time = (MobileBy.XPATH, '//*[@text="空载断电时间"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 高级参数设置-空载断电功率
    advanced_setting_break_power = (MobileBy.XPATH, '//*[@text="空载断电功率"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 更改空载断电设置参数"提交"按钮
    advanced_setting_break_submit = (MobileBy.XPATH, '//*[@text="空载断电参数"]/..//*[@text="提交"]')
    # 高级参数设置-更改最大充电时间
    advanced_setting_mix_charging_time = (MobileBy.XPATH, '//*[@text="最大充电时间"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 更改空载断电设置参数"提交"按钮
    advanced_setting_mix_charging_submit = (MobileBy.XPATH, '//*[@text="最大充电时间"]/..//*[@text="提交"]')
    # 高级参数设置-更改上报温度阈值
    advanced_setting_mix_temperature = (MobileBy.XPATH, '//*[@text="上报温度阈值"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 更改上报温度阈值"提交"按钮
    advanced_setting_mix_temperature_submit = (MobileBy.XPATH, '//*[@text="上报温度阈值"]/..//*[@text="提交"]')
    # 高级参数设置-防止扰民开始时间
    advanced_setting_prevent_start_time = (MobileBy.XPATH, '//*[@text="防止扰民开始时间"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 高级参数设置-防止扰民结束时间
    advanced_setting_prevent_finish_time = (MobileBy.XPATH, '//*[@text="防止扰民结束时间"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 高级参数设置-正常音量
    advanced_setting_normal_volume = (MobileBy.XPATH, '//*[@text="正常音量"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 高级参数设置-扰民音量
    advanced_setting_prevent_volume = (MobileBy.XPATH, '//*[@text="扰民音量"]/..//*[@resource-id="com.qekj.merchant:id/et_centent"]')
    # 更改防扰民设置"提交"按钮
    advanced_setting_prevent_people_submit = (MobileBy.XPATH, '//*[@text="防扰民设置"]/..//*[@text="提交"]')
    iv_search_single = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.qekj.merchant:id/iv_search_single")')
    delete_device_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("删除设备")')
    # '基础信息'选项定位
    base_information = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("基础信息")')

    def into_add_charging_pile_page(self):
        """点击右上角“新增”按钮进入新增充电桩界面"""
        lp = BasePage(self.driver)
        log.info("充电桩管理页面点击'+'号")
        lp.find(self.add_button).click()
        log.info("选择新增设备")
        lp.find(self.add_device).click()
        return self

    def into_detail_charging_pile_page(self):
        """进入充电桩详情界面"""
        lp = BasePage(self.driver)
        log.info("进入充电桩编辑页面")
        lp.find(self.device_name_after_add).click()
        self.driver.get_log('logcat')
        return self

    def into_edit_advanced_setting_page(self):
        """进入高级参数设置界面"""
        lp = BasePage(self.driver)
        lp.find(self.advanced_setting_button).click()
        self.driver.swipe(self.width*0.5,
                          self.height*0.4,
                          self.width*0.5,
                          self.height*0.7
                          )
        return self

    def add_charging_message_complete(self):
        """新增设备信息完善"""
        lp = BasePage(self.driver)
        log.info("向上滑动选择对应型号充电桩")
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.1
                          )
        lp.find(self.device_type).click()
        lp.find(self.confirm_select).click()
        lp.find(self.next_button).click()
        log.info("填写充电桩设备号")
        lp.find(self.device_name_box).send_keys("测试充电桩")
        log.info("选择所属店铺")
        lp.find(self.shop_belong).click()
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.1
                          )
        lp.find(self.confirm_button).click()
        log.info("扫描NQT和IMEI号")
        lp.find(self.NQT_select).click()
        lp.find(self.photo_select).click()
        # 此NQT二维码坐标只适用于HUAWEI nova3手机，其他机型需要重新适配
        self.driver.tap([(208, 268), (352, 412)])
        lp.find(self.confirm_button_after_photo).click()
        lp.find(self.sn_select).click()
        lp.find(self.photo_select).click()
        # 此IMEI二维码坐标只适用于HUAWEI nova3手机，其他机型需要重新适配
        self.driver.tap([(572, 268), (716, 412)])
        lp.find(self.confirm_button_after_photo).click()
        log.info("充电口设置")
        lp.find(self.charging_mouth).click()
        lp.find(self.confirm_button).click()
        log.info("充电价格设置")
        lp.find(self.price_setting).click()
        lp.find(self.add_power_button).click()
        lp.find(self.confirm_button).click()
        # lp.find(self.confirm_button).click()
        log.info("充电模式设置")
        lp.find(self.charging_mode).click()
        lp.find(self.confirm_button).click()
        # 待咨询目前适用哪种充电桩后补充相关用例
        return self

    def submit(self):
        """提交按钮"""
        lp = BasePage(self.driver)
        log.info("提交确认")
        lp.find(self.submit_button).click()
        lp.find(self.i_know_button).click()
        sleep(1)
        self.driver.swipe(self.width*0.5,
                          self.height*0.4,
                          self.width*0.5,
                          self.height*0.7
                          )
        return self

    def click_base_information(self):
        """进入设备详情点击'基础信息'"""
        lp = BasePage(self.driver)
        log.info("点击'基础信息'")
        lp.find(self.base_information).click()
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.6
                          )
        return self

    def edit_change_nqt(self):
        """更换NQT二维码"""
        lp = BasePage(self.driver)
        log.info("更换NQT")
        lp.find(self.change_nqt).click()
        lp.find(self.photo_select).click()
        # 此NQT二维码坐标只适用于HUAWEI nova3手机，其他机型需要重新适配
        self.driver.tap([(936, 268), (1080, 412)])
        lp.find(self.confirm_button_after_photo).click()
        return self

    def edit_change_imei(self):
        """更换IMEI二维码"""
        lp = BasePage(self.driver)
        log.info("更换IMEI")
        lp.find(self.change_imei).click()
        lp.find(self.photo_select).click()
        # 此IMEI二维码坐标只适用于HUAWEI nova3手机，其他机型需要重新适配
        self.driver.tap([(208, 632), (352, 776)])
        lp.find(self.confirm_button_after_photo).click()
        return self

    def edit_price(self):
        """修改价格"""
        lp = BasePage(self.driver)
        log.info("修改充电桩价格")
        lp.find(self.change_price).click()
        lp.find(self.edit_price_button).click()
        ele = lp.find(self.price_input_box)
        ele_text = ele.get_attribute("text")
        ele.click()
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("0.3")
        lp.find(self.confirm_button).click()
        lp.find(self.confirm_button).click()
        return self

    def edit_change_charging_port(self):
        """修改充电口"""
        lp = BasePage(self.driver)
        log.info("修改充电口")
        lp.find(self.change_charging_mouth).click()
        lp.find(self.charging_mouth_select).click()
        lp.find(self.confirm_button).click()
        return self

    def edit_change_charging_way(self):
        """修改充电模式"""
        pass
        return self

    def edit_charging_pile_name(self):
        """编辑设备名"""
        lp = BasePage(self.driver)
        log.info("修改充电桩设备名称")
        lp.find(self.edit_device_name).click()
        ele = lp.find(self.edit_device_name_input)
        ele_text = ele.get_attribute("text")
        ele.click()
        for i in range(len(ele_text)):
            self.driver.keyevent(67)
        ele.send_keys("测试充电桩1")
        lp.find(self.confirm_button).click()
        return self

    def edit_charging_pile_belong(self):
        """设备转移"""
        lp = BasePage(self.driver)
        log.info("设备转移")
        lp.find(self.device_transfer).click()
        lp.find(self.shop_select).click()
        lp.find(self.transfer_confirm).click()
        return self

    def edit_advanced_setting_stop_button(self):
        """更改自停开关"""
        lp = BasePage(self.driver)
        lp.find(self.edit_stop_switch).click()
        # 此坐标只适用于redmi note7手机，其他机型需要重新适配
        self.driver.tap([(619, 1644), (1066, 1771)])
        lp.find(self.advanced_setting_stop_submit).click()
        return self

    def edit_advanced_setting_mix_power(self):
        """更改单路最大功率"""
        lp = BasePage(self.driver)
        lp.find(self.advanced_mix_power).send_keys("2")
        lp.find(self.advanced_submit_button).click()
        return self

    def edit_advanced_setting_stop_param(self):
        """更改充满自停参数"""
        lp = BasePage(self.driver)
        lp.find(self.advanced_stop_time).send_keys("2")
        lp.find(self.advanced_stop_power).send_keys("2")
        lp.find(self.advanced_setting_param_submit).click()
        return self

    def edit_advanced_setting_break(self):
        """更改空载断电设置"""
        lp = BasePage(self.driver)
        lp.find(self.advanced_setting_break_time).send_keys("2")
        lp.find(self.advanced_setting_break_power).send_keys("2")
        lp.find(self.advanced_setting_break_submit).click()
        return self

    def edit_advanced_setting_mix_charging_time(self):
        """更改最大充电时间"""
        lp = BasePage(self.driver)
        lp.find(self.advanced_setting_mix_charging_time).send_keys("2")
        lp.find(self.advanced_setting_mix_charging_submit).click()
        return self

    def edit_advanced_setting_mix_temperature(self):
        """更改上报温度阈值"""
        lp = BasePage(self.driver)
        lp.find(self.advanced_setting_mix_temperature).send_keys("2")
        lp.find(self.advanced_setting_mix_temperature_submit).click()
        return self

    def edit_advanced_setting_prevent_people(self):
        """更改防扰民设置"""
        lp = BasePage(self.driver)
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.1
                          )
        lp.find(self.advanced_setting_prevent_start_time).send_keys("10")
        lp.find(self.advanced_setting_prevent_finish_time).send_keys("10")
        lp.find(self.advanced_setting_normal_volume).send_keys("2")
        lp.find(self.advanced_setting_prevent_volume).send_keys("3")
        lp.find(self.advanced_setting_prevent_people_submit).click()
        return self

    def delete_device(self):
        """删除新增充电桩"""
        lp = BasePage(self.driver)
        log.info("删除充电桩")
        lp.find(self.iv_search_single).click()
        lp.find(self.delete_device_button).click()
        lp.find(self.confirm_button1).click()
        lp.find(self.i_know_button).click()
        return self








