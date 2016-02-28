from room import Room

class DylsRoom(Room):
    
    def __init__(self):
        self.pillowTalk = False
    
    def enter(self):
        print "LOCATION: DYLAN'S ROOM"
        print "You are in Dylan's room."
        print "Slim Dylan. The middle child."
        print "Dylan is asleep in his bed."
        print "There's a picture on his bedside locker. It's a collage."
        while True:
            choice = raw_input("> ")
            if "pic" in choice or "locker" in choice or "collage" in choice:
                print "It's a picture of Dylan with his family, his friends,"
                print "damn near everyone. It says \"HAPPY 5TH BIRTHDAY"
                print "DYLAN, 2004\"."
            elif "dylan" in choice or "Dylan" in choice or "bed" in choice:
                if not self.pillowTalk:
                    print "You pick a pillow off the floor and place it over"
                    print "sleeping Dylan's face."
                    print "He struggles and you hear muffled screams."
                    print "Silence again."
                    self.pillowTalk = True
                else:
                    print "Dylan is 'sleeping'."
            elif ("leave" in choice or "door" in choice or "hall" in choice or
                            "landing" in choice or "back" in choice):
                return "landing"
            else:
                print "You'll wake Dylan if you don't start making sense."
