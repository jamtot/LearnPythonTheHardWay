from room import Room
from dead import Dead
from comeIn import ComeIn

class AtDoor(Room):
    
    def enter(self):
        print "You knock on the door."
        print "......"
        print "Fred, the neighbour answers the door."
        print "\"Oh hi there Bill. What can I do for you?\""

        while True:
            choice = raw_input("> ")
            if "sugar" in choice:
                print "\"Oh sure Bill, you can have some sugar.\""
                print "\"Come on in while I get it.\""
                return "comeIn"
            else:
                print "\"I don't quite get what you're asking, Bill.\""
                print "This is angering."
                print "You pull out your gun and put it to Fred's head."
                print "\"Why do you have a gun, there, Bill?\""
                print "\"P-p-put th-the gun down, there, B-Bill.\""
                print "\"P-please put the g-gun down, Bill.\""
                print "Without thinking, you squeeze the trigger."
                print "eeeeeeeeeeeeeeeeeeeeee"
                print "Fred's face is sprayed across the wall."
                print "\"DADDY?\" comes from the other room."
                print "Oh no. What have I done?"
                print "You turn the gun on yourself."
                return "dead"
