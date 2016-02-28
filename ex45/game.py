from myMap import Map
from engine import Engine

#gameMap = Map("outside").
gameMap = Map("landing")
game = Engine(gameMap)
game.play()
