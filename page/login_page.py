# coding:utf-8

from get_driver.driver import Werdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

'''
page层，元素层
'''


class LoginPage:

    def __init__(self, i):
        driver = Werdriver()
        self.driver = driver.get_driver(i)
        # self.driver = driver.get_driver()

    # 获取首页tab我的按钮元素
    def get_my_element(self):
        time.sleep(3)
        yeye = self.driver.find_element_by_id("com.charminginsurance.app:id/main_tab")
        father = yeye.find_elements_by_class_name("android.widget.LinearLayout")
        return father[4]

    # 获取"登陆"按钮
    def get_click_login(self):
        click_login_elemnet = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'com.charminginsurance.app:id/user_header_hint_tv')))
        return click_login_elemnet

    # 获取输入"手机号码"输入框
    def get_phonenumber(self):
        phonenumber_elemnet = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'com.charminginsurance.app:id/login_mobile_et')))
        return phonenumber_elemnet

    # 获取"确认"按钮元素
    def get_enter(self):
        enter_element = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'com.charminginsurance.app:id/login_go_bt')))

        return enter_element

    # 获取"验证码"输入框元素
    def get_verification_code_8(self):
        code_8_element = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'com.charminginsurance.app:id/t9_key_8')))
        return code_8_element

        # 获取"验证码"输入框元素

    def get_verification_code_9(self):
        code_9_element = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'com.charminginsurance.app:id/t9_key_9')))
        return code_9_element

    def get_verification_code_7(self):
        code_7_element = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'com.charminginsurance.app:id/t9_key_7')))
        return code_7_element

    def get_verification_code_5(self):
        code_5_element = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'com.charminginsurance.app:id/t9_key_5')))
        return code_5_element

    def get_verification_code_6(self):
        code_6_element = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'com.charminginsurance.app:id/t9_key_6')))
        return code_6_element

    def get_nickname(self):
        nickname_element = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'com.charminginsurance.app:id/user_header_nickname_tv')))
        return nickname_element


if __name__ == '__main__':
    pass
    # test = LoginPage()
