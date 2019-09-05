#!/bin/env python3

import asyncio
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("server.crt")
context.check_hostname = False

async def client_process(loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8443, ssl=context, loop=loop)
    writer.write("test".encode())
    data = await reader.read(256)
    print(data.decode())
    writer.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client_process(loop))
    loop.close()
