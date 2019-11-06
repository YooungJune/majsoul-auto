import pyautogui
import time
import random
import num

xunmi=pyautogui.locateAllOnScreen("xunmi.png")
if xunmi != None:
            pyautogui.moveTo(num.duanweichang)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(num.sanrendong)
            pyautogui.click()
            pyautogui.moveTo(num.ziliao)
            pyautogui.click()

for i in range(2500000):
    a=random.random()/3
    time.sleep(a)
    dapai=None
    pon=None
    richi=None
    skip=None
    

    pyautogui.moveTo(num.duanweichang)
    if (i % 50)==0:
        queding=None
        wangluo=None
        over=None
        
        queding=pyautogui.locateCenterOnScreen('queding.png')
        wangluo=pyautogui.locateCenterOnScreen('wangluo.png')
        over=pyautogui.locateCenterOnScreen('over.png')

        if queding != None:
            pyautogui.moveTo(queding)#终局刷新网页
            time.sleep(1)
            pyautogui.click()
            time.sleep(10)
            pyautogui.click()
            time.sleep(30)
            
            xunmi=pyautogui.locateAllOnScreen("xunmi.png")
            if xunmi != None:
                pyautogui.moveTo(num.duanweichang)
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(num.sanrendong)
                pyautogui.click()
                pyautogui.moveTo(num.ziliao)
                pyautogui.click()

        if wangluo != None:
            pyautogui.moveTo(num.refresh)
            pyautogui.click()
            pyautogui.moveTo(num.duanweichang)

        if over != None:
            pyautogui.moveTo(num.refresh)
            pyautogui.click()
            pyautogui.moveTo(num.duanweichang)
    
    richi=pyautogui.locateCenterOnScreen('richi.png')#能否立直牌

    if richi == None:  #不能立直
        pon=pyautogui.locateCenterOnScreen('pon.png')
        if pon == None: #没有碰
            pyautogui.moveTo(1251, 829)
            pyautogui.click()
            pyautogui.moveTo(num.duanweichang)
        if pon != None: #能碰
            pyautogui.moveTo(pon)
            time.sleep(a)
            pyautogui.click()
        dapai=pyautogui.locateCenterOnScreen('S4.png')#判断绿色牌
        if dapai != None:
            pyautogui.moveTo(dapai)
            time.sleep(a)
            pyautogui.click()
                      
        pyautogui.moveTo(num.duanweichang)
        pyautogui.click()
        time.sleep(a)
        pyautogui.click()
        time.sleep(a)
        pyautogui.click()

        if (i % 10)/100 >a:
            pyautogui.moveTo(num.biaoqing)
            pyautogui.click()
            time.sleep(a)

            pyautogui.moveTo(num.biaoqing1)
            pyautogui.click()

                    
    else:  #立直
        dapai=pyautogui.locateCenterOnScreen('S4.png')#判断绿色牌
        pyautogui.moveTo(richi)
        time.sleep(a)
        pyautogui.click()
        pyautogui.moveTo(dapai)
        time.sleep(a)
        pyautogui.click()

        pyautogui.moveTo(num.biaoqing)
        pyautogui.click()
        time.sleep(a)
        pyautogui.moveTo(num.biaoqing3)
        pyautogui.click()

            

    

    

