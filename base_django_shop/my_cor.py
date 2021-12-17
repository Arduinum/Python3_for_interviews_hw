#!/usr/bin/env python3

import asyncio
import aiohttp


# urls = ['http://google.com', 'http://play.google.com', 'http://yandex.ru']
urls = ['http://127.0.0.1:8000/category/products/2/']


async def call_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open('data_site.txt', 'a') as file:
                data = await response.text()
                file.write(f'String {url}\n{data}\n')
            return data


futures = [call_url(url) for url in urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
