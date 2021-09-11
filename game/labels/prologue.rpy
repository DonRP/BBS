image prologue A01 animated:
    "/Prologue/A01A.webp"
    pause 3
    "/Prologue/A01B.webp" with dissolve
    pause 3
    "/Prologue/A01A.webp" with dissolve
    pause 3
    "/Prologue/A01B.webp" with dissolve
    pause 3
    "/Prologue/A01A.webp" with dissolve
    pause 3
    "/Prologue/A01B.webp" with dissolve
    pause 3
    "/Prologue/A02A.webp"
    pause 3
    "/Prologue/A02B.webp" with dissolve
    pause 3
    "/Prologue/A02A.webp" with dissolve
    pause 3
    "/Prologue/A02B.webp" with dissolve
    pause 3
    repeat

image prologue A03 = "/Prologue/A03.webp"
image prologue B00A = "/Prologue/B00A.webp"
image prologue B00B = "/Prologue/B00B.webp"
image prologue B01 = "/Prologue/B01.webp"
image prologue B02 = "/Prologue/B02.webp"
image prologue B03A = "/Prologue/B03A.webp"
image prologue B03B = "/Prologue/B03B.webp"
image prologue B04 = "/Prologue/B04.webp"
image prologue B04 blur = im.Blur("/Prologue/B04.webp", 7)
image prologue B05 = "/Prologue/B05.webp"
image prologue B06 = "/Prologue/B06.webp"
image prologue B07 = "/Prologue/B07.webp"

