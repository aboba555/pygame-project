import pygame
pygame.init()

window = pygame.display.set_mode((1500,1000))

pygame.display.set_caption("Game")

clock = pygame.time.Clock()

playerStand = [pygame.image.load("png/Idle (1).png"),
    pygame.image.load("png/Idle (2).png"),
    pygame.image.load("png/Idle (3).png"),
    pygame.image.load("png/Idle (4).png"),
    pygame.image.load("png/Idle (5).png"),
    pygame.image.load("png/Idle (6).png"),
    pygame.image.load("png/Idle (7).png"),
    pygame.image.load("png/Idle (8).png"),
    pygame.image.load("png/Idle (9).png"),
    pygame.image.load("png/Idle (10).png"),]

walkRight =[pygame.image.load("png/Walk (1).png"),
    pygame.image.load("png/Walk (2).png"),
    pygame.image.load("png/Walk (3).png"),
    pygame.image.load("png/Walk (4).png"),
    pygame.image.load("png/Walk (5).png"),
    pygame.image.load("png/Walk (6).png"),
    pygame.image.load("png/Walk (7).png"),
    pygame.image.load("png/Walk (8).png"),
    pygame.image.load("png/Walk (9).png"),
    pygame.image.load("png/Walk (10).png"),]

walkLeft =[pygame.image.load("png/Walk (1).png"),
    pygame.image.load("png/Walk (2).png"),
    pygame.image.load("png/Walk (3).png"),
    pygame.image.load("png/Walk (4).png"),
    pygame.image.load("png/Walk (5).png"),
    pygame.image.load("png/Walk (6).png"),
    pygame.image.load("png/Walk (7).png"),
    pygame.image.load("png/Walk (8).png"),
    pygame.image.load("png/Walk (9).png"),
    pygame.image.load("png/Walk (10).png"),]

playerJump = [pygame.image.load("png/Jump (2).png"),
# pygame.image.load("png/Jump (3).png"),
# pygame.image.load("png/Jump (4).png"),
pygame.image.load("png/Jump (5).png"),
# pygame.image.load("png/Jump (6).png"),
pygame.image.load("png/Jump (7).png"),
# pygame.image.load("png/Jump (8).png"),
# pygame.image.load("png/Jump (9).png"),
pygame.image.load("png/Jump (10).png"),
pygame.image.load("png/Jump (11).png"),
pygame.image.load("png/Jump (12).png")
              ]

bg = pygame.image.load("png/beach-game-py.png")




x,y = 50,580
width,height = 472,680
speed = 10

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

def drawWindow():
    global animCount
    window.blit(bg, (0, 0))
    if animCount + 1 >= 30:
        animCount = 0

    if left:
        window.blit(walkLeft[animCount//5],(x,y))
        animCount += 1
    elif right:
        window.blit(walkRight[animCount//5],(x,y))
        animCount += 1
    elif isJump:
        window.blit(playerJump[animCount//5],(x,y))
        animCount += 1
    else:
        window.blit(playerStand[animCount//5],(x,y))


    # pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))
    pygame.display.update()




run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 2:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1500-width+100:
        x += speed
        right = True
        left = False
    else:
        right = False
        left = False
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0 :
                y += (jumpCount ** 2)
            else:
                y -= (jumpCount ** 2)
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()





pygame.quit()

