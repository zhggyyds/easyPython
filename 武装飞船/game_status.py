# 管理整个游戏状态的类
import json

class GameStatus:
    def __init__(self, ai_game):

        self.setting = ai_game.setting
        self.is_running = False
        self.ask = False
        self.reset_status()

        with open("high_score.json") as hs:
            self.highest_score = json.load(hs)

    def reset_status(self):
        self.ship_left = self.setting.ship_limit
        self.score = 0
        self.level = 1

