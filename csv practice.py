"""
import requests
import bs4

letter = 'a'
count = 10
homeUrl = f'https://nvbar.org/for-the-public/find-a-lawyer/?usearch={letter}'
res = requests.get(homeUrl)
soup = bs4.BeautifulSoup(res.text, 'lxml')
base_person = soup.select('.user_chunk')[count]  # selects only the name of attorney
email = ''
firm = ''
lawFirm = base_person.select('.one_third')[1]
for i in lawFirm:
    pass


"""

print(len('abcdefghijklmnopqrstuvwxyz'))