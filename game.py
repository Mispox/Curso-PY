import sys
import pygame
import button

pygame.init()

screen_width = 800
screen_height = 600
fps = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The funny oen :D")

font = pygame.font.SysFont("Lilita One", 40)

text_color = (0, 0, 0)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

running = True
while running:

    screen.fill((237, 171, 207))

    draw_text("THE FUNNY OEN :D", font, text_color, 250, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = false

    pygame.display.update()

pygame.quit()