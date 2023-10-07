import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏资源，包括数字资产和行为"""
    def __init__(self):
        """初始化游戏，创建游戏资源"""
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("星际大战")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_sound("bgm")

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监控键盘和鼠标
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self.bullet_delete()
            self._update_aliens()
            # 重画背景颜色 实时刷新屏幕
            self._update_screen()

    def _check_events(self):
        """响应键鼠活动"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_event_keyup_events(event)

    def _check_keydown_events(self, event):
        """处理按键按下动作"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            self.play_sound("bullet_out")

    def play_sound(self, sound_type):
        if sound_type == "bullet_out":
            sound = pygame.mixer.Sound('sounds/bullet_out.wav')
            sound.set_volume(0.8)
            sound.play()
        elif sound_type == "bgm":
            pygame.mixer.music.load('sounds/bgm.wav')
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play(99999)
            #pygame.mixer.music.rewind()
            #sound = pygame.mixer_music('/sound/bgm.wav')
            #sound.set_volume(0.6)
        elif sound_type == "collision":
            sound = pygame.mixer.Sound('sounds/collision.wav')
            sound.set_volume(0.8)
            sound.play()


    def _check_event_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_SPACE:
            print("处理空格键")
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullet(self):
        """创建子弹，并将其加入粒子系统组"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def bullet_delete(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(self.bullets)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            """播放爆炸声音"""
            self.play_sound("collision")
        if not self.aliens:
            self._create_fleet()

    def _update_screen(self):
        """更新屏幕上的图像，刷新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        """创建外星人攻击舰队"""
        # 创建一个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 找出屏幕的高度能容纳的外形舰队的行数
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """创建外星人并将其加入队列"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width) * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """更新外星人位置"""
        self._check_fleet_edges()
        self.aliens.update()


    def _check_fleet_edges(self):
        """如果有外星人碰触到左右屏幕，改变舰队横向移动方向"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """向下移动舰队 改变舰队方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1


if __name__ == '__main__':
    # 初始化游戏实例 ，运行游戏
    ai = AlienInvasion()
    ai.run_game()
