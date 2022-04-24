import pyautogui
from time import sleep

firstCord = 56280100
secCord = 38080900
step = 190
stepsInRow = 100
nrOfClients = 6
direction = False

sleep(3)


def enterInfo(x, y, first, second):
    pyautogui.moveTo(x, y)
    pyautogui.click()

    pyautogui.moveRel(486, 82)
    pyautogui.doubleClick()
    pyautogui.typewrite(str(first / 1000000))

    pyautogui.moveRel(100, 0)
    pyautogui.doubleClick()
    pyautogui.typewrite(str(second / 1000000))

    pyautogui.moveRel(65, 0)
    pyautogui.click()

    pyautogui.moveRel(-45, 500)
    pyautogui.click()


for a in range(stepsInRow):
    temp1 = 15
    temp2 = 452
    firstCord = 56280100
    for c in range(nrOfClients):
        enterInfo(temp1, temp2, firstCord, secCord)
        firstCord = firstCord + step
        temp1 = temp1 + 28
        temp2 = temp2 - 30
        sleep(0.2)

    # asteptat sa se mineze
    sleep(6)

    secCord = secCord + 350
