import pygame.font
from ship import Ship
from pygame.sprite import Group


class ScoreBoard:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.status = ai_game.status

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_image()

    def prep_image(self):
        self.prep_font()
        self.prep_highest_score()
        self.prep_level()
        self.prep_ships()

    def prep_font(self):
        """将数字转换为字符串，再转换为图像"""
        rounded_score = round(self.status.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)
        self.score_image_rect = self.score_image.get_rect()

        self.score_image_rect.right = self.screen.get_rect().right - 20
        self.score_image_rect.top = 20

    def prep_highest_score(self):
        rounded_highest_score = round(self.status.highest_score)
        high_str = "{:,}".format(rounded_highest_score)
        self.high_score_image = self.font.render(high_str, True, self.text_color, self.setting.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()

        self.high_score_rect.centerx = self.screen.get_rect().centerx
        self.high_score_rect.top = self.score_image_rect.top

    def prep_level(self):
        level_str = str(self.status.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.setting.bg_color)
        self.level_rect = self.level_image.get_rect()

        self.level_rect.right = self.score_image_rect.right
        self.level_rect.top = self.score_image_rect.bottom + 20

    def prep_ships(self):
        """创建飞机组"""
        self.ships = Group()
        for ship_num in range(self.status.ship_left):
            new_ship = Ship(self.ai_game)
            new_ship.rect.x = 10 + new_ship.rect.width * ship_num
            new_ship.rect.y = 10
            self.ships.add(new_ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high(self):
        """检查当前得分是否超过最高分"""
        if self.status.score > self.status.highest_score:
            self.status.highest_score = self.status.score
            self.prep_highest_score()
