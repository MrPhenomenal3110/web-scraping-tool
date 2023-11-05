import requests
from bs4 import BeautifulSoup


url = "https://www.flipkart.com/search?q=samsung&marketplace=FLIPKART"

class flipkartSearch():

    def __init__(self, productName,header):
        self.productName = str(productName).replace(" ", "+")
        self.header = header
    
    def getUrl(self):
        url = f"https://www.flipkart.com/search?q={self.productName}&marketplace=FLIPKART"

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
    
    def getBrand(self):
        brands = self.getHTML().select('div[class="_2WkVRV"]')
        return self.toString(brands)

    def getNames(self):
        names = self.getHTML().findAll('div',{'class':'_4rR01T'})
        if(len(names) == 0):
            names = self.getHTML().select('a.IRpwTa')
        if(len(names) == 0):
            names = self.getHTML().select('a.s1Q9rs')
        return self.toString(names) 
    
    def getPrices(self):
        prices = self.getHTML().select('div._30jeq3')

        return self.toString(prices)
    



