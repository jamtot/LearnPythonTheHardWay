import time
import sys

oneAtATime = """Hi. My name is Jonathan Morris. 
I'm trying to get this string to reveal itself one letter at a time. I think that would be pretty cool. 

Especially for my text adventure game."""

#i = 0
#while i < len(oneAtATime):
#    print oneAtATime[i],
#    i += 1
#    time.sleep(0.1)

#for char in oneAtATime:
#    print char
#    time.sleep(0.1)

# the result is spaced out due to the print
# statement adding it's own space between each print
# also the whole line only appears after each
# character has been inserted. This means it goes
# seconds of a blank line, then the whole line
# appears. When printing downwards it works for
# each letter. It must be to do with the terminal
# only being able to print single lines at a
# time. Could try erasing the line and rewriting
# it with an additional letter each time.

def stringWriter(stringToWrite):
    newString = ""
    i = 0
    #using carriage return to go back on the line \r
    while i < len(stringToWrite): 
        newString = newString + stringToWrite[i]
        print "%s" % newString,   
        print "\r",   
        i += 1
        time.sleep(0.05)

    print newString

#stringWriter(oneAtATime)

# trying an online solution

def delay_print(stringToWrite):
    for char in stringToWrite:
        # need to use a stream to get everything in the right place
        sys.stdout.write( '%s' % char )
        # and to flush the buffer
        sys.stdout.flush()
        time.sleep(0.05)

# this works exactly like how I intended
delay_print(oneAtATime)
