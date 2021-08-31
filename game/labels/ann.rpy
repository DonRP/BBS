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
    return
