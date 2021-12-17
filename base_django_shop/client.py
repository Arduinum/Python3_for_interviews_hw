# реализуем клиент подходом green_led
import gevent.monkey
from urllib.request import urlopen

gevent.monkey.patch_all()  # делает выполнение праллельным в потоках

urls = ['http://google.com', 'http://play.google.com', 'http://yandex.ru']


def get_data(url):
    print(f'getting {url}')
    data = urlopen(url).read()
    print(f'received: {len(data)}')


jobs = [gevent.spawn(get_data, url) for url in urls]

gevent.wait(jobs)
