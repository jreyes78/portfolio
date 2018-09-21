from lxml import html
import requests

link = "http://sdirwmp.org/contact-us"
response = requests.get(link) #get page data from server, block redirects
sourceCode = response.content #get string of source code from response
htmlElem = html.document_fromstring(sourceCode) #make HTML element object

tdElems = htmlElem.cssselect("[valign=top]") #list of all td elems
for elem in tdElems:
    text = elem.text_content() #text inside each td elem 
    print(text)