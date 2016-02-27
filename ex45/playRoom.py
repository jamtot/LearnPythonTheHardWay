from room import Room

class PlayRoom(Room):

    def __init__(self):
        self.aaronHere = True
    
    def enter(self):
        print "You enter the playroom."
        print "LOCATION: PLAY ROOM"
        if self.aaronHere:
            print "Aaron, Fred and Mary's youngest son is in here playing."
            print "He doesn't even look up from the car and the dinosaur he"
            print "is crashing together."
        print "The room is nice and cool, but there's nothing really of"
        print "any interest in here."

        while True:
            choice = raw_input("> ")
            if "leave" in choice or "door" in choice or "hall" in choice:
                return "hall"
            elif (("hello" in choice or "hi" in choice or "hey" in choice or
                    "Aaron" in choice or "aaron" in choice) and self.aaronHere):
                print "Aaron's turns his head to look at you."
                print "He cocks his head to the side. Like a dog would."
                print "His forehead wrinkles, as if he's trying to figure"
                print "who you are."
                print "\"It's me, Bill, your neighbour.\""
                print "\"EEEEEEEEEEEEEE!\" the little s**t lets out an ear-"
                print "drum piercing screech!"
                print "He runs at you and latches onto your leg and bites"
                print "your hand. Hard."
                print "You do what any already slightly annoyed person in"
                print "need of that morning shot of caffeine does when they're"
                print "bitten on the hand by a toddler."
                print "You pick him up, lifting him high over your head"
                print "to dropkick him into the wall."
                print "Like something straight out of a comedy,"
                print "the ceiling fan catches him and"
                print "launches him out of the open window."
                print "Didn't see that coming."
                self.aaronHere = False
            elif "shoot" in choice:
                if self.aaronHere:
                    print "You want to shoot a kid? As he plays?"
                    shoot = raw_input("> ")
                    if "ye" in shoot:
                        print "Okay."
                        print "Aaron gets up from his toys as you reach"
                        print "for your gun. He sees the gun, thinking it's"
                        print "a toy gun he grabs it. \"MIIIIIIINE!\""
                        print "The little s**t! \"BANG BANG!\" he shouts"
                        print "as he point the gun at you."
                        print "He manages to squeeze the trigger as you"
                        print "reach for the gun."
                        return "dead"
                    elif "no" in shoot:
                        print "Probably a good choice."
                    else:
                        print "Oh, you were joking."
                else:
                    print "I should have shot him, alright."
                    print "Oh well, no need now."
            else:
                if self.aaronHere:
                    print "Even Aaron is ignoring that. And he talks gibberish"
                    print "for a living."
                else: print "*crickets*"
