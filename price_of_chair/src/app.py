import requests
from bs4 import BeautifulSoup
request = requests.get("https://www.johnlewis.com/us/house-by-john-lewis-hinton-office-chair/p2083183")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
string_price = element.text.strip() #£129.00

price_without_symbol = string_price[1:] #£129.00

price = float(price_without_symbol)

if price < 200:
    print("Buy the Chair")
    print("The current price is {}.".format(string_price))
else:
    print("Don't buy the chair")

#<p class="price price--large">$177.50</p>

#print(request.content)