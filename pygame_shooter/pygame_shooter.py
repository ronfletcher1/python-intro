# 1. Include/Import pygame (module) and any other files to be called as needed by the program
# we needed pip to get this for us because Python doesn't ship with it

import pygame
from hero2 import Hero # this is a separate file that is the Hero Class and 
# contains all Hero defined functions (methods/attributes); my file is hero2.py not same as Rob's example
from BadGuy import BadGuy # this is a separate file that is the BadGuy Class and 
# contains all BadGuy defined functions (methods/attributes)
from the_claw import the_claw # this is a separate file that is the the_claw Class and 
# contains all the_claw defined functions (methods/attributes) this is # 2 on the exercises
from Arrow import Arrow # this is a separate file that is the Arrow Class and 
# contains all Arrow defined functions (methods/attributes)
from Button import Start_Button
# we want to have pygame "groups"
# ** from pygame.sprite import Group new line 26
# make a group for out arrows to live in
# a group is a pygame thing. Its like a list,
# but with cool stuff too
# ** arrows = Group # duplicate below on line #56 **

# importing Classes from other files allows you to "call" the class and 
# utilize it's defined functions (methods/attributes) - they are all called in # 4 below 
# (currently lines 35, 38, 39, 42; line 39 the bad_guy call needs clarification)

# Get Group and groupcollide from the sprite module (these are part of pygame and further clarification required)
from pygame.sprite import Group, groupcollide

# 2. Initialize pygame.
# Why do we need to do this? Because they told us to.

pygame.init()

# 3. make a screen with a size. This MUST be a tuple (tuple = fixed? and where is it)

screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size) #this is to create a screen from pygame module

# set the title of the window that opens...

pygame.display.set_caption("Dynamic Deuce") # this sets the name of the screen at the top middle

# 4. call the class objects

theHero = Hero() # this has called the Hero class object so now the code has access to all the Hero functions

# # this is our BadGuy object
# BadGuy = BadGuy() 
# # this has called the BadGuy class object so now the code has access to all the BadGuy functions
# bad_guy = BadGuy() 
bad_guy = BadGuy()
# make a bad_guys group
bad_guys = Group()
# need clarification, but I think that we created a bad_guy variable that 
# accesses all BadGuy functions; let's see where it's called
# add the bad_guy to the bad_guys Group
bad_guys.add(bad_guy) # added after I left class and included in push (get clarification)
start_button = Start_Button(pygame_screen)

# make a group for our arrows to live in
arrows = Group() 
# A group is a special pygame "list" for Sprites from line 26 (I think...FIND OUT!!!)
# arrows = []


# ======VARIABLES FOR OUR GAME======
# they are all fils from pygame and stored in the same folder as game else 
# you'll have to point to a directory or url, etc... to use
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
# ** arrow_image = pygame.image.load('arrow.png') - commented out and updated
# on arrow.py
# the_claw = pygame.image.load('arrow.png')
tick = 0 # clarification needed
direction = 1 # clarification needed

# Below is code previously writtent that is now contained in 
# one of the classes (it's a shortcut; find out what it was and the shortcut)
# heroLoc = {
#     'x': 0,
#     'y': 0
# }

# # Looks like a music variable  was added and called 
# after I left class and included in push (code below replaced with line 144 - 145)
# bg_music = pygame.mixer.Sound('bg.wav')
# bg_music.play()

# ======MAIN GAME LOOP======

game_on = True
game_start = False

# the loop will run as long as our bool is True

