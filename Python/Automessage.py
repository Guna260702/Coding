import pyautogui
import time

time.sleep(10)

for num in range(100):
    pyautogui.write("Hello")
    pyautogui.press('enter')

print('Script executed successfully')