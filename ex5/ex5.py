my_name = 'Jonathan Morris'
my_age = 24 # for now
my_height = 75 # inches
my_weight = 180 # ish lbs
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Golden Brown'

def inchesToCMs(inches = 0.):
    return 2.54*inches

def poundsToKGs(pounds = 0.):
    return 0.453592*pounds

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "That is %f in CMs." % round(inchesToCMs(my_height),2)
print "He's %d pounds heavy." % my_weight
print "That is %f in KGs." % round(poundsToKGs(my_weight),2)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d, I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
