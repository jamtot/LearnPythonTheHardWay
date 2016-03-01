path = r"/home/jamtot/Python/LrnPython/projects/ex49/ex49/"

# have a reference list of words for each category to compare
# i.e. direction words, verbs, nouns, etc.

def getList(txtPath):
    with open(txtPath) as listTxt:
        lexList = (listTxt.read()).splitlines()
        return lexList

directionList = getList(path+"lex_direction.txt")
verbList = getList(path+"lex_verb.txt")
stopList = getList(path+"lex_stop.txt")
nounList = getList(path+"lex_noun.txt")

def scan(userInput):
    inputList = (userInput.lower()).split()

    result = []
    # compare each input word against the reference lists
    for word in inputList:
        if word in directionList:
            result.append(('direction', word))
        elif word in verbList:
            result.append(('verb', word))
        elif word in stopList:
            result.append(('stop', word))
        elif word in nounList:
            result.append(('noun', word))
        elif convert_number(word) is not None:
            result.append(('number', convert_number(word)))
        else:
            result.append(('error', word))

    # return the tuples
    return result

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
