# The script of the game goes in this file.

# Declare characters used by this game.

default player_name = ""
default met_sienna_jess = False

define e = Character("Eileen")
define prof = Character(_("prof"), color="#c8c8c8")
define Sienna = Character("Sienna", color="#F54927")
define RTS = Character("Red Tape Studio")
define MCname = Character("[player_name]")
define Malik = Character("Malik", color="#0033AA")
define mystery = Character("?????")
define Jess = Character("Jessica")
define Norah = Character("Norah")
define Tiffany = Character("Tiff")
define Misty = Character("Misty")
define Kaia = Character("Kaia")
define Aubrey = Character("Aubrey")

image sienna_smile = "sienna_smile.webp"
image Sienna_1 = "Sienna_1.webp"
image sienna_look_up_movie = Movie(play="Sienna_look_up.avi", loop=False)

image bg e1s1_1 = "images/e1s1_1.webp"
image bg e1s1_2 = "images/e1s1_2.webp"
image bg e1s1_3 = "images/e1s1_3.webp"
image bg e1s1_4 = "images/e1s1_4.webp"
image bg e1s1_6 = "images/e1s1_6.webp"
image bg e1s1_7 = "images/e1s1_7.webp"
image bg e1s1_8 = "images/e1s1_8.webp"
image e1s2_3b = "images/e1s2_3b.webp"
image e1s2_4 = "images/e1s2_4.webp"
image e1s2_4a = "images/e1s2_4a.webp"
image e1s2_4b = "images/e1s2_4b.webp"
image e1s2_6a = "images/e1s2_6a.webp"    #mc mouth closed
image e1s2_6 = "images/e1s2_6.webp"
image e1s2_7 = "images/e1s2_7.webp"
image e1s2_7a = "images/e1s2_7a.webp"
image e1s2_7b = "images/e1s2_7b.webp"
image e1s2_7c = "images/e1s2_7c.webp"
image e1s2_7d = "images/e1s2_7d.webp"
image e1s2_7e = "images/e1s2_7e.webp"
image e1s2_10 = "images/e1s2_10.webp"
image e1s2_10a = "images/e1s2_10a.webp"
image e1s2_10b = "images/e1s2_10b.webp"
image e1s2_10c = "images/e1s2_10c.webp"
image e1s2_14 = "images/e1s2_14.webp"
image e1s2_14a = "images/e1s2_14a.webp"
image e1s2_13a = "images/e1s2_13a.webp"
image e1s2_13 = "images/e1s2_13.webp"
image e1s2_7d = "images/e1s2_7d.webp"
image e1s2_7e = "images/e1s2_7e.webp"
image e1s2_8 = "images/e1s2_8.webp"
image e1s2_9 = "images/e1s2_9.webp"
image e1s2_9a = "images/e1s2_9a.webp"
image e1s2_9b = "images/e1s2_9b.webp"
image e1s2_9c = "images/e1s2_9c.webp"
image e1s2_9d = "images/e1s2_9d.webp"
image e1s2_9e = "images/e1s2_9e.webp"
image e1s2_9f = "images/e1s2_9f.webp"
image e1s2_11 = "images/e1s2_11.webp"
image e1s2_12 = "images/e1s2_12.webp"
image e1s2_13 = "images/e1s2_13.webp"
image e1s2_13a = "images/e1s2_13a.webp"
image e1s2_14 = "images/e1s2_14.webp"
image e1s2_14a = "images/e1s2_14a.webp"
image e1s2_15 = "images/e1s2_15.webp"

image e1s1_5b = "images/e1s1_5b.webp"
image e1s1_5 = "images/e1s1_5.webp"

image e1s2_3 = "images/e1s2_3.webp"
image e1s2_3a = "images/e1s2_3a.webp"

image sienna smirk = "sienna_smirk.webp"
image jess neutral = "jess_neutral.webp"

default walkthrough_enabled = False

