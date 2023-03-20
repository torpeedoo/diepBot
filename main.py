
from pyautogui import * 
import pyautogui 
import numpy as np
import time 
import keyboard 
import random
import win32api, win32con
import math

playerPos = (1442, 295)

def search(startWidth, startHeight, endWidth, endHeight, xJump, yJump):
    for x in range(math.ceil(startWidth*0.5), endWidth, xJump):
        for y in range(math.ceil(startHeight*0.5), endHeight, yJump):

            r, g, b = pic.getpixel((x, y))

            if r == 255 and g == 232 and b == 105:
                return [x, y], True
    
    return [], False
                
            
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    foodPosition = []
    pic = pyautogui.screenshot(region=(1060, 88, 729, 328))

    found = False

    width, height = pic.size

    foodPosition, found = search(width, height, width, height, 5, 5)

    if not found:
        foodPosition, found = search(width, height, width, 0, 5, -5)
    elif not found:
        foodPosition, found = search(width, height, 0, height, -5, 5)
    elif not found:
        foodPosition, found = search(width, height, 0, 0, -5, -5)
    else:
        print("none detected, moving")
        pyautogui.keyDown("w")
        time.sleep(5)
        pyautogui.keyUp("w")
        

    if found: click(foodPosition[0]+1060, foodPosition[1]+88)

    print(foodPosition)





#window position (1060, 88)
#size (1789, 416)

#255, 232, 105 - yellow
