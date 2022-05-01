import threading
from socket import *

from Communication.JsonMapper import JsonMapper

ENCODING = "utf-8"


class Server:

    def __init__(self, database, args):
        self.database = database
        self.args = args

    def handle_client(self, conn, address):
        print(f"New connection from {address}")
        jsondata = ""
        while True:
            received = conn.recv(2048)
            if len(received) > 0:
                jsondata += received.decode(ENCODING)
            else:
                break
        conn.close()
        print(jsondata)
        packet = JsonMapper.get_packet(jsondata)
        print(f"packet json: {packet}")
        self.database.store_alert(packet, self.args)
        print("data stored")

    def start(self, port):
        server = socket(AF_INET, SOCK_STREAM)
        host_ip = "192.168.99.106"
        server.bind((host_ip, port))
        server.listen()
        print(f"Listening on {host_ip}:{port}")
        while True:
            clientconn, clientaddr = server.accept()
            clientthread = threading.Thread(target=self.handle_client, args=(clientconn, clientaddr))
            clientthread.start()
