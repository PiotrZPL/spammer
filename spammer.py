import pyautogui, time, random
time.sleep(10)
wyrazy = []

for i in range(150):
    slow = ""
    for k in range(random.randint(5, 15)):
        a = random.randint(97,122)
        w = chr(a)
        slow = slow + w
    wyrazy = wyrazy + [slow]
    

for j in wyrazy:
    pyautogui.typewrite(j)
    pyautogui.press("enter")
    time.sleep(0.2)
#    print(j)
