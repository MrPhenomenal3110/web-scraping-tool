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
        soup = BeautifulSoup(response, 'lxml')

        return soup
    
    def toString(self, tags):
        for i in range(0,len(tags)):
            tags[i] = tags[i].string

        return tags

    def getNames(self):
        names = self.getHTML().findAll('div',{'class':'s1Q9rs'})

        return (names) 
    
    def getPrices(self):
        prices = self.getHTML().findAll('div',{'class':'_30jeq3'})

        return (prices)
    



