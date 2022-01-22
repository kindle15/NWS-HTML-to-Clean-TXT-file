# J_Epperson: Boise ID Wx forecast text to Kindle PW project Jan2022
import os
import urllib.request, urllib.parse, urllib.error
import urllib.request as urllib2
import html2text #sudo pip install html2text
from urllib.request import urlopen

url = 'https://forecast.weather.gov/product.php?site=NWS&issuedby=BOI&product=A>
response = urllib.request.urlopen(url)

with open('output.txt', 'wb') as f:
     f.write(response.read())

import html2text

with open("output.txt", "r") as f_html:
    html = f_html.read()

with open("Wx_Forcast.txt", "w") as f:
    f.write(html2text.html2text(html))

if os.path.exists("output.txt"):
        os.remove("output.txt")
else:
        print ("The file does not exist")

# email Wx Forcast to Kindle Paperwhite
# CODE HERE
