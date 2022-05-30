import random

from bs4 import BeautifulSoup
import requests


def get_random_cartoon_url():

    def is_page_status_ok(page):
        try:
            assert page.status_code == 200
        except AssertionError:
            raise AssertionError

    page = requests.get('https://t.me/s/elkincartoon')
    is_page_status_ok(page)

    soup = BeautifulSoup(page.content, 'lxml')
    images = soup.find_all("a", class_="tgme_widget_message_photo_wrap")

    last_number = int((images[-1].attrs['href']).split('/')[-1])

    new_page = requests.get(f'https://t.me/elkincartoon/{random.randint(2, last_number)}')
    is_page_status_ok(page)
    new_soup = BeautifulSoup(new_page.content, 'lxml')
    image = new_soup.find_all("meta", attrs={'property': 'og:image'})
    url = image[0].attrs['content']

    return url
