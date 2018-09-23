from lxml import html
from lxml.html import parse
import requests
import cssselect

class WebCrawler():

    def crawl_web(self, initial_url):
        page = requests.get(initial_url)
        webpage = html.fromstring(page.content)
        links = webpage.xpath('//a/@href')
        original_url = "https://en.wikipedia.org"
        response = []
        for link in links:
            if "jpg" in link:
                response.append(requests.head(original_url+link))
            elif link.startswith('https://') == True:
                response.append(requests.head(link))
            elif link.startswith('/wiki/') == True:
                response.append(requests.get(original_url+link))
            elif link.startswith('/w/') == True:
                response.append(requests.get(original_url+link))
            else:
                pass
        print(response)

if __name__=="__main__":
    WebCrawler().crawl_web('https://en.wikipedia.org/wiki/Control_theory')