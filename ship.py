import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Инициализация корабля и указания начальных координат"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('Alien Invasion/images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.settings=ai_game.settings
        self.x=float(self.rect.x)

    def blitme(self):
        """Отрисовка корабля"""
        self.screen.blit(self.image, self.rect)
    def update(self):
        """Обновления координат корабля"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x +=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x -=self.settings.ship_speed
        self.rect.x=self.x
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)