class Settings:
    """存储外星人入侵游戏所有的设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (19, 70, 149)
        # 飞船设置
        self.ship_speed = 1.5
        # 子弹设置
        self.bullet_speed = 3
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 外星人移动速度
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 舰队方向
        self.fleet_direction = 1