label intro:
    show prologue A01 animated
    with fade
    window hide
    pause
    show text _("Special thanks") at center_delay(t = 0.01, y=0.4)
    with dissolve
    window hide
    pause
    show text _("3D Modeling\nBigIrishLug\nkrekerman003\nschlebbsaga\n\nVarious support\nbxIvan\nMegaplayboy10k\nSummmerP") at center_delay(t = 0.01)
    with dissolve
    window hide
    pause
    hide text
    window hide
    pause
    "Newbie" "Did you try that new Italian restaurant... what was it called?! Oh right! Da Luigi."
    "Policewoman" "No!"
    "Newbie" "Me neither, but I've heard good things about it. We could..."
    "Policewoman" "I don't think so!"
    "Newbie" "Um... I wasn't coming on to you, just wanted to know a bit more about you."
    "Policewoman" "Rookie, as I've already explained... I'm here so you don't do anything stupid and two, cause the Captain says I can't work alone... which is just bullshit!"
    "Policewoman" "With that said, I'm not here to make friends, we're partners. Understood?"
    "Newbie" "Yes, Ma'am!"
    window hide
    pause
    "Policewoman" "Okay, we're here."
    window hide
    pause
    "Policewoman" "Newbie, make sure the perp comfortable with the handcuffs."
    "Newbie" "You heard her! Today is your big day..."
    show prologue A03
    with fade
    window hide
    pause
    show prologue B00A
    with fade
    window hide
    pause
    "Cop" "Smile pretty..."
    "Cop" "Okay, now let's see who we have here today:"
    "Cop" "Name:"
    $ mcI.changeName()
    show prologue B00B
    "Cop" "Surname:"
    $ mcI.changeSurname()
    "Cop" "Age: 24 years old."
    "Cop" "Good! Now straight to the interrogation room, officers Murtaugh and Riggs want to have a quick chat with you."
    show prologue B01 at center_delay(0.1)
    with fade
    "Riggs" "Here he is! Our suspect... How about that... He doesn't look like a criminal."
    "Murtaugh" "The real question is whether he is more of a petty thief or a hardened killer."
    "Murtaugh" "Oh my apologies, where are my manners? We are Murtaugh and Riggs, and you are... [mc]! AKA are the bad guy!"
    show prologue B02
    with fade
    show prologue B05
    with fade
    show prologue B03A
    with fade
    "Riggs" "YOU THINK THIS IS A GAME!!! DO YOU WANT TO END UP LIKE YOUR FATHER???"
    "Murtaugh" "Easy... Easy Riggs. We know he's innocent. But to let him go, we need to know who his partner is."
    show prologue B05
    with fade
    show prologue B03B
    with fade
    show prologue B04
    with fade
    "Murtaugh" "Let's take a closer look at your file... After the age of 20 in and out of halfway houses..."
    show icon ann at center_delay(0.1)
    if renpy.variant("pc"):
        show prologue B04 blur with dissolve
    "Riggs" "Whereas, she..."
    $ annI.changeName()
    "Riggs" "Your..."
    $ annR.changeNPClabel()
    "Riggs" "Was desperate to help. But you didn't care. Right?"
    "Murtaugh" "Let's rewind..."
    if (annR.NPClabel.lower() == __("mom") or annR.NPClabel.lower() == __("mother")):
        $ bl_values["incs"] = True
        $ annR.MClabel = __("step son")
        $ annR.NPClabel = __("step mom")
        $ lizforann.MClabel = annR.MClabel
        $ lizforann.NPClabel = annR.NPClabel
        $ lizR.MClabel = __("brother")
        $ lizR.NPClabel = __("sister")
        $ lcyR.MClabel = __("step brother")
        $ lcyR.NPClabel = __("step sister")
        $ jnnR.MClabel = lcyR.MClabel
        $ jnnR.NPClabel = lcyR.NPClabel
        show icon liza at center_delay(0.1)
        "Murtaugh" "Anna, after your step-mother died, decided to bring you and your [lizR.NPClabel] into her home..."
        $ lizI.changeName()
        "Murtaugh" "From the man who was kind enough to impregnated her when she was only 18 and then left her with nothing."
        show icon lucy at center_delay(0.1)
        "Murtaugh" "Not caring about her..."
        $ lcyI.changeName()
        show icon jenny at center_delay(0.1)
        "Murtaugh" "After that she tried to rebuild her life by having another child with a better man...."
        $ jnnI.changeName()
    else:
        $ bl_values["incs"] = False
        $ annR.MClabel = __("landlord")
        $ annR.NPClabel = __("leaseholder")
        $ lizforann.MClabel = annR.MClabel
        $ lizforann.NPClabel = annR.NPClabel
        $ lizR.MClabel = __("housemate")
        $ lizR.NPClabel = __("housemate")
        $ lcyR.MClabel = lizR.MClabel
        $ lcyR.NPClabel = lizR.NPClabel
        $ jnnR.MClabel = lcyR.MClabel
        $ jnnR.NPClabel = lcyR.NPClabel
        "Murtaugh" "[ann], after your step-mother died, she decided to bring you into her home..."
        "Murtaugh" "Although you are the son of her ex-boyfriend."
        show icon lucy at center_delay(0.1)
        "Murtaugh" "Treating you like a son, letting you sleep under the same roof as her daughters..."
        $ lcyI.changeName()
        show icon jenny at center_delay(0.1)
        "Murtaugh" "And..."
        $ jnnI.changeName()
        show icon liza at center_delay(0.1)
        "Murtaugh" "and the other..."
        $ lizI.changeName()
    show prologue B04 with dissolve
    hide icon
    show prologue B05
    with fade
    show prologue B01
    with fade
    show prologue B03B
    with fade
    show prologue B06
    with fade
    "Riggs" "You don't talk much, huh?"
    "Riggs" "Well, we have enough to keep you in for a few nights. let's see if you change your mind!"
    show prologue B07
    with fade
    mc "What happened to me... I was such a happy child... I really thought I was leaving all that pain behind."
    mc "At first, at [ann]'s house, it seemed to go well. I was really hoping everything would work out."
    mc "But then, at the end of summer a few years ago... (scoffing) when Nokia was still a good smartphone."
    mc "It all started unravelling after that dream...."
    hide prologue
    return
