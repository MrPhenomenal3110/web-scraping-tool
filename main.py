from flipkart_scrapper import flipkartSearch
from amazon_scrapper import amazonSearch
from prettytable import PrettyTable

header_flipkart = {
    "user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G570Y Build/MMB29K)",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    }

header_amazon = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
}

name = input("Enter the name of the product to search : ")
n = int(input("Enter the number of search results required : "))

print("Searching Flipkart ....")

flipkartProduct = flipkartSearch(name, header_flipkart)


flipkart_names_all = flipkartProduct.getNames()

flipkart_prices_all = flipkartProduct.getPrices()

flipkart_names = []
flipkart_prices = []

for i in range(0,min(n,len(flipkart_names_all))):
    if(flipkart_names_all[i] is not None):
        flipkart_names.append(flipkart_names_all[i])

for i in range(0,min(n,len(flipkart_prices_all))):
    if(flipkart_prices_all[i] is not None):
        flipkart_prices.append(flipkart_prices_all[i])

flipkart_table = PrettyTable(align='l')

flipkart_table.field_names = ["Product Name", "Price (INR)"]

for name, price in zip(flipkart_names, flipkart_prices):
    flipkart_table.add_row([name, price])



print(flipkart_table)

print("Searching Amazon ....")


amazonProduct = amazonSearch(name, header_amazon)


amazon_names_all = amazonProduct.getNamesAndPrices()["names"]

amazon_prices_all = amazonProduct.getNamesAndPrices()["prices"]

amazon_names = []
amazon_prices = []

for i in range(0,min(n,len(amazon_names_all))):
    amazon_names.append(amazon_names_all[i])

for i in range(0,min(n,len(amazon_prices_all))):
    amazon_prices.append(amazon_prices_all[i])

amazon_table = PrettyTable(align='l')

amazon_table.field_names = ["Product Name", "Price (INR)"]

for name, price in zip(amazon_names, amazon_prices):
    amazon_table.add_row([name, price])

print(amazon_table)
