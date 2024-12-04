#  client.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 12. 04. 20:24

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((socket.gethostname(), 30020))
s.connect((socket.gethostbyname('192.168.0.172'), 30020))
full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)
