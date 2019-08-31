# TLS Connection Practice

1. Prepare the key and certificate
   `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt`

2. Execute TLS server `./server.py`
3. Execute TLS client `./client.py`

## Reference

[TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html)
