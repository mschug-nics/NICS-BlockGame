import pygame
pygame.init()
pygame.display.set_caption("Example Program!")
screen = pygame.display.set_mode((640, 480))
myrect = pygame.Rect(0,0,640,480)
image = pygame.image.load("player.png")
running=True
clock = pygame.time.Clock()
while running:
        clock.tick(60)
        screen.fill((0, 0, 0))
        screen.blit(image,myrect)
        pygame.display.flip()        
        events = pygame.event.get()
        for event in events:
                if event.type == pygame.QUIT:
                        running=False
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
                pygame.quit()
                running=False
        if key[pygame.K_UP]:
                myrect.y=myrect.y-5
        if key[pygame.K_DOWN]:
                myrect.y=myrect.y+5
        if key[pygame.K_LEFT]:
                myrect.x=myrect.x-5
        if key[pygame.K_RIGHT]:
                myrect.x=myrect.x+5
        if key[pygame.K_SPACE]:
                pygame.quit()
                running=False
