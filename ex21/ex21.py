def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(19, 5)
height = subtract(79, 4)
weight = multiply(90, 2)
iq = divide(200, 2) 

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (
    age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"

print "Can you use the functions to figure out 24 + 34 / 100 - 1023?"
answer = add(24, divide(34, subtract(100,1023)))
print "Why yes I can, the answer is %d." % answer

print "Can you use the functions to figure out (24 + 34) / (100 - 1023)?"
answer = divide( add( 24, 34), subtract(100, 1023) )
print "Why yes I can, the answer is %d." % answer
