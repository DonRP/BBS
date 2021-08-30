label intro_dream:
    window hide
    pause
    show bg AnnaDream A01
    with fade
    window hide
    mc "Wow!!"
    pause
    mc "Mmmm! Is fantastic!"
    window hide
    pause
    show bg AnnaDream A02A animated
    window hide
    pause
    mc "WTF!"
    if (bl_values["incs"]):
        "[annR.NPClabel]?!"
    else:
        "Mrs. [ann]?!"
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
