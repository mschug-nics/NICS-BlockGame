import pygame
pygame.init()
pygame.display.set_caption("Example Program!")
screen = pygame.display.set_mode((640, 480))
myrect = pygame.Rect(128,128,16,16)
image = pygame.image.load("player.png")
brick = pygame.image.load("brick16x16.png")
clock = pygame.time.Clock()
running=True
# 40x30
walls = [(0,0),(1,1),(2,2)]
wrect = pygame.Rect(0,0,16,16)
while running:
        clock.tick(300)
        screen.fill((66, 164, 244))
        screen.blit(image,myrect)
        for i in walls:
                wrect.x=i[0]*16
                wrect.y=i[1]*16
                screen.blit(brick,wrect)
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
                if event.type == pygame.QUIT:
                        pygame.quit()
                        running=False
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
                pygame.quit()
                running=False
        if key[pygame.K_UP]:
                if myrect.y>0:
                        myrect.y=myrect.y-1
        if key[pygame.K_DOWN]:
                if myrect.y<480-16:
                        myrect.y=myrect.y+1
        if key[pygame.K_LEFT]:
                if myrect.x>0:
                        myrect.x=myrect.x-1
        if key[pygame.K_RIGHT]:
                if myrect.x<640-16:
                        myrect.x=myrect.x+1
