class Setting:
    """游戏属性默认设置"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_blue = (187, 255, 255)
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 子弹属性
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_max_num = 10

        # 外星人
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.alien_direction = 1

        self.rain_width = 60
        self.rain_height = 57

        self.alien_score = 10

        # 增加游戏难度
        self.speedup = 1.1
        self.score_up = 1.5

    def init_setting(self):
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.alien_direction = 1
        self.alien_score = 10
