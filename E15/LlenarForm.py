import pyautogui,time
from faker import Faker

opt = int(input("Elige una opción: \n1)Marvel \n2)DC \n3)Ambos \n4)Ninguno \n> "))
if opt == 1:
    pyautogui.click(x = 453, y = 437, clicks = 1)
elif opt == 2:
    pyautogui.click(x = 458, y = 478, clicks = 1)
elif opt == 3:
    pyautogui.click(x = 461, y = 521, clicks = 1)
elif opt == 4:
    pyautogui.click(x = 455, y = 559, clicks = 1)

pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite("El unico modo de hacer un gran trabajo es amar lo que haces")
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
opt2 = int(input("Elige una hora: \n1)8AM \n2)9AM \n3)10AM \n4)11AM \n5)12PM \n6)1PM \n7)2PM \n8)3PM \n9)4PM \n10)5PM \n11)6PM \n12)Después de las 7PM \n>"))
if opt2 == 1:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    pyautogui.press('enter')
if opt2 == 2:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    pyautogui.press('down')
    pyautogui.press('enter')
if opt2 == 3:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    for i in range(1,3):
        pyautogui.press('down')
    pyautogui.press('enter')
if opt2 == 4:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    for i in range(1,4):
        pyautogui.press('down')
    pyautogui.press('enter')
if opt2 == 5:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    for i in range(1,5):
        pyautogui.press('down')
    pyautogui.press('enter')
if opt2 == 6:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    for i in range(1,6):
        pyautogui.press('down')
    pyautogui.press('enter')
if opt2 == 7:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    for i in range(1,7):
        pyautogui.press('down')
    pyautogui.press('enter')
if opt2 == 8:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    for i in range(1,8):
        pyautogui.press('down')
    pyautogui.press('enter')
if opt2 == 9:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    for i in range(1,9):
        pyautogui.press('down')
    pyautogui.press('enter')
if opt2 == 10:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    for i in range(1,10):
        pyautogui.press('down')
    pyautogui.press('enter')
if opt2 == 11:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    for i in range(1,11):
        pyautogui.press('down')
    pyautogui.press('enter')
if opt2 == 12:
    pyautogui.click(x = 738, y = 837, clicks = 1)
    for i in range(1,12):
        pyautogui.press('down')
    pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite("falso")
pyautogui.hotkey('altright','q')#@
pyautogui.typewrite("falso.com")
pyautogui.press('tab')
time.sleep(10)
pyautogui.press('enter')
