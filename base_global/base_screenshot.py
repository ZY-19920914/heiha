import os
import time


class Screenshots:

    def screenshot_filepath(self):
        """用例失败截图"""
        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        tm = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screen_path = base_path + '/screenshots/' + day + tm + '.png'
        return screen_path