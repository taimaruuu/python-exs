# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

from bs4 import BeautifulSoup
import requests

url = 'http://www.nytimes.com'
r = requests.get(url).text
soup = BeautifulSoup(r)

title = soup.find_all('h2') # since nytimes is built with variable titles and classes we must just use h2 as our guide

print("Here are the headlines on the homepage for nytimes.com:")
for row in title[0:-2]:  # to remove the last two h2 items which are simply naviation items
    print(row.text)
