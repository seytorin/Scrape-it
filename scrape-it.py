import urllib3
from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


#Grab the HTML using userlib3.  Opens and assigns the HTML to page.
page = requests.get('https://cnn.com')

#Create an object
soup = BeautifulSoup(page.text, 'html.parser')

index_update = soup.find_all('html')
print(index_update)

