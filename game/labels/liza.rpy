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
        "Not yet!":
            liz 06 "Go ahead! What are you waiting for."
            jump after_wait

    liz 08 "Finally! what took you so long?"
    menu:
        "I couldn't find it":
            mc 02 "I had a little trouble finding it!"
            liz 03 "Bah, you are so weird! it was right on my nightstand."
        "About your password...":
            mc 06 "By the way, what is the password?"
            liz 09 "Excuse me?!! Why do you ask?"
            liz 05 "Wait, what did you want to look at?"
            mc 08 "Nooo... nothing..."
            liz 02 "Ha ha! You little pervert..."
    show bg LizaKitchen A01B
    mc 10 "So where's my breakfast?"
    liz 01 "There's nothing here for you, [lizN.MClabel]!"
    mc 08 "What??"
    mc 11 "But we made a deal!"
    liz 03 "I'm sorry, it's all for me because you don't deserve it!"
    mc 01 "Okay, {p}All right, {p}I'm not hungry anyway!"
    mc 01 "{i}I hate her!"
    show bg Bobby A02
    mc 02 "{i}Guess I'll have to make do with a coffee."
    show bg LizaKitchen A02
    mc 02 "Hey, could you give me a cup of coffee?"
    mc 00 "They are in that drawer"
    liz 08 "They are in the bottom drawer."
    show bg LizaKitchen A03
    mc 08 "{i}Wow, what a cute little ass!"
    if (bl_values["incs"]):
        mc 03 "{i}Hmm... maybe I shouldn't stare at it like that."
    else:
        mc 03 "{i}Hmm...maybe I shouldn't stare at my [lizR.NPClabel] like that."
    show bg LizaKitchen A04A
    mc 03 "{i}Damn! [liz] how can she be so sour, but so hot..."
    show bg LizaKitchen A04B
    liz 08 "Catch!"
    mc 00 "Thanks!"
    show bg Bobby A02
    window hide
    pause
    jump liza_kitchen1end
label liza_kitchen1Error:
    jump liza_kitchen1end
label liza_kitchen1end:
    jump after_wait
