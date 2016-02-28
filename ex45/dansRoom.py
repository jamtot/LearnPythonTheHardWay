from room import Room

class DansRoom(Room):
    
    def enter(self):
        print "LOCATION: DANIEL'S ROOM"
        print "You are in Daniel's room."
        return "landing"
