import requests
import bs4

url = 'https://publicinfo.fresnosheriff.org/inmateinfocenter/incustody'

req = requests.get(url)
soup = bs4.BeautifulSoup(req.text, 'lxml')

soup = soup.select('e-control e-btn e-lib e-link')

print(soup)
