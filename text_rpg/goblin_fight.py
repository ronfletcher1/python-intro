# This is a procedural approach to a text based rpg
# The hero is fighting the goblin.
# The hero has the option to:
# 1. Fight
# 2. Dance
# 3. Flee :  

# Go get the os module from pythom
import os
# os.system(os) #will take any linux command
# and if python can run it, it will

print """
Luv Dragons  _)               (_
            _) \ /\%/\ /\_/\ / (_
           _)  \\(0 0) (0 0)//  (_
Art by     )_ -- \(oo) (oo)/ -- _(
 VampLadee  )_ / /\\__,__//\ \ _(
             )_ /   --;--   \ _(
         *.    ( (  )) ((  ) )    .*
           '...(____)z z(____)...'
"""

# get hero name from the player
hero_name = raw_input( "What is tyh name brave soul? " )

def fight():
    print "Welcome, %s. Thou art brave " % hero_name
    # declare some variables
    # These variables are in the scope of the function only (non global access)
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2
    
    # run the game as long as BOTH characters have health > 0
    while hero_health > 0 and goblin_health > 0:
        message = """You have %d health and %d power." 
        The goblin has %d health and %d power." 
        What do you want to do?
        1. fight goblin
        2. dance
        3. flee"""
        print message % (hero_health, hero_power, goblin_health, goblin_power)
        # Get the user's choice
        user_input = raw_input( "> " )

        if user_input == "1":
            # The hero has decided to attack!
            # subtract goblins health by hero power
            goblin_health -= hero_power
            print "You have done %d damage to the goblin!" % hero_power
        elif user_input == "2":
            hero_health += 5
            print """The goblin stares at you in disbelief of your stupidity.  
            His jaw dropped as your wounds heal."""
            print "your health is now %d" % hero_health
        elif user_input == "3":
            print "Goodbye, cowardly %s" % hero_name
            # thr break statement will end the loop IMMEDIATELY!!
            break
        else:
            # user entered something that we didn't offer
            print " Thou fool.  Thou has sumbledith (invalid input)"

            # now it's the goblin's tunr
            # unless he just died form the hero attack
            if goblin_health > 0:
                hero_health -= goblin_power
                print " The goblin hits you for %d damage" % goblin_power
                if hero_health <= 0:
                    print "Thou hast been slain"
            # else: 
                # os.system( "say Hooray. Thou hast killed the goblin!")
            if hero_health < 5:
                print " %s has gone into a rage as death approaches.  Power increased!" % hero_name
                hero_power += 5
                raw_input ( "Hit any key to continue" )
                os.system ("clear")

                    
# ANYTIME you have ()
# print hero health
fight ()
    
# print "Fight the goblin"



    