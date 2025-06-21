import pygame, sys
from player import Player
import obstacle
from alien import Alien, Extra
from random import choice, randint
from laser import Laser

class Game:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        player_sprite = Player((screen_width / 2, screen_height),screen_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    	# health and score setup
        self.lives = 3
        self.live_surf = pygame.image.load('/graphics/player.png').convert_alpha()
        self.live_x_start_pos = screen_width - (self.live_surf.get_size()[0] * 2 + 20)
        self.score = 0
        self.font = pygame.font.Font('/font/Pixeled.ttf',20)

    def run(self):
        self.player.draw(self.screen)
        self.player.update()

if __name__ == "__main__":
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    game = Game(screen, screen_width, screen_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30))
        game.run()
        pygame.display.flip()
        clock.tick(60)