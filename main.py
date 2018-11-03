"""

Main game file

A pygame template I created watching the "KidsCanCode" tutorial
series on Youtube by Chris Bradfield.

https://www.youtube.com/watch?v=VO8rTszcW4s

A basic python 3 pygame "game" with a player, enemy, play grid, movement locked
to grid, key bindings, and basic collision detection. Heavily commented for a
friend which basically outlines the program.

"""
import pygame as pg
import sys
from settings import *
from sprites import *
# DEFINE GAME CLASS
class Game:
    def __init__(self):
        # INITIALIZE GAME WINDOW
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # ENABLES REPEAT KEY PRESSES AFTER 400 ms
        pg.key.set_repeat(400, 100)
        self.running = True

    def new(self): # NEW GAME FUNCTION
        # CREATE PYGAME GROUPS
        self.all_sprites = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        # CREATE PLAYER ENTITY
        self.player = Player(self, 2, GRIDHEIGHT / 2)
        # ADD PLAYER TO ALL SPRITES GROUP TO AID COLLISION DETECTION
        self.all_sprites.add(self.player)
        # CREATE ENEMY ENTITI
        self.mob = Mob(self, 29, GRIDHEIGHT / 2)
        # ADD ENEMY TO ALL SPRITES GROUP TO AID COLLISION DETECTION
        self.all_sprites.add(self.mob)
        # START RUN METHOD
        self.run()

    def run(self): # RUN METHOD
        # GAME LOOP FUNCTION
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def quit(self): #QUIT METHOD
        pg.quit()
        sys.exit()

    def update(self): # GAME UPDATE METHOD
        # GAME LOOP UPDATE
        self.all_sprites.update()

    def events(self): # GAME EVENTS METHOD
        # GAME LOOP EVENTS
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN: #KEY BINDINGS
                if event.key == pg.K_ESCAPE: # ESCAPE QUITS GAME
                    self.quit() # QUIT
                if event.key == pg.K_LEFT: # MOVE LEFT WITH LEFT ARROW
                    self.player.move(dx=-1) # MOVE LEFT ie negative x
                if event.key == pg.K_RIGHT:# MOVE RIGHT WITH RIGHT ARROW
                    self.player.move(dx=1) # MOVE RIGHT ie positve x
                if event.key == pg.K_UP: # MOVE UP WITH UP ARROW
                    self.player.move(dy=-1) # MOVE UP ie negative y
                if event.key == pg.K_DOWN: # MOVE DOWN WITH DOWN ARROW
                    self.player.move(dy=1) # MOVE DOWN ie positve y

    def draw(self): # GAME DRAW METHOD
        # GAME LOOP DRAW
        self.screen.fill(BGCOLOR)
        # DRAW A GRID ON GAME
        self.draw_grid()
        # DRAW ALL SPRITES IN THE PYGAME GROUP all_sprites
        self.all_sprites.draw(self.screen)
        # UPDATE DISPLAY
        pg.display.flip()

    def draw_grid(self): # DRAW GRID METHOD
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, GRIDCOLOR, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, GRIDCOLOR, (0, y), (WIDTH, y))

    def show_start_screen(self): #PLACEHOLDER FOR FUTURE CODE
        # SHOW START SCREEN
        pass

    def show_go_screen(self): #PLACEHOLDER FOR FUTURE CODE
        # SHOW GAME OVER SCREEN
        pass

g = Game() # CREATE GAME OBJECT
g.show_start_screen() # SHOW THE START SCREEN
while g.running: # WHILE LOOP IS ACTIVE
    g.new() # START NEW GAME

pg.quit() #PYGAME QUIT
