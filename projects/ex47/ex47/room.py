class Room(object):

    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def list_items(self):
        if not list:
            print "There are no items."
        else:
            for item in self.items:
                print item

    def grab_item(self, item):
        if item in self.items:
            for i in range(len(self.items)):
                if self.items[i] == item:
                    print "Grabbing %s." % item
                    return self.items.pop(i)    
                    break # no need to continue looping            
        else:
            print "You can't grab what isn't here."

    def drop_item(self, item):
        self.items.append(item)

    def amount_of_items(self):
        return len(self.items)
