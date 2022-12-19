import pygame
from . import color

pygame.font.init()
FONT = pygame.font.SysFont("monospace", 50)
WIDTH, HEIGHT = 700, 500


def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= 500:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


class Score:

    def __init__(self):
        self.left_score = 0
        self.right_score = 0

    def score(self, player='left'):
        if player == "left":
            self.left_score += 1
        else:
            self.right_score += 1

    def reset(self):
        self.left_score = 0
        self.right_score = 0

    def draw(self, win):

        left_score_text = FONT.render(f"{self.left_score}", 1, color.WHITE)
        right_score_text = FONT.render(f"{self.right_score}", 1, color.WHITE)
        win.blit(left_score_text,
                 (WIDTH // 4 - left_score_text.get_width() // 2, 20))
        win.blit(right_score_text,
                 (WIDTH * (3 / 4) - right_score_text.get_width() // 2, 20))
