from room import Room

class DownStairs(Room):

    def enter(self):
        print "You head down the stairs."
        return "hall"
