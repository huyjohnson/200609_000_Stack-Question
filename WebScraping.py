import requests
import json
##import shutil
from bs4 import BeautifulSoup
##import urllib.request as urllib

# Enter the URL of the webpage you want to download the images from
page = 'https://www.archdaily.com/63267/ad-classics-house-vi-peter-eisenman/5037e0ec28ba0d599b000190-ad-classics-house-vi-peter-eisenman-image'

# Returns the webpage source code under page_doc
result = requests.get(page)
##result = requests.get(page)
page_doc = result.content

# Returns the source code as BeautifulSoup object, as nested data structure
soup = BeautifulSoup(page_doc, 'html.parser')
img = soup.find('div', class_='afd-gal-items')
img_list = img.attrs['data-images']
##print(img_list)
##for k, v in img_list():
##    if k == 'url_large':
##        print(v)


jsonData = json.loads(img.attrs['data-images'])
print(jsonData['url_large'])
