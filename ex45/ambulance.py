from room import Room

class Ambulance(Room):

    def enter(self):
        print "The ambulance is called."
        print "The police come."
        print "They ask you questions."
        print "A lot of questions."
        print "You haven't had your coffee."
        print "You hulk out and get gunned down by the cops."
        return "dead"
