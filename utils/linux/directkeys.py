import ctypes
import time
from pynput.keyboard import Key, Controller, KeyCode

keyboard = Controller()

# Actuals Functions

def PressKey(hexKeyCode):
    keyboard.release(KeyCode.from_vk(hexKeyCode))

def ReleaseKey(hexKeyCode):
    keyboard.release(KeyCode.from_vk(hexKeyCode))

if __name__ == '__main__':
    PressKey(0x11)
    time.sleep(1)
    ReleaseKey(0x11)
    time.sleep(1)
