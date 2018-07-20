import pygame
import os
import background
import sprites
import projectiles
import player
import level
import titleScreen
import time

def start():
    #---------------------Game Loop--------------------------
    hp = player.health
    tabCount = 0
    chosenElement = element[0]      #defualt to fire

    while not title.isFinished():
        screen.fill((0,0,0))
        title.startTitle(screen)
        pygame.display.flip()
    printer = 0

    while not level1.isComplete(exitGroup):

        pygame.event.pump()
        xCounter = yCounter = 0
        for event in pygame.event.get():    #event handler, checks for key presses (not holds)
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    tabCount+=1
                    if tabCount >= len(element):
                        tabCount = 0
                    chosenElement = element[tabCount]
                    print(tabCount)
                elif event.key == pygame.K_SPACE and player.alive():
                    allSprites.add(projectiles.projectiles(player, chosenElement, enemies, player.rect.center))
                    magic.add(projectiles.projectiles(player, chosenElement, enemies, player.rect.center))



        screen.fill((0,0,0))                #reset screen, for clean animation
        background.makeBackground(screen, img, wallDown, sFloor, floor, tFloor, cFloor)
        myfont = pygame.font.SysFont('Comic Sans MS', 50)
        textsurface = myfont.render('Health: %d' %(hp), False, (255, 255, 255))
        screen.blit(textsurface,(0,0))
        myfont = pygame.font.SysFont('Comic Sans MS', 35)
        textsurface = myfont.render('Level 1 - Room 1', False, (255, 255, 255))
        screen.blit(textsurface,(425,0))
        if level1.isComplete(enemyGroup):
            for sp in por:
                sp.target = player
                sp.rect.center = (300,350)
                allSprites.add(sp)
                textsurface = myfont.render('"Exit has appeared!"', False, (255, 255, 255))
                screen.blit(textsurface,(100,300))
        if level1.isComplete(heroGroup):
            myfont = pygame.font.SysFont('Comic Sans MS', 50)
            textsurface = myfont.render('"Mr.Stark I dont feel so good..."', False, (255, 255, 255))
            screen.blit(textsurface,(100,300))
        allSprites.update(pygame.key.get_pressed())
        allSprites.draw(screen)
        pygame.display.flip()   #ACTUALLY display all the images
        clock.tick(60)      #all animation and timing is based on this 60fps counte

def level2(screen):
    L2 = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-','-','-','!'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
          ['-', '-', '-', '$', '-', '-', '*', '-', '-', '%','-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-']]

        #--------------Create some sprite variables--------------
    allSprites2 = pygame.sprite.Group()
    enemies = []
    chest1 = []
    chest2 = []
    chest3 = []
    hp = player.health
    por = []
    level2 = level.level(L2, enemies,chest1,chest2,chest3,por,screen)
    level2.makeLevel()
    element = ['projectiles/fireProj.png', 'projectiles/iceProj.png', 'projectiles/lightProj.png']
    magic = pygame.sprite.Group()
    obstacles = level2.boxes
    obstacleGroup = pygame.sprite.Group()
    for spr in level2.boxes:
        allSprites2.add(spr)
        obstacleGroup.add(spr)
    allSprites2.add(player)
    heroGroup = pygame.sprite.Group(player)
    for chest in chest1:
        chest.target = player
        allSprites2.add(chest)
    for chest in chest2:
        chest.target = player
        allSprites2.add(chest)
    for chest in chest3:
        chest.target = player
        allSprites2.add(chest)
    for sp in por:
        sp.target = player
        allSprites2.add(sp)
    for enemy in enemies:
        enemy.target = player
        allSprites2.add(enemy)
    exitGroup = pygame.sprite.Group(por)
    chest1Group = pygame.sprite.Group(chest1)
    chest2Group = pygame.sprite.Group(chest2)
    chest3Group = pygame.sprite.Group(chest3)

    tabCount = 0
    chosenElement = element[0]      #defualt to fire

        #-----------------------Load images----------------------
    while not level2.isComplete(exitGroup):

        pygame.event.pump()
        xCounter = yCounter = 0
        for event in pygame.event.get():    #event handler, checks for key presses (not holds)
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    tabCount+=1
                    if tabCount >= len(element):
                        tabCount = 0
                    chosenElement = element[tabCount]
                    print(tabCount)
                elif event.key == pygame.K_SPACE and player.alive():
                    allSprites2.add(projectiles.projectiles(player, chosenElement, enemies, player.rect.center))
                    magic.add(projectiles.projectiles(player, chosenElement, enemies, player.rect.center))
        screen.fill((0,0,0))                #reset screen, for clean animation
        background.makeBackground(screen, img, wallDown, sFloor, floor, tFloor, cFloor)
        if level2.isComplete(chest1Group):
            for sp in por:
                sp.target = player
                sp.rect.center = (300,350)
                allSprites2.add(sp)
                textsurface = myfont.render('"Exit has appeared!"', False, (255, 255, 255))
                screen.blit(textsurface,(100,300))
        if level2.isComplete(heroGroup):
            myfont = pygame.font.SysFont('Comic Sans MS', 50)
            textsurface = myfont.render('"Mr.Stark I dont feel so good..."', False, (255, 255, 255))
            screen.blit(textsurface,(100,300))
        if level2.isComplete(chest3Group):
            myfont = pygame.font.SysFont('Comic Sans MS', 20)
            textsurface = myfont.render('Radiation Effects : -2 HP', False, (255, 255, 255))
            screen.blit(textsurface,(50,30))
        if level2.isComplete(chest2Group):
            myfont = pygame.font.SysFont('Comic Sans MS', 20)
            textsurface = myfont.render('Health Bonus : +1 HP', False, (255, 255, 255))
            screen.blit(textsurface,(50,40))
        myfont = pygame.font.SysFont('Comic Sans MS', 50)
        hp = player.health
        textsurface = myfont.render('Health: %d' %(hp), False, (255, 255, 255))
        screen.blit(textsurface,(0,0))
        myfont = pygame.font.SysFont('Comic Sans MS', 35)
        textsurface = myfont.render('Level 1 - Room 2', False, (255, 255, 255))
        screen.blit(textsurface,(425,0))
        allSprites2.update(pygame.key.get_pressed())
        allSprites2.draw(screen)
        pygame.display.flip()   #ACTUALLY display all the images
        clock.tick(60)      #all animation and timing is based on this 60fps counter




