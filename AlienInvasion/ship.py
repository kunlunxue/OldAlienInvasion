import pygame


class Ship:
    """管理飞船类"""
    def __init__(self, ai_game):
        """初始化飞船"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图片
        self.image = pygame.image.load('images/aoteman2.jpg')
        self.image = pygame.transform.scale(self.image, (80, 60))
        self.rect = self.image.get_rect()
        # 在屏幕的正下方显示飞船
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # 左右移动标志
        self.moving_right = False
        self.moving_left = False




    def blitme(self):
        """在当前位置画出飞船"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """根据左右移动标志，左右移动飞船"""
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        self.rect.x = self.x

