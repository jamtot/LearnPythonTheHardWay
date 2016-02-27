from room import Room

class UpStairs(Room):
    
    def enter(self):
        print "You head up the stairs."
        return "landing"  
