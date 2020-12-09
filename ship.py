import pygame
from settings import Settings
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self, ai_settings, screen):
		'''Инициализирует корабль и задает его начальную позицию.'''
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#Загрузка изображения корабля и получение прямоугольника
		self.image = pygame.image.load('images/ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#Каждый новый корабль появляется у нижнего края 
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Сохранение вещественной координаты центра корабля 
		self.center = float(self.rect.centerx)
		# Флаги перемещения 
		self.moving_right = False
		self.moving_left = False
		
		# Обновление атрибута rect на основании self.center
		self.rect.centerx = self.center


	def blitme(self):
		'''Рисует корабль в текущей позиции'''
		self.screen.blit(self.image, self.rect)

	def update(self):
		'''Обновление позиции корабля с учетом флагов'''
		# Обновление артрибута center (не rect)
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= self.ai_settings.ship_speed_factor

	def center_ship(self):
		'''Размещает корабль в центре нижней стороны'''
		self.center = self.screen_rect.centerx
		
