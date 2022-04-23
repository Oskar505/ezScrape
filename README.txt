Hello, thenk you for using ezScrape!


At first you must download requests and beautifullSoup. (pip install requests and pip install beautifulsoup4)
Then you must import ezScrape. (from ezScrape import ezScrape)
Then you must define url to __init__ function.
scrape = ezScrape('url')


And then you can scrape by classes, IDs and element types.


CLASSES 

scrape.scrapeByClass('class')
You can add toText option for return only text. toText option is boolean and by default it's set to True.
then you can add an elementNumber. This option is set by default to 0 and it's order of the element in html.


IDs

scrape.scrapeById('id')
You can add toText option for return only text. toText option is boolean and by default it's set to True.


ELEMENTS

scrape.scrapeByElement('elementType')
You can add toText option for return only text. toText option is boolean and by default it's set to True.
then you can add an elementNumber. This option is set by default to 0 and it's order of the element in html.