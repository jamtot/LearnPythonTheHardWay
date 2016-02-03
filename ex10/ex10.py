#using escape character to put quote marks into string
print "I am 6'3\" tall."
print 'I am 6\'3" tall.'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

timer = 10000
while timer > 0:
    timer = timer - 1
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
        
