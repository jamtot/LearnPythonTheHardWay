from Room import Room
from random import randint

class Dead(Room):
    
    lines = [
        "You just died in a game about borrowing sugar.",
        "You just... died? In this game? How?",
        "Did you have to do that?",
        "Goddamnit Bill.",
        "..."
    ]

    def enter(self):
        print "You have died."
        print Dead.lines[randint(0, len(self.lines)-1)]
        exit(1)
