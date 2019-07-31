# coding:utf-8


from util.dos import Dos
from util.get_command_list import Get_command
import multiprocessing
from util.get_devices import GetDevices
from util.write_user_commed import WriteUserCommand
import time


class Server:
    '''

    appium -p 4700 -bp 4701 -U LKX7N17C09001728

    check_port生成可用端口
    get_devices 生成设备信息号

    '''

    def __init__(self):
        self.dos = Dos()
        self.get_devices = GetDevices()
        self.device_list = self.get_devices.get_deviceslist()
        self.write_file = WriteUserCommand()
        print(self.device_list)

    # 获取启动命令列表
    def create_command_list(self, i):
        command_list_object = Get_command()
        command_list = command_list_object.create_command_list(i)
        return command_list

    # 杀死进程
    def kill_server(self):
        server_list = self.dos.dos('ps -ef | grep node')
        if len(server_list) > 0:
            self.dos.dos('pkill -f node')

    # 启动服务
    def start_server(self, i):
        start_list = self.create_command_list(i)
        self.dos.dos(start_list[0])

    # 主方法
    def main(self):
        self.kill_server()
        self.write_file.clear_data()
        for i in range(len(self.device_list)):
            appium_start = multiprocessing.Process(target=self.start_server, args=(i,))
            appium_start.start()
        time.sleep(5)


if __name__ == '__main__':
    test = Server()
    # a = test.main()
    test.kill_server()

    # test.main()

    # test.case()
