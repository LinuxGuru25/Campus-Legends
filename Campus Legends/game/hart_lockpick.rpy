# ============================================================
# CAMPUS LEGENDS - SKYRIM STYLE LOCKPICKING MINIGAME
#
#   label hart_lockpick
#
#   Controls
#     mouse / LEFT RIGHT .. set the pick angle
#     SPACE or LMB ........ hold to turn the lock
#     ESC ................. give up
#
#   Configure before jumping (all optional):
#     $ hart_lock_difficulty = "Adept"      # Novice..Master
#     $ hart_lock_pick_count = 3
#     $ hart_lock_title = "Professor Hart's Office"
# ============================================================

## ------------------------------------------------------------------ art

image hart_lp_glow   = "images/lockpick/glow.png"
image hart_lp_plate  = "images/lockpick/lock_plate.png"
image hart_lp_cyl    = "images/lockpick/lock_cylinder.png"
image hart_lp_pick   = "images/lockpick/pick.png"
image hart_lp_wrench = "images/lockpick/wrench.png"
image hart_lp_icon   = "images/lockpick/pick_icon.png"

## ------------------------------------------------------------- variables

default hart_lock_running = False
default hart_lock_result = None
default hart_lock_open = False

default hart_lock_title = "Professor Hart's Office"
default hart_lock_difficulty = "Adept"
default hart_lock_pick_count = 3

default hart_lock_pick = 0.0
default hart_lock_cyl = 0.0
default hart_lock_tension = False
default hart_lock_dir = 0
default hart_lock_sweet = 0.0
default hart_lock_tol = 17.0
default hart_lock_dur = 100.0
default hart_lock_dur_i = 100
default hart_lock_dur_color = "#c9a227"
default hart_lock_picks = 3
default hart_lock_tries = 0
default hart_lock_stall = False
default hart_lock_shake = 0.0
default hart_lock_flash = 0.0

default hart_lock_msg = ""
default hart_lock_msg_color = "#c8ccd6"
default hart_lock_title_u = ""
default hart_lock_diff_u = ""

default hart_lock_last_t = 0.0
default hart_lock_mouse = (0.0, 0.0)
default hart_lock_end_at = 0.0
default hart_lock_slip_at = 0.0
default hart_lock_cooldown = 0.0

## --------------------------------------------------------------- python

