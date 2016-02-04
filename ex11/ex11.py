print "What is your name?",
name = raw_input()
print "How old are you, %s?" % name,
age = raw_input()
print "So you're %s years old, how tall are you?" % age,
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# changed %r for raw input, to %s, to output the strings interpreted by the raw_input() command
print "So %s, you're %s years old, %s tall and %s heavy. Thanks!" % (
    name, age, height, weight)
