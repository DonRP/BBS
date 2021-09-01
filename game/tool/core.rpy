label after_load:
    $ updateTimeHandler()
    $ clearExpiredSPActions()
    $ clearExpiredSPRoutine()
    $ updateBL()

    #BBS
    if ("mc" in stats):
        $ stats["mc"] = Statistics(gender = "M", virgin = True)
    return
