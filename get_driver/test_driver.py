# coding:utf-8


from appium import webdriver


class Werdriver:

    def get_driver(self):
        configure = {
            "platformName": "Android",
            "deviceName": "PBV0216922007470",
            "app": "/Users/luyunpeng/Downloads/ci_v1.5.0_2019-07-18_16-35_qa.apk",
            "noReset": "true"

        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", configure)

        return driver


if __name__ == '__main__':
    test = Werdriver()
    test.get_driver()
