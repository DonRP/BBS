# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Bobby's family
default mcI = Information(name = "Bobby", sname = "Brown", age = 18, active = True, rel_status = rel.get('single'))
define mc = Character("{b}[mcI.name]{/b}", color="#09f")
default lizI = Information(name = "Liza", sname = mcI.sname, age = (19), active = True)
define liz = Character("{b}[lizI.name]{/b}", color="#d600d0")
default lizR = Relationship("housemate", "housemate", True)
default lizN = Relationship("", _("Smurf"), True)
default lizforann = Relationship("leaseholder", "landlord", True)
# Ann's family
default annI = Information(name = "Ann", sname = "Bernard", age = 40, active = True, rel_status = rel.get('single'))
define ann = Character("{b}[annI.name]{/b}", color="#8a0086")
default annR = Relationship("landlord", "leaseholder", True)
default lcyI = Information(name = "Lucy", sname = annI.sname, age = (22))
define lcy = Character("{b}[lcyI.name]{/b}", color="#a800a3")
default lcyR = Relationship("housemate", "housemate", True)
default jnnI = Information(name = "Jenny", sname = annI.sname, age = (18))
define jnn = Character("{b}[lcyI.name]{/b}", color="#a800a3")
default jnnR = Relationship("housemate", "housemate", True)

# The game starts here.

label start:
    # The real start of the game
    call screen check_age
    "Welcome to [config.name]"

    call intro

    return
