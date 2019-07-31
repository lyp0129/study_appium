# coding:utf-8

import os

'''
获取devices
'''


class GetDevices:

    def get_deviceslist(self):
        a = os.popen("adb devices").readlines()  # 获取,设备信
        if a is not None:
            c = ''.join(a).split("\n")  # 列表转字符串，字符串去除\n
            d = []
            last_devices = []
            for i in c:
                if i == "List of devices attached":
                    continue
                d.append(i)

            devices_list = [i for i in d if i != '']  # 删除列表空值

            for i in devices_list:
                last_devices.append(i.replace('\tdevice', ''))  # "\tdevice"替换 ''

            return last_devices
        else:
            print("没有设备信息")


if __name__ == '__main__':
    test = GetDevices()
    a = len(test.get_deviceslist())
    print(test.get_deviceslist())
    print(a)
