import pygame


class Player:

    def __init__(self, x, y, width, height, color):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 4

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.y - self.vel >= 0:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y + self.height < 500:
            self.y += self.vel
        self.update()

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
