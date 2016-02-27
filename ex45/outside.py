from room import Room

class Outside(Room):

    def enter(self):
        print "You are outside a house."
        print "Your neighbours house."
        print "You are looking to borrow some sugar."
        print "The front door to the house is in front of you."
        print "Your car is behind you."
        print "LOCATION: OUTSIDE FRED'S HOUSE"

        while True:
            choice = raw_input("> ")
            if "door" in choice:
                return "atDoor"
            elif "car" in choice:
                print "You want to leave?"
                print "Without any sugar?"
                print "Are you f**king serious?!"
                youSure = raw_input("> ")
                if "yes" in youSure:
                    print "It seems you are serious."
                    return "inCar"
                elif "no" in youSure:
                    print "Oh good, you were joking."
                    print "Funny."
                else:
                    print "I'm taking that as a no."
                    print "Even though it isn't."
            else:
                print "The choice is simple."
                print "It really is."