init python:

    import math
    import time

    # Centre of the lock and the angle at which the cylinder opens.
    HART_LOCK_CX = 960.0
    HART_LOCK_CY = 505.0
    HART_LOCK_OPEN_ANGLE = 170.0

    # Half width, in degrees, of the hidden sweet spot.
    HART_LOCK_DIFFS = {
        "Novice": 34.0,
        "Apprentice": 25.0,
        "Adept": 17.0,
        "Expert": 12.0,
        "Master": 8.0,
    }

    HART_LOCK_HINT_START = "Set the pick, then hold {b}SPACE{/b} (or the left mouse button) to turn the lock."
    HART_LOCK_HINT_IDLE = "Feel for where the cylinder gives, then ease off and move the pick."

    def hart_lock_sfx(name):
        renpy.sound.play("audio/lockpick/" + name)

    def hart_angdiff(a, b):
        """Smallest distance between two angles, in degrees."""
        d = (a - b) % 360.0
        if d > 180.0:
            d -= 360.0
        return abs(d)

    def hart_lock_begin():
        global hart_lock_running, hart_lock_result, hart_lock_open
        global hart_lock_pick, hart_lock_cyl, hart_lock_tension, hart_lock_dir
        global hart_lock_sweet, hart_lock_tol, hart_lock_dur, hart_lock_dur_i
        global hart_lock_dur_color, hart_lock_picks, hart_lock_tries
        global hart_lock_stall, hart_lock_shake, hart_lock_flash
        global hart_lock_msg, hart_lock_msg_color, hart_lock_title_u
        global hart_lock_diff_u, hart_lock_last_t, hart_lock_mouse
        global hart_lock_end_at, hart_lock_slip_at, hart_lock_cooldown

        hart_lock_tol = HART_LOCK_DIFFS.get(hart_lock_difficulty, HART_LOCK_DIFFS["Adept"])

        hart_lock_sweet = renpy.random.uniform(0.0, 360.0)
        hart_lock_pick = 0.0
        hart_lock_cyl = 0.0
        hart_lock_tension = False
        hart_lock_dir = 0

        hart_lock_dur = 100.0
        hart_lock_dur_i = 100
        hart_lock_dur_color = "#c9a227"
        hart_lock_picks = max(1, int(hart_lock_pick_count))
        hart_lock_tries = 0

        hart_lock_stall = False
        hart_lock_shake = 0.0
        hart_lock_flash = 0.0

        hart_lock_result = None
        hart_lock_running = True
        hart_lock_open = False

        hart_lock_msg = HART_LOCK_HINT_START
        hart_lock_msg_color = "#c8ccd6"
        hart_lock_title_u = hart_lock_title.upper()
        hart_lock_diff_u = hart_lock_difficulty.upper()

        now = time.monotonic()
        hart_lock_last_t = now
        hart_lock_end_at = now + 3600.0
        hart_lock_slip_at = now - 10.0
        hart_lock_cooldown = 0.0
        hart_lock_mouse = renpy.get_mouse_pos()

    def hart_lock_set_dir(direction):
        global hart_lock_dir
        if hart_lock_result is None:
            hart_lock_dir = direction

    def hart_lock_release_dir(direction):
        global hart_lock_dir
        if hart_lock_dir == direction:
            hart_lock_dir = 0

    def hart_lock_set_tension(on):
        global hart_lock_tension, hart_lock_tries
        if hart_lock_result is not None or not hart_lock_running:
            return
        if on:
            if not hart_lock_tension:
                hart_lock_tries += 1
                if time.monotonic() >= hart_lock_cooldown:
                    hart_lock_sfx("lp_creak.wav")
            hart_lock_tension = True
        else:
            hart_lock_tension = False

    def hart_lock_abort(result="giveup"):
        global hart_lock_result, hart_lock_end_at, hart_lock_msg
        global hart_lock_msg_color, hart_lock_tension, hart_lock_cyl, hart_lock_stall
        if hart_lock_result is not None:
            return
        hart_lock_result = result
        hart_lock_tension = False
        hart_lock_stall = False
        hart_lock_shake = 0.0
        hart_lock_cyl = 0.0
        hart_lock_msg = "I ease the pick out and step back."
        hart_lock_msg_color = "#9aa0ac"
        hart_lock_end_at = time.monotonic() + 0.3

    def hart_lock_break(now):
        global hart_lock_picks, hart_lock_dur, hart_lock_dur_i, hart_lock_dur_color
        global hart_lock_cyl, hart_lock_result, hart_lock_msg, hart_lock_msg_color
        global hart_lock_end_at, hart_lock_cooldown, hart_lock_tension, hart_lock_stall
        global hart_lock_shake

        hart_lock_picks -= 1
        hart_lock_cyl = 0.0
        hart_lock_tension = False
        hart_lock_stall = False
        hart_lock_shake = 0.0
        hart_lock_cooldown = now + 0.75
        hart_lock_sfx("lp_break.wav")

        if hart_lock_picks <= 0:
            hart_lock_dur = 0.0
            hart_lock_dur_i = 0
            hart_lock_result = "fail"
            hart_lock_msg = "The last pick snaps clean off."
            hart_lock_msg_color = "#e06a5a"
            hart_lock_end_at = now + 1.7
        else:
            hart_lock_dur = 100.0
            hart_lock_dur_i = 100
            hart_lock_dur_color = "#c9a227"
            hart_lock_msg = "Snap! The pick breaks - [hart_lock_picks] left."
            hart_lock_msg_color = "#e06a5a"

    def hart_lock_tick():
        global hart_lock_running, hart_lock_result, hart_lock_open, hart_lock_pick
        global hart_lock_cyl, hart_lock_tension, hart_lock_stall, hart_lock_shake
        global hart_lock_dur, hart_lock_dur_i, hart_lock_dur_color, hart_lock_msg
        global hart_lock_msg_color, hart_lock_last_t, hart_lock_mouse, hart_lock_end_at
        global hart_lock_slip_at, hart_lock_flash

        now = time.monotonic()
        dt = now - hart_lock_last_t
        hart_lock_last_t = now
        if dt < 0.0 or dt > 0.10:
            dt = 0.0

        # Ending animation: hold the final frame, then let the label continue.
        if hart_lock_result is not None:
            if hart_lock_flash > 0.0:
                hart_lock_flash = max(0.0, hart_lock_flash - 3.0 * dt)
            if now >= hart_lock_end_at:
                hart_lock_running = False
            return

        # ---------------------------------------------------------- pick
        mx, my = renpy.get_mouse_pos()

        if hart_lock_dir:
            hart_lock_pick = (hart_lock_pick + hart_lock_dir * 175.0 * dt) % 360.0
            hart_lock_mouse = (mx, my)
        else:
            lastx, lasty = hart_lock_mouse
            moved = (mx - lastx) ** 2 + (my - lasty) ** 2 > 6.0
            hart_lock_mouse = (mx, my)

            vx = mx - HART_LOCK_CX
            my_ = my - HART_LOCK_CY
            radius = math.hypot(vx, my_)
            if moved and 80.0 < radius < 440.0:
                hart_lock_pick = math.degrees(math.atan2(vx, -my_)) % 360.0

        # ------------------------------------------------------- tension
        applying = hart_lock_tension and now >= hart_lock_cooldown

        if applying:
            err = hart_angdiff(hart_lock_pick, hart_lock_sweet)

            if err <= hart_lock_tol:
                limit = HART_LOCK_OPEN_ANGLE
            else:
                limit = HART_LOCK_OPEN_ANGLE * (1.0 - (err - hart_lock_tol) / (180.0 - hart_lock_tol))
                if limit < 0.0:
                    limit = 0.0

            if hart_lock_cyl >= HART_LOCK_OPEN_ANGLE - 0.01:
                # ------------------------------------------------ opened
                hart_lock_result = "open"
                hart_lock_open = True
                hart_lock_cyl = HART_LOCK_OPEN_ANGLE
                hart_lock_tension = False
                hart_lock_stall = False
                hart_lock_shake = 0.0
                hart_lock_flash = 1.0
                hart_lock_msg = "The lock clicks open."
                hart_lock_msg_color = "#f0c96a"
                hart_lock_end_at = now + 1.3
                hart_lock_sfx("lp_open.wav")
                return

            if hart_lock_cyl >= limit - 0.05:
                # ------------------------------------------ jammed: damage
                hart_lock_stall = True
                hart_lock_shake = 2.4 * math.sin(now * 54.0)

                rate = 30.0 * (0.26 + 0.74 * min(1.0, err / 180.0))
                hart_lock_dur -= rate * dt

                if hart_lock_dur <= 0.0:
                    hart_lock_break(now)
                    return

                if hart_lock_cyl > 55.0:
                    hart_lock_msg = "It's turning... barely. Hold it and nudge the pick."
                    hart_lock_msg_color = "#f0c96a"
                else:
                    hart_lock_msg = "It's jammed - ease off and shift the pick."
                    hart_lock_msg_color = "#e06a5a"

                if now - hart_lock_slip_at > 0.45:
                    hart_lock_slip_at = now
                    hart_lock_sfx("lp_slip.wav")
            else:
                # ------------------------------------------- cylinder moving
                hart_lock_stall = False
                hart_lock_shake = 0.0
                hart_lock_msg = "It's turning..."
                hart_lock_msg_color = "#f0c96a"
        else:
            hart_lock_cyl = max(0.0, hart_lock_cyl - 460.0 * dt)
            hart_lock_stall = False
            hart_lock_shake = 0.0

            if now >= hart_lock_cooldown:
                if hart_lock_tries:
                    hart_lock_msg = HART_LOCK_HINT_IDLE
                else:
                    hart_lock_msg = HART_LOCK_HINT_START
                hart_lock_msg_color = "#c8ccd6"

        # ---------------------------------------------------- durability
        left = max(0.0, hart_lock_dur)
        hart_lock_dur_i = int(left + 0.5)
        if left > 60.0:
            hart_lock_dur_color = "#c9a227"
        elif left > 30.0:
            hart_lock_dur_color = "#e08c2a"
        else:
            hart_lock_dur_color = "#c0392b"

        if hart_lock_flash > 0.0:
            hart_lock_flash = max(0.0, hart_lock_flash - 3.0 * dt)