###############################################
# START OF GAME
###############################################

label start:

    "Welcome to Campus Legends."

    "Before we get started, do you want to enable mini-games?"

    menu:
        "Yes, enable mini-games.":
            $ mini_games_enabled = True
            "Mini-games have been enabled."
        "No, disable mini-games.":
            $ mini_games_enabled = False
            "Mini-games have been disabled."

    "Would you like to enable the in-game walkthrough?"

    menu:
        "Enable walkthrough":
            $ walkthrough_enabled = True
            "Walkthrough enabled."
        "Disable walkthrough":
            $ walkthrough_enabled = False
            "Walkthrough disabled."

    call init_phone

    scene expression "Siennaphone.webp"

    Sienna ".{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}.{w=0.4}."

    pause 0.5

    # RTS shouts her name
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

    jump get_name

###############################################
# NAME INPUT
###############################################

label get_name:

    $ player_name = renpy.input("What's your name handsome?")
    $ player_name = player_name.strip()

    if not player_name:
        $ player_name = "Emanuel"
        jump name_confirmed

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

    Sienna "Campus Legends is an epic journey that features highs and lows and choices matter so think before you click sweetie."

    Sienna "Now that you know what ya need to know I'll see you in game handsome!!!"

    scene black with fade
    pause 0.5
    jump game_start

###############################################
# MAIN GAME START
###############################################

label game_start:

    scene bg e1s1_1

    show screen phone_button

    "Your first day at Southside University begins..."

    MCname "(Damn… it’s been a long journey, but here we are. SSU. Not my first choice, but hey—SVU didn’t want me. Their loss.)"

    scene bg e1s1_2
    with fade
    pause 1.0

    "You take in the sights and two girls catch your eye..."

    scene bg e1s1_3
    with dissolve
    pause 0.75

    MCname "*(Damn, they are kinda cute though..)"

    scene bg e1s1_4
    with dissolve
    pause 0.5

    mystery "Yoo bro, Haven't seen you around, you a freshie?"

    scene e1s1_5a
    with dissolve
    mystery "Sienna and Jessica."

    scene e1s1_5
    with dissolve
    MCname "What."

    scene e1s1_5a
    with dissolve
    mystery "The redhead is Sienna."

    scene e1s1_5
    with dissolve
    MCname "..."

    scene e1s1_5a
    with dissolve
    mystery "The blonde is Jessica."

    scene e1s1_5
    with dissolve
    MCname "..."

    # NEW LINE — fixes the flow
    scene e1s1_5a
    with dissolve
    mystery "Sienna's the president of FLAUNT, and Jess is the VP."

    scene e1s1_5
    with dissolve
    MCname "FLAUNT?"

    scene e1s1_5a
    with dissolve
    mystery "It's the most popular sorority on campus."

    scene e1s1_5
    with dissolve
    MCname "..."

    scene e1s1_5a
    with dissolve
    mystery "They're all hot and full of attitude."

    scene e1s1_5
    with dissolve
    MCname "..."

    scene e1s1_5a
    with dissolve
    mystery "Jess is the grounded one though, love her to death"

    scene e1s1_5
    with dissolve
    MCname "So you guys are dating?"

    scene e1s1_5a
    with dissolve
    mystery "Naw."

    scene e1s1_5
    with dissolve
    MCname "..."

    scene e1s1_5a
    with dissolve
    mystery "It's not because of a lack of effort..you know how these things go."

    scene e1s1_5
    with dissolve
    MCname "And Sienna?"

    scene e1s1_5a
    with dissolve
    mystery "Many have tried and failed that conquest."

    scene e1s1_5
    with dissolve
    MCname "..."

    scene e1s1_5a
    with dissolve
    mystery "Well my friend im gonna go holla at the ladies!!"

    jump campus_intro_choice

###############################################
# CHOICE: FOLLOW Malik OR NOT
###############################################

