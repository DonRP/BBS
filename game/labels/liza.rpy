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
        mc 03 "{i}Hmm...maybe I shouldn't stare at my [lizR.NPClabel] like that."
    else:
        mc 03 "{i}Hmm... maybe I shouldn't stare at it like that."
    show bg LizaKitchen A04A
    mc 03 "{i}Damn! [liz] how can she be so sour, but so hot..."
    show bg LizaKitchen A04B
    liz 08 "Catch!"
    mc 00 "Thanks!"
    show bg Bobby A02
    window hide
    pause
    scene black
    mc 02 "{i}My stomach is growling... What a fam!"
    show bg LizaKitchen A05
    with fade
    mc 07 "{i}It looks like your breakfast is so good!"
    mc 01 "{i}Hmm... I'll get my revenge somehow."
    mc 20 "So how's breakfast?"
    liz 01 "Mmmmmm"
    liz 00 "It's so good!"
    liz 01 "I am such a good cook!"
    liz 02 "Don't worry, you can eat some fruit from the table!"
    mc 06 "{i}I've got an idea! I could get revenge now..."
    show bg LizaKitchen A07
    mc 05 "Ha ha! You don't know what you're missing... [ann] did buy them on special delivery yesterday."
    mc 05 "I have never had such good fruit, too bad they are all for me."
    menu:
        mc "Just because you're my [lizR.NPClabel], I could give you one:"
        "Ananas":
            show item LizaKitchen B ananas
            jump liza_kitchen1Error
        "Banana":
            show item LizaKitchen B banana
            pass
        "Kiwi":
            show item LizaKitchen B kiwi
            jump liza_kitchen1Error
    liz 04 "Did you say in special consegana!?"
    mc 00 "Yes! you know, only Anna knows where to buy good fresh fruit, at a good price."
    liz 04 "Hmm... Okay! They say bananas are good for fitness."
    hide item
    show bg LizaKitchen A08A
    mc 04 "Here, try one! It's so sweet."
    liz 03 "Haha, you tried!"
    mc 10 "Go ahead! Try it for yourself."
    mc 00 "You can take a little bite!"
    liz 08 "Ha ha ha really?! Get lost!"
    mc 11 "I'm not going anywhere until you try it!"
    liz 08 "Okay, but then leave me alone, you pervert!"
    show bg LizaKitchen A08B
    window hide
    pause
    show bg LizaKitchen A08C
    window hide
    pause
    show bg LizaKitchen A08D
    liz 06 "Mmmmmmmm"
    window hide
    pause
    show bg LizaKitchen A08E
    window hide
    pause
    show bg LizaKitchen A08F
    liz 06 "(Cough...)"
    window hide
    pause
    show bg LizaKitchen A08G
    window hide
    pause
    $ stats["liz"].change("anger", 1)
    liz 05 "You are dead!!!"
    show bg LizaKitchen A09
    mc 12 "Ow! Ow! You're hurting me!"
    window hide
    pause
    show bg Bobby A01
    mc 07 "{i}Ow! What a pain! But it was worth it!"
    mc 05 "{i}It was crazy!"
    mc 04 "{i}My sweet revenge!"
    show bg Bobby A03
    mc 05 "{i}I definitely should have pushed it deeper down her throat!"
    mc 07 "{i}...."
    mc 07 "{i}Damn!!!"
    mc 07 "{i}What's wrong with me ... she is my [lizR.NPClabel]!!"
    mc 07 "{i}He will probably tell [ann]..."
    mc 07 "{i}Shit, I have to think of an excuse."
    jump liza_kitchen1end
label liza_kitchen1Error:
    liz 04 "Hmmm... also no... thanks!"
    liz 10 "Just give a little taste."
    liz 05 "NO! go away! before I call [ann]."
    hide item
    show bg Bobby A03
    mc 07 "Damn!!!"
    mc 07 "I failed! I must think of another revenge."
    jump liza_kitchen1end
label liza_kitchen1end:
    "(A few hours later)"
    $ del sp_routine["liza_kitchen1B"]
    $ cur_room = rooms[0]
    $ tm.new_hour(5)
    $ del smartphone_liza
    $ sp_routine["lucy_livingroom1"] = Commitment(chs={"lucy" : TalkObject()}, tm_start=0, tm_stop=24, id_location="house", id_room="livingroom", label_event="lucy_livingroom1")
    jump after_wait

label liza_lizaroom1:
    jump after_wait
