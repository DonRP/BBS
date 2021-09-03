label lucy_livingroom1:
    show bg LucyLivingroom A01A
    mc 00 "Ehilà"
    window hide
    pause
    mc 02 "Hi [lcy]..." 
    lcy 02 "Ehi..." 
    mc 00 "What are you doing?" 
    show bg LucyLivingroom A02
    lcy 02 "What does it look like I'm doing?" 
    show bg LucyLivingroom A01B
    mc 10 "Need help?" 
    show bg LucyLivingroom A03
    lcy 06 "From you... No, thanks! I don't need your help." 
    show bg LucyLivingroom A01C
    mc 03 "{i}Mmm... Look at that little foot!" 
    mc 03 "{i}She's so hot!"
    show bg LucyLivingroom A05
    mc 06 "Mhhh..."
    menu:
        mc "What should I tell [lcy] about her nails:"
        "They are coming bad":
            show bg LucyLivingroom A04B
            mc 04 "Why transparent, so bad looking!"
            lcy 06 "I know, right?"
        "They are coming along well":
            mc 00 "It's coming along nicely!"
            show bg LucyLivingroom A04B
            lcy 06 "It doesn't!" 
    lcy 02 "I hate clear nail polish!" 
    show bg LucyLivingroom A04A
    lcy 05 "Actually... you could help me."
    lcy 05 "[liz] has great nail polish that I could use, but she'll never lend it to me!" 
    lcy 07 "It would be great if you could... Steal it from her?" 
    show bg LucyLivingroom A04B
    mc 08 "What? You're crazy!" 
    mc 08 "She'll kill me if she finds out!" 
    show bg LucyLivingroom A04A
    lcy 07 "Come on... you're my little [lcyR.MClabel]!!!! Be nice, do it for me." 
    mc 06 "{i}When she stretches her boobs like that... I would literally do anything to my [lcyR.NPClabel]"
    mc 05 "Okay, but you owe me!" 
    lcy 03 "Great, it's the pink one."
    $ sp_routine["lucy_livingroom1"] = Commitment(chs={"lucy" : TalkObject(bg_before_after="bg LucyLivingroom A06", label_talk="lucy_livingroom1B")}, tm_start=0, tm_stop=24, id_location="house", id_room="livingroom")
    $ sp_routine["liza_lizaroom1"] = Commitment(chs={"liza" : TalkObject()}, tm_start=0, tm_stop=24, id_location="house", id_room="liza_room", label_event="liza_lizaroom1")
    $ nail_polish = False
    jump after_wait
label lucy_livingroom1B:
    show bg LucyLivingroom A06
    lcy 01 "So?!" 
    menu:
        lcy "Were you able to get the nail polish?"
        "Indeed!" if (nail_polish): 
            pass
        "Not yet!": 
            lcy 06 "Come on!!! I'm waiting for you!" 
            jump after_wait
    show bg LucyLivingroom A07    
    menu: 
        lcy "Really?! Let me see!"
        "Look and admire":
            lcy 03 "No way!"
            show bg LucyLivingroom A07A
            lcy 05 "It's great!" 
            lcy 01 "Who would have thought you had skills!" 
        "Not yet":
            lcy 06 "Let's go!!!" 
            lcy 06 "Give it to me!" 
    show bg LucyLivingroom A07A
    $ fable_minigame_score = 0
    mc 06 "{i}Hmm... Think [mc]..."
    menu:
        mc "{i}You owe me a favor:"
        "Not so fast!":
            show bg LucyLivingroom A08
            mc 10 "Actually.... I was thinking you should let me apply this on you!" 
            lcy 07 "What??" 
            lcy 06 "Stop messing around, [mc]!" 
            lcy 02 "Come on, I'm in a hurry!" 
            mc 00 "I'm serious, let me try!" 
            mc 04 "Or return it to [liz]..." 
            lcy 06 "You know what...it's fine!" 
            lcy 01 "You deserve it!" 
            lcy 07 "But you better apply it perfectly or you are doomed!"
            mc 08 "{i}Oh my gosh!!! I can't believe I'm actually going to touch her feet!" 
            mc 03 "{i}This is great!"
    $ fable_minigame_goal = 3
    show bg LucyLivingroom A08
    call start_fable_2_minigame
    mc 06 "{i}She didn't notice...I can go on!"
    menu: 
        "Try to get closer":
            pass
    show bg LucyLivingroom A08 2
    $ fable_minigame_score = 2
    $ fable_minigame_goal = 5
    call start_fable_2_minigame
    show bg LucyLivingroom A11
    window hide
    pause
    mc 03 "{i}Oh my god!!! I can feel my [lcyR.NPClabel]'s foot on my cock!" 
    $ fable_minigame_score = 0
    $ fable_minigame_goal = 7
    call start_fable_2_minigame
    show bg LucyLivingroom A12
    window hide
    pause
    mc 10 "What's going on? [lcy]?!"
    lcy 06 "Easy [lcyN.MClabel] don't push!" 
    lcy 02 "That's enough for you!"
    show bg LucyLivingroom A13A
    lcy 00 "Ehi! Where did you learn to do these things?" 
    lcy 05 "You came out great here! But all in all..."
    lcy 05 "Well"
    show bg LucyLivingroom A13B
    lcy 07 "Good job boy" 
    lcy 05 "Now go play somewhere else!"
    $ closed_rooms["livingroom"] = sp_routine["lucy_livingroom1"]
    $ del sp_routine["lucy_livingroom1"]
    $ del nail_polish
    $ del closed_rooms["liza_room"]
    show bg LucyLivingroom A01A
    with fade
    $ tm.new_hour(2)
    $ sp_actions["lizasmartphone"] = Action(name = _("Liza smartphone"), icon = "/location/lizaroom-smartphone.webp", icon_selected = "/location/lizaroom-smartphone a.webp", label = "liza_lizasmartphone0", sp_room='liza_room',
            is_in_room = True, xpos = 922, ypos = 563)
    jump after_wait
