# coding:utf-8


import time


class Slide:
    def __init__(self, driver):
        self.driver = driver

    def get_window_size(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width, height

    '''左滑动'''

    def Left_Slide(self):
        size = self.get_window_size()  # 返回了一个元祖类型
        start_x = size[0] / 10 * 9
        end_x = size[0] / 10
        y = size[1] / 2
        time.sleep(4)
        self.driver.swipe(start_x, y, end_x, y)

    '''右滑动'''

    def Right_Slide(self):
        size = self.get_window_size()
        start_x = size[0] / 10
        end_x = size[0] / 10 * 9
        y = size[1] / 2
        time.sleep(4)
        self.driver.swipe(start_x, y, end_x, y)

    '''向上滑动'''

    def Up_slide(self):
        size = self.get_window_size()
        x = size[0] / 2
        start_y = size[1] / 10 * 9
        end_y = size[1] / 10
        time.sleep(4)
        self.driver.swipe(x, start_y, x, end_y)

    '''向下滑动'''

    def Down_slide(self):
        size = self.get_window_size()
        x = size[0] / 2
        start_y = size[1] / 10
        end_y = size[1] / 10 * 9
        time.sleep(4)
        self.driver.swipe(x, start_y, x, end_y)

    def slide(self, direction):
        if direction == "Left":
            Left_Slide()

        elif direction == "Right":
            Right_Slide()

        elif direction == "Up":
            Up_slide()
        else:
            Down_slide()


if __name__ == '__main__':
    pass
