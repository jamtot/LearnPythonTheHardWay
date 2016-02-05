from sys import argv

script, input_file = argv

def print_all(f):
#prints all contents of file f
    print f.read()

def rewind(f):
#moves back to the start of file f
    f.seek(0)

def print_a_line(line_count, f):
#prints the position of the current line,
#along with the current line
    print line_count, f.readline(),

#opens and puts the input file into var current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

#calls print_all function on current_file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#calls rewind function on current_file
rewind(current_file)

print "Let's print three lines:"

#sets a line counter
current_line = 1
#prints the line using the print_a_line function
print_a_line(current_line, current_file)

#increments the line counter
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
