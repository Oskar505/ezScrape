try:
    import requests
    from bs4 import BeautifulSoup as bs

except:
    print('You must install requests and beautifullSoup')


class ezScrape():

    # Get html
    def __init__(self, url):
        urlGet = requests.get(url)
        html = urlGet.text
        self.soup = bs(html, 'html.parser')


    # By class
    def scrapeByClass(self, elementClass, toText=True, elementNumber=0):
        assert isinstance(toText ,bool), 'toText must be boolean.'
        assert elementNumber >= 0, 'elementNumber must be higher or equals to zero.'

        if toText == True:
            try:
                return self.soup.select(f'.{elementClass}')[elementNumber].text

            except:
                return 'Element was not find. Try correct elementClass.'
        
        else:
            try:
                return self.soup.select(f'.{elementClass}')[elementNumber]

            except:
                return 'Element was not find. Try correct elementClass.'

    #By ID
    def scrapeById(self, elementId, elementType, toText=True):
        assert isinstance(toText ,bool), 'toText must be boolean.'

        if toText == True:
            try:
                return self.soup.find(elementType, {"id": elementId})

            except:
                return 'Element was not find. Try correct elementId.'

    # By Element type
    def scrapeByElement(self, elementType, toText=True, elementNumber=0):
        if toText == True:
            return self.soup.find(elementType, {})[elementNumber].text
        
        else:
            return self.soup.find(elementType, {})[elementNumber]






# TEST


#scrape = ezScrape('https://www.skikarlov.cz/lyzovani/sjezdovky-lanovky-a-vleky/')

#print(scrape.scrapeByClass('line'))
#print(scrape.readme)





#urlGet = requests.get('https://www.skikarlov.cz/lyzovani/sjezdovky-lanovky-a-vleky/')
#html = urlGet.text
#soup = bs(html, 'html.parser')

#print(soup.select('.line')[0].text)
#print(soup.find('div', {}).text)