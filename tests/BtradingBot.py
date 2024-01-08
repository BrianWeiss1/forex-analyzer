from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import numpy as np
from datetime import datetime
import time
import MetaTrader5 as mt5
# Initialize the bound
mt5.initialize()

# Set the symbol
symbol = "XAUUSD"
import pygame

pygame.init()

sound_file = "message-ringtone-magic.mp3"  # Replace with the path to your sound file
pygame.mixer.music.load(sound_file)

# Set filling mode
filling_type = mt5.symbol_info(symbol).filling_mode

# Set the point
point = mt5.symbol_info(symbol).point

username = 'amiramirmashgh'
password = '1234Asdf'

tv = TvDatafeed(username, password)
