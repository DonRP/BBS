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

## Functions for discord
# https://arianeb.com/2019/07/19/adding-discord-rich-presence-to-renpy-games/
init -20 python:
    if renpy.variant("pc"):
        import discord_rpc
        import time

        def readyCallback(current_user):
            print('Our user: {}'.format(current_user))

        def disconnectedCallback(codeno, codemsg):
            print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
                codeno, codemsg
            ))

        def errorCallback(errno, errmsg):
            print('An error occurred! Error {}: {}'.format(
                errno, errmsg
            ))

label before_main_menu:
    if renpy.variant("pc"):
        python:
            # Note: 'event_name': callback
            callbacks = {
                'ready': readyCallback,
                'disconnected': disconnectedCallback,
                'error': errorCallback,
            }
            discord_rpc.initialize('882718196749193286', callbacks=callbacks, log=False)
            start = time.time()
            print(start)
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()
            discord_rpc.update_presence(
                **{
                    'details': 'Main Menu',
                    'start_timestamp': start,
                    'large_image_key': 'Bad Bobby Saga'
                }
            )
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()

    return
## END Functions for discord


# The game starts here.

label start:
    ## Adding Discord Rich
    if renpy.variant("pc"):
        python:
            callbacks = {
                'ready': readyCallback,
                'disconnected': disconnectedCallback,
                'error': errorCallback,
            }
            discord_rpc.initialize('882718196749193286', callbacks=callbacks, log=False)
            start = time.time()
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()
            discord_rpc.update_presence(
                **{
                    'details': 'At College',
                    'state': 'Lecture Hall',
                    'large_image_key': 'Bad Bobby Saga',
                    'start_timestamp': start
                }
            )

            discord_rpc.update_connection()
            discord_rpc.run_callbacks()

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
