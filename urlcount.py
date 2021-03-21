from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter the url: ')
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
tags = soup('span')
for tag in tags :
    tag = int(tag.contents[0])
    # print(tag)   
    count = tag + count
print(count)