from room import Room

class Hall(Room):
    
    def __init__(self):
        self.fredFell = False
    
    def enter(self):
        print "LOCATION: HALL"
        print "You are in the hall."
        print "The kitchen is in front of you."
        print "The living room is to your left."
        print "The play room is to your right."
        print "So is the stairs."
        if not self.fredFell:
            print "You hear a noise in the kitchen." 
            self.fredFell = True   
                
        while True:
            choice = raw_input("> ")
            if "kitchen" in choice:
                return "kitchen"
            elif "living" in choice:
                return "livingRoom"
            elif "play" in choice:
                return "playRoom"
            elif "stairs" in choice or "up" in choice:
                return "upStairs"
            elif "front" in choice or "leave" in choice or "door" in choice:
                print "You are not leaving without the sugar."
            else:
                print "Not really sure what you want me to do."
