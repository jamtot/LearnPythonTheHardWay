from room import Room
from livingRoom import LivingRoom
from hall import Hall

class Kitchen(Room):

    fredHidden = False

    def __init__(self):
        self.checkedBowl = False  
        #self.lRoomInst = LivingRoom()  
        

    def enter(self):
        Hall.fredFell = True
        print "LOCATION: KITCHEN"
        if not self.fredHidden:
            print "Fred is lying unresponsive on the floor."
            print "There's blood pooled around his head."
        else:
            print "There's some blood on the floor."
        if not self.checkedBowl:
            print "You can see the sugar bowl in the cabinet."
        print "There's a door to the living room, the hall, and the pantry."

        while True:
            choice = raw_input("> ")
            if "sugar" in choice or "cabinet" in choice:
                print "You step over Fred to get to the cabinet."
                print "You take down the sugar bowl and take off the lid."
                print "It's empty."
                print "\"F**k.\" you mutter under your breath."
                print "You put the empty sugar bowl back."
                self.checkedBowl = True
                return "kitchen"
            elif ("help" in choice or "Fred" in choice or "fred" in choice) and (
                    LivingRoom.maryPresent and not self.fredHidden):
                print "\"FRED!\" you shout. \"OH MY GOD!\""
                print "\"I NEED THAT SUGAR, C'MON FRED!\""
                print "He doesn't move."
                print "His wife runs in from the living room asking what"
                print "all the commotion is about."
                print "She screams when she you over her lifeless,"
                print "bleeding husband."
                print "\"WHAT THE F**K HAVE YOU DONE, BILL?\""
            
                while True:
                    whatDone = raw_input("> ")
                    if ("nothing" in whatDone or "slipped" in whatDone or
                            "help" in whatDone or "milk" in whatDone):
                        print "You gotta help, Mary!"
                        print "Fred slipped on some spilt milk."
                        print "I think he's really hurt!"
                        return "ambulance"
                    elif "kill" in whatDone:
                        print "\"I killed him.\" you say sarcastically."
                        print "\"Obviously I killed him.\""
                        print "Mary screams at the top of her lungs!"
                        print "The sarcasm goes over Mary's head."
                        print "She pulls out her phone and starts running."
                        LivingRoom.maryPresent = False
                        return "kitchen"
                    else:
                        print "Mary assumes the worst."
                        print "She runs out of the kitchen screaming."
                        LivingRoom.maryPresent = False
                        return "kitchen"

            elif ("help" in choice or "Fred" in choice or "fred" in choice or 
                    "mary" in choice or "Mary" in choice) and (
                    not LivingRoom.maryPresent and not self.fredHidden):
                print "Mary's gone. You try to help Fred."
                print "He doesn't seem to have a pulse."
                print "I'm no doctor, but I think Fred is dead."
            elif ("help" in choice or "Fred" in choice or "fred" in choice or 
                    "mary" in choice or "Mary" in choice) and (
                    LivingRoom.maryPresent and self.fredHidden):
                print "Mary comes in to see what all the commotion is about."
                print "\"Oh hi, Bill. Didn't realise you were here. Fred must"
                print "have let you in. He's probably nipped off to the bath-"
                print "room. Can I help you?"
                while True:
                    maryHelp = raw_input("> ")
                    if "sugar" in maryHelp:
                        print "\"Oh sugar? If there's none in the sugar bowl"
                        print "or in the pantry, it's probably upstairs in"
                        print "our bedroom. We've had to start hiding it on"
                        print "little Dylan. He eats the stuff by the bag"
                        print "when he finds it. Won't go near the sweetener."
                        print "Only sugar. Funny, that.\""
                        print "Mary heads back into the living room."
                        return "kitchen"
                    elif "fred" in maryHelp or "Fred" in maryHelp:
                        print "Fred? I don't know where Fred is."
                        print "I'm sure he'll be back soon."
                    elif "cupboard" in maryHelp:
                        print "You tell Mary to check the cupboard."
                        print "As she goes to look she's laughing, asking"
                        print "you if it's a present, or Fred hiding."
                        print "You take out your gun and take aim as she"
                        print "opens the door. \"What the hell?\""
                        print "Mary turns around with a horrified look on her"
                        print "face. \"Is this a jo..\" she's staring down the"
                        print "barrel. You pull the trigger."
                        print "Realising what you've done, you turn the gun"
                        print "on yourself."
                        return "dead"
            elif ("hide" in choice or "body" in choice or "move" in choice) and (
                    not self.fredHidden):
                print "You search frantically for a place to hide Fred's body."
                print "You stuff him the cupboard under the sink."
                self.fredHidden = True
            elif ("hide" in choice or "body" in choice or "move" in choice) and (
                    self.fredHidden):
                print "You've already hidden the body."
                print "The body of your neighbour."
                print "You monster."
            elif "living" in choice:
                return "livingRoom"
            elif "hall" in choice:
                return "hall"
            elif "pantry" in choice:
                return "pantry"
