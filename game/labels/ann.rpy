label intro_dream:
    window hide
    pause
    show bg AnnaDream A01
    with fade
    window hide
    mc 03 "Wow!!"
    pause
    mc 00 "Mmmm! Is fantastic!"
    window hide
    pause
    show bg AnnaDream A02A animated
    window hide
    pause
    mc 08 "WTF!"
    if (bl_values["incs"]):
        mc 08 "[annR.NPClabel]?!"
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
    mc 08 "{i}Oh God!!! It couldn't have been just a dream. "
    show bg Bobby A00
    with fade
    mc 07 "{i}What has gotten into me?! This is so wrong!"
    mc 07 "{i}Mhh... Better to hide the flag raising before..."
    show bg AnnaMCRoom A01B
    "(KNOCK KNOCK)"
    mc 08 "{i}Shit!"
    show bg AnnaMCRoom A01C
    window hide
    pause
    show bg AnnaMCRoom A01A
    return
