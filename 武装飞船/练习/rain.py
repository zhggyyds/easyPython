import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    def __init__(self, blue_bg):
        super().__init__()

        self.main_screen = blue_bg.screen
        self.screen_rect = self.main_screen.get_rect()
        self.setting = blue_bg.setting

        self.image = pygame.image.load("../images/drop.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.setting.rain_width
        self.rect.y = self.setting.rain_height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.setting.alien_speed
        self.rect.y = self.y

    def check_rain(self):
        if self.rect.top >= self.main_screen.get_rect().bottom:
            return True


