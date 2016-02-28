from room import Room

class DylsRoom(Room):
    
    def enter(self):
        print "LOCATION: DYLAN'S ROOM"
        print "You are in Dylan's room."
        return "landing"
