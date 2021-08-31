label liza_kitchen1:
    show bg LizaKitchen A00
    liz 00 "Hey there [lizN.MClabel]!"
    liz 01 "Yawn! Be nice I forgot my cell phone in my room...go get it!"
    menu:
        "Okay":
            mc 02 "Okay"
            pass
        "What about me?!":
            mc 10 "What about me?! What do I get in return?"
            liz 04 "For you?!"
            liz 02 "Haha! Well, I was thinking of making some eggs... what do you say?"
            mc 00 "Hmm... that's good"
    $ smartphone_liza = False
    $ sp_actions["lizasmartphone"] = Action(name = _("Liza smartphone"), icon = "/location/lizaroom-smartphone.webp", icon_selected = "/location/lizaroom-smartphone a.webp", label = "liza_kitchen1_lizasmartphone", sp_room='liza_room',
            is_in_room = True, xpos = 922, ypos = 563)
    $ sp_routine["liza_kitchen1B"] = Commitment(chs={"liza" : TalkObject(bg_before_after="bg LizaKitchen A01", label_talk="liza_kitchen1B")}, tm_start=0, tm_stop=24, id_location="house", id_room="kitchen")
    return
label liza_kitchen1_lizasmartphone:
    mc 09 "{i}Hmmm, Liza's phone! She's always on the phone, I wonder who she's chatting with. I might..."
    show smartphone bobby liza
    mc 09 "{i}Shit, he's got the password!"
    mc 10 "{i}Ah though! what a background... slutty."
    $ del sp_actions["lizasmartphone"]
    $ smartphone_liza = True
    hide smartphone
    jump after_wait
label liza_kitchen1B:
    show bg LizaKitchen A01
    liz 01 "So, did you get my phone?"
    menu:
        "Indeed!" if (smartphone_liza):
            pass
        "Not yet!" if True:
            liz 06 "Go ahead! What are you waiting for."
            jump after_wait
    jump liza_kitchen1end
label liza_kitchen1Error:
    jump liza_kitchen1end
label liza_kitchen1end:
    jump after_wait
