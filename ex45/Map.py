from Outside import Outside
from FinalRoom import FinalRoom
from Dead import Dead
from AtDoor import AtDoor
from InCar import InCar
from Kitchen import Kitchen
from ComeIn import ComeIn

class Map(object):

    rooms = {
        "outside" : Outside(),
        "atDoor" : AtDoor(),
        "inCar" : InCar(),
        "comeIn" : ComeIn(),
        "kitchen" : Kitchen(),
        "dead" : Dead(),
        "finalRoom" : FinalRoom()
        }

    def __init__(self, firstRoom):
        self.currentRoom = firstRoom

    def nextRoom(self, nextRoom):
        val = self.rooms.get(nextRoom)
        return val
    
    def firstRoom(self):
        return self.nextRoom(self.currentRoom)
