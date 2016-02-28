from room import Room

class AaronsRoom(Room):
    
    def enter(self):
        print "LOCATION: AARON'S ROOM"
        print "You are in Aaron's room."
        return "landing"
