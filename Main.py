import pygame
import DotFactory
import Obstacle
screen = pygame.display.set_mode((1250, 750))
pygame.display.set_caption("Gen 0")
pygame.font.init()
pygame.init()

clock = pygame.time.Clock()

if __name__ == "__main__":
	obs = [Obstacle.Obstacle(250, 300, 750, 50, screen), Obstacle.Obstacle(250, 0, 50, 300, screen)]
	factory = DotFactory.DotFactory(screen.get_width()/2, screen.get_height() - 50, screen.get_width()/2, 50, screen, 1000, obs)

	while factory.gen < 10:
		pygame.display.set_caption("Gen " + str(factory.gen))
		clock.tick(150)
		screen.fill((255, 255, 255))

		pygame.draw.circle(screen, (255, 0, 0), (round(screen.get_width()/2), 50), 10)

		if factory.allDotsDead():
			factory.calculateFitness()
			factory.naturalSelection()
			factory.mutate(0.1)
		else:
			for o in obs:
				o.draw()
			factory.update()
			factory.show()

		pygame.display.flip()

		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			break


