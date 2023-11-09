import requests
from bs4 import BeautifulSoup

# URL of Yahoo Finance's forex page
url = "https://finance.yahoo.com/currencies"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing forex trading pairs
forex_table = soup.find('table', {'class': 'W(100%)'})

# Extract forex pairs from the table
forex_pairs = []
for row in forex_table.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')
    base_currency = columns[0].text
    quote_currency = columns[1].text
    forex_pair = f"{base_currency}/{quote_currency}"
    forex_pairs.append(forex_pair)

# Print the list of forex trading pairs
for pair in forex_pairs:
    print(pair)
aVal = 5
bVal = 10
cVal = 12
max(aVal, bVal, cVal)
