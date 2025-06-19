import pygame
pygame.init()
pygame.font.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_CAPTION = "MY FIRST GAME SCREEN"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RECT_COLOR = BLUE
RECT_WIDTH = 200
RECT_HEIGHT = 100
TEXT_CONTENT = "Hello, Pygame!"
TEXT_COLOR = BLACK
FONT_SIZE = 48
FONT_NAME = None
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_CAPTION)
rectangle = pygame.Rect(0, 0, RECT_WIDTH, RECT_HEIGHT)
rectangle.centerx = WINDOW_WIDTH // 2
rectangle.centery = WINDOW_HEIGHT // 2
font = pygame.font.Font(None, FONT_SIZE)
text_surface = font.render(TEXT_CONTENT, True, TEXT_COLOR)
text_rect = text_surface.get_rect()
text_rect.centerx = WINDOW_WIDTH // 2
text_rect.bottom = rectangle.top - 20
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, RECT_COLOR, rectangle)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()