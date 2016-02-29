import datetime

class WeightChecker(object):
    
    def __init__(self, wFile): 
        self.weightTxtFile = wFile
        with open(self.weightTxtFile) as weightFile:
            self.weightFileData = weightFile.read()
            self.weightLines = self.weightFileData.splitlines()

    def printLines(self):
        for line in self.weightLines:
            print line
    
    def addLine(self):
        newLine = raw_input("How heavy are you in lbs? ")
        newLine = ('').join((newLine,'lbs'))
        today = datetime.datetime.now().strftime("%d/%m/%y")
        newLine = ('|').join((newLine, today))
        self.weightLines.append(newLine)
        print "Line added."

    def saveFile(self):
        with open(self.weightTxtFile, 'r+') as weightFile:
            newFileData = ('\n').join(self.weightLines)
            weightFile.write(newFileData)
            print "File saved."
