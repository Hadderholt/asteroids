import pygame
from constants import *
from player import Player  # Add this import


def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x, y)  # Store the Player object in a variable
	
	# Game Loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		
		dt = clock.tick(60) / 1000
		player.update(dt)
		
		screen.fill((0, 0, 0))
		player.draw(screen)  # Now you can use the player variable
		pygame.display.flip()
		


if __name__ == "__main__":
	main()
