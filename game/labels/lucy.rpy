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
    mc 06 "{i}When she stretches her boobs like that... I would literally do anything to my [lcyR.MClabel]"
    mc 05 "Okay, but you owe me!" 
    lcy 03 "Great, it's the pink one." 
    $ sp_routine["liza_kitchen1B"] = Commitment(chs={"lucy" : TalkObject(bg_before_after="bg LucyLivingroom A06", label_talk="lucy_livingroom1B")}, tm_start=0, tm_stop=24, id_location="house", id_room="livingroom")
    $ sp_routine["lucy_livingroom1"] = Commitment(chs={"liza" : TalkObject()}, tm_start=0, tm_stop=24, id_location="house", id_room="liza_room", label_event="liza_lizaroom1")
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
    jump after_wait
