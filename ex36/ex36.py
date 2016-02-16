#a text adventure game, made as part of exercise 36

import time
import sys

def type_printer(stringToWrite, delay = 0.05):
    for char in stringToWrite:
        # need to use a stream to get everything in the right place
        sys.stdout.write( '%s' % char )
        # and to flush the buffer
        sys.stdout.flush()
        time.sleep(delay)

def intro():
    """Introduces the scenario, you arrive at a spooky house in the middle of nowhere."""

    type_printer("As you drive along the dark, windy, long, forest road, you wonder where the turn off is.\n", writeSpeed)
    type_printer("\"It should be somewhere along here,\" you think.\n", writeSpeed)
    type_printer("Just ahead you see two large, crumbling pillars, hung with two wide open metal gates in need of a lick of paint.\n", writeSpeed)   
    type_printer("\"This must be the place,\" you think, as you slowly turn in through the gate.\n", writeSpeed)
    type_printer("\"I hope this is the right place.\"\n\n", writeSpeed)

    type_printer("You slowly drive up the driveway, the sound of gravel crunching under your car wheels as it crawls along.\n", writeSpeed)
    type_printer("In the distance you see a house shrouded in darkness, barely lit by the light of the moon.\n", writeSpeed)
    type_printer("\"They weren't lying, this place really is creepy.\"\n\n", writeSpeed)

    type_printer("As you get closer to the house, your headlights reveal a fountain in front of the house.\n", writeSpeed)
    type_printer("The shadow cast across the face of the house gives you the heebie jeebies.\n", writeSpeed)
    type_printer("You don't see any other cars.\n", writeSpeed)
    type_printer("Maybe they're parked out back.\n", writeSpeed)
    type_printer("Maybe you're the first one here.\n\n", writeSpeed)

    type_printer("You pull up alongside the fountain.\n", writeSpeed)
    type_printer("You sit there idling for a minute, wondering where the others are before you kill the car engine.\n\n", writeSpeed)
    
    type_printer("\"Do I call Mike, or do I just try the door? Or do I flat out just leave?\"\n", writeSpeed)
    type_printer("This place is spooking me out. The point of course.\n\n", writeSpeed)

    type_printer("Knowing Mike, he'd never let me live down calling him. \"Awh, are you scared, buddy?\"\n", writeSpeed)
    type_printer("Who even owns the house? He wasn't very specific.\n", writeSpeed)
    type_printer("\"There are going to be loads of people there.\" Yeah right.\n\n", writeSpeed)
    
    type_printer("You check your phone, it's 7.54pm. He said be there for 8.\n\n", writeSpeed)
    
    start(True)

def start(mike_been_called):
    """Set's up the initial choice to join the party or leave."""
    
    mike_called = mike_been_called
    in_car = True
    
    while (in_car):
        if not mike_called:
            type_printer("You consider calling Mike, getting out of the car, or just flat out leaving.\n", writeSpeed)
        else:
            type_printer("You consider leaving, or getting out of the car.\n", writeSpeed)
        choice = raw_input("> ")

        # if you decide to call Mike
        if "call" in choice and mike_called == False:
            type_printer("You decide to call Mike.\n", writeSpeed)
            type_printer("The phone rings twice before he declines your call.\n", writeSpeed)
            type_printer("\"Goddamn it, Mike!\"\n", writeSpeed)
            mike_called = True

        # if you call Mike again
        elif "call" in choice and mike_called == True:
            type_printer("You try calling Mike again in hopes of an answer.\n", writeSpeed)
            type_printer("It doesn't even ring. His phone must be off.\n", writeSpeed)
                
        # if you decide to get out of the car
        elif "get" in choice and "out" in choice and "car" in choice:
            type_printer("You get out of the car.\n", writeSpeed)
            in_car = False
            courtyard(mike_called, True)

        # if you decide to get out
        elif "get" in choice and "out" in choice:
            carOrArea = ""
            # loop prompting until the player decides what to get out of          
            while not (("car" in carOrArea) or ("leave" in carOrArea) or (
            "back" in carOrArea)):
                type_printer("Get out of the car, or leave altogether? (or just go back?)\n", writeSpeed)
                carOrArea = raw_input("> ")

            if "car" in carOrArea:
                type_printer("You get out of the car.\n", writeSpeed)
                in_car = False
                courtyard(mike_called, True)
            elif "leave" in carOrArea:
                leftCourtyard()
            elif "back" in carOrArea:
                pass
            else:
                type_printer("Huh?!\n", writeSpeed)

        elif "leave" in choice:
            leftCourtyard()

        else:
            type_printer("I don't know what that means.\n", writeSpeed)
        
    