label campus_intro_choice:

    scene e1s1_5a
    with dissolve
    Malik "You can roll with me if you want."

    menu:
        "Yeah, why not.\n{color=#00ff00}{i}[[Malik +1]]{/i}{/color}":
            $ relationship_api.add_affection("Malik", +1)
            $ walkthrough("Malik +1")
            jump meet_sienna_jess

        "I should really get going and unpack.\n{color=#ff0000}{i}[[Malik -1]]{/i}{/color}":
            $ relationship_api.add_affection("Malik", -1)
            $ walkthrough("Malik -1")
            $ met_sienna_jess = False
            jump dorm_arrival

label meet_sienna_jess:

    Malik "Come on, man. They’re right over here."

    # Show the approach render cleanly
    scene bg e1s1_6
    with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.85, delay=0.5)

    pause 0.8

    with dissolve
    $ renpy.music.set_volume(1.0, delay=0.5)

    Malik "Ladies! Look who I found wandering around like a lost puppy."

    # Sienna speaks → switch to her render
    scene bg e1s1_7 with dissolve
    Sienna "Oh? And who’s this?"
    Sienna "{i}(Cute… ){/i}"

    # Jess speaks → switch to her render
    scene bg e1s1_8 with dissolve
    Jess "Hi. I’m Jess."
    MCname "[MCname], pleasure to meet you"
    Jess ".....likewise"
    Jess "Malik, you didn’t scare him already, did you?"

    Malik "Little ole meeee? Never."

    ########################################
    # FIRST MENU
    ########################################

    menu:

        "Smile back at Sienna.\n{color=#00ff00}{i}[Sienna +1]{/i}{/color}":
            $ relationship_api.add_affection("Sienna", 1)
            $ walkthrough("Sienna +1")
            scene bg e1s1_7 with dissolve
            Sienna "[MCname], Pleasure to meet you."

        "Smile at Jess.\n{color=#00ff00}{i}[Jess +1]{/i}{/color}":
            $ relationship_api.add_affection("Jess", 1)
            $ walkthrough("Jess +1")
            scene bg e1s1_8 with dissolve
            Jess ",,,,,,,."

        "Stay neutral.":
            MCname "Hey. Nice to meet you."
            scene bg e1s1_7 with dissolve
            Sienna "Playing it cool, huh?"

    ########################################
    # SECOND MENU
    ########################################

    menu:
        "Ask Sienna about Flaunt.\n{color=#00ff00}{i}[Sienna +1 / Sienna Trust +1 / Confident +1]{/i}{/color}":
            $ relationship_api.add_affection("Sienna", 1)
            $ walkthrough("Sienna +1")
            $ relationship_api.add_trust("Sienna", 1)
            $ walkthrough("Sienna Trust +1")

            scene bg e1s1_7 with dissolve
            Sienna "Why? You thinking about joining?"
            Sienna "Maybe as our official janitor?"
            MCname "Haha, i can barley keep up with my own cleaning duties."
            Sienna "Shame, i hade a maid outfit and everything haha"

            $ add_personality("Confident", 1)

        "Ask Jess how long she’s been VP.\n{color=#00ff00}{i}[Jess +1]{/i}{/color}":
            $ relationship_api.add_affection("Jess", 1)
            $ walkthrough("Jess +1")
            scene bg e1s1_8 with dissolve
            Jess "I joined as a freshman and have been VP for around 2 years now give or take."
            MCname "That’s impressive. You must be one hell of a VP."
            Jess "I… try my best. It means a lot to hear that."
            Jess "Tahnks"

        "Talk to Malik.\n{color=#00ff00}{i}[Malik +1]{/i}{/color}":
            $ relationship_api.add_affection("Malik", 1)
            $ walkthrough("Malik +1")
            MCname "Alright everyoen im tired and i need to get settled in before to late,so im gonna head out."
            Malik "Alright bro i'll see you around!!!"

    $ met_sienna_jess = True

    jump dorm_arrival

