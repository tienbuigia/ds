import socket
import time
import pickle
import sys
import pygame
from _thread import start_new_thread
from src.player import Player
from src.ball import Ball
from src import game
from src.game import Score
from src.constant import HEIGHT, WIDTH, BALL_RADIUS, WINNING_SCORE

server = 'localhost'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print('waiting for connection...')

players = [
    Player(0, HEIGHT / 2 - 50, 20, 100, (0, 255, 0)),
    Player(WIDTH - 20, HEIGHT / 2 - 50, 20, 100, (0, 0, 255)),
]
ball = Ball(WIDTH / 2 - BALL_RADIUS, HEIGHT / 2 - BALL_RADIUS, BALL_RADIUS)
score = Score()


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ''
    # global ready
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            players[player] = data
            if not data:
                print('disconnected')
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
            # print("recieved:", data.ready)
            # print("sending:", reply.ready)
        except Exception as e:
            print(e)
            break
    print('Lost connection')
    ball.ready = False
    conn.close()


clock = pygame.time.Clock()


def move_ball(ball):
    while True:
        try:
            clock.tick(60)
            ball.move()

            game.handle_collision(ball, players[0], players[1])

            if ball.x < 0:
                score.score('right')
                ball.reset()
            elif ball.x > WIDTH:
                score.score('left')
                ball.reset()

            if score.left_score >= WINNING_SCORE:
                score.left_score = 'You WIN!'
                time.sleep(3)
                score.reset()
                ball.reset()
                # players[0].reset()
                # players[1].reset()
            elif score.right_score >= WINNING_SCORE:
                score.right_score = 'You WIN!'
                time.sleep(3)
                score.reset()
                ball.reset()
                # players[0].reset()
                # players[1].reset()

        except Exception as e:
            print(e)
            break


def check_ready():
    # global ready
    while True:
        clock.tick(20)
        if players[0].ready and players[1].ready:
            ball.ready = True
        else:
            ball.ready = False


countPlayer = 0
currentPlayer = 0
while True:
    try:
        conn, addr = s.accept()
    except KeyboardInterrupt:
        print("exited.")

    countPlayer += 1
    print('connected to', addr)

    start_new_thread(threaded_client, (conn, currentPlayer))

    if countPlayer == 2:
        start_new_thread(check_ready, ())
        start_new_thread(move_ball, (ball, ))
    currentPlayer += 1

sys.exit(0)
