import pygame, sys
from player import Player

class Game:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        player_sprite = Player((screen_width / 2, screen_height),screen_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

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