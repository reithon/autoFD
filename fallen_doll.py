import pyautogui
from time import sleep
import numpy as np
import cv2
from time import time


DEBUG = False
info = 'init'
mark = '+'
cumMode = 2
resRate = 1
opTime = time()


def switchMark():
    global mark
    mark = '-' if mark == '+' else '+'


def log(buf):
    global info
    global mark
    global opTime
    if time() - opTime > 120:
        pyautogui.press('1')
        opTime = time()
    if buf != info:
        opTime = time()
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

    x, y = template.shape[0:2]
    template = cv2.resize(template, (int(y * resRate), int(x *resRate)))

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
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.leftClick()
    wait(0.1)
    pyautogui.leftClick()


def wait(sec):
    sleep(sec / 2)


def ready_to_cum():
    return match(f'cum{cumMode}')


def ready_to_start():
    return match('start')


def ready_to_finish():
    return match('finish')


def cum():
    pos = match(f'cum{cumMode}')
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.leftClick()
    wait(0.1)
    pyautogui.leftClick()


def finish():
    pos = match('finish')
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.leftClick()
    wait(0.1)
    pyautogui.leftClick()


def give():
    win = pyautogui.getWindowsWithTitle('FallenDoll')[0]
    x, y = win.left, win.top
    pyautogui.moveTo(x + 339 * resRate, y + 280 * resRate + 35)
    pyautogui.leftClick()
    wait(0.2)
    pyautogui.moveTo(x + 94 * resRate, y + 310 * resRate + 60)
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
        pyautogui.moveRel(50 * resRate, 50 * resRate)
        log('点击开始')
        wait(0.2)

    while not ready_to_cum():
        log('未能cum')
        wait(0.2)
    while ready_to_cum():
        cum()
        pyautogui.moveRel(50 * resRate, 50 * resRate)
        log('cum')
        wait(0.2)

    while not ready_to_finish():
        log('等待结束')
        wait(0.2)
    while ready_to_finish():
        finish()
        pyautogui.moveRel(50 * resRate, 50 * resRate)
        log('结束')
        wait(0.2)
    give()


if __name__ == '__main__':
    while True:
        loop()
