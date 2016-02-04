#imports the command-line arguments from sys 
from sys import argv

#puts the arguments values in variables, the name of the script, and the filename typed
script, filename = argv

#opens the file and puts it into a variable 
txt = open(filename)

#prints the name of the file
print "Here's your file %r:" % filename
#reads the contents of the file txt
print txt.read()
txt.close()

print "Type the filename again:"
#takes in the name of the file through user input this time
file_again = raw_input("> ")

#opens the file and puts it into a variable
txt_again = open(file_again)

#reads the contents of the file txt_again
print txt_again.read()
txt_again.close()
