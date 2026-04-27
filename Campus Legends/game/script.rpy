# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define Sienna = Character("Sienna", color= "F54927")

define RTS = Character("Red Tape Studio")

define MCname = Character ("[MCname]")


# The game starts here.

label start:

    scene bg room
    show eileen phone  # Sienna looking at her phone

    # Sienna distracted, dots appear one at a time
    Sienna ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}."

pause 0.5

# Player shouts her name
RTS "SIENNA!!!"

# Sound effect AFTER the shout
play sound "MGS.ogg"

# Sienna reacts
show eileen happy

Sienna "Holy shit dude!!! When did you get here... you scared the shit outta me bro"

RTS "Wait, Sienna..."

Sienna "Rude ass motha—"

RTS "Sienna, I just want to say thank you to the players for checking out Campus Legends, and we here at Red Tape Studio hope you enjoy the ride!!!"

play sound "FAAAAAAA.ogg"

Sienna "...oh. Well damn, you could’ve led with that."

Sienna "Anywho, I'm Sienna and welcome to Campus Legends!!"

Sienna "Before I let you go on this epic journey, I have a few important questions I gotta ask you."




label get_name:

    $ MCname = renpy.input("What's your name handsome?")
    $ MCname = MCname.strip()

    # If blank → use default and skip confirmation
    if not MCname:
        $ MCname = "Emanuel"
        jump name_confirmed

    # Otherwise → ask for confirmation
    "Are you sure you want your name to be [MCname]?"

    menu:
        "Yep, that's my name.":
            pass

        "Nah, let me change it.":
            jump get_name

    jump name_confirmed


label name_confirmed:

    Sienna "[MCname], that's cute. Let's move on."

    Sienna "Campus Legends contains adult themes and content that is only for adults 18 years old and over."

    Sienna "Are you at least 18 years old?"

    menu:
        "Yes, I am 18 or older.":
            Sienna "Perfect. Then we can continue."

        "No, I'm not 18.":
            Sienna "Sorry, but you must be 18 or older to play this game."


    Sienna "Campus Legends is an epic journey that features highs and lows and choices matterso think before you click sweetie"


    # Hype send-off
    Sienna "Now that you know what ya need to know i'll see you in game handsome!!!"

    # Transition into the actual game
    scene black with fade
    pause 0.5
    jump game_start


label game_start:

    scene bg campus_day with dissolve

    "Your first day at Southside University begins..."

return

    # Continue your storreturn

