from room import Room

class DansRoom(Room):
    
    def enter(self):
        # maybe rewrite. maybe not.
        print "LOCATION: DANIEL'S ROOM"
        print "You are in Daniel's room."
        print "There's a thing, and a yoke."
        while True:
            choice = raw_input("> ")
            if "thing" in choice:
                print "You look at the thing."
                print "There's a date, wow, really? A pattern?"
                print "This one is 96. Dan's DOB."
            elif "yoke" in choice:
                print "Do useless distracting yoke that adds choice."
            elif ("leave" in choice or "door" in choice or "hall" in choice or
                            "landing" in choice or "back" in choice):
                return "landing"
            else:
                print "This goes here as a catch-all. Try again."
