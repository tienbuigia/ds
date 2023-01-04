import pygame

from network import Network
from src import color

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("multiplayer pong")

FONT = pygame.font.SysFont("monospace", 50)

FPS = 60


#def draw(win):
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
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


if __name__ == '__main__':
    main()
