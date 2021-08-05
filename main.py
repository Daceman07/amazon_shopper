from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
MY_NUMBER = "PHONE NUMBER"
TWILO_SID = "TWILO SID"
AUTH_TOKEN = "AUTH TOKEN"
TWILO_PHONE_NUMBER = "TWILO NUMBER"
Product_link = "AMAZON LINK"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                   "88.0.4324.190 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=Product_link, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
print(soup)

price_from_site = soup.find(id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString")

price = price_from_site.get_text()[1:]
buy_price = 22
client = Client(TWILO_SID, AUTH_TOKEN)


if float(price) <= float(buy_price):
    message = client.messages.create(
        body=f"Your victims are currently {price}.\n Click here to order: {Product_link}",
        from_='TWILO NUMBER',
        to='YOUR NUMBER'
    )
else:
    message = client.messages.create(
        body=f"No sale today",
        from_='TWILO NUMBER',
        to='YOUR NUMBER')