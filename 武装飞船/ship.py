import pygame


class Ship(pygame.sprite.Sprite):
    """管理飞船"""

    def __init__(self, ai_game):
        """带入AlienInvasion实例"""
        super().__init__()

        # 获取主屏幕,surface对象
        self.main_screen = ai_game.screen
        # 获取相应的surface的rect属性：主屏幕的rect属性
        self.screen_rect = self.main_screen.get_rect()
        # 获得设置属性
        self.setting = ai_game.setting

        # 加载图片并以surface为对象,返回该图片,并下一步获取该图片的rect属性
        self.image = pygame.image.load('images/ship.bmp')
        # surface对象的rect属性可以调整其在主窗口中的位置
        self.rect = self.image.get_rect()
        # 设置图片的rect的midottom属性使图片居主屏幕的中下,两个rect.后的属性必须一致，不然会出错
        self.rect.midbottom = self.screen_rect.midbottom
        # 提取self.rect.x属性必须放置在设置完居中位置后，不然飞船起始位置会不对，因self.x的值会不对
        # 将self.rect值只能就收整数，先将它赋给可以接收小数的数进行后续的计算，再赋回来
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 判断是否要持续移动
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.main_screen.blit(self.image, self.rect)

    def update(self):
        """控制飞船移动"""
        # top bottom left right 表示飞船图片矩形的边缘的x,y属性
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.setting.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
