import pyautogui
import time
pyautogui.FAILSAFE = False
# like for 5 post react
for i in range(0, 5):
    time.sleep(3)
    # command 
    pyautogui.press('j') # j for scrolling
    time.sleep(3)
    pyautogui.press('c') # l for comment
    time.sleep(5)
    pyautogui.write('haha') # comment
    time.sleep(1)
    pyautogui.press('enter') 