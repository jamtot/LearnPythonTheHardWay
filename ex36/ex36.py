#a text adventure game, made as part of exercise 36

import time
import sys

def type_printer(stringToWrite, delay = 0.05):
    """A function for getting the text to roll out one letter at a time."""

    for char in stringToWrite:
        # need to use a stream to get everything in the right place
        sys.stdout.write( '%s' % char )
        # and to flush the buffer
        sys.stdout.flush()
        time.sleep(delay)

def tPrint(string):
    """Prints a line using the type_printer function, with a newline at the end"""

    type_printer("%s\n" % string, writeSpeed)

def intro():
    """Introduces the scenario, you arrive at a spooky house in the middle of nowhere."""

    tPrint("As you drive along the dark, windy, long, forest road, you wonder where the turn off is.")
    tPrint("\"It should be somewhere along here,\" you think.")
    tPrint("Just ahead you see two large, crumbling pillars, hung with two wide open metal gates in need of a lick of paint.")   
    tPrint("\"This must be the place,\" you think, as you slowly turn in through the gate.")
    tPrint("\"I hope this is the right place.\"\n")

    tPrint("You slowly drive up the driveway, the sound of gravel crunching under your car wheels as it crawls along.")
    tPrint("In the distance you see a house shrouded in darkness, barely lit by the light of the moon.")
    tPrint("\"They weren't lying, this place really is creepy.\"\n")

    tPrint("As you get closer to the house, your headlights reveal a fountain in front of the house.")
    tPrint("The shadow cast across the face of the house gives you the heebie jeebies.")
    tPrint("You don't see any other cars.")
    tPrint("Maybe they're parked out back.")
    tPrint("Maybe you're the first one here.\n")

    tPrint("You pull up alongside the fountain.")
    tPrint("You sit there idling for a minute, wondering where the others are before you kill the car engine.\n")
    
    tPrint("\"Do I call Mike, or do I just try the door? Or do I flat out just leave?\"")
    tPrint("This place is spooking me out. The point of course.\n")

    tPrint("Knowing Mike, he'd never let me live down calling him. \"Awh, are you scared, buddy?\"")
    tPrint("Who even owns the house? He wasn't very specific.")
    tPrint("\"There are going to be loads of people there.\" Yeah right.\n")
    
    tPrint("You check your phone, it's 7.54pm. He said be there for 8.\n")
    
    start()

def start():
    """Set's up the initial choice to join the party or leave."""
    
    tPrint("LOCATION: IN CAR")

    in_car = True
    global mike_called
    
    if not mike_called:
        tPrint("You consider calling Mike, getting out of the car, or just flat out leaving.")
    else:
        tPrint("You consider leaving, or getting out of the car.")

    while (in_car):

        choice = raw_input("> ")

        # if you decide to call Mike
        if "call" in choice and mike_called == False:
            tPrint("You decide to call Mike.")
            tPrint("The phone rings twice before he declines your call.")
            tPrint("\"Goddamn it, Mike! It's Joe, call me back when you get this.\"")
            mike_called = True

        # if you call Mike again
        elif "call" in choice and mike_called == True:
            tPrint("You try calling Mike again in hopes of an answer.")
            tPrint("It doesn't even ring. His phone must be off.")
                
        # if you decide to get out of the car
        elif "get" in choice and "out" in choice and "car" in choice:
            tPrint("You get out of the car.")
            in_car = False
            courtyard()

        # if you decide to get out
        elif "get" in choice and "out" in choice:
            carOrArea = ""
            # loop prompting until the player decides what to get out of          
            while not (("car" in carOrArea) or ("leave" in carOrArea) or (
            "back" in carOrArea)):
                tPrint("Get out of the car, or leave altogether? (or just go back?)")
                carOrArea = raw_input("> ")

            if "car" in carOrArea:
                tPrint("You get out of the car.")
                in_car = False
                courtyard()
            elif "leave" in carOrArea:
                leftCourtyard()
            elif "back" in carOrArea:
                pass
            else:
                tPrint("Huh?!")

        elif "leave" in choice:
            leftCourtyard()

        else:
            tPrint("I don't know what that means.")
        
    
