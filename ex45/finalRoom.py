from room import Room

class FinalRoom(Room):

    def enter(self):
        print "This is the final room."
        exit(1)
