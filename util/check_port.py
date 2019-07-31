# coding:utf-8
import os
import socket


class CheckPort:

    def net_is_used(self, port, ip='127.0.0.1'):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.connect((ip, port))

            s.shutdown(2)

            return True
        except IOError:

            return False

    def create_port_list(self, start_port, device_list):

        # param start_port,param device_list,return: 生成可用端口

        port_list = []
        if device_list is not None:
            while len(port_list) != len(device_list):
                if self.net_is_used(start_port) is not True:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print("生成可用端口失败")
            return None


if __name__ == '__main__':
    aaa = CheckPort()

    li = [1, 2, 3, 4, 5]
    print(aaa.create_port_list(4722, li))
