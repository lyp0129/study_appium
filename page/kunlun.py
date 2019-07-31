# coding:utf-8

# from get_driver.driver import Werdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from slide.Slide_Method import Slide
from get_driver.test_driver import Werdriver
import time

'''
page层，元素层
'''


class LoginPage:

    def __init__(self):
        driver = Werdriver()
        self.driver = driver.get_driver()
        time.sleep(5)
        self.slide = Slide(self.driver)

    # 获取首页tab"卓铭保险按钮"
    def get_charming_element(self):
        time.sleep(3)
        yeye = self.driver.find_element_by_id("com.charminginsurance.app:id/main_tab")
        father = yeye.find_elements_by_class_name("android.widget.LinearLayout")
        father[1].click()
        # return father[0]

    # 首页下滑
    def HomePage_DownSlide(self):
        time.sleep(1)
        self.slide.Up_slide()
        time.sleep(1)
        self.slide.Up_slide()
        time.sleep(1)
        self.slide.Up_slide()

    # 获取首页tab"卓铭保险按钮"
    def kunlun_element(self):
        time.sleep(1)
        phonenumber_elemnet = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, '//*[contains(@text,"昆仑")]'))).click()

        # return phonenumber_elemnet

    def toubao_element(self):
        time.sleep(1)
        phonenumber_elemnet = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, '//*[contains(@text,"我要")]'))).click()


if __name__ == '__main__':
    test = LoginPage()
    test.get_charming_element()
    test.HomePage_DownSlide()
    test.kunlun_element()
    test.toubao_element()
