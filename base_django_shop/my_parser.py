from bs4 import BeautifulSoup
import requests


def parser():
    main_url = 'http://127.0.0.1:8000/'
    page = requests.get(main_url, 'lxml')
    soup = BeautifulSoup(page.text, 'html.parser')

    return soup.findAll('a')


print(parser())