###############################################
# DORM ARRIVAL
###############################################

label dorm_arrival:

    scene e1s2_1
    with dissolve

    MCname "Damn,here's where i'll be staying...kinda smells like ass...."

    MCname "Lets see..room 204"

    scene e1s2_2
    with dissolve

    MCname "Here it is...i wonder what my roommate is gonna be like? Hopefully not a douche canoe.."

    #MC KNOCKS ON DOOR

    scene e1s2_3
    with dissolve

    Malik "Yoooo [MCname], couldnt get enough of me could you!!! i know man i know"

    scene e1s2_3a
    with dissolve
    MCname "Hahaha this is actually my dormroom"

    scene e1s2_3
    with dissolve
    Malik "Correction my good sir!!! This is [MCname]'S and Malik's den of iniquity!!"

    scene e1s2_3a
    with dissolve
    MCname "Haha there's something wrong with you dude!!!"

    scene e1s2_3b
    with dissolve
    Malik "Well dont just stand there like a lost puppy get your ass in here bro!!"

    scene e1s2_4
    with dissolve

    scene e1s2_4a
    with dissolve

    scene e1s2_4b
    with dissolve

    # MC walks into the dorm room looking around

    Malik "Welcome to the batcave my friend!!"

    scene e1s2_6
    with dissolve
    MCname "Well shit..not bad,alot bigger than i imagined tbh"

    scene e1s2_6a
    with dissolve

    scene e1s2_7
    with dissolve
    Malik "Right it kinda threw me off too when i first got here last year"

    scene e1s2_7a
    with dissolve

    scene e1s2_6
    with dissolve
    MCname "Last year? so you're a sophmore or junior?"

    scene e1s2_7
    with dissolve
    Malik "Sophmore baby!! That means i can actually move into the Kappa's house!!"
    scene e1s2_7a

    with dissolve
    scene e1s2_6
    MCname "Kappa house?"

    scene e1s2_7
    with dissolve
    Malik "Yeah dude it's the Phi Kappa Alpha house,they're the frat on campus!!"

    scene e1s2_6
    with dissolve
    MCname "Damn ok, Mr.Big Shit over here."

    scene e1s2_7
    with dissolve
    Malik "Haha, you should join us bro"

    scene e1s2_6
    with dissolve
    MCname "Idk man that's not even rometly something that i can think about seriously right this moment"

    scene e1s2_7
    with dissolve
    Malik "Felt broski,felt."

    scene e1s2_6
    with dissolve
    MCname "Yeah, I should unpack. Long day already."

    scene e1s2_7
    with dissolve
    Malik "Alright man im gonna chillax just holla if ya need help."

    # Fade cleanly to black
    scene black
    with fade

    "{i}One hour later...{/i}"
    pause 0.8

    # Fade back in
    scene e1s2_10
    with fade

    Malik "Bruh you still unpacking?"

    scene e1s2_10a
    with dissolve

    MCname "Naw man just a few more things and im done."

    scene e1s2_10
    with dissolve
    Malik "So where's home? you know before you crashed my party haha."
    scene e1s2_10a
    with dissolve

    MCname "I'm from the Southside of Compton"

    scene e1s2_10
    with dissolve
    Malik "Word"
    scene e1s2_10a
    with dissolve

    scene e1s2_10
    with dissolve
    Malik "Oh—before I forget. Jess texted me."
    scene e1s2_10a
    with dissolve

    MCname "She did?"

    scene e1s2_10
    with dissolve
    Malik "Yeah, Flaunt and the Kappa's party together so i help coordinate sometimes plus i told her we're roomies now!!"
    scene e1s2_10a
    with dissolve

    MCname "{i}(Not gonna press him if he doesnt elaborate....){/i}"

    jump dorm_scene_main

###############################################
# DORM MAIN SCENE
###############################################

