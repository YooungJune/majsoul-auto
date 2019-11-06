import pyautogui
import time
a=0.5
xp=375
for i in range(14):
    richi2=(xp,960)
    pyautogui.moveTo(richi2)
    time.sleep(a)
    pyautogui.click()
    xp=xp+82