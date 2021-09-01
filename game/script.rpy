# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Bobby's family
default mcI = Information(name = "Bobby", sname = "Brown", age = 18, active = True, rel_status = rel.get('single'))
define mc = Character("{b}[mcI.name]{/b}", color="#09f", image="mcemo")
default lizI = Information(name = "Liza", sname = mcI.sname, age = (19), active = True)
define liz = Character("{b}[lizI.name]{/b}", color="#d600d0", image="lizemo")
default lizR = Relationship("housemate", "housemate", True)
default lizN = Relationship("", _("smurf"), True)
default lizforann = Relationship("leaseholder", "landlord", True)
# Anna's family
default annI = Information(name = "Anna", sname = "Bernard", age = 40, active = True, rel_status = rel.get('single'))
define ann = Character("{b}[annI.name]{/b}", color="#8a0086", image="annemo")
default annR = Relationship("landlord", "leaseholder", True)
default lcyI = Information(name = "Lucy", sname = annI.sname, age = (22))
define lcy = Character("{b}[lcyI.name]{/b}", color="#a800a3", image="lcyemo")
default lcyN = Relationship("", _("dwarf"), True)
default lcyR = Relationship("housemate", "housemate", True)
default jnnI = Information(name = "Jenny", sname = annI.sname, age = (18))
define jnn = Character("{b}[lcyI.name]{/b}", color="#a800a3", image="jnnemo")
default jnnR = Relationship("housemate", "housemate", True)
# Olther
default mikI = Information(name = "Mike", sname = "Williams", age = (20))
define mik = Character("{b}[lcyI.name]{/b}", color="#09f", image="mikemo")

# The game starts here.

label start:
    # The real start of the game
    stop music fadeout 1.0
    call screen check_age
    show screen watermark
    "Welcome to [config.name]"

    call intro
    call intro_dream
    call start_scene

    $ sp_routine["liza_kitchen1"] = Commitment(chs={}, tm_start=0, tm_stop=24, id_location="house", id_room="kitchen", label_event="liza_kitchen1")

    $ cur_room = rooms[0]
    $ cur_location = locations[cur_room.id_location]
    $ prev_room = rooms[0]
    $ updateBL()
    $ bl_values["block_spendtime"] = True

    call after_wait
    return
