class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def remove_line(self, remline):
        print "LINE REMOVAL"
        lines = len(self.lyrics)
        self.sing_me_a_song()
        print "There are %d lines to start." % lines
        if (remline < lines):
            print "Line removed: %s" % self.lyrics.pop(remline)
            self.sing_me_a_song()
        else:
            print "Not possible to remove that line."

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song() 

print '-' * 10

happy_bday.remove_line(0)

print '-' * 10

bulls_on_parade.remove_line(1) 

print '-' * 10

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song() 
