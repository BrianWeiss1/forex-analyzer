import pyautogui
import time
time.sleep(5)
for i in range(25):
    pyautogui.write(f"count{i} = 0\n")