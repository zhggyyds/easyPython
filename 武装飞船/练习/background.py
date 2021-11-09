import pygame
import sys
import rain
from setting import Setting


class BG:
    """蓝色背景主窗口"""
    # 初始化pygame的各功能
    def __init__(self):
        pygame.init()

        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_height, self.setting.screen_height))
        pygame.display.set_caption("雨滴")
        self.rains = pygame.sprite.Group()

        self.create_rains()

    def create_rain(self, rain_number):
        for num in range(rain_number):
            now_rain = rain.Rain(self)
            rain_width = now_rain.rect.width
            now_rain.x = rain_width + 2 * rain_width * num
            now_rain.rect.x = now_rain.x
            self.rains.add(now_rain)

    def create_rains(self):
        new_rain = rain.Rain(self)
        rain_width = new_rain.rect.width

        available_space_x = self.screen.get_rect().width - 2*rain_width
        rain_number = available_space_x // (2 * rain_width)

        self.create_rain(rain_number)

    def delete_rains(self):
        for now_rain in self.rains.sprites():
            self.rains.remove(now_rain)

    def check_edges(self):
        for now_rain in self.rains.sprites():
            if now_rain.check_rain():
                self.delete_rains()
                break

    def update_rains(self):
        self.rains.update()
        self.check_edges()
        if len(self.rains) == 0:
            self.create_rains()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        self.screen.fill((255, 255, 255))
        self.rains.draw(self.screen)

    def run(self):
        while True:
            self.check_event()
            self.update_screen()
            self.update_rains()
            pygame.display.flip()


if __name__ == "__main__":
    BB = BG()
    BB.run()
