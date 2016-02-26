from outside import Outside
from finalRoom import FinalRoom
from dead import Dead
from atDoor import AtDoor
from inCar import InCar
from kitchen import Kitchen
from comeIn import ComeIn

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
