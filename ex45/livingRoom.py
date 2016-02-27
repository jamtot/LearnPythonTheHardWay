from room import Room
from aneurysm import Aneurysm

class LivingRoom():

    maryPresent = True # using a class variable

    def __init__(self):
        pass

    def enter(self):
        from kitchen import Kitchen

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
            elif ("fred" in choice or "Fred" in choice) and self.maryPresent:
                print "\"Oh Fred? I think he's out in the kitchen, if not"
                print "he'll be back in a minute.\""
            else:
                if self.maryPresent and Kitchen.fredHidden:
                    print "Mary tells you to shush, without looking away"
                    print "from at the TV."
                    print "You look to see what she's watching, and it's"
                    print "the finale of your favourite show."
                    print "You had it recorded to watch later, and now it's"
                    print "being ruined!"
                    print "\"AWW S**T!\" you roar as you try grab for your"
                    print "gun. As you try swing it around to point at Mary"
                    print "it slips from your hand. She shrieks and lunges"
                    print "for the gun. \"FRED?! FRED?! WHAT HAVE YOU DONE"
                    print "TO HIM?\""
                    print "She runs out to the kitchen while keeping the gun"
                    print "pointed at you. \"THERE'S BLOOD! WHY IS THERE"
                    print "BLOOD, BILL?\""
                    print "\"I-I can exp-plain...\" you stutter out."
                    print "As she approaches with the gun pointed at you,"
                    print "you take the opportunity to lunge for it."
                    print "She squeezes the trigger before you can get it."
                    return "dead"
                elif self.maryPresent and not Kitchen.fredHidden:
                    print "Mary turns and asks you where Fred is."
                    print "\"He said he was getting me some sugar,"
                    print "but he's been a while,\" you answer."
                    print "\"I'll go check on him,\" says Mary as she gets"
                    print "up off the sofa. She disappears into the kitchen."
                    print "\"FRED? FRED! OH GOD FRED!\" you hear her wail."
                    print "You run in to see her holding Fred, with his"
                    print "limp head on her lap. \"CALL THE AMBULANCE, I"
                    print "THINK HE COULD BE REALLY HURT!\""
                    return "ambulance"
                elif not self.maryPresent:
                    print "You look around. The TV is on."
                    print "It's your favourite show. It's the finale!"
                    print "Mary must have been watching it. You had it"
                    print "recorded because you didn't get to watch it"
                    print "last night with the in-law dinner."
                    print "\"GODDAMN IT!\" you screech as a pivotal plot-"
                    print "point unfolds in front of you."
                    return "aneurysm"

    # haven't yet got these implementations to work
    def getMaryPresent(self): 
        return self.maryPresent

    def setMaryPresent(self, mPresent):
        self.maryPresent = mPresent
