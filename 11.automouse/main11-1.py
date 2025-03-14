import pyautogui
import pyperclip
import threading
import schedule
import os
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def send_masaage():
    threading.Timer(10, send_masaage).start()

    picPosition = pyautogui.locateOnScreen('pic1.png')
    print(picPosition)

    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy("이 메세지는 자동으로 보내는 메세지 입니다!~")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2.0)
    pyautogui.write(["enter"])
    time.sleep(2.0)
    pyautogui.write(["escape"])
    time.sleep(1.0)

send_masaage()