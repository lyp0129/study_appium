# coding:utf-8

import yaml
from util.get_devices import GetDevices
from util.check_port import CheckPort


class WriteUserCommand:

    def get_devices(self):
        get_devices = GetDevices()
        devices = get_devices.get_deviceslist()
        return devices

    def read(self, key, value):
        with open("../yamlll/test.yaml") as fp:
            content = yaml.load(fp.read(), Loader=yaml.FullLoader)
            value = content[key][value]
            return value
            # print(value)

    def join_data(self, i, device, bp, port):
        data = {"user_info_" + str(i): {"deviceName": device, "bp": bp, "port": port}}
        return data

    def write(self, i, device, bp, port):
        data = self.join_data(i, device, bp, port)
        with open("../yamlll/test.yaml", "a") as fp:
            yaml.dump(data, fp)

    def clear_data(self):
        with open("../yamlll/test.yaml", "w") as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        with open("../yamlll/test.yaml") as fp:
            content = yaml.load(fp.read(), Loader=yaml.FullLoader)
        return len(content)


if __name__ == '__main__':
    test = WriteUserCommand()
    print(test.get_file_lines())
    # test.read(key="user_info_0", value="bp")
    # test.get_port()
    # test.write2(data1)
