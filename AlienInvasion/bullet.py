import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理从飞船上射击出来的子弹"""
    def __init__(self, ai_game):
        """初始化子弹类"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 创建一个0尺寸的子弹，然后设置其位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 用小数形式存储子弹位置
        self.y = float(self.rect.y)

    def update(self):
        """在屏幕上，从下向上移动子弹"""
        self.y -= self.settings.bullet_speed
        # 更新子弹位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上画出子弹"""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
