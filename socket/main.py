#  main.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 12. 04. 20:24

import socket
# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
while True:
    # now our endpoints knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Conection from {address} has been established.")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()