label dorm_scene_main:

    scene e1s2_7b
    with dissolve
    Malik "Alright bro, welcome to SSU. Fresh start, new chaos, questionable decisions."

    Malik "Since you’re officially moved in, you get one free perk:"
    Malik "You can ask me anything about this place before it eats you alive."

    jump dorm_questions_menu

###############################################
# DORM QUESTIONS LOOP
###############################################

label dorm_questions_menu:

    menu:

        "Ask about SSU in general.":
            scene e1s2_7b
            with dissolve
            Malik "Alright, real talk? SSU’s a weird mix in the best way."
            Malik "People treat it like a party school, and yeah, it absolutely is… but the academics sneak up on you."
            Malik "You’ll see someone shotgun a beer at two in the morning, then ace a midterm on three hours of sleep like it’s nothing."
            Malik "It’s chaotic, but somehow it works. You just kinda learn to ride the wave."
            scene e1s2_7c
            with dissolve
            jump dorm_questions_menu

        "Ask about the fraternities.":
            scene e1s2_7b
            with dissolve
            Malik "So SSU’s got two big ones, and they’re basically opposites."
            Malik "First is Phi Kappa Alpha aka the Kappas. Biggest frat on campus. Loud, confident, everywhere."
            Malik "That’s the one I joined. Parties, sports, hookups… the whole ‘college experience’ package."
            Malik "Then you’ve got Alpha Rho Chi — ARC. Total academic powerhouse. Honors kids, scholarship students, future CEOs."
            Malik "They’re serious. Organized. Scary smart. If the Kappas runs the social scene, ARC runs the academic one."
            Malik "Two different worlds, man. Depends on what kind of people you want around you."
            scene e1s2_7c
            with dissolve
            jump dorm_questions_menu


        "Ask about clubs and activities.":
            scene e1s2_7b
            with dissolve
            Malik "Pretty much everything. Sports, debate, gaming, dance, photography, volunteer groups… whatever you’re into."
            Malik "If it exists, there’s a club. If it doesn’t, someone will make one."
            scene e1s2_7c
            with dissolve
            jump dorm_questions_menu

        "Ask about Malik himself.":
            scene e1s2_7b
            with dissolve
            Malik "Me? I’m just trying to survive college without losing my sanity."
            Malik "I like people, I like parties, and I really like not failing my classes."
            Malik "And I’m your roommate, so… unfortunately for you, you’re stuck with me."
            scene e1s2_7c
            with dissolve
            jump dorm_questions_menu

        "I'm good for now.":
            scene e1s2_7b
            with dissolve
            Malik "Cool."
            Malik "Orientation starts tomorrow, so get some rest."

    jump dorm_scene_end

###############################################
# DORM SCENE END + MIXER INVITE
###############################################

