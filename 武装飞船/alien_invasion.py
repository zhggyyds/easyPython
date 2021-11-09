# 个人认为之所以这些东西能够显示在屏幕上都是因为pygame.display，将这些display赋给self下的属性只是为了方便调用数据，比如说调整图片元素位置等等
# while循环为了窗体一直存在，其中的pygame.event.get()我认为是将主窗口一直保持在屏幕上的原因
import sys
import pygame
from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_status import GameStatus
from button import Button
from scoreBoard import ScoreBoard
import json


class AlienInvasion:
    """管理游戏资源和行为"""

    def __init__(self):
        """初始化游戏"""
        # 初始化操作
        pygame.init()

        # 将游戏属性都集合到Setting类中,方便后续代码修改，无序在代码中一一修改
        self.setting = Setting()

        # 创建显示窗口。display.set_mode返回一个游戏窗口，该对象是surface，它是屏幕的一部分，并赋给screen
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 👈🏻全屏
        
        # 设置窗体名称
        pygame.display.set_caption("Alien Invasion")

        self.init_every_exponent()

    def init_every_exponent(self):
        """重构，创建东西太多，简化构造函数"""
        # 创建飞船类
        self.ship = Ship(self)
        # 创建子弹类的group，group类似于列表
        self.bullets = pygame.sprite.Group()
        # 创建外星人类group
        self.aliens = pygame.sprite.Group()
        self.create_alien_fleet()
        # 创建游戏状态类
        self.status = GameStatus(self)

        # 创建PLAY按钮
        self.play_button_easy = Button(self, "PLAY")

        # 创建记分牌
        self.score_board = ScoreBoard(self)

    def create_alien(self, alien_num, alien_row):
        """用于重构创建外星人群"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_num
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * alien_row
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def create_alien_fleet(self):
        """创建外星人战队，并加入group"""
        new_alien = Alien(self)
        # 返回一个包含宽高的元组
        alien_width, alien_height = new_alien.rect.size

        # 求的实际可用宽度，获取可打印外星人个数
        available_space_x = self.screen.get_rect().width - 2 * alien_width
        alien_number = available_space_x // (2 * alien_width)

        # 获得实际行数
        available_space_y = self.screen.get_rect().height - 3*alien_height - self.ship.rect.height
        alien_row_num = available_space_y // (2 * alien_height)

        # 打印外星人群
        for row_num in range(alien_row_num):
            for num in range(alien_number):
                # 传入列号，行号
                self.create_alien(num, row_num)

    def change_fleet_direction(self):
        """改变外星人舰队移动方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.alien_direction *= -1

    def check_fleet_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self.change_fleet_direction()
                break

    def check_aliens_bottom(self):
        """处理外星人碰到窗口底部"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self.ship_hit()
                break

    def fire_bullet(self):
        """创建一颗子弹,并加入group"""
        if len(self.bullets) < self.setting.bullet_max_num:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def start_game(self):
        """按下p键开始游戏"""
        if not self.status.is_running:
            self.status.is_running = True
            pygame.mouse.set_visible(False)
            self.status.reset_status()
            self.score_board.prep_font()

            self.aliens.empty()
            self.bullets.empty()

            self.create_alien_fleet()
            self.ship.center_ship()
            self.score_board.prep_ships()

    def ask_again(self):
        """由于退出后游戏记录没有了，所以要再次询问是否退出"""
        pygame.mouse.set_visible(True)
        self.status.is_running = False
        self.status.ask = True

    def is_key_down(self, event):
        """处理按键按下后飞船移动"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE and self.status.is_running:
            # 创造子弹
            self.fire_bullet()
        elif event.key == pygame.K_q:
            self.ask_again()
        elif event.key == pygame.K_p:
            if self.status.ship_left > 0:
                self.status.is_running = True
            else:
                self.start_game()
        elif event.key == pygame.K_s and self.status.is_running:
            # 暂停键
            self.status.is_running = False

    def is_key_up(self, event):
        """处理按键松开后飞船停止移动"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def check_mouse_pos(self, mouse_pos):
        """检查鼠标点击的坐标是否在play按键内部,点击成功后重置属性"""
        # 只有点击位置符合，并且在游戏非运行状态下，才会重置
        if self.play_button_easy.rect.collidepoint(mouse_pos) and not self.status.is_running:
            if self.status.ship_left > 0:
                self.status.is_running = True
            else:
                self.start_game()
        # 退出后提示，并选择
        elif self.play_button_easy.yes_rect.collidepoint(mouse_pos):

            with open("high_score.json", "w") as hs:
                json.dump(self.status.highest_score, hs)

            sys.exit()

        elif self.play_button_easy.no_rect.collidepoint(mouse_pos):
            self.status.ask = False

    def check_events(self):
        """ for循环为事件（用户鼠标或者键盘键入）循环，程序能够响应某些特定的事件,
            pygame.event.get() 可以返回列表，包含上一次调用后发生的事件
            event.type是事件类型,一般都是pygame.---
            event.KEY是键盘按键值,一般都是pygame.K_---
        """
        for event in pygame.event.get():
            # 退出程序
            if event.type == pygame.QUIT:
                self.status.is_running = False
                self.status.ask = True
            # 飞船移动
            elif event.type == pygame.KEYDOWN:
                self.is_key_down(event)
            elif event.type == pygame.KEYUP:
                self.is_key_up(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 返回一个元组，表示鼠标点击位置的x,y坐标
                mouse_pos = pygame.mouse.get_pos()
                self.check_mouse_pos(mouse_pos)

    def game_more_difficult(self):
        self.setting.alien_speed *= self.setting.speedup
        self.setting.ship_speed *= self.setting.speedup
        self.setting.alien_score = int(self.setting.alien_score * self.setting.score_up)

    def update_game_level(self):
        self.bullets.empty()
        self.create_alien_fleet()
        self.game_more_difficult()
        self.status.level += 1
        self.score_board.prep_level()

    def check_collision(self):
        """下面的方法用于检测子弹与外星人的碰撞，发生碰撞就在它返回的字典里添加一个键值对，这个字典是嵌套，在字典中嵌套列表，{ '子弹' ：[外星人列表],.....}两个True表示删除这两个rect元素"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                # 遍历所有键值对，击中多个外星人会加上相应数量的分数
                self.status.score += len(aliens) * self.setting.alien_score
            # 每当分数增加都要重新绘制分数
            self.score_board.prep_font()
            self.score_board.check_high()

        # 当外星人群为空，清空子弹，重建外星人群,提高游戏难度
        if not self.aliens:
            self.update_game_level()

    def update_bullets(self):
        """更新子弹位置，限制子弹数量，对group进行删除sprite"""
        # ↓执行该组内所有sprite的update函数，修改子弹的rect.y
        self.bullets.update()
        # python要求在用for循环遍历列表或group时不能编辑它，所以通过遍历副本，再实现删除
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # 检查子弹是否击中飞碟
        self.check_collision()

    def ship_hit(self):
        """飞船撞击飞碟后的处理，并在生命值用完后暂停游戏"""
        # 生命值-1
        self.status.ship_left -= 1
        if self.status.ship_left > 0:
            # 清空外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            self.setting.init_setting()

            # 重置飞船位置,重建外星人
            self.create_alien_fleet()
            self.ship.center_ship()
            self.score_board.prep_ships()

            # 暂停5秒
            sleep(0.5)
        else:
            self.status.is_running = False
            pygame.mouse.set_visible(True)

    def update_aliens(self):
        """利用group控制aliens_fleet移动"""

        # 检查是否碰到窗口边界，并改变移动方向
        self.check_fleet_edge()

        # 更新rect信息
        self.aliens.update()

        # 检测一个元素和一个group中的任意sprite碰撞，碰撞返回那个sprite,否则返回None
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()

        # 触底检测
        self.check_aliens_bottom()

    def update_screen(self):
        """根据发生的事件，更新主窗口显示"""
        # 设置背景色,screen是surface对象，由于fill是处理surface，并只有一种实参：颜色，所以screen可以调用fill
        self.screen.fill(self.setting.bg_color)

        # 确保飞船在填充背景后，否则被遮盖
        self.ship.blitme()

        # 更新子弹位置，后者返回一个列表，包括所有sprite
        # NOTE: 只有sprite是图片才可以使用group内置的draw方法绘制图像到主窗口上！，自制的rect用下面的办法进行一一绘制
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 不使用Alien类定义的方法，而是通过pygame.group中的draw方法将所有sprite绘制到screen上
        self.aliens.draw(self.screen)

        # 显示分数板
        self.score_board.show_score()

        # 当游戏状态暂停，显示Play按钮
        if not self.status.is_running and not self.status.ask:
            self.play_button_easy.draw_button()
        if not self.status.is_running and self.status.ask:
            self.play_button_easy.draw_ask()

        # 更新屏幕，让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        """控制游戏运行"""
        # while循环保证主窗口一直出现在屏幕上
        while True:
            self.check_events()

            if self.status.is_running:
                # 下面都是修改rect属性的，只有当游戏正常运行时才需要改变，如果不改变，下面更新屏幕也就没有意义了
                # 所谓的游戏结束就是不更新图像的rect属性
                self.ship.update()
                self.update_bullets()
                self.update_aliens()

            self.update_screen()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
