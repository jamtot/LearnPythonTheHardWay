# create a function that takes an amount of cheese,
# and amount of crackers and outputs a message
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
print "We can just give the function numbers directly:"
# call the function using hard-coded numbers
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# call the function using numbers stored in variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# call the function using hard-coded numbers, and math
cheese_and_crackers(10 + 50, 5 + 6)

print "And we can combine the two, variables and math:"
# call the function using a combo of variables, hard-coded numbers, and math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def numSummer(num1, num2):
    num = num1 + num2
    print "The sum of the nums is %d." % num
    return num

def getNum(prompt):
    return int(raw_input(prompt))

num = numSummer(getNum("giz a num: "),getNum("giz anuvver num: "))
num = numSummer(num, getNum("Give me another number, and I'll add it to the last: "))
num = numSummer(num, getNum("Sure one more time: "))
