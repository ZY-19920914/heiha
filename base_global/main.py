from time import sleep
from base_global.base_page import BasePage
from base_global.base_management import BaseroomManagement
from base_global.base_log import log


class Main(BasePage):

    def goto_all_management(self):
        lp = BasePage(self.driver)
        """点击“全部应用”按钮进入"""
        self.driver.swipe(self.width*0.5,
                          self.height*0.9,
                          self.width*0.5,
                          self.height*0.1
                          )
        try:
            log.info("点击'全部应用'")
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("全部应用")').click()
        except Exception as e:
            print("点击'全部应用'失败，原因是：{}".format(e))
            self.driver.get_screenshot_as_file(lp.screenshot_filepath())
        return BaseroomManagement(self.driver)