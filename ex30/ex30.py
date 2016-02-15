people = 30
cars = 40
trucks = 15

#if cars are greater than people
if cars > people:
    print "We should take the cars."
#else if cars are less than people
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

#if trucks are greater than cars
if trucks > cars:
    print "That's too many trucks."
#else if trucks are less than cars
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

# if people are greater than trucks
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
