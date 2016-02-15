def looper(loops, inc=1):
    i = 0
    numbers = []

    while i < loops:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

looper(6)
looper(20,3)


def forLooper(loops, inc=1):
    i = 0
    numbers = []

    for i in range(0, loops, inc):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

forLooper(6)
forLooper(20, 3)
