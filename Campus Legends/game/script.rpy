# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default player_name = ""

define e = Character("Eileen")

define Sienna = Character("Sienna", color= "F54927")

define RTS = Character("Red Tape Studio")

define MCname = Character ("[player_name]")

define Nick = Character ("Nick", color= "#0033AA" )

define mystery = Character("?????")

define Jess = Character ("Jessica")

image sienna_smile = "sienna_smile.png"

image Sienna_1 = "Sienna_1.png"

image sienna_look_up_movie = Movie(play="Sienna_look_up.avi", loop=False)




# The game starts here.

# label start:

#     call init_phone

#     scene expression "siennaphone.png"
#     # Sienna looking at her phone

#     # Sienna distracted, dots appear one at a time
#     Sienna ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}."

pause 0.5

# Player shouts her name
RTS "SIENNA!!!"

# Sound effect AFTER the shout
play sound "MGS.ogg"

# Immediately switch to her smiling sprite
scene Sienna_1

show sienna_look_up_movie onlayer transient
$ renpy.pause(1.0, hard=True)
hide sienna_look_up_movie onlayer transient


Sienna "Holy shit dude!!! When did you get here... you scared the shit outta me bro"

RTS "Wait, Sienna..."

Sienna "Rude ass motha—"

RTS "Sienna, I just want to say thank you to the players for checking out Campus Legends, and we here at Red Tape Studio hope you enjoy the ride!!!"

play sound "FAAAAAAA.ogg"

Sienna "...oh. Well damn, you could’ve led with that."

scene sienna_smile
with dissolve

Sienna "Anywho, I'm Sienna and welcome to Campus Legends!!"

Sienna "Before I let you go on this epic journey, I have a few important questions I gotta ask you."




label get_name:

    $ player_name = renpy.input("What's your name handsome?")
    $ player_name = player_name.strip()

    # If blank → use default and skip confirmation
    if not player_name:
        $ player_name = "Emanuel"
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
            return

    Sienna "Campus Legends is an epic journey that features highs and lows and choices matterso think before you click sweetie"


    # Hype send-off
    Sienna "Now that you know what ya need to know i'll see you in game handsome!!!"

    # Transition into the actual game
    scene black with fade
    pause 0.5
    jump game_start

label start:
    call init_phone
    jump game_start

label game_start:

    scene bg campus_day with dissolve

    

    show screen phone_button

    "Your first day at Southside University begins..."

    MCname "(Damn… it’s been a long journey, but here we are. SSU. Not my first choice, but hey—SVU didn’t want me. Their loss.)"

    "You take in the sights and two girls catch your eye..."

    MCname "*(Damn, they are kinda cute though..)"

    #"A hand suddenly claps your shoulder."

    mystery "Yoo bro, Havent seen you around, you a freshie?"

    MCname "Yeah just got here a few minutes ago im [MCname]"

    #"Nick follows his gaze and smirks"

    mystery "Sienna and Jessica"

    MCname "what?"

    mystery "The red head is Sienna and the blonde is Jessica, Sienna is the president of FLAUNT and Jess is the VP"

    MCname "FLAUNT?"

    mystery "It's the most popular sorority on campus.. they're all hot and full of attitude except for Jess,she's the one grounded soul they have"

    mystery "Sienna is cool asf though, i havent talked to the rest that much though"

    MCname "Do they have boyfriends?"

    $ sienna_m1.advance_expired()
    $ message(sienna, sienna_m2)
    $ new_post(sienna_pf, sienna_post1)


    mystery "Naw, Most guys cant handle Sienna and well Jess is sorta unavailable"

    MCname "(Interesting...)"

    Nick "I gotta get going dude im Nick by the way!! i gotta holla at the ladies."

label campus_intro_choice:

    Nick "You can roll with me if you want."

    menu:
        "Yeah, why not.":
            $ change_points("Nick", +1)
            jump meet_sienna_jess

        "I should really get going and unpack.":
            $ change_points("Nick", -1)
            jump dorm_arrival

label meet_sienna_jess:

    scene campus_gate with dissolve

    Nick "Come on, man. They’re right over here."

    show Sienna neutral at left
    show jess neutral at right

    Nick "Ladies! Look who I found wandering around like a lost puppy."

    Sienna "Oh? And who’s this?"
    Sienna "{i}(Cute… and new.){/i}"

    Jess "Hi. I’m Jess. Vice President of Flaunt."
    Jess "Nick, you didn’t scare him already, did you?"

    Nick "Me? Never."

    # First branching flirt/interest choice
    menu:
        "Smile back at Sienna.":
            $ change_points("Sienna", +1)
            Sienna "Hmm… confident. I like that."

        "Greet Jess politely.":
            $ change_points("Jess", +1)
            Jess "Oh— um… hi. Nice to meet you."

        "Stay neutral.":
            "You keep it simple. No need to overplay it."

    # Second choice to deepen the route
    menu:
        "Ask Sienna about Flaunt.":
            $ change_points("Sienna", +1)
            $ change_points("Confident", +1)

            Sienna "Why You thinking about joining?"
            Sienna "Or are you just trying to impress me?"

            MCname "If I wanted to impress you, trust me… you’d know."

            #Confident point awarded *because* of the bold retort
            $ change_points("Confident", +1)

            Sienna "Oh?"

        "Ask Jess how long she’s been VP.":
            $ change_points("Jess", +1)

            Jess "I joined as a freshmen and have been VP for around 2 years now give or take"
            MCname "That’s impressive. You must be one hell of a VP if Sienna’s kept you around"
            Jess "I… try my best. It means a lot to hear that"
            

        "Talk to Nick instead.":
            $ change_points("Nick", +1)
            Nick "See? I told you they’re cool."


    # Optional auto-check for romance route opening
    $ check_romance_unlock("Sienna")
    $ check_romance_unlock("Jess")

    jump dorm_arrival

label dorm_arrival:

    scene dorm_hall with dissolve

    MCname "Yeah, I should unpack. Long day already."

    Nick "Suit yourself, bro. I’ll catch you later."

    # Nick loses a point for skipping
    # Already applied in the choice above

    scene dorm_room with fade

    Nick "Yo! You made it. I already claimed the left side."

    # Continue into your dorm scene
    jump dorm_scene_main










return

    # Continue your storreturn

