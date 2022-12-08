
import socket
import pickle


class Network:
       

    def get_player(self):
        return self.player


    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            reply = pickle.loads(self.client.recv(4096 * 2))
            return reply
        except socket.error as e:
            return str(e)