label dorm_scene_end:

    scene e1s2_7b
    with dissolve
    Malik "Alright, that's the SSU crash course. You're basically a local now."

    scene e1s2_7c
    with dissolve
    MCname "Good looking out bro!!"
    scene e1s2_7b
    with dissolve
    Malik "Hey, that's what roommates are for."
    Malik "Besides, you'll figure out most of this once the year gets rolling."
    scene e1s2_7c
    with dissolve
   
    MCname "{i}(It's weird… I actually feel a little more prepared now.){/i}"
    scene e1s2_7b
    with dissolve
    Malik "We've got the whole year ahead of us."
    Malik "No point trying to figure everything out on night one."
    scene e1s2_7c
    with dissolve

    pause 0.5

    "*knock knock*"
    scene e1s2_7d
    with dissolve
    Malik "Huh?"
    scene e1s2_7e
    with dissolve
    Malik "I'm not expecting anyone."
    scene e1s2_8
    with dissolve
    MCname "I'll get it."
    MCname "{i}(Who could it be?){/i}"

    scene e1s2_9
    with dissolve

    scene e1s2_9c
    with dissolve
    Sienna "Well, well, well…"
    scene e1s2_9d
    with dissolve

    scene e1s2_9c
    with dissolve
    Sienna "Look at this cozy little setup."
    scene e1s2_9d
    with dissolve

    Malik "Oh, shit."

    scene e1s2_9a
    with dissolve
    Jess "Hi, Malik."

    Jess "Hi… um—"

    if met_sienna_jess:

        Jess "[MCname], right?"
        scene e1s2_9b
        with dissolve
        MCname "Yeah. Hey."

        scene e1s2_9c
        with dissolve
        Sienna "We figured we'd stop by."

        Sienna "Freshman mixer this Friday."

        Sienna "Mandatory fun."
        scene e1s2_9d
        with dissolve

    else:
        scene e1s2_9a
        with dissolve
        Jess "You must be Malik's roommate."
        scene e1s2_9b
        with dissolve
        MCname "Yeah, that's me."
        scene e1s2_9c
        with dissolve
        Sienna "Cute."

        Sienna "Anyway… there's a freshman mixer this Friday."

        Sienna "You two are coming."
        scene e1s2_9d
        with dissolve

    Malik "Wait… you came all the way to our dorm to tell us that?"

    scene e1s2_9c
    with dissolve
    Sienna "Relax, Romeo."

    Sienna "We're telling everyone on this floor."
    scene e1s2_9d
    with dissolve

    scene e1s2_9a
    with dissolve
    Jess "{i}(quietly){/i} Mostly everyone."
    scene e1s2_9b
    with dissolve

    MCname "{i}(…What does that mean?){/i}"
    scene e1s2_9c
    with dissolve
    Sienna "Mixer starts at eight. Friday night."

    Sienna "Dress to impress, boys."
    scene e1s2_9d
    with dissolve

    scene e1s2_9a
    with dissolve
    Jess "And don't be late."

    Jess "It gets crowded pretty quickly."
    scene e1s2_9b
    with dissolve

    Malik "We'll be there."

    Malik "Right, bro?"

menu:

    "Yeah, sounds fun.\n{color=#00ff00}{i}[Sienna +1 / Jess +1 / Confident +1]{/i}{/color}":

        MCname "Yeah. We'll come through."
        scene e1s2_9c
        with dissolve
        Sienna "Good."
        Sienna "I like enthusiasm."
        scene e1s2_9d
        with dissolve

        Malik "That's what I'm talking about."

        $ add_confidence(1)

        # First impressions → affection bumps
        $ relationship_api.add_affection("Sienna", 1)
        $ relationship_api.add_affection("Jess", 1)

        if walkthrough_enabled:
            $ walkthrough("Sienna +1 / Jess +1 / Confident +1")

        MCname "{i}(Okay… maybe this won't be so bad.){/i}"


    "I'm not really a party person…\n{color=#00ff00}{i}[Jess +2 / Sienna -1]{/i}{/color}":

        MCname "I don't know if parties are really my thing."

        Jess "It's not really a party."
        Jess "More like a social warm-up."

        Sienna "Translation: you're coming."

        Malik "Bro, it'll be fine."
        Malik "I'll keep you out of trouble."

        # First impressions
        $ relationship_api.add_affection("Jess", 1)
        $ relationship_api.add_affection("Sienna", -1)

        if walkthrough_enabled:
            $ walkthrough("Jess +2 / Sienna -1")

        MCname "{i}(Great… forced socializing. Just what I needed.){/i}"


    "Where is it?\n{color=#00ff00}{i}[Growth +1 / Jess +1]{/i}{/color}":

        Jess "Flaunt House."
        Jess "Friday at eight."

        Sienna "If you miss it, we'll come drag you out ourselves."
        MCname "{i}(Okay… at least I know where I'm going.){/i}"

        $ mc_adjust_growth(1)

        # First impressions
        $ relationship_api.add_affection("Jess", 1)
        $ relationship_api.add_affection("Sienna", 0)

        if walkthrough_enabled:
            $ walkthrough("Growth +1 / Jess +1")

