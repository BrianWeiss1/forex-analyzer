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
get_StochasticRelitiveStrengthIndex(df, 78, 3, 46)
get_StochasticRelitiveStrengthIndex(df, 195, 89, 18)
get_StochasticRelitiveStrengthIndex(df, 290, 8, 209)
get_StochasticRelitiveStrengthIndex(df, 114, 3, 58)
get_StochasticRelitiveStrengthIndex(df, 105, 3, 46)
get_StochasticRelitiveStrengthIndex(df, 99, 3, 45)
get_StochasticRelitiveStrengthIndex(df, 290, 3, 214)
get_StochasticRelitiveStrengthIndex(df, 115, 3, 43)
get_StochasticRelitiveStrengthIndex(df, 92, 3, 45)
get_StochasticRelitiveStrengthIndex(df, 103, 2, 53)
get_StochasticRelitiveStrengthIndex(df, 258, 7, 212)
get_StochasticRelitiveStrengthIndex(df, 41, 3, 114)
get_StochasticRelitiveStrengthIndex(df, 52, 4, 262)
get_StochasticRelitiveStrengthIndex(df, 96, 3, 58)
get_StochasticRelitiveStrengthIndex(df, 53, 3, 257)
get_StochasticRelitiveStrengthIndex(df, 84, 4, 43)
get_StochasticRelitiveStrengthIndex(df, 139, 3, 51)
get_StochasticRelitiveStrengthIndex(df, 87, 2, 54)
get_StochasticRelitiveStrengthIndex(df, 53, 3, 269)
get_StochasticRelitiveStrengthIndex(df, 60, 2, 66)
get_StochasticRelitiveStrengthIndex(df, 41, 3, 105)
get_StochasticRelitiveStrengthIndex(df, 182, 11, 296)
get_StochasticRelitiveStrengthIndex(df, 66, 4, 69)
get_StochasticRelitiveStrengthIndex(df, 72, 4, 50)
get_StochasticRelitiveStrengthIndex(df, 223, 8, 266)
get_StochasticRelitiveStrengthIndex(df, 274, 5, 225)
get_StochasticRelitiveStrengthIndex(df, 245, 9, 194)
get_StochasticRelitiveStrengthIndex(df, 66, 3, 61)
get_StochasticRelitiveStrengthIndex(df, 226, 8, 249)
get_StochasticRelitiveStrengthIndex(df, 135, 2, 297)
get_StochasticRelitiveStrengthIndex(df, 58, 3, 97)
get_StochasticRelitiveStrengthIndex(df, 98, 3, 51)
get_StochasticRelitiveStrengthIndex(df, 55, 3, 102)
get_StochasticRelitiveStrengthIndex(df, 180, 11, 268)
get_StochasticRelitiveStrengthIndex(df, 204, 13, 231)
get_StochasticRelitiveStrengthIndex(df, 292, 14, 198)
get_StochasticRelitiveStrengthIndex(df, 245, 12, 188)
get_StochasticRelitiveStrengthIndex(df, 169, 2, 39)
get_StochasticRelitiveStrengthIndex(df, 101, 3, 36)
get_StochasticRelitiveStrengthIndex(df, 197, 3, 290)
get_StochasticRelitiveStrengthIndex(df, 133, 3, 29)
get_StochasticRelitiveStrengthIndex(df, 242, 11, 199)
get_StochasticRelitiveStrengthIndex(df, 70, 5, 43)
get_StochasticRelitiveStrengthIndex(df, 74, 3, 59)
get_StochasticRelitiveStrengthIndex(df, 197, 12, 234)
get_StochasticRelitiveStrengthIndex(df, 115, 3, 35)
get_StochasticRelitiveStrengthIndex(df, 194, 14, 246)
get_StochasticRelitiveStrengthIndex(df, 52, 3, 205)
get_StochasticRelitiveStrengthIndex(df, 43, 3, 90)
get_StochasticRelitiveStrengthIndex(df, 195, 12, 239)
get_StochasticRelitiveStrengthIndex(df, 274, 1, 274)
get_StochasticRelitiveStrengthIndex(df, 42, 3, 96)
get_StochasticRelitiveStrengthIndex(df, 180, 11, 277)
get_StochasticRelitiveStrengthIndex(df, 34, 4, 183)
get_StochasticRelitiveStrengthIndex(df, 66, 3, 28)
get_StochasticRelitiveStrengthIndex(df, 84, 3, 28)
get_StochasticRelitiveStrengthIndex(df, 148, 3, 36)
get_StochasticRelitiveStrengthIndex(df, 34, 4, 178)
get_StochasticRelitiveStrengthIndex(df, 274, 1, 266)
get_StochasticRelitiveStrengthIndex(df, 238, 3, 292)
get_StochasticRelitiveStrengthIndex(df, 179, 2, 29)
get_StochasticRelitiveStrengthIndex(df, 66, 3, 23)
get_StochasticRelitiveStrengthIndex(df, 168, 3, 26)
get_StochasticRelitiveStrengthIndex(df, 205, 3, 287)
get_StochasticRelitiveStrengthIndex(df, 141, 2, 29)
get_StochasticRelitiveStrengthIndex(df, 18, 6, 105)
get_StochasticRelitiveStrengthIndex(df, 114, 2, 48)
get_StochasticRelitiveStrengthIndex(df, 98, 3, 57)
get_StochasticRelitiveStrengthIndex(df, 50, 3, 266)
get_StochasticRelitiveStrengthIndex(df, 194, 4, 272)
get_StochasticRelitiveStrengthIndex(df, 50, 3, 253)
get_StochasticRelitiveStrengthIndex(df, 114, 5, 42)
get_StochasticRelitiveStrengthIndex(df, 151, 10, 181)
get_StochasticRelitiveStrengthIndex(df, 115, 3, 61)
get_StochasticRelitiveStrengthIndex(df, 194, 3, 299)
get_StochasticRelitiveStrengthIndex(df, 136, 2, 295)
get_StochasticRelitiveStrengthIndex(df, 50, 3, 259)
get_StochasticRelitiveStrengthIndex(df, 153, 3, 40)
get_StochasticRelitiveStrengthIndex(df, 146, 2, 41)
get_StochasticRelitiveStrengthIndex(df, 130, 3, 34)
get_StochasticRelitiveStrengthIndex(df, 131, 4, 42)
get_StochasticRelitiveStrengthIndex(df, 99, 2, 48)
get_StochasticRelitiveStrengthIndex(df, 98, 3, 70)
get_StochasticRelitiveStrengthIndex(df, 163, 2, 30)
get_StochasticRelitiveStrengthIndex(df, 140, 4, 49)
get_StochasticRelitiveStrengthIndex(df, 98, 3, 65)
get_StochasticRelitiveStrengthIndex(df, 114, 3, 53)
get_StochasticRelitiveStrengthIndex(df, 84, 3, 43)
get_StochasticRelitiveStrengthIndex(df, 98, 3, 42)
get_StochasticRelitiveStrengthIndex(df, 146, 3, 35)
get_StochasticRelitiveStrengthIndex(df, 194, 14, 240)
get_StochasticRelitiveStrengthIndex(df, 130, 4, 47)
get_StochasticRelitiveStrengthIndex(df, 146, 10, 191)
get_StochasticRelitiveStrengthIndex(df, 114, 3, 35)
get_StochasticRelitiveStrengthIndex(df, 148, 2, 178)
get_StochasticRelitiveStrengthIndex(df, 132, 3, 29)
get_StochasticRelitiveStrengthIndex(df, 163, 13, 8)
get_StochasticRelitiveStrengthIndex(df, 167, 2, 40)
get_StochasticRelitiveStrengthIndex(df, 148, 3, 28)
get_StochasticRelitiveStrengthIndex(df, 179, 11, 275)
get_StochasticRelitiveStrengthIndex(df, 114, 3, 66)
get_StochasticRelitiveStrengthIndex(df, 138, 2, 31)
get_StochasticRelitiveStrengthIndex(df, 168, 3, 28)
get_StochasticRelitiveStrengthIndex(df, 99, 4, 35)
get_StochasticRelitiveStrengthIndex(df, 130, 2, 24)
get_StochasticRelitiveStrengthIndex(df, 146, 3, 21)
get_StochasticRelitiveStrengthIndex(df, 66, 3, 24)
get_StochasticRelitiveStrengthIndex(df, 114, 3, 26)
get_StochasticRelitiveStrengthIndex(df, 154, 3, 28)
"""

# Use regular expressions to extract the numbers
matches = re.findall(r'(\d+), (\d+), (\d+)', text)

# Convert the matched values to tuples and store them in a list
data = [(int(match[0]), int(match[1]), int(match[2])) for match in matches]
print(data)

# def should_remove(t1, t2):
#     return (abs(t1[0] - t2[0]) < 2) and (abs(t1[1] - t2[1]) < 2) and (abs(t1[2] - t2[2]) < 2)

# result = []

# for i in range(len(data)):
#     should_keep = True
#     for j in range(len(data)):
#         if i != j and should_remove(data[i], data[j]):
#             should_keep = False
#             break
#     if should_keep:
#         result.append(data[i])

# print(result)



# f = open("test.txt", 'r')
# val = f.readline()
# counter = 0
# while val:
#     counter+=1
#     print(f"stochRSIK{counter}, stochRSID{counter} = {val.strip()}")
#     val = f.readline()





# data =  [(18, 6, 105), (19, 6, 109), (19, 6, 108), (18, 6, 106), (114, 2, 48), (98, 3, 57), (98, 3, 56), (98, 3, 55), (50, 3, 266), (114, 3, 45), (98, 2, 55), (194, 4, 272), (100, 3, 55), (50, 3, 253), (114, 5, 45), (114, 5, 42), (151, 10, 181), (50, 3, 267), (115, 3, 61), (114, 3, 43), (50, 3, 254), (51, 3, 255), (194, 3, 299), (136, 2, 295), (50, 3, 259), (51, 3, 257), (50, 3, 260), (114, 5, 47), (99, 3, 61), (50, 3, 258), (114, 2, 52), (50, 3, 257), (99, 2, 54), (100, 4, 60), (151, 10, 179), (153, 3, 40), (51, 3, 266), (99, 3, 57), (50, 3, 256), (135, 2, 295), (51, 3, 267), (99, 3, 56), (146, 2, 41), (115, 2, 52), (99, 4, 60), (114, 5, 44), (98, 3, 61), (153, 3, 39), (130, 3, 34), (132, 2, 296), (98, 4, 61), (135, 2, 294), (149, 3, 39), (98, 4, 60), (135, 2, 298), (115, 5, 47), (131, 4, 42), (130, 3, 32), (146, 2, 42), (99, 2, 48), (98, 2, 50), (130, 4, 43), (98, 3, 70), (135, 2, 296), (163, 2, 30), (132, 3, 32), (162, 2, 30), (147, 2, 43), (150, 3, 39), (146, 2, 43), (140, 4, 49), (98, 3, 65), (98, 2, 51), (146, 2, 45), (114, 3, 53), (134, 2, 298), (84, 3, 43), (98, 3, 42), (134, 2, 299), (131, 3, 39), (98, 3, 47), (99, 2, 51), (146, 3, 35), (114, 4, 48), (132, 4, 42), (150, 10, 180), (194, 14, 240), (130, 4, 47), (146, 10, 191), (114, 3, 49), (114, 3, 35), (148, 2, 178), (132, 3, 29), (163, 13, 8), (167, 2, 40), (146, 2, 44), (98, 3, 52), (194, 14, 242), (148, 3, 28), (115, 3, 50), (98, 3, 64), (130, 3, 31), (114, 4, 49), (162, 2, 31), (130, 3, 30), (148, 3, 29), (114, 3, 50), (99, 3, 52), (195, 14, 241), (131, 3, 31), (165, 2, 40), (132, 3, 31), (114, 3, 34), (114, 3, 52), (162, 3, 29), (179, 11, 275), (148, 3, 27), (148, 3, 35), (114, 3, 66), (167, 2, 39), (138, 2, 31), (131, 3, 38), (149, 3, 36), (147, 3, 35), (130, 3, 28), (131, 3, 29), (165, 3, 28), (168, 3, 28), (194, 14, 241), (147, 3, 29), (132, 3, 28), (130, 3, 29), (148, 3, 38), (98, 3, 63), (132, 3, 30), (164, 3, 29), (134, 3, 29), (114, 4, 50), (146, 3, 25), (163, 2, 29), (166, 3, 26), (139, 3, 27), (99, 4, 35), (98, 2, 52), (130, 2, 24), (133, 3, 31), (166, 3, 28), (146, 3, 21), (149, 3, 35), (163, 3, 28), (167, 3, 26), (163, 3, 29), (162, 3, 28), (168, 2, 39), (162, 2, 34), (99, 3, 40), (98, 2, 53), (131, 3, 28), (98, 4, 38), (98, 2, 61), (134, 3, 30), (100, 3, 58), (130, 2, 30), (99, 3, 47), (98, 5, 58), (147, 3, 28), (162, 2, 29), (146, 12, 192), (99, 4, 58), (131, 3, 30), (194, 14, 243), (150, 2, 31), (66, 3, 24), (114, 3, 26), (149, 2, 29), (154, 3, 28), (135, 3, 28), (133, 3, 30)]

# def filter_close_pairs(pair_list, threshold):
#     filtered_pairs = []

#     for i, pair1 in enumerate(pair_list):
#         add_pair = True

#         for pair2 in filtered_pairs:
#             if abs(pair1[0] - pair2[0]) < threshold and abs(pair1[1] - pair2[1]) < threshold and abs(pair1[2] - pair2[2]) < threshold:
#                 # If the pairs are too close, don't add the current pair
#                 add_pair = False
#                 break

#         if add_pair:
#             filtered_pairs.append(pair1)

#     return filtered_pairs

# # Example usage with a threshold of 5
# threshold = 5
# original_pairs = data
# filtered_pairs = filter_close_pairs(original_pairs, threshold)

# print("Original pairs:", original_pairs)
# print("Filtered pairs:", filtered_pairs)

