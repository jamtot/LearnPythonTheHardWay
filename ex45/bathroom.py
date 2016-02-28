from room import Room

class Bathroom(Room):

    def enter(self):
        print "LOCATION: BATHROOM"
        print "You are in the bathroom."
        return "landing"
