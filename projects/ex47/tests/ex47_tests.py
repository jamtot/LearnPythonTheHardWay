from nose.tools import *
from ex47.room import Room
from ex47.engine import Engine

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down':down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_items():
    itemroom = Room('itemroom', "There are items in this room.", ['item1', 'item2', 'item3'])
    assert_equal( itemroom.amount_of_items(), 3)    
    assert_equal( itemroom.grab_item('item2'), 'item2')
    assert_equal( itemroom.amount_of_items(), 2)

def test_engine():
    top = Room("TopRoom", "This room is on top of the bottom room.")
    bottom = Room("BottomRoom", "This room is on the bottom of the top room.")
    top.add_paths({'down': bottom, 'bottom': bottom})
    bottom.add_paths({'up': top, 'top': top})

    test_engine = Engine()
    assert_equal(test_engine.tryGo(top, 'down'), bottom)
