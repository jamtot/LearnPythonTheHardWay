from Map import Map

class Engine(object):
    def __init__(self, roomMap):
        self.roomMap = roomMap

    def play(self):
        currentRoom = self.roomMap.firstRoom()
        lastRoom = self.roomMap.nextRoom("finalRoom")

        while currentRoom != lastRoom:
            nextRoomName = currentRoom.enter()
            currentRoom = self.roomMap.nextRoom(nextRoomName)

        currentRoom.enter()  # so we still enter the last room

