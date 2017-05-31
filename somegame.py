import pygame
pygame.init()
pygame.display.set_caption("Example Program!")
screen = pygame.display.set_mode((640, 480))
myrect = pygame.Rect(128,128,16,16)
image = pygame.image.load("player.png")
brick = pygame.image.load("brick16x16.png")
tree = pygame.image.load("tree16x16.png")
clock = pygame.time.Clock()
running=True
# 40x30
mymap = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                TT  TTT               W",
"W                 TTT                  W",
"W                TT T                  W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                   W                  W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                   W                  W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"W                                      W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]
walls = []
trees = []
# Each row
wx = 0
wy = 0
for i in mymap:
        # Each Column
        for j in i:
                if j=="W":
                        walls.append((wx,wy))
                if j=="T":
                        trees.append((wx,wy))
                wx=wx+1
        wy=wy+1
        wx=0

wallsrects = []
for i in walls:
        wallsrects.append(pygame.Rect(i[0]*16,i[1]*16,16,16))
for i in trees:
        wallsrects.append(pygame.Rect(i[0]*16,i[1]*16,16,16))

wrect = pygame.Rect(0,0,16,16)

# move_axis = move one axis at a time
# NOTE: do not move more than one axis at at time
# person - is the rect of the object we want to move
# dx - the amount to move in the x direction
# dy - the amount to move in the y direction
def move_axis(person,dx,dy):
        person.x = person.x + dx
        person.y = person.y + dy
        # This is where we check for walls
        for i in wallsrects:
                if person.colliderect(i):
                        if dx>0:
                                person.right=i.left
                        if dx<0:
                                person.left=i.right
                        if dy>0:
                                person.bottom=i.top
                        if dy<0:
                                person.top=i.bottom        

# person - is the rect of the object we want to move
# dx - the amount to move in the x direction
# dy - the amount to move in the y direction
def move(person,dx,dy):
        if dx != 0:
                move_axis(person,dx,0)
        if dy != 0:
                move_axis(person,0,dy)

while running:
        clock.tick(300)
        screen.fill((66, 164, 244))
        screen.blit(image,myrect)
        for i in walls:
                wrect.x=i[0]*16
                wrect.y=i[1]*16
                screen.blit(brick,wrect)
        for i in trees:
                wrect.x=i[0]*16
                wrect.y=i[1]*16
                screen.blit(tree,wrect)
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
                move(myrect,0,-1)
        if key[pygame.K_DOWN]:
                move(myrect,0,1)
        if key[pygame.K_LEFT]:
                move(myrect,-1,0)
        if key[pygame.K_RIGHT]:
                move(myrect,1,0)