def courtyard():
    """What happens when you exit the car."""
    
    tPrint("LOCATION: COURTYARD")

    global carOK
    global f_door_open

    in_courtyard = True
    tPrint("You are in the courtyard, by the fountain.")
    tPrint("You take out your phone and use the flashlight on that.")
    tPrint("The light is weak, but it's enough to see what's nearby.")
    tPrint("You are right beside the fountain.")
    tPrint("The door to the house is up some steps.")
    tPrint("There could be other cars out the back.")
       
    while in_courtyard:
        choice = raw_input("> ")

        if ("search" in choice or "look" in choice) and "fountain" in choice:
            tPrint("You shine your flashlight into the fountain.")
            tPrint("The fountain is dry. Looks like it has been for quite a while.")
            tPrint("There appears to be some kind of flyer flapping gently in the wind.")
        elif ("knock" in choice or "open" in choice) and "door" in choice:
            if f_door_open:
                livingRoom()
            else:
                tPrint("You try knocking the door.")
                tPrint("..........................")            
                tPrint("No answer.")
                tPrint("You try opening the door.")
                tPrint("It won't budge.")
        elif ("grab" in choice or "get" in choice) and "flyer" in choice:
            tPrint("You pick up the flyer.")
            tPrint("\"2SPOOKY4ME house party, 8PM sharp @ <this address>\"")
            tPrint("Guess I must be in ther right place after all.")
            tPrint("Looks like someone has wrote on the back.")
            tPrint("\"DON'T GO\" is scrawled messily... in red pen?")
        elif "leave" in choice:
            tPrint("Leave in your car?")
            leave = raw_input("> ")
            if "yes" in leave and carOK:
                tPrint("You hop back into your car and start the engine.")
                leftCourtyard()
            elif "yes" in leave and not carOK:
                tPrint("You hop back into your car, but it won't start.")
                tPrint("You hear something rustle in the back seat.")
                tPrint("It's already too late.")
                dead("Your throat is slit from ear to ear, you've lost consciousness before you even realise.")
            elif "no" in leave:
                pass
            else:
                tPrint("I don't understand what you mean.")
        elif "car" in choice:
            tPrint("Get back into car?")
            car = raw_input("> ")
            if "yes" in car and carOK:
                tPrint("You get back into your car")
                start()
            elif "yes" in car and not carOK:
                tPrint("You hop back into your car.")
                tPrint("You hear something rustle in the back seat.")
                if armed:
                    tPrint("You try to defend yourself with the knife.")
                    tPrint("But the attacker is too strong.")
                else:                
                    tPrint("It's already too late.")
                dead("Your throat is slit from ear to ear, you've lost consciousness before you even realise.")
            elif "no" in car:
                tPrint("OK.")
            else:
                tPrint("I don't know what you mean.")
        elif "back" in choice and ("out" in choice or "house" in choice):
            outBack()
        else:
            tPrint("I don't understand.")
            
        # look in fountain - see flyer - grab flyer
        # knock door - no answer - try open - won't budge
        # return to car, and leave 
        # look out back
        #exit(0)

def leftCourtyard():
    """What happens when you leave before the party gets started."""

    tPrint("\"I didn't want to party tonight anyway!\"\n")
    tPrint("You start up your car engine, turn around and leave without looking back.")
    tPrint("I'll just go with him next time.\n")
    tPrint("You get home, watch some TV and wait for a call that never comes.")
    tPrint("You hit the hay early and wake up feeling refreshed the next morning.\n")
    tPrint("As you're sitting down to breakfast, there's a sudden, loud banging at your door.")
    tPrint("You get up to find out who is at the door to find your sister and your mother.")
    tPrint("\"Oh thank god!\" your sister, Emily, shouts as she lunges at you, hugging you tightly.")
    tPrint("\"I'm so sorry about Mike,\" your mom exclaims, fighting back tears.")
    tPrint("\"Umm, what? What are you guys doing here? What did Mike do?\"")
    tPrint("\"He doesn't know!\"\n")
    tPrint("\"I don't know what?! Tell me!\"")
    tPrint("\"That party... The one you were going to...\"")
    tPrint("\"Yeah? I got there and it seemed like no-one was there, and I couldn't get through to Mi-\"\n")
    tPrint("\"They were all found dead this morning...\"\n")
    exit(0)

def outBack():
    global carOK
    tPrint("LOCATION: BACK OF HOUSE")

    tPrint("You are at the back of the house.") 
    if carOK:
        carOK = False
        tPrint("There are no other cars.") 
        tPrint("You hear a loud thunk out the front of the house.")
    tPrint("The back door of the house looks slightly ajar.")
    
    while True:
        choice = raw_input("> ")
        if "open" in choice or "door" in choice:
            kitchen()
        elif "front" in choice:
            courtyard()
        else:
            tPrint("I don't know what that means.")
            tPrint("Go in the back door, or back out the front.") 
    
def kitchen():
    global armed
    tPrint("LOCATION: KITCHEN")

    tPrint("You push open the back door, revealing a kitchen.")
    tPrint("There's rotting food on the table.")
    
    if not armed:
        tPrint("There's a knife on the table by the food.")

    tPrint("There's a dark passageway to the east.")
    tPrint("There's a stairs leading up to the south.")
    tPrint("You can also leave through the back door.")
    tPrint("What would you like to do?")
    
    while True:
        choice = raw_input("> ")
        if ("grab" in choice or "get" in choice and "knife" in choice) or "knife" in choice:
            armed = True
            tPrint("You grab the knife.")
        elif "back" in choice and "door" in choice:
            outBack()
        elif "east" in choice or "passageway" in choice:
            livingRoom()
        elif "stairs" in choice:
            upstairs()
        else:
            tPrint("What?! (try \"back door\", \"passageway\", or \"stairs\")")
        
    
