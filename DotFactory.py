from Dot import Dot
from random import random as r


class DotFactory:
	def __init__(self, x, y, gx, gy, screen, pop, obs):
		self.dots = []
		self.pop = pop
		self.x = x
		self.y = y
		self.obs = obs
		for i in range(pop):
			self.dots.append(Dot(x, y, r()*20-10, r()*20-10, gx, gy, screen, obs))
		self.minStep = 10000
		self.fitnessSum = 0
		self.bestDot = 0
		self.gen = 0

	def show(self):
		for d in self.dots:
			d.show()

	def update(self):
		for d in self.dots:
			if d.steps > self.minStep + 300:
				d.dead = True
			else:
				d.move()

	def calculateFitness(self):
		self.fitnessSum = 0
		for d in self.dots:
			self.fitnessSum += d.calculateFitness()

	def allDotsDead(self):
		for d in self.dots:
			if not d.dead and not d.reachedGoal:
				return False
		return True

	def naturalSelection(self):
		newDots = []
		self.setBestDot()
		self.calculateFitness()

		newDots.append(self.dots[self.bestDot].clone(self.x, self.y))
		newDots[0].isBest = True

		for i in range(1, self.pop):
			newDots.append(self.selectParent().clone(self.x, self.y))

		self.dots = newDots[:]
		self.gen += 1


	def setBestDot(self):
		max = 0
		mi = 0
		for i in range(len(self.dots)):
			if self.dots[i].calculateFitness() > max:
				max = self.dots[i].calculateFitness()
				mi = i

		self.bestDot = mi

		if self.dots[mi].reachedGoal:
			self.minStep = self.dots[mi].steps

	def selectParent(self):
		threshold = r()*self.fitnessSum
		s = 0

		for d in self.dots:
			s += d.calculateFitness()
			if s > threshold:
				return d

		# Shouldn't hit this point
		print(self.fitnessSum, threshold, s)

		return None

	def mutate(self, rate):
		for i in range(1, len(self.dots)):
			self.dots[i].mutate(rate)
