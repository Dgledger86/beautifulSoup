import requests
import bs4
website = 'https://en.wikipedia.org/wiki/Etana'  # anysite goes here between the quotation marks ''
"""
so far can only grab one set of images within thumbinner


it also opens and closes file everytime iit creates an image. can I hold all photos and print and past all photos in a 
group? maybe as a list?

"""

filename = website.split('/')[-1]
res = requests.get(website)
soups = bs4.BeautifulSoup(res.text, 'lxml')  # select how to read webpage this is usually default


def grab_image(soup):
    counter = 0
    try:
        for pic in range(0, 100):
            soup.select('.thumbinner')

            computer = soup.select('.thumbimage')[counter]  # increase this number to change photos
            solo_photo = 'https:' + computer['src']  # this becomes what we are saving. add https: to the front.

            # to download image:
            # add https: put in front of image source from above and add it below
            image_link = requests.get(solo_photo)
            # image_link.content # binary for image.
            f = open(f'{filename}{counter}.jpg', 'wb')  # this creates a file if the file didn't exist.
            # make sure to include wb. it ensures it writes in binary and creates the image.
            f.write(image_link.content)
            f.close()  # ALWAYS CLOSE FILES.
            counter += 1
    except IndexError:
        print('complete')

