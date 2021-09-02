label intro_dream:
    window hide
    pause
    show bg AnnaDream A01
    with fade
    window hide
    mc 03 "Wow!!"
    pause
    mc 00 "Mmmm! It's fantastic!"
    window hide
    pause
    show bg AnnaDream A02A animated
    window hide
    pause
    mc 08 "WTF!"
    if (bl_values["incs"]):
        mc 08 "[annR.NPClabel] Huh?!"
    else:
        mc 08 "Mrs. [ann]?!"
    window hide
    pause
    show bg AnnaDream A02B animated
    window hide
    pause
    show bg AnnaDream A02C
    window hide
    pause
    hide bg
    return

label start_scene:
    show black
    with fade
    mc 08 "{i}Oh God!!! Was it just a dream. "
    show bg Bobby A00
    with fade
    mc 07 "{i}What has gotten into me?! This is so wrong!"
    mc 07 "{i}Mhh... Better to hide this tent pole before..."
    show bg AnnaMCRoom A01B
    "(KNOCK KNOCK)"
    mc 08 "{i}Damn it!"
    show bg AnnaMCRoom A01C
    window hide
    pause
    show bg AnnaMCRoom A01A
    ann 00 "Good morning Bobby! Time to get up!"
    mc 12 "Yawn! Morning."
    ann 00 "I'm doing laundry, do you have anything to wash?"
    show bg AnnaMCRoom A02A
    mc 07 "Yawn! Sorry, I can't remember."
    ann 00 "Let's see, I had left... ah! there it is!"
    show bg AnnaMCRoom A02B
    window hide
    pause
    show bg AnnaMCRoom A02C
    menu:
        ann "What's the matter, honey? You're so quiet this morning."
        "About the dream":
            mc 00 "I'm fine, I just a weird dream."
            ann 00 "Tell me! What dream?"
            mc 08 "Ahahahah... emmm... it's a bit hard to explain."
        "I would like a hug":
            mc 10 "I really need a hug...."
            ann 00 "Ahah! {p}Don't be silly."
    window hide
    pause
    show bg AnnaMCRoom A03C
    window hide
    pause
    ann 00 "I'll wash this for you!"
    show bg AnnaMCRoom A03D
    window hide
    pause
    mc 10 "{i}Oh fuck, what nice curves..."
    mc 06 "{i}Think [mc]..."
    menu:
        mc "What I could do now:"
        "Play a trick on her":
            show bg AnnaMCRoom A03C
            window hide
            pause
            show bg AnnaMCRoom A03A
            if (bl_values["incs"]):
                mc 13 "[annR.NPClabel] Huh?!"
            else:
                mc 13 "Mrs. [ann]?!"
            show bg AnnaMCRoom A03B
            ann 02 "Ohh, you scared me!"
            mc 10 "Here. Let me help you with the basket."
            show bg AnnaMCRoom A04C
            $ stats["ann"].change("submission", 1)
            ann 04 "... It's okay baby, I can do it!"
            mc 03 "{i}Oh my gosh!!! it feels so good!"
        "Help her with the basket":
            show bg AnnaMCRoom A04A
            mc 00 "Hey [annR.NPClabel]! Let me help you with this."
            show bg AnnaMCRoom A04B
            ann 01 "Oh honey, you're so sweet."
            mc 08 "..."
            window hide
            pause
            show bg AnnaMCRoom A04C
            $ stats["ann"].change("favour", 1)
            ann 03 "It's okay, I can handle it."
    window hide
    pause
    show bg AnnaMCRoom A01D
    window hide
    pause
    show bg AnnaMCRoom A01B
    window hide
    pause
    return
