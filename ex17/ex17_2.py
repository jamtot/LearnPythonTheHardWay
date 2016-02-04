from sys import argv
from os.path import exists

script, from_file, to_file = argv

if exists(from_file):
    print "Copying from %s to %s" % (from_file, to_file)
    indata = open(from_file).read()
    out_file = open(to_file, 'w').write(indata)
    
else:
    print "The file you are copying from does not exist."
