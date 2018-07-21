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

        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render('Welcome to the dungeon', False, (255, 255, 255))
        screen.blit(textsurface,(425,25))
        if level1.isComplete(enemyGroup):
            for sp in por:
                sp.target = player
                sp.rect.center = (300,50)
                allSprites.add(sp)
                textsurface = myfont.render('"Exit has appeared!"', False, (255, 255, 255))
                screen.blit(textsurface,(100,300))
        if level1.isComplete(heroGroup):
            myfont = pygame.font.SysFont('Comic Sans MS', 50)
            textsurface = myfont.render('"Dead already?!"', False, (255, 255, 255))
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
        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render('Get some hair on your chest', False, (255, 255, 255))
        screen.blit(textsurface,(405,25))
        allSprites2.update(pygame.key.get_pressed())
        allSprites2.draw(screen)
        pygame.display.flip()   #ACTUALLY display all the images
        clock.tick(60)      #all animation and timing is based on this 60fps counter

def level3(screen):
    L3 = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-','-','-','!'],
          ['-', '-', '-', '#', '-', '-', 'X', '-', '#', '-','-', '-', '-'],
          ['-', '-', '-', 'X', '-', '-', 'X', '-', '-', 'X','¡', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
          ['-', '-', '-', '-', '#', '-', '#', '-', '#', '-','#', '-', '-'],
          ['-', '-', '#', '-', '-', '-', '-', '-', '#', '-','-', '-', '-'],
          ['-', '¡', '-', '-', '-', '-', '-', '-', '-', '-','-', '#', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-']]

        #--------------Create some sprite variables--------------
    allSprites3 = pygame.sprite.Group()
    enemies = []
    chest1 = []
    chest2 = []
    chest3 = []
    hp = player.health
    por = []
    level3 = level.level(L3, enemies,chest1,chest2,chest3,por,screen)
    level3.makeLevel()
    element = ['projectiles/fireProj.png', 'projectiles/iceProj.png', 'projectiles/lightProj.png']
    magic = pygame.sprite.Group()
    allSprites3.add(player)
    heroGroup = pygame.sprite.Group(player)
    obstacles = level3.boxes
    obstacleGroup = pygame.sprite.Group()
    for spr in level3.boxes:
        allSprites3.add(spr)
        obstacleGroup.add(spr)
        spr.target = player
    for chest in chest1:
        chest.target = player
        allSprites3.add(chest)
    for chest in chest2:
        chest.target = player
        allSprites3.add(chest)
    for chest in chest3:
        chest.target = player
        allSprites3.add(chest)
    for sp in por:
        sp.target = player
        allSprites3.add(sp)
    for enemy in enemies:
        enemy.target = player
        allSprites3.add(enemy)
    enemygroup = pygame.sprite.Group(enemies)
    exitGroup = pygame.sprite.Group(por)
    chest1Group = pygame.sprite.Group(chest1)
    chest2Group = pygame.sprite.Group(chest2)
    chest3Group = pygame.sprite.Group(chest3)

    tabCount = 0
    chosenElement = element[0]      #defualt to fire

        #-----------------------Load images----------------------
    while not level3.isComplete(exitGroup):

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
                    allSprites3.add(projectiles.projectiles(player, chosenElement, enemies, player.rect.center))
                    magic.add(projectiles.projectiles(player, chosenElement, enemies, player.rect.center))
        screen.fill((0,0,0))                #reset screen, for clean animation
        background.makeBackground(screen, img, wallDown, sFloor, floor, tFloor, cFloor)
        if level3.isComplete(enemygroup):
            for sp in por:
                sp.target = player
                sp.rect.center = (300,350)
                allSprites3.add(sp)
                myfont = pygame.font.SysFont('Comic Sans MS', 30)
                textsurface = myfont.render('"Exit has appeared!"', False, (255, 255, 255))
                screen.blit(textsurface,(120,300))
        if level3.isComplete(heroGroup):
            myfont = pygame.font.SysFont('Comic Sans MS', 50)
            textsurface = myfont.render('"Mr.Stark I dont feel so good..."', False, (255, 255, 255))
            screen.blit(textsurface,(100,300))
        myfont = pygame.font.SysFont('Comic Sans MS', 50)
        hp = player.health
        textsurface = myfont.render('Health: %d' %(hp), False, (255, 255, 255))
        screen.blit(textsurface,(0,0))
        myfont = pygame.font.SysFont('Comic Sans MS', 35)
        textsurface = myfont.render('Level 2 - Room 1', False, (255, 255, 255))
        screen.blit(textsurface,(425,0))
        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render('More dungeon stuff', False, (255, 255, 255))
        screen.blit(textsurface,(415,25))
        allSprites3.update(pygame.key.get_pressed())
        allSprites3.draw(screen)
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
    L1 = [['-', '-', '-', 'X', 'X', '-', '-', '-', '-', 'X','X', '-', '-','-','-','!'],
          ['-', '-', '#', '-', 'X', '-', '-', '-', '-', 'X','-', '#', '-'],
          ['-', '-', '¡', '-', '#', '-', '-', '-', '-', '#','-', '¡', '-'],
          ['-', '-', '-', '-', '¡', '-', '-', '-', '-', '¡','-', '-', '-'],
          ['-', '-', '#', '-', '#', '-', '-', '-', '-', '#','-', '#', '-'],
          ['-', '-', '¡', '-', '-', '-', '-', '-', '-', '-','-', '¡', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
          ['-', '-', '-', '-', '¡', '-', '-', '-', '-', '¡','-', '-', '-']]



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
    for x in obstacleGroup.sprites():
        x.kill()
        x.rect.center = (-55,-55) #Put self out-of-bounds -- but not (-5,-5)
    level2(screen)
    level3(screen)

    exit()
