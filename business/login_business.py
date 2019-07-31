# coding:utf-8

from handle.login_handle import LoginHandle
import time


class LoginBusiness:

    def __init__(self, i):
        self.login_handle = LoginHandle(i)
        # self.login_handle = LoginHandle()

    def login_pass(self):
        self.login_handle.click_my_element()
        self.login_handle.click_login()
        self.login_handle.send_keys_login("13261737595")
        self.login_handle.click_enter()
        self.login_handle.click_verification_code_8()
        time.sleep(1)
        self.login_handle.click_verification_code_9()
        time.sleep(1)
        self.login_handle.click_verification_code_7()
        time.sleep(1)
        self.login_handle.click_verification_code_5()
        time.sleep(1)
        self.login_handle.click_verification_code_7()
        time.sleep(1)
        self.login_handle.click_verification_code_6()
        time.sleep(1)
        nickname_element = self.login_handle.get_nickname()
        if nickname_element:
            return True
        else:
            print("打印一下失败截图")
            timestr = time.strftime("%Y-%m-%d_%H_%M_%S")  # 定义截图名称即时间戳，字符串类型
            self.login_handle.login_page.driver.get_screenshot_as_file(
                "..jpg/screenshot_" + timestr + ".png")
            return False


if __name__ == '__main__':
    test = LoginBusiness(0)
    test.login_pass()
