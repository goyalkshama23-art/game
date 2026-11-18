import pygame
import random
screen_width, screen_height = 500, 400
movement_speed = 5
font_size = 72
pygame.init()
background_image = pygame.transform.scale(pygame.image.load("\\Users\\ankur\\OneDrive\\Documents\\python_codes\\lesson18\\lesson29\\bg.jpg"), (screen_width, screen_height))
font = pygame.font.SysFont("Times New Roman", font_size)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("dodgerblue"))
        pygame.draw.rect(self.image, color, pygame.Rect(0,0,width, height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, screen_width - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, screen_height - self.rect.height), 0)
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color("#D22222"), 20, 30)
sprite1.rect.x, sprite1.rect.y = (random.randint(0, screen_width- sprite1.rect.width), random.randint(0, screen_height- sprite1.rect.height))
all_sprites.add(sprite1)
sprite2 = Sprite(pygame.Color("#3efdb7"), 20, 30)
sprite2.rect.x, sprite2.rect.y = (random.randint(0, screen_width- sprite2.rect.width), random.randint(0, screen_height- sprite2.rect.height))
all_sprites.add(sprite2)
running, won = True, False
clock = pygame.time.Clock()
while running:
    if pygame.type == pygame.QUIT or (pygame.type == pygame.KEYDOWN and pygame.key == pygame.K_x):
        running = False
    if won:
        win_text = font.render("You Win", True, pygame.Color("#783838"))
        screen.blit(win_text, (screen_width - win_text.get_width())//2, (screen_height - win_text.get_height())//2)
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]*movement_speed)
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]*movement_speed)
        if sprite1.rect.colliderate(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True
        screen.blit(background_image, (0,0))
        all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(90)
pygame.quit()