import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # 继承Sprite,可进行编组，可以同时操作编组中的元素

    def __init__(self, ai_game):
        """初始化子弹"""
        super().__init__()

        self.main_screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        # Pygame中的Rect方法创建一个矩形  x,y,宽，高
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 将子弹的y坐标赋给可以接受小数值的属性
        self.y = float(self.rect.y)

    def update(self):
        """更新发射后子弹位置"""
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        # 绘制矩形到在参数1上，以参数2为填充色的参数3矩形，width = 0 表示用参数2颜色填充
        pygame.draw.rect(self.main_screen, self.color, self.rect, width=0)
