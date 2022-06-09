
"""
initial structure for bs4.BeautifulSoup.


###current work:
* add notes to code and recommit to repository

###changes:
* changed res to reqs for personal readability.
* added notes throughout.
"""


import requests
import bs4
import csv

alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = []

for letter in alphabet:
    # cycles through entire alphabet as the search parameter on lawyer database website. This creates duplicates that
    # we remove further down.
    homeUrl = f'https://nvbar.org/for-the-public/find-a-lawyer/?usearch={letter}'
    reqs = requests.get(homeUrl)
    soup = bs4.BeautifulSoup(reqs.text, 'lxml')
    count = 0  # helps print 'status' see below.
    maxListings = 10  # how many listings per letter. site caps at 500.

    while True:
        # will print the 'status' of current task to ensure we didn't freeze. change to fit needs.
        if count % 2 == 0:  # can raise the number to decrease frequency of 'updates'.
            print('working...', count, f"names so far in '{letter.upper()}'")

        # try loop keeps from receiving an index error if pages/search results are not known.
        try:
            # checks if you have reached the desired cap we set per search result.
            if count >= maxListings:
                break
            # this is the main 'else' statement with most of the action. This also includes the collection of the name.
            # in retrospect this should have been separated. WILL DO
            else:
                # initial variable set up and selection of correct classes in html. this will change with every site.
                email = ''
                lawFirm = ''
                # selects only the name of attorney. can scroll through each name by changing index number.
                base_person = soup.select('.user_chunk')[count]
                # selects persons name within the .user_chunk
                name = base_person.find('h3')
                # turns name in h3 into a string.
                name = name.text

                # this uses the same process as above but gathers the email instead by digging deeper into the
                # .user_chunk. notice it's the same .user_chunk as the base_person.
                if '@' in base_person.text:
                    base_email = soup.select('.user_chunk')[count]('a')
                    # the email did not always appear in the same line of code nor did it always appear at all,
                    # but it was always within the same 'a' chunk that we are able to iterate through.
                    # research a more efficient way. WILL DO.
                    for line in base_email:
                        if '@' in line.text:
                            # sets email variable to its final form. (unless no email is present)
                            email = line.text
                        else:
                            continue

                else:
                    # can set this to the default response and get rid of this else statement. WILL DO
                    email = '* Email: Not Listed *'

                # this one uses a different class within the .user_chunk as above.
                lawFirm = base_person.select('.one_third')[1]

                # the lawFirm did not always appear in the same line of code nor did it always appear at all
                # but it was always withing the same .one_third chunk. chunk that we are able to iterate through.
                # research a more efficient way. WILL DO.
                for i in lawFirm:

                    if 'company' in i.text.lower():  # doesn't work without .lower
                        # each company name had 'company: ' withing the str from .text. index 9 was always the beginning
                        # of the company name.
                        lawFirm = i.text[9::]
                        break
                    else:
                        # can set this to the default response and get rid of this else statement. WILL DO
                        lawFirm = '* Company: Not Listed *'

                # adds the info to the final result.
                result.append((name, email, lawFirm))
                # raising count by one everytime allows us to cycle through each .user_chunk.
                count += 1

        # if maxListings is higher than available listings, this will keep an error from occurring and breaks the
        # current while cycle. it also gives us a customizable 'update'
        except IndexError:
            print(f"end of '{letter.upper()}' list", count)

            break

result = set(result)

# below writes the data to a csv file with customizable headers.

# open the file in the write mode
with open('NVScrapeEmailFix.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)
    writer.writerow(['Name', 'Email', 'Company'])

    # writes a row to the csv file for all tuples in result.
    for i in result:
        writer.writerow(i)
