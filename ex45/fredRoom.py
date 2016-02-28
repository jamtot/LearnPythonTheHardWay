from room import Room

class FredRoom(Room):
    
    def enter(self):
        print "LOCATION: FRED AND MARY'S ROOM"
        print "You are in Fred and Mary's room."
        return "landing"
