from outside import Outside
from finalRoom import FinalRoom
from dead import Dead
from atDoor import AtDoor
from inCar import InCar
from kitchen import Kitchen
from comeIn import ComeIn
from hall import Hall
from livingRoom import LivingRoom
from playRoom import PlayRoom
from upStairs import UpStairs
from downStairs import DownStairs
from landing import Landing
from ambulance import Ambulance
from pantry import Pantry

class Map(object):

    rooms = {
        "outside" : Outside(),
        "atDoor" : AtDoor(),
        "inCar" : InCar(),
        "comeIn" : ComeIn(),
        "kitchen" : Kitchen(),
        "hall" : Hall(),
        "dead" : Dead(),
        "livingRoom" : LivingRoom(),
        "playRoom" : PlayRoom(),
        "upStairs" : UpStairs(),
        "downStairs" : DownStairs(),
        "ambulance" : Ambulance(),
        "landing" : Landing(),
        "pantry" : Pantry(),
        "finalRoom" : FinalRoom()
        }

    def __init__(self, firstRoom):
        self.currentRoom = firstRoom

    def nextRoom(self, nextRoom):
        val = self.rooms.get(nextRoom)
        return val
    
    def firstRoom(self):
        return self.nextRoom(self.currentRoom)
