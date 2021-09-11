# "special" actions:
# they are not usual actions, but actions inserted and removed for a specific reason, for example for a quest.
# IMPORTANT: specify in sp_room the id of the room where the action will take place
default sp_actions = {}

# habitual actions
define df_actions = {
        "nap"               :   Action(_("Nap"), "/location/mcroom-bed.webp", label = "nap", tm_start=5, tm_stop=23,
            is_in_room = True, xpos = 830, ypos = 411),
        "sleep"             :   Action(_("Sleep"), icon = "/location/mcroom-bed.webp", label = "sleep", tm_start=23, tm_stop=5,
            is_in_room = True, xpos = 830, ypos = 411),
        "laptop"            :   Action(name = _("Laptop"), icon = "/location/mcroom-laptop.webp", icon_selected = "/location/mcroom-laptop a.webp", label = "laptop",
            is_in_room = True, xpos = 271, ypos = 396),
        "carpet"            :   Action(_("Stealth Training"), icon = "/location/mcroom-carpet.webp", label = "carpet",
            is_in_room = True, xpos = 732, ypos = 776),
        "laptop_liza"       :   Action(name = _("Laptop"), icon = "/location/lizaroom-laptop.webp", icon_selected = "/location/lizaroom-laptop a.webp", label = "laptop",
            is_in_room = True, xpos = 1575, ypos = 331),
        "kitchen"   :   Action(name = _("Go to the Kitchen"), icon = "/location/livingroom-kitchen.webp", label = "go_kitchen",
            is_in_room = True, xpos = 408, ypos = 664),
    }
