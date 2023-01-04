import socket
import pickle
import sys
import pygame
from _thread import start_new_thread
from src.player import Player
from src.ball import Ball
from src import game
from src.game import Score

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


players = [
    Player(0, HEIGHT / 2 - 50, 20, 100, (0, 255, 0)),
    Player(WIDTH - 20, HEIGHT / 2 - 50, 20, 100, (0, 0, 255))
]
ball = Ball(WIDTH / 2 - BALL_RADIUS, HEIGHT / 2 - BALL_RADIUS, BALL_RADIUS)
score = Score()


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            players[player] = data
            if not data:
                print("disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

            # conn.sendall(pickle.dumps((reply, (ball.x, ball.y))))
            conn.sendall(pickle.dumps((
                reply,
                ball,
                score,
            )))
        except:
            break
    print("Lost connection")
    conn.close()

clock = pygame.time.Clock()

def move_ball(ball):
    while True:
        try:
            clock.tick(60)
            ball.move()

            game.handle_collision(ball, players[0], players[1])
            # print("recieved:", data)
            # print("sending:", reply)

            if ball.x < 0:
                score.score('right')
                ball.reset()
            elif ball.x > WIDTH:
                score.score('left')
                ball.reset()

        except:
            break

currentPlayer = 0
countPlayer = 0
while True:
    conn, addr = s.accept()
    countPlayer += 1
    print("connected to", addr)
    
    start_new_thread(threaded_client, (conn, currentPlayer))
    if countPlayer == 2:
        start_new_thread(move_ball, (ball, ))
    currentPlayer += 1
    
sys.exit(0)