def courtyard(called_mike, carOK):
    """What happens when you exit the car."""
    
    in_courtyard = True
    type_printer("You are in the courtyard, by the fountain.\n", writeSpeed)
    type_printer("You take out your phone and use the flashlight on that.\n", writeSpeed)
    type_printer("The light is weak, but it's enough to see what's nearby.\n", writeSpeed)
    type_printer("You are right beside the fountain.\n", writeSpeed)
    type_printer("The door to the house is up some steps.\n", writeSpeed)
    type_printer("There could be other cars out the back.\n", writeSpeed)
    type_printer("What would you like to do?\n", writeSpeed)
       
    while in_courtyard:
        choice = raw_input("> ")

        if ("search" in choice or "look" in choice) and "fountain" in choice:
            type_printer("You shine your flashlight into the fountain.\n", writeSpeed)
            type_printer("The fountain is dry. Looks like it has been for quite a while.\n", writeSpeed)
            type_printer("There appears to be some kind of flyer flapping gently in the wind.\n", writeSpeed)
        elif ("knock" in choice or "open" in choice) and "door" in choice:
            type_printer("You try knocking the door.\n", writeSpeed)
            type_printer("..........................\n", writeSpeed)            
            type_printer("No answer.\n", writeSpeed)
            type_printer("You try opening the door.\n", writeSpeed)
            type_printer("It won't budge.\n", writeSpeed)
        elif ("grab" in choice or "get" in choice) and "flyer" in choice:
            type_printer("You pick up the flyer.\n", writeSpeed)
            type_printer("\"2SPOOKY4ME house party, 8PM sharp @ <this address>\"\n", writeSpeed)
            type_printer("Guess I must be in ther right place after all.\n", writeSpeed)
            type_printer("Looks like someone has wrote on the back.\n", writeSpeed)
            type_printer("\"DON'T GO\" is scrawled messily... in red pen?\n", writeSpeed)
        elif "leave" in choice:
            type_printer("Leave in your car?\n", writeSpeed)
            leave = raw_input("> ")
            if "yes" in leave and carOK:
                type_printer("You hop back into your car and start the engine.\n", writeSpeed)
                leftCourtyard()
            elif "yes" in leave and not carOK:
                type_printer("You hop back into your car, but it won't start.\n", writeSpeed)
                type_printer("You hear something rustle in the back seat.\n", writeSpeed)
                type_printer("It's already too late.\n", writeSpeed)
                dead("Your throat is slit from ear to ear, you've lost consciousness before you even realise.")
            elif "no" in leave:
                pass
            else:
                type_printer("I don't understand what you mean.\n", writeSpeed)
        elif "car" in choice:
            type_printer("Get back into car?\n", writeSpeed)
            car = raw_input("> ")
            if "yes" in car and carOK:
                type_printer("You get back into your car\n", writeSpeed)
                start(called_mike)
            elif "yes" in car and not carOK:
                type_printer("You hop back into your car.\n", writeSpeed)
                type_printer("You hear something rustle in the back seat.\n", writeSpeed)
                type_printer("It's already too late.\n", writeSpeed)
                dead("Your throat is slit from ear to ear, you've lost consciousness before you even realise.")
            elif "no" in car:
                type_printer("OK.\n", writeSpeed)
            else:
                type_printer("I don't know what you mean.\n", writeSpeed)
        elif "back" in choice and ("out" in choice or "house" in choice):
            outBack()
        else:
            type_printer("I don't understand.\n", writeSpeed)
            
        # look in fountain - see flyer - grab flyer
        # knock door - no answer - try open - won't budge
        # return to car, and leave 
        # look out back
        #exit(0)

def leftCourtyard():
    """What happens when you leave before the party gets started."""

    type_printer("\"I didn't want to party tonight anyway!\"\n\n", writeSpeed)
    type_printer("You start up your car engine, turn around and leave without looking back.\n", writeSpeed)
    type_printer("I'll just go with him next time.\n\n", writeSpeed)
    type_printer("You get home, watch some TV and wait for a call that never comes.\n", writeSpeed)
    type_printer("You hit the hay early and wake up feeling refreshed the next morning.\n\n", writeSpeed)
    type_printer("As you're sitting down to breakfast, there's a sudden, loud banging at your door.\n", writeSpeed)
    type_printer("You get up to find out who is at the door to find your sister and your mother.\n", writeSpeed)
    type_printer("\"Oh thank god!\" your sister shouts as she lunges at you, hugging you tightly.\n", writeSpeed)
    type_printer("\"I'm so sorry about Mike,\" your mom exclaims, fighting back tears.\n", writeSpeed)
    type_printer("\"Umm, what? What are you guys doing here? What did Mike do?\"\n", writeSpeed)
    type_printer("\"He doesn't know!\"\n\n", writeSpeed)
    type_printer("\"I don't know what?! Tell me!\"\n", writeSpeed)
    type_printer("\"That party... The one you were going to...\"\n", writeSpeed)
    type_printer("\"Yeah? I got there and it seemed like no-one was there, and I couldn't get through to Mi-\"\n\n", writeSpeed)
    type_printer("\"They were all found dead this morning...\"\n\n", writeSpeed)
    exit(0)

def outBack():
    type_printer("You go out the back of the house.\n", writeSpeed)   
    type_printer("There are no other cars.\n", writeSpeed) 
    type_printer("You hear a loud thunk out the front of the house.\n", writeSpeed)
    exit(0)

def dead(why):
    type_printer("%s\n" % why, writeSpeed)
    exit(0)

writeSpeed = ''
print "********************" # just a marker to show the start  
try: # try convert the input to a float    
    writeSpeed = float(raw_input("How fast would you like the text to appear? (in seconds, 0 for instant)\n > "))
except: # if it doesn't work, just set the text to appear instantly
    writeSpeed = 0.0
print "********************"


intro()
start(False)
