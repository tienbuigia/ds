import socket
import pickle


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.player = self.connect()

    def get_player(self):
        return self.player

    def connect(self):
        self.client.connect(self.addr)
        return pickle.loads(self.client.recv(2048 * 2))

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            reply = pickle.loads(self.client.recv(4096 * 2))
            return reply
        except socket.error as e:
            return str(e)
