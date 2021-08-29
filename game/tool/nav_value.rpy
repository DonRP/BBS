define rooms = [
        Room(id="mc_room", id_location="house", name=_("[mc] room"), icon="icon mcroom", bg="bg mcroom", id_actions = ["sleep", "nap", "laptop", "carpet",]), 
        Room(id="liza_room", id_location="house", name=_("[liz] room"), icon="icon lizaroom", bg="bg lizaroom", id_actions = ["laptop_liza",]), 
        Room(id="livingroom", id_location="house", name=_("Lounge"), icon="icon livingroom", bg="bg livingroom", id_actions = ["kitchen",]),
        Room(id="kitchen", id_location="house", name=_("Kitchen"), bg="bg kitchen"),
    ]

define locations = {
        "house"     :   Location(id = "house", key_map="map", id_externalroom="livingroom", name=_("[mc] house"), icon="icon map home", xalign=0.3, yalign=0.2), 
    }

define map_images = {
        "map"       :   "bg map",
    }

define ch_icons = {
    }

default cur_room = rooms[0]
default cur_location = locations[cur_room.id_location]
# Variable to check the map screen: if it is True then the player is viewing the map.
default map_open = False
