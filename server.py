import socket
import sys

WIDTH, HEIGHT = 700, 500
WINNING_SCORE = 5
BALL_RADIUS = 7

server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("waiting for connection...")

currentPlayer = 0
countPlayer = 0
while True:
    conn, addr = s.accept()
    countPlayer += 1
    print("connected to", addr)

sys.exit(0)
