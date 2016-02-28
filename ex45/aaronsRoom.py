from room import Room

class AaronsRoom(Room):
    
    def enter(self):
        print "LOCATION: AARON'S ROOM"
        print "You are in Aaron's room."
        print "There's a framed picture on the wall."
        print "Aaron's bed is a car. The kid has it made."
        while True:
            choice = raw_input("> ")
            if "bed" in choice or "car" in choice:
                print "You hop onto the bed and pretend to drive it."
                print "\"Brrrrrrrruuuuum!\""
                print "What is wrong with you?"
                print "Don't answer that."
            elif "pic" in choice or "frame" in choice or "wall" in choice:
                print "It looks like it's a birthday memory type picture."
                print "It says when Aaron was born, '01, who his grandparents"
                print "and parents are, where he was born, etc."
                print "Sentimental s**t he won't care about."
            elif ("leave" in choice or "door" in choice or "landing" in choice or
                        "hall" in choice or "back" in choice):
                return "landing"
            else:
                print "Here you are, just standing in Fred and Mary's youngests'"
                print "room."