## ------------------------------------------------------------- transforms

transform hart_place(cx, cy):
    xpos cx
    ypos cy
    xanchor 0.5
    yanchor 0.5

transform hart_spin(angle, cx, cy):
    xpos cx
    ypos cy
    xanchor 0.5
    yanchor 0.5
    rotate angle

## ---------------------------------------------------------------- screen

screen hart_lockpick_ui():
    modal True
    zorder 2000

    # ----------------------------------------------------------- input
    key "anyrepeat_K_LEFT" action Function(hart_lock_set_dir, -1)
    key "keyup_K_LEFT" action Function(hart_lock_release_dir, -1)
    key "anyrepeat_K_RIGHT" action Function(hart_lock_set_dir, 1)
    key "keyup_K_RIGHT" action Function(hart_lock_release_dir, 1)

    key "anyrepeat_K_SPACE" action Function(hart_lock_set_tension, True)
    key "keyup_K_SPACE" action Function(hart_lock_set_tension, False)
    key "mousedown_1" action Function(hart_lock_set_tension, True)
    key "mouseup_1" action Function(hart_lock_set_tension, False)

    key "game_menu" action Function(hart_lock_abort, "giveup")
    key ">" action NullAction()
    key "shift_K_PERIOD" action NullAction()

    # -------------------------------------------------------- backdrop
    add Solid("#05060a") xysize (1920, 1080)

    add "hart_lp_glow" at hart_place(HART_LOCK_CX, HART_LOCK_CY) alpha 0.85
    add "hart_lp_plate" at hart_place(HART_LOCK_CX, HART_LOCK_CY)
    add "hart_lp_cyl" at hart_spin(hart_lock_cyl, HART_LOCK_CX, HART_LOCK_CY)
    add "hart_lp_wrench" at hart_spin(hart_lock_cyl, HART_LOCK_CX, HART_LOCK_CY)
    add "hart_lp_pick" at hart_spin(hart_lock_pick + hart_lock_shake, HART_LOCK_CX, HART_LOCK_CY)

    if hart_lock_flash > 0.0:
        add Solid("#ffe6b0") xysize (1920, 1080) alpha (hart_lock_flash * 0.20)

    # ----------------------------------------------------------- title
    text hart_lock_title_u:
        xalign 0.5
        ypos 26
        font "static/Montserrat-Medium.ttf"
        size 20
        color "#727887"
        outlines [(1, "#000000cc", 0, 0)]

    text hart_lock_diff_u + " LOCK":
        xalign 0.5
        ypos 54
        font "PirataOne-Regular.ttf"
        size 46
        color "#e8c56a"
        outlines [(3, "#000000aa", 0, 0)]

    # --------------------------------------------------------- status
    text hart_lock_msg:
        xalign 0.5
        ypos 900
        font "static/Montserrat-SemiBold.ttf"
        size 30
        color hart_lock_msg_color
        outlines [(2, "#000000", 0, 0)]

    # --------------------------------------------------- picks remaining
    text "PICKS":
        xpos 140
        ypos 956
        font "static/Montserrat-Medium.ttf"
        size 18
        color "#727887"
        outlines [(1, "#000000cc", 0, 0)]

    hbox:
        xpos 140
        ypos 984
        spacing 14
        for i in range(hart_lock_picks):
            add "hart_lp_icon"

    # ------------------------------------------------------- integrity
    text "PICK INTEGRITY":
        xpos 760
        ypos 956
        font "static/Montserrat-Medium.ttf"
        size 18
        color "#727887"
        outlines [(1, "#000000cc", 0, 0)]

    add Solid("#241a1a") xysize (300, 12) xpos 760 ypos 992
    add Solid(hart_lock_dur_color) xysize (max(0, int(300 * hart_lock_dur / 100.0)), 12) xpos 760 ypos 992

    text "[hart_lock_dur_i]%":
        xpos 1074
        ypos 984
        font "static/Montserrat-SemiBold.ttf"
        size 18
        color hart_lock_dur_color
        outlines [(1, "#000000cc", 0, 0)]

    # -------------------------------------------------------- controls
    text "SET PICK  ·  mouse  /  LEFT RIGHT":
        xpos 1780
        xanchor 1.0
        ypos 956
        font "static/Montserrat-Medium.ttf"
        size 20
        color "#8a90a0"
        outlines [(1, "#000000cc", 0, 0)]

    text "TURN LOCK  ·  hold SPACE or LEFT MOUSE BUTTON":
        xpos 1780
        xanchor 1.0
        ypos 986
        font "static/Montserrat-Medium.ttf"
        size 20
        color "#8a90a0"
        outlines [(1, "#000000cc", 0, 0)]

    text "GIVE UP  ·  ESC":
        xpos 1780
        xanchor 1.0
        ypos 1016
        font "static/Montserrat-Medium.ttf"
        size 20
        color "#5f6472"
        outlines [(1, "#000000cc", 0, 0)]

## ---------------------------------------------------------------- label

label hart_lockpick:

    "I crouch in front of the lock and slide my pick into place."

    "I need to find the angle where the lock gives."

    $ hart_lock_begin()

    show screen hart_lockpick_ui

    while hart_lock_running:
        $ hart_lock_tick()
        $ renpy.config.skipping = None
        $ renpy.pause(0.03, modal=False)

    hide screen hart_lockpick_ui

    if hart_lock_result == "open":
        "The cylinder rolls past the shear line with a quiet click."
        "The office door eases open."
    elif hart_lock_result == "fail":
        "The pick gives with a snap. I hear footsteps somewhere down the hall."
    else:
        "I ease the pick out before someone comes down the corridor."

    return
