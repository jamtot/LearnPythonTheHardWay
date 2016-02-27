from room import Room

class Pantry(Room):
    
    def enter(self):
        print "You enter enter the pantry. You can't see any sugar."
        print "There's sweetener, but that's worse than no sugar."
        return "kitchen"
