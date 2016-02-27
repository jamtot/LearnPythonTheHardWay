from room import Room

class Aneurysm(Room):

    def enter(self):
        print "You get so worked up, your face turns red and you can"
        print "actually hear a loud pop."
        print "Your head feels light, yet stuffy."
        print "Your vision starts to get spotty as you feel yourself"
        print "drop to the floor."
        print "You feel pressure in your head as your vision goes black."
        return "dead"