while game_on:
    # we are in the game loop from here on out!
    # 5. Listen for events and quit if the user clicks the x (on the panel; closing the window)
    # the events are already defined in pygame
    tick += 1
    if (tick % 90 == 0):
        bad_guys.add(BadGuy())
    # ***adds a new bad guy
    # =====EVENT CHECKER=====
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # THE USER CLICKED THE RED DOT!
            # These aren't the droids we're looking for. quit.
            game_on = False
        elif event.type == pygame.KEYDOWN:
            # the user pressed a key!! (duh, key down)
            print (event.key) # the event key commands are the arrows on the keyboard 
            # the numbers represent the keystroke up, down, left, right
            if event.key == 275:
                # the user pressed the right arrow!!! move our dude right
                # code below was replaced with the Hero class objects should_move 
                # and draw_me functions
                #theHero.x += 10
                #theroLoc ['x'] += 10
                theHero.should_move("right")
            elif event.key == 276:
                # the user pressed the left arrow!!! move our dude left
                # theHero.x += -10
                theHero.should_move("left")
            if event.key == 273:
                # the user pressed the top arrow!!! move our dude up
                # theHero.y += -10
                theHero.should_move("up")
            elif event.key == 274:
                # the user pressed the down arrow!!! move our dude down
                # theHero.y += 10
                theHero.should_move("down")
            elif event.key == 32:
                    new_arrow = Arrow(theHero)
                    arrows.add(new_arrow)
        elif event.type == pygame.KEYUP:
        # the user RELEASED a key (duh the key going up after it was pressed down KEYDOWN)
            if event.key == 275:
                theHero.should_move("right",False)
            elif event.key == 276:
                theHero.should_move("left",False)
            if event.key == 273:
                theHero.should_move("up",False)
            elif event.key == 274:
                theHero.should_move("down",False)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print (mouse_x,mouse_y)
            if start_button.rect.collidepoint(mouse_x, mouse_y):
                game_start = True
                bg_music = pygame.mixer.Sound('faf.wav')
                bg_music.play()

                    # Space Bar... FIRE!!!!
                # elif event.key == 32:
                # # Space Bar... FIRE!!!!
        #======Code below added after leaving class=====
        #         new_arrow = Arrow(theHero) # variables added for access to theHero only
        #         arrows.add(new_arrow)
        # elif event.type == pygame.KEYUP:
           

    
    # ==========DRAW STUFF==========
    # We use blit to draw on the screem. blit = block image transfer
    # blit is a method, that takes 2 arguments
    # 1. What to draw
    # 2. Where to draw it
    # in the docs... SURFACE = our "pygame_screen"
    pygame_screen.blit(background_image,[0,0])
    
    #code added from Robs push
    if game_start == True:
        theHero.draw_me(512,480)
        for bad_guy in bad_guys:
            bad_guy.update_me(theHero)
            pygame_screen.blit(monster_image,[bad_guy.x,bad_guy.y])

        for arrow in arrows:
            arrow.update_me()
            pygame_screen.blit(arrow.img,[arrow.x,arrow.y])
        pygame_screen.blit(hero_image,[theHero.x,theHero.y])

        arrow_hit = groupcollide(arrows,bad_guys,True,True)
        # print arrow_hit
        if arrow_hit:
            bad_guys.add(BadGuy())

    if game_start == False:
        start_button.setup_message()
        start_button.draw_button()
    
    pygame.display.flip()
    # # insertion of code to be moved
    # #if game_start == True:
    # #theHero.draw_me(512,480)
    # pygame_screen.blit(hero_image,[theHero.x,theHero.y])

    # # draw the arrows
    # for arrow in arrows:
    #     arrow.update_me()
    #     pygame_screen.blit(arrow_image,[arrow.x,arrow.y])

    # arrow_hit = groupcollide(arrows,bad_guys,True,True)

    # # print arrow_hit
    # if arrow_hit:
    #     bad_guys.add(BadGuy())
    # # bottom of copy to be indented
    # if game_start == False:
    #     start_button.setup_message()
    #     start_button.draw_button()

    # # draw the bad guys
    # for bad_guy in bad_guys:
    #     bad_guy.update_me(theHero)
    #     pygame_screen.blit(monster_image,[bad_guy.x,bad_guy.y])
    # pygame.display.flip()

    # Adding another character
    # # draw the the_claw
    # for bad_guy in bad_guys:
    #     bad_guy.update_me(theHero)
    #     pygame_screen.blit(monster_image,[bad_guy.x,bad_guy.y])
    # pygame.display.flip()
    
    #=====MY PREVIOUS CODE modified above after I left class)
    # pygame_screen.blit(background_image, [0,0])
    # theHero.draw_me()
    # BadGuy.update_me(theHero)
    # pygame_screen.blit(hero_image,[theHero.x,theHero.y])
    # pygame_screen.blit(monster_image,[BadGuy.x,BadGuy.y])
    # # pygame_screen.blit(hero_image, [theHero.x, theHero.y])
    # # pygame_screen.blit(goblin_image, )
    # # pygame_screen.blit(monster_image, [bad_guy,0])
    # # pygame_screen.blit(arrow_image, [0,0])
    # pygame.display.flip()

    # the commands above are from pygame modules. I found documentaiton on the web 
    # at https://www.pygame.org/ftp/contrib/pygame_docs.pdf for the draw_me, display.flip();
    # also heavy documentation on what is being used that comes with pygame; describes 
    # the events and usage as well as the QUIT and KEYDOWN used on line 

    # code looks good but it's not working right, characters and arrows keep scrolling off the screen