def livingRoom():
    global has_key
    global mem_jogged
    global f_door_open
    tPrint("LOCATION: LIVING ROOM")
    tPrint("You are in the living room.")
    if f_door_open == False:
        f_door_open = True
        tPrint("The front door is wide open.")    
    tPrint("There is a door to the south.")
    tPrint("There is a family photo on the mantlepiece.")
    while True:    
        choice = raw_input("> ")

        if "door" in choice and "front" in choice:
            courtyard() 
        elif "door" in choice and "south" in choice:
            if has_key:
                basement()
            else:
                tPrint("The door is locked.")
        elif "picture" in choice or "photo" in choice:
            if mem_jogged:
                tPrint("The picture is of my family.")
                tPrint("How could I not recognise them, me, before?")
                tPrint("It was a long time ago.")
                tPrint("My brother died in a farming accident when he was 5.")
                tPrint("My father went missing shortly after.")
                tPrint("All I had left was my mother and my sister.")
                tPrint("We moved shortly after.")
                tPrint("I was very young at the time.")
            else:      
                tPrint("The photo is of a family of 5.")
                tPrint("The two parents, and three young kids.")
                tPrint("Two boys and girl.")
                tPrint("They are stood as a family outside the front of this house.")
                tPrint("The house looked a lot nicer then.")
        else:
            tPrint("Not really sure what that means.")    

def upstairs():
    tPrint("LOCATION: UPSTAIRS HALLWAY")
    tPrint("You climb the creaky stairs.")
    tPrint("At the top is a hall with 3 doors.")
    tPrint("On door 1, there is the pink letter \"E\".")
    tPrint("On door 2, there are the blue letters \"J + N\".")
    tPrint("It looks like someone has tried removing the N.")
    tPrint("Door 3 has a childs crayon drawing of a family with \"Mommy and Daddy's room\" scrawled on it.")

    while True:
        choice = raw_input("> ")
        
        if "stairs" in choice or "down" in choice:
            livingRoom()
        elif "1" in choice or "e" in choice:
            esRoom()
        elif "2" in choice or "j" in choice or "n" in choice:
            jnsRoom()
        elif "3" in choice or "mom" in choice or "dad" in choice:
            momdadsRoom()
        else:
            tPrint("I don't understand. (Choose a door number, or go back down the stairs.)")

def esRoom():
    global mem_jogged   
    tPrint("LOCATION: E's ROOM") 
    if mem_jogged:
        tPrint("My sister Emily's got a whole cluster of butterfly tattoos now.")
    else:
        tPrint("The room is clearly a girls room.")
        tPrint("The yellow walls are decorated with pink butterflys.")
    tPrint("There is a teddy bear behind the pink bed.")
    tPrint("On the dresser, there is a drawing.")

    while True:
        choice = raw_input("> ")
        if "teddy" in choice or "bear" in choice:
            if mem_jogged:
                tPrint("You look at the teddy bear.")
                tPrint("The engraved name \"Jonathan\" was an amalgamation of your name and your brothers.")
            else:            
                tPrint("It has an engraved nametag. \"Jonathan\"")
                tPrint("Coincidentally, my sister has always had a teddy bear with the same name.")

        elif "drawing" in choice or "dresser" in choice:
            tPrint("The drawing is of a family of 5 stick figures.")
            tPrint("\"My family\" is wrote over it.")
            tPrint("One of the young boys is scribbled over with red crayon.")
        elif "door" in choice or "hallway" in choice or "leave" in choice:
            upstairs()
        else:
            tPrint("Not quite sure what that means.")
            
        

def jnsRoom():
    tPrint("LOCATION: J + N's ROOM")
    global mem_jogged
    mem_jogged = True
    pass

def momdadsRoom():
    tPrint("LOCATION: MOM AND DAD's ROOM")
    pass

def basement():
    tPrint("LOCATION: BASEMENT")
    tPrint("The door opens to a stairs leading to the basement.")
    exit(0)
    

def dead(why):
    tPrint("%s" % why)
    exit(0)



writeSpeed = ''
try: # try convert the input to a float    
    # taking the writespeed from a prompt    
    #writeSpeed = float(raw_input("How fast would you like the text to appear? (in seconds, 0 for instant)\n > "))
    # taking the writespeed from a commandline argument
    writeSpeed = float(sys.argv[1])
except: # if it doesn't work, just set the text to appear instantly
    writeSpeed = 0.0
print "********************"

mike_called = False
carOK = True
armed = False
has_key = False
f_door_open = False
mem_jogged = False

intro()
start()
