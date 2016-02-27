from room import Room

class Landing(Room):

    def enter(self):
        print "LOCATION: UPSTAIRS LANDING"
        print "You are on the upstairs landing."
        exit(1)
