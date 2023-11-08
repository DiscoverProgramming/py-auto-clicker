import pyautogui
import time
import threading

LEN = input('Time(seconds): ')
DELAY = input('Delay(seconds): ')
CPS = input('CPS: ')

input('ready?')

time.sleep(int(DELAY))

stop = False

def start():
    pyautogui.PAUSE = 0
    while True:
        if not stop:
            pyautogui.leftClick()
            time.sleep(1 / float(CPS))
        else:
            break

def wait():
    global stop
    time.sleep(int(LEN))
    stop = True


threading.Thread(target=start).start()
wait()
