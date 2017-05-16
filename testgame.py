import pygame
pygame.init()
pygame.display.set_caption("Example Program!")
screen = pygame.display.set_mode((640, 480))
myrect = pygame.Rect(0,0,640,480)
image = pygame.image.load("player.png")
screen.fill((0, 0, 0))
screen.blit(image,myrect)
pygame.display.flip()
running=True
while running:
        events = pygame.event.get()
        for event in events:
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                                pygame.quit()
                                running=False
