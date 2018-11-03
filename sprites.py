"""

Sprites: All game objects and entities.

"""
import pygame as pg
from settings import *
# DEFINE PLAYER CLASS
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites # ADD TO ALL SPRITES GROUP
        pg.sprite.Sprite.__init__(self, self.groups) #INIT SPRITE
        self.image = pg.Surface((TILESIZE, TILESIZE)) # DEFINE IMAGE SIZE
        self.image.fill(GREEN) # FILL IMAGE WITH GREEN
        self.rect = self.image.get_rect() # DEFINE RECTANGLE COORDS
        self.game = game
        self.x = x
        self.y = y

    def update(self): # UPDATE METHOD
        self.rect.x = self.x * TILESIZE # ONLY ALLOW MOVEMENT BASED ON TILESIZE
        self.rect.y = self.y * TILESIZE

    def move(self, dx=0, dy=0): # MOVE METHOD, set defaults so only one option can be specified
        if not self.collide_with_mob(dx, dy): # CHECK IF SQUARE IS OCCUPIED BEFORE MOVING
            self.x += dx
            self.y += dy

    def collide_with_mob(self, dx=0, dy=0): # CHECK FOR COLLISION WITH MOBS GROUP
        for mob in self.game.mobs:
            if mob.x == self.x + dx and mob.y == self.y + dy:
                return True # COLLISION - now to decide what happens next
        return False # NO COLLISION
# DEFINE MOB CLASS
class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs # ADD TO ALL SPRITES AND MOBS GROUP
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.game = game
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