scene e1s2_9c
with dissolve
Sienna "Alright, boys."

Sienna "See you Friday."
scene e1s2_9d
with dissolve

scene e1s2_9a
with dissolve
Jess "Bye."
scene e1s2_9b
with dissolve

pause 0.5

scene e1s2_11
with dissolve

Malik "Bro…"
Malik "They came to our room. OUR room."

MCname "You're really impressed by that?"

Malik "Dude, that's Sienna. You don’t get it."
Malik "She doesn’t just show up places. People go to her."
Malik "If she’s at your door on day one? That’s… that’s a whole thing."

MCname "{i}(Apparently, I have a lot to learn.){/i}"

Malik "And Jess too? Jess never tags along unless it matters."
Malik "If both of them showed up, that mixer is gonna be huge."

Malik "Friday night is going to be fucking crazy."
Malik "Like… ‘you’ll remember it for the rest of the year’ crazy."

MCname "{i}(…This school is going to be insane.){/i}"

jump dorm_monday_night

###############################################
# DORM MONDAY NIGHT
###############################################

label dorm_monday_night:

    scene e1s2_11
    with dissolve

    Malik "Bro… that was insane."
    Malik "They really came all the way here just to tell us about a mixer."

    scene e1s2_14
    with dissolve
    MCname "Yeah. And it’s not even until Friday."
    scene e1s2_14a
    with dissolve

    scene e1s2_13
    with dissolve
    Malik "Which means we’ve got four days to prepare ourselves."
    scene e1s2_13a
    with dissolve

    scene e1s2_14
    with dissolve
    MCname "You say that like it’s easy."
    scene e1s2_14a
    with dissolve

    scene e1s2_13
    with dissolve
    Malik "It is easy. Just don’t be weird."
    scene e1s2_13a
    with dissolve

    MCname "{i}(…Great. That’s basically my whole personality.){/i}"

menu:

    "Brush it off — pretend you’re fine.\n{color=#00ff00}{i}[Confident +1]{/i}{/color}":
        $ add_personality("Confident", 1)
        scene e1s2_14
        with dissolve
        MCname "I’ll be fine. It’s just a mixer."
        scene e1s2_14a
        with dissolve
        scene e1s2_13
        with dissolve
        Malik "That’s the spirit."
        scene e1s2_13a
        with dissolve

        if walkthrough_enabled:
            $ walkthrough("Confident +1")


    "Admit you’re anxious about it.\n{color=#00ff00}{i}[Anxiety +1]{/i}{/color}":
        $ mc_adjust_anxiety(1)
        scene e1s2_14
        with dissolve
        MCname "I’m already overthinking it."
        scene e1s2_14a
        with dissolve

        scene e1s2_13
        with dissolve
        Malik "Hey, it’s days away. You’ve got time."
        scene e1s2_13a
        with dissolve

        if walkthrough_enabled:
            $ walkthrough("Anxiety +1")


    "Joke about it to hide nerves.\n{color=#00ff00}{i}[Anxiety +1]{/i}{/color}":
        $ mc_adjust_anxiety(1)
        scene e1s2_14
        with dissolve
        MCname "If I pass out, just drag me to the courtyard."
        scene e1s2_14a
        with dissolve

        scene e1s2_13
        with dissolve
        Malik "Bro, I’m not carrying you across campus."
        scene e1s2_13a
        with dissolve

        if walkthrough_enabled:
            $ walkthrough("Anxiety +1")

scene e1s2_13
with dissolve
Malik "Anyway… we’ve got class in the morning. You should get some sleep."
scene e1s2_13a
with dissolve

scene e1s2_14
with dissolve
MCname "Yeah… probably."
scene e1s2_14a
with dissolve

scene e1s2_15
with dissolve
MCname "{i}(Friday… mixer… Jess and Sienna…){/i}"
MCname "{i}(This week is going to be something.){/i}"

jump tuesday_morning

# End of prolouge
