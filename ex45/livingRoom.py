from room import Room

class LivingRoom():

    maryPresent = True # using a class variable

    def __init__(self):
        pass

    def enter(self):
        print "You are in the living Room."
        if self.maryPresent:
            print "Mary is here."
        else:
            print "There is no-one here."
        print "The TV is on."
        print "There's a door back into the hall, and a door into the"
        print "kitchen."

        while True:
            choice = raw_input("> ")
            if "hall" in choice:
                return "hall"
            elif "kitchen" in choice:
                return "kitchen"
            else:
                print "Mary just looks at you, then back at the TV."
        # Fred's wife watching your favourite show
        # the finale,
        # you had it recorded
        # hadn't got to see it yet
        # the end happens right then
        # you are pissed

    # haven't yet got these implementations to work
    def getMaryPresent(self): 
        return self.maryPresent

    def setMaryPresent(self, mPresent):
        self.maryPresent = mPresent