#START OF MAIN

print(pygame.__path__)
pygame.init()


#--------------------Set some variables-------------------
himitsu = open(os.path.join('himitsu', 'passes.txt'), 'r')
lValue = int(himitsu.read())
himitsu.close()
width = 640
height = 480
center = ((480/2), (640/2))
size = width, height
screen = pygame.display.set_mode(size)  #opens the physical screen
clock = pygame.time.Clock()     #keeps track of the fps and stuff
check = 1


# Lets run some looooops!
while check != 0:
    L1 = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-','-','-','!'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
          ['-', '-', '-', 'X', 'X', 'X', 'X', 'X', 'X', 'X','-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
          ['-', '-', '#', '#', '#', '-', '-', '-', '#', '#','#', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-']]



    #--------------Create some sprite variables--------------
    allSprites = pygame.sprite.Group()
    enemies = []
    por = []
    chest1 = []
    chest2 = []
    chest3 = []
    level1 = level.level(L1, enemies,chest1,chest2,chest3,por,screen)
    level1.makeLevel()
    element = ['projectiles/fireProj.png', 'projectiles/iceProj.png', 'projectiles/lightProj.png']
    magic = pygame.sprite.Group()
    obstacles = level1.boxes
    obstacleGroup = pygame.sprite.Group()
    for spr in level1.boxes:
        allSprites.add(spr)
        obstacleGroup.add(spr)
    player = player.player('Character/DownAnim/Down2.png', obstacles, (width/2, height-50))
    allSprites.add(player)
    heroGroup = pygame.sprite.Group(player)
    for sp in por:
        sp.target = player
        allSprites.add(sp)
    for enemy in enemies:
    	enemy.target = player
    	allSprites.add(enemy)
    enemyGroup = pygame.sprite.Group(enemies)
    exitGroup = pygame.sprite.Group(por)

    #-----------------------Load images-----------------------
    img = pygame.image.load('images/bot_wall.jpg').convert()
    wallDown = pygame.image.load('images/Side_Walls_05.jpg').convert()
    sFloor = pygame.image.load('images/Left_edge_floor.jpg').convert()
    floor = pygame.image.load('images/floor.jpg').convert()
    tFloor = pygame.image.load('images/Top_edge_floor.jpg').convert()
    cFloor = pygame.image.load('images/Left_corner_floor.jpg').convert()
    title = titleScreen.titleScreen(lValue)
    hp = player.health
    start()
    level2(screen)



exit()
