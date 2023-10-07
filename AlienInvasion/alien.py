import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """舰队中单个外星人"""
    def __init__(self, ai_game):
        """初始化外星人 并 设置位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings

        # 加载外星人图片 并 设置其 矩形属性
        self.image = pygame.image.load('images/monster.bmp')
        self.image = pygame.transform.scale(self.image, (80, 60))
        self.rect = self.image.get_rect()

        # 存储外星人具体的水平位置x坐标
        self.x = float(self.rect.x)

    def update(self):
        """向右移动外星人"""
        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """返回真，如果有外星人碰触到左右屏幕界限"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
