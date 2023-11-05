import requests
from bs4 import BeautifulSoup

class amazonSearch():

    def __init__(self, productName,header):
        self.productName = str(productName).replace(" ", "+")
        self.header = header
    
    def getUrl(self):
        url = f"https://www.amazon.in/s?k={self.productName}&ref=nb_sb_noss_1"

        return url

    def makeRequest(self):
        request = requests.get(self.getUrl(), headers=self.header)
        data = request.content
        statusCode = request.status_code
        response = {"status-code" : statusCode, "resp" : data}

        return response
    
    def getStatusCode(self):
        return self.makeRequest()["status-code"]

    def getHTML(self):
        response = self.makeRequest()["resp"]
        soup = BeautifulSoup(response, 'html.parser')

        return soup
    
    def toString(self, tags):
        for i in range(0,len(tags)):
            tags[i] = tags[i].string

        return tags

    def getNamesAndPrices(self):
        products_names = self.getHTML().select('div[data-component-type="s-search-result"]')
        names = []
        for product in products_names:
            name = product.select('span[class="a-size-base-plus a-color-base a-text-normal"]')
            if(len(name) == 0):
                name = product.select('span[class="a-size-medium a-color-base a-text-normal"]')
            name_str = name[0].string
            if(len(name_str) > 40):
                name_str = f"{name_str[0:41]} ..."
            names.append(name_str)

        products_prices = self.getHTML().select('span[class="a-price"]')
        prices = []
        for product in products_prices:
            price = product.select('span[class="a-price-whole"]')
            price_str = price[0].string
            
            prices.append(f"₹{price_str}")

        return {"names" : names, "prices" : prices}
