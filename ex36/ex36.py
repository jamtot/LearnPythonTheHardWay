#a text adventure game, made as part of exercise 36

def intro():
    """Introduces the scenario, you arrive at a spooly house in the middle of nowhere."""

    print "********************" # just a marker to show the start
    
    print "As you drive along the dark, windy, long, forest road, you wonder where the turn off is."
    print "\"It should be somewhere along here,\" you think."
    print "Just ahead you see two large, crumbling pillars, hung with two wide open metal gates, in need of a lick of paint."    
    print "\"This must be the place,\" you think, as you slowly turn in through the gate."
    print "\"I hope this is the right place.\"\n"

    print "You slowly drive up the driveway, the sound of gravel crunching under your car wheels as it crawls along."
    print "In the distance you see a house shrouded in darkness, barely lit by the light of the moon."
    print "\"They weren't lying, this place really is creepy.\"\n"

    print "As you get closer to the house, your headlights reveal a fountain in front of the house." 
    print "The shadow cast across the face of the house gives you the heebie jeebies."
    print "You don't see any other cars."
    print "Maybe they're parked out back."
    print "Maybe you're the first one here.\n"

    print "You pull up alongside the fountain."
    print "You sit there idling for a minute, wondering where the others are before you kill the car engine.\n"
    
    print "\"Do I call Mike, or do I just try the door? Or do I flat out just leave?\"" 
    print "This place is spooking me out. The point of course.\n"

    print "Knowing Mike, he'd never let me live down calling him. \"Awh, are you scared, buddy?\""
    print "Who even owns the house? He wasn't very specific."
    print "\"There are going to be loads of people there.\" Yeah right.\n"
    
    print "You check your phone, it's 7.54pm. He said be there for 8.\n"
    
    start()

def start():
    """Set's up the initial choice to join the party or leave."""
    
    mike_called = False
    in_car = True
    
    while (in_car):
        if not mike_called:
            print "You consider calling Mike, getting out of the car, or just flat out leaving."
        else:
            print "You consider leaving, or getting out of the car."
        choice = raw_input("> ")

        # if you decide to call Mike
        if "call" in choice and mike_called == False:
            print "You decide to call Mike."
            print "The phone rings twice before he declines your call."
            print "\"Goddamn it, Mike!\""
            mike_called = True
        # if you call Mike again
        elif "call" in choice and mike_called == True:
            print "You try calling Mike again in hopes of an answer."
            print "It doesn't even ring. His phone must be off."
                
        # if you decide to get out of the car
        elif "get" in choice and "out" in choice and "car" in choice:
            print "You get out of the car.\n"
            in_car = False
            courtyard(mike_called)

        # if you decide to get out
        elif "get" in choice and "out" in choice:
            carOrArea = ""  
            # loop prompting until the player decides what to get out of          
            while not (("car" in carOrArea) or ("leave" in carOrArea) or (
            "back" in carOrArea)):
                print "Get out of the car, or leave altogether? (or just go back?)"
                carOrArea = raw_input("> ")

            if "car" in carOrArea:
                print "You get out of the car.\n"
                in_car = False
                courtyard(mike_called)
            elif "leave" in carOrArea:
                leftCourtyard()
            elif "back" in carOrArea:
                pass
            else:
                print "Huh?!"

        elif "leave" in choice:
            leftCourtyard()

        else:
            print "I don't know what that means."
        
    
def courtyard(called_mike):
    """What happens when you exit the car."""

    print "You are in the courtyard, by the fountain."
    # more to come
    exit(0)

def leftCourtyard():
    """What happens when you leave before the party gets started."""

    print "\"I didn't want to party tonight anyway!\"\n"
    print "You start up your car engine, turn around and leave without looking back."
    print "I'll just go with him next time.\n"
    print "You get home, watch some TV and wait for a call that never comes."
    print "You hit the hay early and wake up feeling refreshed the next morning."
    print "As you're sitting down to breakfast, there's a sudden, loud banging at your door."
    print "You get up to find out who is at the door to find your sister and your mother."
    print "\"Oh thank god!\" your sister shouts as she lunges at you, hugging you tightly."
    print "\"I'm so sorry about Mike,\" your mom exclaims, fighting back tears."
    print "\"Umm, what? What are you guys doing here? What did Mike do?\""
    print "\"He doesn't know!\""
    print "\"I don't know what?! Tell me!\""
    print "\"That party... The one you were going to...\""
    print "\"Yeah? I got there and it seemed like no-one was there, and I couldn't get through to Mi-\""
    print "\"They were all found dead this morning...\""
    exit(0)
    
intro()
start()
