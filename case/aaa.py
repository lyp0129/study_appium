import unittest
import HTMLTestRunner
from business.login_business import LoginBusiness
from util.server import Server
import multiprocessing
from util.write_user_commed import WriteUserCommand
import time


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class CaseTest(ParameTestCase):

    @classmethod
    def setUpClass(cls):
        pass
        # print("setUpclass---->", parames)

    def test_01(self):
        print("He is %d" % (parames))
        print("!!!!!!!!!!!!!!")


def get_suite(i):
    print("get_suite里面的", i)
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01", parame=i))
    print(parames)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    for i in range(2):
        t = multiprocessing.Process(target=get_suite, args=(i,))
        t.start()
