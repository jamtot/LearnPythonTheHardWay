from room import Room

class Engine(object):
    
    def __init__(self):#, current_room):
        pass#self.current_room = current_room

    def play(self, current_room):
        current_room.print_location()
        while True:
            pInput = raw_input("> ")
            action = pInput.split(' ')
            temp_room = current_room
            
            if "list" in action[0] or 'item' in action[0]:
                current_room.list_items()
            elif len(action) == 1:
                current_room = self.tryGo(current_room, action[0])
            elif len(action) == 2 and (action[0] == 'go' or action[0] == 'walk'):
                current_room = self.tryGo(current_room, action[1])
            else:
                print "I don't understand."

    def tryGo(self, current_room, direction):

        temp_room = current_room        
        try:
            current_room = current_room.go(direction)
            current_room.print_location()
        except:
            print "Invalid input."
            # set to last room
            current_room = temp_room
        return current_room

