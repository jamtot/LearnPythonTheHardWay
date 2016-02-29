from engine import Engine
from room import Room

north = Room("North Room", """This room is to the north of the center room.
You can also reach the East and West rooms from here.""", ['kid\'s water floaties'])
south = Room("South Room", """This room is to the south of the center room.
You can also reach the East and West rooms from here.""")
center = Room("Center Room", """This room is surrounded by 4 rooms. 
To the North, South, East and West.""", ['sword', 'chocolate bar', 'helmet'])
east = Room("East Room", """This room is to the east of the center room. 
You can also reach the North and South rooms from here.""")
west = Room("""West Room", "This room is to the west of the center room.
You can also reach the North and South rooms from here.""", ['walkman', 'fanny pack'])

north.add_paths({'down': center, 'center': center, 'east': east, 'west': west})
south.add_paths({'up': center, 'center': center, 'east': east, 'west': west})
center.add_paths({'north': north, 'south': south, 'east': east, 'west': west})
east.add_paths({'center': center, 'north': north, 'south': south})
west.add_paths({'center': center, 'north': north, 'south': south})

test_engine = Engine()
test_engine.play(center)
