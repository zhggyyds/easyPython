import pygame.font


class Button:
    def __init__(self, ai_game, msg):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.width, self.height = 300, 50
        self.button_color = (200, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.y_rect = pygame.Rect(0, 0, 90, self.height)
        self.y_rect.left = self.rect.left
        self.y_rect.top = self.rect.bottom + 10

        self.n_rect = pygame.Rect(0, 0, 90, self.height)
        self.n_rect.right = self.rect.right
        self.n_rect.top = self.rect.bottom + 10

        self.prep_msg(msg)
        self.prep_ask()

    def prep_msg(self, msg):
        """将文字转换为图像，并设置rect为button框的中心"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def prep_ask(self):
        """再次确认按钮设置"""
        self.ask_image = self.font.render("Are you sure ?", True, self.text_color, self.button_color)
        self.ask_rect = self.ask_image.get_rect()
        self.ask_rect.center = self.rect.center

        self.yes_image = self.font.render("Yes", True, self.text_color, self.button_color)
        self.yes_rect = self.yes_image.get_rect()
        self.yes_rect.center = self.y_rect.center

        self.no_image = self.font.render("No", True, self.text_color, self.button_color)
        self.no_rect = self.no_image.get_rect()
        self.no_rect.center = self.n_rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_ask(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.ask_image, self.ask_rect)

        self.screen.fill(self.button_color, self.y_rect)
        self.screen.blit(self.yes_image, self.yes_rect)

        self.screen.fill(self.button_color, self.n_rect)
        self.screen.blit(self.no_image, self.no_rect)
