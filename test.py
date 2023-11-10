# import requests
# from bs4 import BeautifulSoup

# # URL of Yahoo Finance's forex page
# url = "https://finance.yahoo.com/currencies"

# # Send an HTTP GET request to the URL
# response = requests.get(url)

# # Parse the HTML content of the page using BeautifulSoup
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find the table containing forex trading pairs
# forex_table = soup.find('table', {'class': 'W(100%)'})

# # Extract forex pairs from the table
# forex_pairs = []
# for row in forex_table.find_all('tr')[1:]:  # Skip the header row
#     columns = row.find_all('td')
#     base_currency = columns[0].text
#     quote_currency = columns[1].text
#     forex_pair = f"{base_currency}/{quote_currency}"
#     forex_pairs.append(forex_pair)

# # Print the list of forex trading pairs
# for pair in forex_pairs:
#     print(pair)
aVal = 5
bVal = 10
cVal = 12
max(aVal, bVal, cVal)

import re

# The text containing the values
text = """
get_StochasticRelitiveStrengthIndex(df, 366, 3, 1017)
get_StochasticRelitiveStrengthIndex(df, 161, 3, 316)
get_StochasticRelitiveStrengthIndex(df, 370, 3, 218)
get_StochasticRelitiveStrengthIndex(df, 459, 2, 251)
get_StochasticRelitiveStrengthIndex(df, 217, 5, 774)
get_StochasticRelitiveStrengthIndex(df, 527, 7, 482)
get_StochasticRelitiveStrengthIndex(df, 625, 11, 400)
get_StochasticRelitiveStrengthIndex(df, 664, 4, 265)
get_StochasticRelitiveStrengthIndex(df, 301, 7, 325)
get_StochasticRelitiveStrengthIndex(df, 264, 3, 159)
get_StochasticRelitiveStrengthIndex(df, 114, 3, 413)
get_StochasticRelitiveStrengthIndex(df, 217, 3, 343)
get_StochasticRelitiveStrengthIndex(df, 313, 6, 160)
get_StochasticRelitiveStrengthIndex(df, 304, 7, 253)
get_StochasticRelitiveStrengthIndex(df, 348, 7, 186)
get_StochasticRelitiveStrengthIndex(df, 348, 4, 445)
get_StochasticRelitiveStrengthIndex(df, 249, 4, 346)
get_StochasticRelitiveStrengthIndex(df, 649, 10, 425)
get_StochasticRelitiveStrengthIndex(df, 206, 4, 186)
get_StochasticRelitiveStrengthIndex(df, 161, 3, 316)
get_StochasticRelitiveStrengthIndex(df, 203, 7, 65)
get_StochasticRelitiveStrengthIndex(df, 307, 5, 186)
get_StochasticRelitiveStrengthIndex(df, 700, 4, 136)
get_StochasticRelitiveStrengthIndex(df, 306, 3, 152)
get_StochasticRelitiveStrengthIndex(df, 948, 2, 531)
get_StochasticRelitiveStrengthIndex(df, 547, 8, 517)
get_StochasticRelitiveStrengthIndex(df, 310, 6, 179)
get_StochasticRelitiveStrengthIndex(df, 433, 4, 155)
get_StochasticRelitiveStrengthIndex(df, 323, 5, 139)
get_StochasticRelitiveStrengthIndex(df, 278, 6, 157)
get_StochasticRelitiveStrengthIndex(df, 964, 3, 495)
get_StochasticRelitiveStrengthIndex(df, 282, 6, 275)
get_StochasticRelitiveStrengthIndex(df, 227, 6, 412)
get_StochasticRelitiveStrengthIndex(df, 295, 8, 179)
get_StochasticRelitiveStrengthIndex(df, 386, 15, 261)
get_StochasticRelitiveStrengthIndex(df, 236, 4, 219)
get_StochasticRelitiveStrengthIndex(df, 32, 1302, 876)
get_StochasticRelitiveStrengthIndex(df, 255, 298, 15)
get_StochasticRelitiveStrengthIndex(df, 1217, 138, 52)
get_StochasticRelitiveStrengthIndex(df, 686, 4, 984)
get_StochasticRelitiveStrengthIndex(df, 321, 7, 150)
get_StochasticRelitiveStrengthIndex(df, 10, 130, 148)
get_StochasticRelitiveStrengthIndex(df, 230, 20, 860)
get_StochasticRelitiveStrengthIndex(df, 401, 4, 272)
get_StochasticRelitiveStrengthIndex(df, 595, 4, 830)
get_StochasticRelitiveStrengthIndex(df, 886, 2, 551)
get_StochasticRelitiveStrengthIndex(df, 320, 10, 599)
get_StochasticRelitiveStrengthIndex(df, 401, 11, 223)
get_StochasticRelitiveStrengthIndex(df, 521, 9, 238)
"""

# Use regular expressions to extract the numbers
matches = re.findall(r'(\d+), (\d+), (\d+)', text)

# Convert the matched values to tuples and store them in a list
result = [(int(match[0]), int(match[1]), int(match[2])) for match in matches]

print(result)

f = open("test.txt", 'r')
val = f.readline()
counter = 0
while val:
    counter+=1
    print(f"stochRSIK{counter}, stochRSID{counter} = {val.strip()}")
    val = f.readline()



