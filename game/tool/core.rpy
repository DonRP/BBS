label after_load:
    $ updateTimeHandler()
    $ clearExpiredSPActions()
    $ clearExpiredSPRoutine()
    $ updateBL()

    #BBS
    if not ("mc" in stats):
        $ stats["mc"] = Statistics(gender = "M", virgin = True)
    if not ("ann" in stats):
        $ stats["ann"] = Statistics(gender = "F", virgin = False)
    if not ("liz" in stats):
        $ stats["liz"] = Statistics(gender = "F", virgin = True)
    if not ("lucy" in stats):
        $ stats["lucy"] = Statistics(gender = "F", virgin = True)
    if not ("jnn" in stats):
        $ stats["jnn"] = Statistics(gender = "F", virgin = True)
    return
