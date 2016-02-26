from Room import Room

class AtDoor(Room):
    
    def enter(self):
        print "You knock on the door."
        print "......"
        print "Fred, the neighbour answers the door."
        return "finalRoom"
