import socket

if __name__ == "__main__":
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))

    s.listen(5)
    while True:
        c, addr = s.accept()
        print("Got connection from, ", addr)
        szoveg = bytes("Thank you for conecting", "utf-8")
        c.send(szoveg)
        c.close()
