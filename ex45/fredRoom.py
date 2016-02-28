from room import Room

class FredRoom(Room):
    def __init__(self):
        self.code = "019996"
        self.picDown = False
        self.safeLocked = True
    
    def enter(self):
        print "LOCATION: FRED AND MARY'S ROOM"
        print "You are in Fred and Mary's room."
        print "There's a pink, flowery kimono on the bed."
        if not self.picDown:
            print "The wall is adorned by a single, out-of-place picture on" 
            print "the wall by their wardrobe."
        else:
            if self.safeLocked:
                print "There's a safe on the wall."
            else:
                print "The safe is wide open."
        while True:
            choice = raw_input("> ")
            if "kimono" in choice:
                print "You try on the kimono."
                print "You adore yourself in the mirror."
                print "It looks pretty damn good on you."
                print "You take it off and put it back."
            elif "pic" in choice and not self.picDown:
                print "You slap the picture off the wall, it's ruining the"
                print "feng shui of the room."
                print "The picture was covering a safe."
                self.picDown = True
            elif "safe" in choice and self.picDown:
                print "The safe takes 6 digits. I bet it's something"
                print "easy like their kids' birth years or something."
                while True:
                    safeCode = raw_input("> ")
                    if safeCode == "019996":
                        print "*CLICK* Woah. Of course it was the kids' birthdays."
                        print "You open the safe door. It contains 5 passports"
                        print "and a bag of sugar."
                        print "They keep their sugar in the safe? Of course they do."
                        self.safeLocked = False
                        return "finalRoom"
                    elif ("stop" in safeCode or "back" in safeCode or "quit" in safeCode or
                                "room" in safeCode or "leave" in safeCode):
                        return "fredRoom"
                    else:
                        print "You have a million to one chance of guessing."
                        print "It's actually a million to one, 0-999999."
            elif ("leave" in choice or "hall" in choice or "door" in choice or
                            "landing" in choice or "back" in choice):
                return "landing"
            else:
                print "No."

