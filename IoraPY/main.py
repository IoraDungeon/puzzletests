import pygame
import os
import background
import sprites
import projectiles
import player
import level
import titleScreen
import time


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
items = []
exit = []
level1 = level.level(L1, enemies,items,exit)
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
for chest in items:
	chest.target = player
	allSprites.add(chest)
for sp in exit:
    sp.target = player
    allSprites.add(sp)
for enemy in enemies:
	enemy.target = player
	allSprites.add(enemy)
enemyGroup = pygame.sprite.Group(enemies)
exitGroup = pygame.sprite.Group(exit)

#-----------------------Load images-----------------------
img = pygame.image.load('images/bot_wall.jpg').convert()
wallDown = pygame.image.load('images/Side_Walls_05.jpg').convert()
sFloor = pygame.image.load('images/Left_edge_floor.jpg').convert()
floor = pygame.image.load('images/floor.jpg').convert()
tFloor = pygame.image.load('images/Top_edge_floor.jpg').convert()
cFloor = pygame.image.load('images/Left_corner_floor.jpg').convert()
title = titleScreen.titleScreen(lValue)
#---------------------Game Loop--------------------------
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
    hp = player.health
    textsurface = myfont.render('Health: %d' %(hp), False, (255, 255, 255))
    screen.blit(textsurface,(0,0))
    """
        myfont = pygame.font.SysFont('Comic Sans MS', 50)
        textsurface = myfont.render('Who is the best teacher?', False, (255, 255, 255))
        screen.blit(textsurface,(150,235))
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        textsurface = myfont.render('Sharanya', False, (255, 255, 255))
        screen.blit(textsurface,(60,335))
        textsurface = myfont.render('Not Sharanya', False, (255, 255, 255))
        screen.blit(textsurface,(250,335))
        textsurface = myfont.render('Not Sharanya', False, (255, 255, 255))
        screen.blit(textsurface,(450,335))
    """
    if level1.isComplete(enemyGroup):
        for sp in exit:
            sp.target = player
            sp.rect.center = (300,350)
            allSprites.add(sp)
    allSprites.update(pygame.key.get_pressed())
    allSprites.draw(screen)
    pygame.display.flip()   #ACTUALLY display all the images
    clock.tick(60)      #all animation and timing is based on this 60fps counte

L2 = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-','-','-','!'],
      ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
      ['-', '-', '-', '*', '-', '-', '*', '-', '-', '*','-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-']]

    #--------------Create some sprite variables--------------
allSprites2 = pygame.sprite.Group()
enemies = []
items = []
exit = []
level2 = level.level(L2, enemies,items,exit)
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
for chest in items:
    chest.target = player
    allSprites2.add(chest)
for sp in exit:
    sp.target = player
    allSprites2.add(sp)
for enemy in enemies:
    enemy.target = player
    allSprites2.add(enemy)
exitGroup = pygame.sprite.Group(exit)
itemsGroup = pygame.sprite.Group(items)

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
    if level2.isComplete(itemsGroup):
        for sp in exit:
            sp.target = player
            sp.rect.center = (300,350)
            allSprites2.add(sp)
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    hp = player.health
    textsurface = myfont.render('Health: %d' %(hp), False, (255, 255, 255))
    screen.blit(textsurface,(0,0))
    allSprites2.update(pygame.key.get_pressed())
    allSprites2.draw(screen)
    pygame.display.flip()   #ACTUALLY display all the images
    clock.tick(60)      #all animation and timing is based on this 60fps counter


exit()
