import pygame
from random import random as r


class Dot:
	def __init__(self, x, y, xv, yv, gx, gy, screen, obs):
		self.x = x
		self.y = y
		self.xv = xv
		self.yv = yv
		self.gx = gx
		self.gy = gy
		self.steps = 0
		self.reachedGoal = False
		self.dead = False
		self.isBest = False
		self.screen = screen
		self.obs = obs

	def move(self):
		if not self.reachedGoal and not self.dead:
			if self.x < 10 or self.x > self.screen.get_width():
				self.xv *= -1
			if self.y < 10 or self.y > self.screen.get_height():
				self.yv *= -1
			self.x += self.xv
			self.y += self.yv
			self.steps += 1
		if ((self.x - self.gx)**2 + (self.y - self.gy)**2)**.5 < 12:
			self.reachedGoal = True
		if self.steps > 600:
			self.dead = True
		for o in self.obs:
			if o.collide(self.x, self.y):
				self.dead = True
				# self.xv *= -1
				# self.yv *= -1

	def show(self):
		if self.isBest:
			pygame.draw.circle(self.screen, (0, 255, 0), (round(self.x), round(self.y)), 8)
		else:
			pygame.draw.circle(self.screen, (0, 0, 0), (round(self.x), round(self.y)), 5)

	def calculateFitness(self):
		if self.reachedGoal:
			fitness = 1.0 / float(self.steps)
		else:
			fitness = 1.0 / float(((self.x - self.gx)**2 + (self.y - self.gy)**2)**1.5)
		return fitness

	def clone(self, x, y):
		return Dot(x, y, -1*self.xv, self.yv, self.gx, self.gy, self.screen, self.obs)

	def mutate(self, rate):
		if r() < rate:
			self.xv += r() * 2 - 1
			self.yv += r() * 2 - 1
