import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Try to load the image, if it fails, create a colored rectangle
        try:
            self.image = pygame.image.load('graphics/player.png').convert_alpha()
        except pygame.error:
            # Create a simple colored rectangle if image doesn't exist
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))  # Red rectangle
        
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 5
        print(f"Player created at position: {self.rect.x}, {self.rect.y}")

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            print(f"Moving right to: {self.rect.x}")
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            print(f"Moving left to: {self.rect.x}")

    def update(self):
        self.get_input()