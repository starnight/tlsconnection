#!/bin/env python3

import asyncio
import ssl

class server:
    def __init__(self):
        self.svr_ip = "127.0.0.1"
        self.svr_port = 8443
        self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        self.context.load_cert_chain("server.crt", "server.key")

    async def deal_cli(self, reader, writer):
        addr = writer.get_extra_info('peername')
        data = await reader.read(256)
        print("Client {}: {}".format(addr, data.decode()))
        data = "Server got {}".format(data.decode())
        writer.write(data.encode())
        writer.close()

    def run(self):
        self.loop = asyncio.get_event_loop()
        coro = asyncio.start_server(self.deal_cli, self.svr_ip, self.svr_port, ssl=self.context, loop=self.loop)
        self.loop.run_until_complete(coro)

        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self.loop.close()

if __name__ == '__main__':
    svr = server()
    print("Server start")
    svr.run()
