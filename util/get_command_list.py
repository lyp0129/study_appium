from util.check_port import CheckPort
from util.get_devices import GetDevices
from util.write_user_commed import WriteUserCommand


class Get_command:

    def create_command_list(self, i):
        w = WriteUserCommand()
        port = CheckPort()  # 实例化获取port对象
        get_devices = GetDevices()  # 实例化获取devices对象
        devices_list = get_devices.get_deviceslist()  # 获取设备信息列表
        port_list = port.create_port_list(4700, devices_list)  # 根据设备列表生成可用端口列表
        bootstrap_port_list = port.create_port_list(4900, devices_list)  # 根据设备列表生成可用设备端口列表
        command_list = []
        command = 'appium -p' + str(port_list[i]) + ' -bp ' + str(bootstrap_port_list[i]) + ' -U ' + \
                  devices_list[i]
        command_list.append(command)
        # print(devices_list)
        w.write(i, devices_list[i], str(bootstrap_port_list[i]), str(port_list[i]))
        return command_list


if __name__ == '__main__':
    test = Get_command()
    print(test.create_command_list(0))
