from room import Room
from livingRoom import LivingRoom

class Bathroom(Room):

    def enter(self):
        print "LOCATION: BATHROOM"
        print "You are in the bathroom."
        if LivingRoom.maryPresent:
            print "There isn't anything in here, other than the usual"
            print "bathroom stuff. Shampoo, toothbrushes, toilet paper,"
            print "bath tub, toilet. All standard stuff."
        else:
            print "It's just a normal bathroom."
            print "Although... the shower curtain is pulled closed."
            print "And you can hear muffled, shallow breathing."
        while True:
            choice = raw_input("> ")
            if ("leave" in choice or "door" in choice or "landing" in choice or
                    "hall" in choice or "back" in choice):
                return "landing"
            elif ("curtain" in choice or "pull" in choice) and not LivingRoom.maryPresent:
                print "As you pull back the curtain, Mary screams and she"
                print "pulls the trigger on the gun trembling in her hand."
                return "dead"
            else:
                print "Again. There's nothing of interest in here."
