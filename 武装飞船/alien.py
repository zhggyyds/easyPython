from pygame.sprite import Sprite
import pygame


class Alien(Sprite):
    """外星人类"""
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """外星人移动"""
        self.x += (self.setting.alien_speed * self.setting.alien_direction)
        self.rect.x = self.x

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.left <= 0 or self.rect.right >= screen_rect.right:
            return True
