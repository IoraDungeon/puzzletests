import pygame
import sprites
import projectiles
import chest
import pygame
import enemy
import portal

class level():
	def __init__(self, design, enemies,chest1,chest2,chest3,portal,screen):	  #design is a 2d list
		self.boxGroup = pygame.sprite.Group()
		self.boxes = []
		self.enemies = enemies
		self.chest1 = chest1
		self.chest2 = chest2
		self.chest3 = chest3
		self.exit = portal
		self.screen = screen
		self.design = design
		self.isPuzzleDone = False



	def makeLevel(self):
		counter = 0
		xSpot = 16
		ySpot = 16
		for x in self.design:
			for y in x:
				print(y)
				if y is '#':
					self.boxes.append(sprites.sprites('Obstacles/box.png', (xSpot, ySpot)))
					self.boxGroup.add(self.boxes[counter])
					counter+=1
				xSpot+=48
			xSpot=0
			ySpot+=58
		xSpot = 16
		ySpot = 16
		for x in self.design:
			for y in x:
				print(y)
				if y is '¡':
					self.boxes.append(sprites.sprites('Obstacles/torch.gif', (xSpot, ySpot)))
					self.boxGroup.add(self.boxes[counter])
					counter+=1
				xSpot+=48
			xSpot=0
			ySpot+=58
		xSpot = 16
		ySpot = 16
		for x in self.design:
			for y in x:
				print(y)
				if y is '!':
					self.exit.append(portal.portal('images/portal.png', (xSpot, ySpot), self.boxes))
				xSpot+=48
			xSpot=0
			ySpot+=58
		#Reset counters to iterate through again -- this time for spawning enemies.
		#(Obstacles list must be passed in for each enemy.)
		xSpot = 16
		ySpot = 16
		for x in self.design:
			for y in x:
				print(y)
				if y is '*':
					self.chest1.append(chest.chest('Obstacles/chest.png', (xSpot, ySpot), self.boxes,1,self.screen))
				xSpot+=48
			xSpot=0
			ySpot+=58
		xSpot = 16
		ySpot = 16
		for x in self.design:
			for y in x:
				print(y)
				if y is '%':
					self.chest2.append(chest.chest('Obstacles/chest.png', (xSpot, ySpot), self.boxes,2,self.screen))
				xSpot+=48
			xSpot=0
			ySpot+=58

		xSpot = 16
		ySpot = 16
		for x in self.design:
			for y in x:
				print(y)
				if y is '$':
					self.chest3.append(chest.chest('Obstacles/chest.png', (xSpot, ySpot), self.boxes,3,self.screen))
				xSpot+=48
			xSpot=0
			ySpot+=58
		#Reset counters to iterate through again -- this time for spawning enemies.
		#(Obstacles list must be passed in for each enemy.)
		xSpot = 16
		ySpot = 16
		for x in self.design:
			for y in x:
				if y is 'X':
					self.enemies.append(enemy.enemy('Enemies/slime.png', (xSpot, ySpot), self.boxes))
				xSpot+=48
			xSpot=0
			ySpot+=58

	def isComplete(self, enemyGroup):		   #checks to see if all enemies are cleared out
		print(enemyGroup)
		if not enemyGroup:
			return True
		return False
