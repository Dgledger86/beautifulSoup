import requests
import bs4

req = requests.get('https://wic.sjgov.org/WhosInCustody/InmateDetail/24286420')
soup = bs4.BeautifulSoup(req.text, 'lxml')
result = soup.select('inner-content')
print(result)