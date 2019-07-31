import unittest
import HTMLTestRunner


class TestMathFunc(unittest.TestCase):

    def test_01(self):
        self.assertEqual(4, 5)

    def test_02(self):
        self.assertEqual(5, 5)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMathFunc('test_01'))
    suite.addTest(TestMathFunc('test_02'))
    filepath = '../report/result.html'
    ftp = open(filepath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='welcome to this web')
    runner.run(suite)
