import asyncio


class EchoServer(asyncio.Protocol):
    def connection_made(self, transport: asyncio.transports.BaseTransport) -> None:
        """Подключение нового клиента"""
        self.transport = transport
        print('connection_made')

    def data_received(self, data: bytes) -> None:
        """Получение данных"""
        print(f'received len {len(data)}')
        self.transport.write(data)


async def handle_connection(reader, writer):
    print('connection_made')
    while True:
        data = await reader.read(100)  # ждём данные и читаем данные в ограниченном колличестве
        if data:
            data_len = len(data)
            print(f'received len {data_len}')
            writer.write(data)  # записываем данные в буфер
            await writer.drain()  # опустошаем буфер
        else:
            print('closed')
            writer.close()
            break


# запуск простейего callback http server
def run_proto():
    loop = asyncio.get_event_loop()
    server = loop.create_server(EchoServer, '127.0.0.1', 15555)
    loop.run_until_complete(server)
    loop.run_forever()


# запуск асинхроннго сервера
def run_handler():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.ensure_future(asyncio.start_server(handle_connection, '127.0.0.1', 15555), loop=loop)
    )
    loop.run_forever()


run_handler()
