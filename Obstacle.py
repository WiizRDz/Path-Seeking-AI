import pygame


class Obstacle:
	def __init__(self, x, y, w, h, screen):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.screen = screen

	def draw(self):
		pygame.draw.rect(self.screen, (0, 0, 255), (self.x, self.y, self.w, self.h), 0)

	def collide(self, ox, oy):
		return self.x <= ox <= self.x + self.w and self.y <= oy <= self.y + self.h
