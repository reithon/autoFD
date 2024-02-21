import pyautogui
from time import sleep
import numpy as np
import cv2
from random import randint


DEBUG = False
info = 'init'
mark = '+'


def switchMark():
    global mark
    mark = '-' if mark == '+' else '+'


def log(buf):
    global info
    global mark
    if buf != info:
        info = buf
        print(f'\n  {info}', end='')
    else:
        print(f'\r{mark}', end='')
        switchMark()


def match(template_name, ac=0.85):
    
    img = pyautogui.screenshot()
    open_cv_image = np.array(img)

    img_gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(f'./{template_name}.png', 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    w, h = template.shape[::-1]

    if DEBUG:
        print(max_val, max_loc)

    if max_val < ac:
        return None

    return w // 2 + max_loc[0], h // 2 + max_loc[1]


def start():
    pos = match('start')
    pyautogui.click(pos[0], pos[1], duration=0.1)


def wait(sec):
    sleep(sec / 2)


def ready_to_cum():
    return match('cum')


def ready_to_start():
    return match('start')


def ready_to_finish():
    return match('finish')


def is_red():
    return match('red')


def cum():
    win = pyautogui.getWindowsWithTitle('FallenDoll')[0]
    x, y = win.left, win.top
    pyautogui.click(x + 429, y + 852, duration=0.2)


def click1():
    choice = f'{randint(1, 1)}'
    pyautogui.press(choice)
    log(f'大力抽插{choice}')


def finish():
    pos = match('finish')
    pyautogui.click(pos[0], pos[1], duration=0.2)


def give():
    win = pyautogui.getWindowsWithTitle('FallenDoll')[0]
    x, y = win.left, win.top
    pyautogui.moveTo(x + 339, y + 332)
    pyautogui.leftClick()
    wait(0.2)
    pyautogui.moveTo(x + 94, y + 375)
    wait(0.2)
    pyautogui.leftClick()
    wait(0.2)
    pyautogui.leftClick()
    wait(0.2)
    pyautogui.leftClick()
    wait(0.2)


def loop():
    while not ready_to_start():
        log('未找到开始')
        wait(0.2)
    while ready_to_start():
        start()
        pyautogui.moveRel(50, 50)
        log('点击开始')
        wait(0.2)

    while not ready_to_cum():
        log('未能cum')
        # if is_red():
        #     log('红了')
        #     click1()
        wait(0.2)
    while ready_to_cum():
        cum()
        log('cum')
        wait(0.2)

    while not ready_to_finish():
        log('等待结束')
        wait(0.2)
    while ready_to_finish():
        finish()
        pyautogui.moveRel(50, 50)
        log('结束')
        wait(0.2)
    give()


if __name__ == '__main__':
    while True:
        loop()
