from room import Room

class Landing(Room):

    def enter(self):
        print "LOCATION: UPSTAIRS LANDING"
        print "You are on the upstairs landing."
        print "There's 4 bedrooms and the bathroom."  
        print "The 3 kids have their names on the doors."
        print "There's Daniel's room, Dylan's room, and Aaron's room."
        print "There's Fred and Mary's room."
        print "And there's the bathroom."

        while True:
            choice = raw_input("> ")
            if "Dan" in choice or "dan" in choice:
                return "dansRoom"
            elif "Dyl" in choice or "dyl" in choice:
                return "dylsRoom"
            elif "Aar" in choice or "aar" in choice:
                return "aaronsRoom"
            elif "bath" in choice or "toilet" in choice:
                return "bathroom"
            elif ("Fred" in choice or "fred" in choice or "Mary" in choice or
                    "mary" in choice or "parents" in choice):
                return "fredRoom"
            elif "stairs" in choice or "down" in choice or "hall" in choice:
                return "downStairs"
