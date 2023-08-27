import pyautogui
import time
from functions.GrabData import GrabCurrentData
import pandas as pd
# time.sleep(3)
# print(pyautogui.position())


symbol = "EURUSD"
data = GrabCurrentData(symbol)
from datetime import datetime

timestamp1 = "2023-07-30 09:45"
timestamp2 = "2023-08-02 21:05"

# Convert timestamps to datetime objects
datetime1 = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M")
datetime2 = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M")

# Calculate the time difference in seconds
time_difference = (datetime2 - datetime1).total_seconds()

print("Time difference in seconds:", time_difference)

f = open('documents/data.txt', 'w')
