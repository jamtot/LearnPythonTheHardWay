from room import Room

class DansRoom(Room):
    
    def __init__(self):
        self.marblesFree = False
    
    def enter(self):
        # maybe rewrite. maybe not.
        print "LOCATION: DANIEL'S ROOM"
        print "You are in Daniel's room."
        print "There's a CD lying upside down on his table, and"
        if not self.marblesFree:
            print "a bag of marbles."
        else:
            print "the floor is covered in marbles."
        while True:
            choice = raw_input("> ")
            if "cd" in choice or "CD" in choice:
                print "You look at the CD. It's one of those CDs that has"
                print "hit songs from the year you were born."
                print "\"HITS FROM 1996!\""
            elif "marb" in choice:
                print "You open the bag of marbles and pour them all over"
                print "the floor."
                print "You are a rebel."
                self.marblesFree = True
            elif ("leave" in choice or "door" in choice or "hall" in choice or
                            "landing" in choice or "back" in choice):
                return "landing"
            else:
                print "There's a nice view of the abandoned trampoline"
                print "in the backyard from here."
