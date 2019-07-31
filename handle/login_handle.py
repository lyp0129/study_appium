# coding:utf-8

from page.login_page import LoginPage

import time

'''
handle 操作层
'''


class LoginHandle:
    def __init__(self, i):
        self.login_page = LoginPage(i)
        # self.login_page = LoginPage()

    # 点击首页底部tab我的按钮
    def click_my_element(self):
        self.login_page.get_my_element().click()

    # 在"我的"页面点击"登陆"按钮
    def click_login(self):
        self.login_page.get_click_login().click()

    # 输入"登陆手机号"
    def send_keys_login(self, key):
        self.login_page.get_phonenumber().send_keys(key)

    # 点击"确认"按钮
    def click_enter(self):
        self.login_page.get_enter().click()

    # 输入验证码
    def click_verification_code_8(self):
        self.login_page.get_verification_code_8().click()

    # 输入验证码
    def click_verification_code_9(self):
        self.login_page.get_verification_code_9().click()

    # 输入验证码
    def click_verification_code_7(self):
        self.login_page.get_verification_code_7().click()

    # 输入验证码
    def click_verification_code_5(self):
        self.login_page.get_verification_code_5().click()

    # 输入验证码
    def click_verification_code_6(self):
        self.login_page.get_verification_code_6().click()

    def get_nickname(self):
        nickname_element = self.login_page.get_nickname()
        if nickname_element:
            return True
        else:
            return False


if __name__ == '__main__':
    pass
    # test = LoginHandle()
