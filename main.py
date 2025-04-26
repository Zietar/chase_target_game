'''
gracz chodzenie, nie wychodz poza ekran
jeśli wykryta kolizja z graczem wyświetl w innym losowym miejscu
punkty
'''
import pygame
import random

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 35)
running = True

background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background, (screen_width, screen_height))

player = pygame.Rect(64, 64, 32, 32)
speed = 4

target = pygame.Rect(128, 128, 32, 32)

score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dx, dy = 0, 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        dy -= speed
    if keys[pygame.K_s]:
        dy += speed
    if keys[pygame.K_a]:
        dx -= speed
    if keys[pygame.K_d]:
        dx += speed

    player.x += dx
    player.y += dy

    if player.left < 0:
        player.left = 0
    if player.right > screen_width:
        player.right = screen_width
    if player.top < 0:
        player.top = 0
    if player.bottom > screen_height:
        player.bottom = screen_height

    if player.colliderect(target):
        target.x = random.randint(0, screen_width - target.width)
        target.y = random.randint(0, screen_height - target.height)
        score += 1

    screen.blit(background)

    pygame.draw.rect(screen, "green", player)

    pygame.draw.rect(screen, "red", target)

    text = font.render(f"Score: {score}", True, (20, 20, 20))
    screen.blit(text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()