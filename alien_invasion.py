import pygame
from settings import Settings
from gamestats import GameStats
from scoreboard import ScoreBoard 
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
	# Инициализирует pygame, settings и объект экрана
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Создание кнопки Play.
	play_button = Button(ai_settings, screen, 'Play')
	
	# Создание экземпляра GameStats и ScoreBoard.
	stats = GameStats(ai_settings)
	sb = ScoreBoard(ai_settings, screen, stats)
	# Создание корабля
	ship = Ship(ai_settings, screen)
	# Создание группы для хранения пуль
	bullets = Group()
	# Создание группы пришельцев
	aliens = Group()

	# Создание флота пришельцев
	gf.create_fleet(ai_settings, screen, ship, aliens) 

	# Запуск основного цикла игры
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

	
run_game()
