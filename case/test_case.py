import unittest
import HTMLTestRunner
from business.login_business import LoginBusiness
from util.server import Server
import multiprocessing
from util.write_user_commed import WriteUserCommand
import time
import sys


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = LoginBusiness(parames)

    def test_01(self):
        flag = self.login.login_pass()
        self.assertTrue(flag)

    def test_02(self):
        # self.login = LoginBusiness(parames)
        flag = self.login.login_pass()
        self.assertTrue(flag)


def appium_init():
    server = Server()
    server.main()


def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01", parame=i))
    suite.addTest(CaseTest("test_02", parame=i))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    filepath = "../report/result" + str(i) + ".html"
    ftp = open(filepath, 'wb')
    HTMLTestRunner.HTMLTestRunner(stream=ftp, title='welcome to this web').run(suite)


def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count


if __name__ == '__main__':
    appium_init()
    threads = []
    for i in range(get_count()):
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
