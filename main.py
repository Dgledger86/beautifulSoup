
import requests
import bs4
import csv

alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = []

for letter in alphabet:
    homeUrl = f'https://nvbar.org/for-the-public/find-a-lawyer/?usearch={letter}'
    res = requests.get(homeUrl)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    count = 0
    maxListings = 1000000

    while True:

        if count % 100 == 0:
            print('working...', count, f"names so far in '{letter.upper()}'")

        try:
            if count >= maxListings:
                break
            else:
                email = ''
                lawFirm = ''
                base_person = soup.select('.user_chunk')[count]  # selects only the name of attorney
                name = base_person.find('h3')
                name = name.text

                if '@' in base_person.text:
                    base_email = soup.select('.user_chunk')[count]('a')
                    for line in base_email:
                        if '@' in line.text:
                            email = line.text
                        else:
                            continue

                else:
                    email = '* Email: Not Listed *'

                lawFirm = base_person.select('.one_third')[1]

                for i in lawFirm:
                    if 'company' in i.text.lower():
                        lawFirm = i.text[9::]
                        break
                    else:
                        lawFirm = '* Company: Not Listed *'

                result.append((name, email, lawFirm))
                count += 1

        except IndexError:
            print(f"end of '{letter.upper()}' list", count)

            break

result = set(result)
# open the file in the write mode
with open('NVScrapeEmailFix.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)
    writer.writerow(['Name', 'Email', 'Company'])

    # write a row to the csv file
    for i in result:
        writer.writerow(i)
