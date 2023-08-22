
# from functions.RSI import main
from src.functions.AMX import findADXslope
# from src.functions.specialFunctions import findLocation

# symbol = "APPL"
# # main("APPL", 5)
# findLocation(5)
# reset_location = (1459, 494)
# goodLocation = (1443, 484)
# badlocation = (1455, 625)

value = (findADXslope("EURJPY", 5))
# print(key[0:5])
print(value)
