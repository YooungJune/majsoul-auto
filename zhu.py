import pyautogui
import num
import time
import random


def showit():
    a=random.random()/3
    time.sleep(a)
    dapai=None
    richi=None
    richi=pyautogui.locateCenterOnScreen('richi.png')#能否立直牌
    if richi == None:
        dapai=pyautogui.locateCenterOnScreen('S4.png')#判断绿色牌
        pyautogui.moveTo(dapai)
        time.sleep(a)
        pyautogui.click()
    else:
        pyautogui.moveTo(richi)
        time.sleep(a)
        pyautogui.click()
        xp=375
        for i in range(14):
            richi2=(xp,960)
            pyautogui.moveTo(richi2)
            time.sleep(a)
            pyautogui.click()
            xp=xp+82
        pyautogui.moveTo(num.biaoqing)
        pyautogui.click()
        time.sleep(a)
        pyautogui.moveTo(num.biaoqing2)
        pyautogui.click()



def emoji():
    a=random.random()/3
    pyautogui.moveTo(num.biaoqing)
    pyautogui.click()
    time.sleep(a)
    b=int((a*30) % 10)
    c='num.biaoqing'+str(b)
    pyautogui.moveTo(eval(c))    
   


def restart():
    queding=pyautogui.locateCenterOnScreen('queding.png')
    if queding != None:
        pyautogui.moveTo(num.refresh)#终局刷新网页
        pyautogui.click()


def startgame():
    xunmi=pyautogui.locateAllOnScreen("xunmi.png")
    if xunmi!= None:
        pyautogui.moveTo(num.duanweichang)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.moveTo(num.ziliao)
        pyautogui.click()
