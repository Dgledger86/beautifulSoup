# ---current issues---

# * It's ALIIIIIVE!!! First web scraping script from scratch and it met the specs of the project!

# * Does not add company to result output. tested code separately and worked before I fixed th email issue.

# ---issues fixed---:

# * Still working on fixing the email issue. does not line up with the names. either the same one over and over again,
# or they randomly match here and there.

# *
import requests
import bs4
import csv

alphabet = 'a'  # 'abcdefghijklmnopqrstuvwxyz'
result = []
"""
for letter in alphabet:
    homeUrl = f'https://apps.calbar.ca.gov/attorney/LicenseeSearch/QuickSearch?FreeText={letter}'
    res = requests.get(homeUrl)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    count = 0
    maxListings = 1

    while True:

        if count % 100 == 0:
            print('working...', count, f"names so far in '{letter.upper()}'")

        try:
            if count >= maxListings:
                break
            else:
                # Rename these for the specs of the webscraping. these will feed into your final tuple results. 
                email = '' 
                lawFirm = ''
                name = '' # Delete this line if the program breaks. ***********************
                
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
"""
"""
for i in result:
    print(i)
"""

# homeUrl = f'https://apps.calbar.ca.gov/attorney/LicenseeSearch/QuickSearch?FreeText={alphabet}' # changed to 'alphabet' from 'letter' for testing. CHANGE BACK
homeUrl = 'http://www.inmatesearchca.org/San_Joaquin_County'
res = requests.get(homeUrl)
soup = bs4.BeautifulSoup(res.text, 'lxml')


