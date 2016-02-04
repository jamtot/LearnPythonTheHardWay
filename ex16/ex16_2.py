#asks user for input as to whether they want to read or write a file
print "Would you like to read or write a file? Insert r or w"
readOrWrite = raw_input(" >")

#if the user types a word beginning with r or R do this
if readOrWrite[0] == 'r' or readOrWrite[0] == 'R':
    print "Enter the name of the file you would like to read:"
    filename = raw_input(' >')
    #get the files name from input, and open the file into a var
    txt = open(filename)
    
    print "Here's your file %r:" % filename
    #read the file
    print txt.read()
    #close the file
    txt.close()
    
#if the user types a word beginning with w or W
elif readOrWrite[0] == 'w' or readOrWrite[0] == 'W':
    print "Enter the name of the file you would like to create/edit:"
    #get the files name from output
    filename = raw_input(' >')

    print "We're going to erase %r." % filename
    print "If you don't want that, hit CTRL-C (^C)."
    print "If you do want that, hit RETURN."

    raw_input("?")

    print "Opening the file..."
    #open the file to be written
    target = open(filename, 'w')

    #remove everything from the file
    print "Truncating the file.  Goodbye!"
    target.truncate()

    print "Now I'm going to ask you for three lines."

    #take in 3 lines to write to the file
    line1 = raw_input("line 1: ")
    line2 = raw_input("line 2: ")
    line3 = raw_input("line 3: ")

    print "I'm going to write these to the file."
    
    #write each line to the file
    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")
    target.write(line3)
    target.write("\n")

    print "And finally, we close it."
    #close the file
    target.close()

else:
    #a catch for if the user types something 
    #other than a letter or word beginning with r or w
    print "Yeah... that's not an 'r' or a 'w', buddy.",
    print "You can even type in the whole word, because I only check the first letter!"
