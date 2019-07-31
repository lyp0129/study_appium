# coding:utf-8


from configparser import ConfigParser


class Readini:
    '''
    构造方法，读取配置文件的地址
    self.vlaue = self.get_data() 直接获取到configParser对象，使用里面的方法
    '''

    def __init__(self, path=None):
        if path == None:
            self.path = '/Users/luyunpeng/PycharmProjects/study_appium/config/localelment.ini'
        else:
            self.path = path
        self.vlaue = self.get_data()

    def get_data(self):
        config = ConfigParser()
        config.read(self.path)
        return config

    '''
    ini文件格式：
    [xx]
    a=b
    
    key_ini:xx
    key=a
    
    '''

    def get_value(self, key_ini, key):

        try:
            value = self.vlaue.get(key_ini, key)
        except IOError:
            value = None

        return value


if __name__ == '__main__':
    test = Readini()
    a = test.get_value("login_element", "user")
    print(a)
