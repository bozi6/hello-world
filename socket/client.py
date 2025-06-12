#  client.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 12. 04. 20:24

import socket

# Use TCP to match the server implementation in ``main.py``.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the local server on the same host.
s.connect((socket.gethostname(), 1234))
full_msg = ''
while True:
    msg = s.recv(8)
    if not msg:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)
