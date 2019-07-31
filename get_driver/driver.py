# coding:utf-8


from appium import webdriver
from util.write_user_commed import WriteUserCommand


class Werdriver:

    def get_driver(self, i):
        write_file = WriteUserCommand()
        devices = write_file.read(key="user_info_" + str(i), value="deviceName")
        port = write_file.read(key="user_info_" + str(i), value="port")
        configure = {
            "platformName": "Android",
            "deviceName": devices,
            # "deviceName": "PBV0216922007470",
            "app": "/Users/luyunpeng/Downloads/ci_v1.5.0_2019-07-18_16-35_qa.apk",
            "noReset": "true"

        }
        driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub", configure)
        # driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", configure)
        print(port)
        return driver


if __name__ == '__main__':
    test = Werdriver()
    test.get_driver(0)
