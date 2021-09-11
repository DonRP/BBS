## Actions they do are meant to pass time

label wait_onehour:
    $ wait_hour = 1
    jump wait

label nap:
    call check_block_spendtime

    menu:
        "Nap for 3 hours..":
            $ wait_hour = 3
            jump wait
        "Sleep":
            jump sleep
        "Return":
            pass
    call screen room_navigation

label sleep:
    call check_block_spendtime

    menu:
        "What time do you want to set the alarm?"
        "[tm.hour_new_day]:00":
            call new_day
            call check_event
        "7:00":
            call new_day
            call check_event
            $ tm.new_hour(7-tm.hour_new_day)
        "9:00":
            call new_day
            call check_event
            $ tm.new_hour(9-tm.hour_new_day)
        "Return":
            pass
    jump after_wait

## Error and warming Label

label error_label:
    "ERROR"
    return

label development:
    "In development"
    call screen room_navigation

## BBS
# Laptop
label laptop:
    call coming_soon
    jump after_wait

label laptop_liza:
    call coming_soon
    jump after_wait

label go_kitchen:
    $ prev_room = cur_room
    $ cur_room = rooms[3] # kitchen
    $ sp_bg_change_room = getBgRoomRoutine(cur_routines_location, cur_room.id)
    jump change_room

label carpet:
    menu:
        "Tutorial":
            "You want to become a ninja?! then what are you waiting for!"
            "Start the game to level up the stealth."
            "The game is very simple: you have to click or press space when the ball is in the middle of the bar."
            "And with each round you will increase your stealth by 1."
            jump after_wait
        "Start training":
            $ fable_minigame_goal = 15
            call start_fable_2_minigame
            $ stats["mc"].change("stealth", 1)
            $ notifyEx(msg=__("{color=#00ff00}{b}+{/b} Stealth"))
            jump after_wait
        "Back":
            jump after_wait
