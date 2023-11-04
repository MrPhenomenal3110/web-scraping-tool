from flipkart_scrapper import flipkartSearch
from prettytable import PrettyTable

header = {
    "User-Agent" : 'AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    }

name = input("Enter the name of the product to search : ")
n = int(input("Enter the number of search results required : "))

flipkartProduct = flipkartSearch(name, header)

print(flipkartProduct.getStatusCode())


flipkart_names_all = flipkartProduct.getNames()

flipkart_prices_all = flipkartProduct.getPrices()

flipkart_names = []
flipkart_prices = []

for i in range(0,min(n,len(flipkart_names_all))):
    flipkart_names.append(flipkart_names_all[i])

for i in range(0,min(n,len(flipkart_prices_all))):
    flipkart_prices.append(flipkart_prices_all[i])

flipkart_table = PrettyTable(align='l')

flipkart_table.field_names = ["Product Name", "Price (INR)"]

for name, price in zip(flipkart_names, flipkart_prices):
    flipkart_table.add_row([name, price])

print(flipkart_table)
