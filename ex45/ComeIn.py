from Room import Room

class ComeIn(Room):

    def enter(self):
        print "You follow Fred down the hall towards the kitchen."
        print "You pass the living room on your left, the play room"
        print "and the stairs are on your right."
        print "\"You startled me there when you knocked on the door.\""
        print "\"The knock was so hard I thought it was the police.\""
        print "\"I spilt my milk as I poured it on my breakfast.\""
        print "\"You must really need that sugar,\" laughs Fred."
        print "\"Yea..\" you mumble under your breath."
        print "As you walk in through the door to the kitchen, you see"
        print "the open jug and all the spilt milk on the table."
        print "Fred wasn't joking."
        print "He heads around the table towards the cabinets."
        print "As he reaches out to a cabinet he slips and cracks his"
        print "head on the corner of the table, and hits the floor with"
        print "a thunk."
        print "\"Uh.. Fred?\""
        print "No answer."
        return "kitchen"
