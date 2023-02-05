import pygame
from src.constant import WIDTH, HEIGHT, FPS

from network import Network
from src import color

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('multiplayer pong')

FONT = pygame.font.SysFont('monospace', 50)

# def draw(win):
#    win.fill(color.BLACK)
#    pygame.display.update()


def draw(win, players, ball, score):
    win.fill((40, 40, 40))

    score.draw(win)

    for player in players:
        player.draw(win)

    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, color.WHITE,
                         (WIDTH // 2 - 5, i, 10, HEIGHT // 20))

    ball.draw(win)
    pygame.display.update()


def main():
    pygame.init()
    run = True
    n = Network()
    player = n.get_player()
    clock = pygame.time.Clock()
    keys = pygame.key.get_pressed()

    while run:
        clock.tick(FPS)
        player2, ball, score = n.send(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
                pygame.quit()

        player.move()
        draw(WIN, [player, player2], ball, score)

    pygame.quit()


if __name__ == '__main__':
    main()
