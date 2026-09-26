define Aubrey = Character("Aubrey")
define Tiffany = Character("Tiff")
label episode_2_start:

    scene dorm_morning
    with dissolve

    MCname "(Day two.)"
    MCname "(Still weird waking up somewhere that isn't home... but it's starting to feel a little less strange.)"

    show nick grin at left
    with dissolve

    Nick "Look who survived freshman day one."

    MCname "Barely."

    Nick "Hey, barely still counts."

    MCname "You're way too awake for this."

    Nick "Coffee."

    MCname "I don't see any coffee."

    Nick "Exactly."
    Nick "Imagine how powerful I'd be if I actually had some."

    MCname "(I'm ninety percent sure he's running on pure stupidity.)"

    Nick "So..."
    Nick "What's the game plan today?"

    $ personality = get_mc_personality()

    if personality == "Confident":
        Nick "Yesterday you walked around like you already owned the campus."
        Nick "Kind of worked, honestly."

    elif personality == "Playful":
        Nick "You somehow managed to stir things up on your very first day."
        Nick "That's impressive."

    elif personality == "Anxious":
        Nick "You hanging in there?"
        Nick "First week hits everybody differently."

    else:
        Nick "Yesterday was... something."
        Nick "Campus has a funny way of throwing people into the deep end."

    MCname "I'm still figuring everything out."

    Nick "That's college."
    Nick "Nobody actually knows what they're doing."

    MCname "You seem pretty confident."

    Nick "Fake it until graduation."

    MCname "That's... surprisingly honest."

    Nick "Don't tell anyone."

    Nick "Anyway..."

    Nick "If you're looking to kill some time before class..."

    Nick "Sienna's usually out getting a workout in before most people are even awake."
    Nick "Jess is probably wandering around with a coffee the size of her head."
    Nick "Norah's already judging the entire student body before breakfast."
    Nick "Aubrey..."
    Nick "Honestly, finding Aubrey is less of a plan and more of an accident waiting to happen."

    MCname "That's... weirdly specific."

    Nick "You'll see."

    Nick "Or..."
    Nick "You could ignore everybody, go straight to class, and make responsible life choices."

    MCname "You don't sound very convincing."

    Nick "Because responsible people don't make interesting stories."

    MCname "(He's probably right.)"
    MCname "(So... who do I want to run into today?)"

    jump ep2_choice_gate_1


label ep2_choice_gate_1:

    scene dorm_morning
    with dissolve

    MCname "(I've got a little time before class...)"
    MCname "(Who do I want to spend the morning with?)"

    menu:

        "See if Sienna's out training.":
            jump ep2_sienna_morning

        "Grab a coffee with Jess.":
            jump ep2_jess_morning

        "Go find Norah.":
            jump ep2_norah_morning

        "Track down Aubrey.":
            jump ep2_aubrey_morning

        "Hang out with Nick for a bit.":
            jump ep2_nick_morning

        "Head straight to class.":
            jump ep2_classroom_morning


label ep2_sienna_morning:

    $ add_relationship_points("Sienna", 5)

    scene campus_track_morning
    with dissolve

    MCname "(Nick was right... if anyone's awake this early, it'd be Sienna.)"
    MCname "(The athletic field should be around here.)"

    show sienna workout determined at center
    with dissolve

    Sienna "You're late."

    MCname "Late?"
    MCname "You never actually invited me."

    Sienna "Exactly."

    MCname "(...I walked right into that one.)"

    Sienna "They're quiet."
    Sienna "No crowds."
    Sienna "No pointless conversations."
    Sienna "...Usually."

    MCname "Wow."
    MCname "Good morning to you too."

    MCname "(Did... she just laugh?)"

    Sienna "What?"

    MCname "Nothing."
    MCname "Just wasn't expecting you to have a sense of humor."

    Sienna "I don't."
    pause 0.2
    Sienna "It was an accident."

    Sienna "Walk with me."

    scene campus_track_path
    with dissolve

    show sienna workout neutral at right
    show mc at left

    Sienna "You looked less lost yesterday."

    MCname "Less?"

    Sienna "You're still wandering onto an athletic field at seven in the morning."

    MCname "Fair point."

    Sienna "Most freshmen spend this hour asleep."

    MCname "Most freshmen don't know anybody."

    Sienna "..."
    Sienna "That's true."

    MCname "(She actually thought about that.)"

    menu:

        "I figured I'd rather spend the morning with someone interesting.":
            $ add_relationship_points("Sienna", 1)
            $ change_personality("Confident", 1)

            MCname "Classes can wait a few minutes."
            MCname "Interesting people can't."

            Sienna "Careful."
            Sienna "Flattery has a very low success rate on me."

            MCname "Worth testing."

        "Nick said I'd probably find you here.":
            $ add_relationship_points("Sienna", 1)

            MCname "Honestly?"
            MCname "Nick practically gave me your schedule."

            Sienna "I'm going to kill him."

            MCname "He said that was a possibility."

            Sienna "At least he's self-aware."

        "I couldn't sleep anyway.":
            $ add_relationship_points("Sienna", 1)
            $ change_personality("Anxious", 1)

            MCname "Everything's still new."
            MCname "My brain hasn't gotten the memo yet."

            Sienna "It gets easier."

            MCname "Yeah?"

            Sienna "Eventually this place starts feeling normal."

    Sienna "I need to finish my laps."

    MCname "How many do you have left?"

    Sienna "Eight."

    MCname "Left?"

    Sienna "Problem?"

    MCname "No."
    MCname "I'm just realizing we're very different people."

    Sienna "That's probably true."

    Sienna "Hey."

    MCname "Yeah?"

    Sienna "You came looking for me."

    MCname "I did."

    Sienna "..."
    Sienna "Thanks."

    hide sienna
    with dissolve

    MCname "(For someone who acts tough...)"
    MCname "(She doesn't seem used to people choosing to spend time with her.)"
    MCname "(There's definitely more to Sienna than she lets people see.)"

    jump ep2_classroom_morning


label ep2_norah_morning:

    $ add_relationship_points("Norah", 5)

    MCname "(Nick said Norah was probably judging people somewhere...)"
    MCname "(Not exactly a helpful clue.)"

    Norah "He's not wrong."

    MCname "How long have you been standing there?"

    Norah "Long enough to hear you talking to yourself."

    MCname "I wasn't talking to myself."

    Norah "No?"

    MCname "Okay, maybe a little."

    Norah "Self-awareness."
    Norah "That's refreshing."

    MCname "Reading before class?"

    Norah "Is that unusual?"

    MCname "Most people are glued to their phones."

    Norah "Most people also stop in the middle of doorways."
    Norah "Observe."
    Norah "Predictable."

    MCname "You've really thought about this."

    Norah "People are remarkably consistent."

    MCname "So..."
    MCname "Nick says you judge everyone."

    Norah "I make observations."

    MCname "There's a difference?"

    Norah "One is based on evidence."
    pause 0.2
    Norah "The other is Twitter."

    MCname "..."

    menu:
    
        "So what's your observation about me?":

            $ add_relationship_points("Norah", 1)
            $ change_personality("Confident", 1)

            MCname "Go ahead."
            MCname "I'm curious."

            Norah "You're trying very hard to seem relaxed."
            Norah "Most freshmen do."

        "You're impossible to read.":

            $ add_relationship_points("Norah", 1)


            MCname "Do you ever let people know what you're thinking?"

            Norah "Usually."
            pause 0.2
            Norah "Just not the people asking."

            MCname "...Fair."

        "Sounds exhausting, noticing everything.":

            $ change_personality("Caring", 1)

            Norah "...Sometimes."
    
    MCname "Can I ask you something?"

    Norah "You just did."

    MCname "You're impossible."

    Norah "I've heard that."

    MCname "You don't seem bothered."

    Norah "The opinions of strangers usually aren't worth carrying."

    MCname "That's... actually good advice."

    Norah "Don't get used to it."

    Norah "By the way."

    MCname "Yeah?"

    Norah "You asked questions instead of pretending to know everything."
    pause 0.2
    Norah "That's rarer than you'd think."

    hide norah
    with dissolve

    MCname "(She compliments people like she's issuing parking tickets.)"
    MCname "(I think that was a compliment.)"

    jump ep2_classroom_morning

label ep2_aubrey_morning:

    $ add_relationship_points("Aubrey", 2)

    scene campus_quad_morning
    with dissolve

    MCname "(Nick made Aubrey sound like a natural disaster.)"
    MCname "(Hopefully he was exaggerating...)"

    "WHACK!"

    MCname "Ow!"

    MCname "...Was that..."
    MCname "...an apple?"

    show aubrey casual grin at center
    with dissolve

    Aubrey "Yep."

    MCname "Did you just throw fruit at me?"

    Aubrey "Relax."
    Aubrey "I was aiming for the trash can."

    Aubrey "...Mostly."

    MCname "(She's smiling way too much for someone who just assaulted me with produce.)"

    MCname "You're Aubrey."

    Aubrey "Damn."
    Aubrey "My reputation really is getting around."

    MCname "Nick mentioned you."

    Aubrey "Of course he did."
    Aubrey "Lemme guess."
    Aubrey "\"She's trouble.\""

    MCname "More like..."
    MCname "\"Chaos potential.\""

    Aubrey "Ha!"
    Aubrey "I'm stealing that."

    Aubrey "C'mon."

    MCname "Where are we going?"

    Aubrey "No clue."

    MCname "That's... not reassuring."

    Aubrey "Exactly."

    scene campus_walkway
    with dissolve

    show aubrey casual smirk at right

    Aubrey "You always this cautious?"

    menu:
    
        "Only around people throwing apples.":

            $ add_relationship_points("Aubrey", 1)

            MCname "I've got trust issues now."

            Aubrey "Good."
            Aubrey "Means you're learning."

        "I'm just trying not to die before my second class.":

            $ add_relationship_points("Aubrey", 1)

            Aubrey "Boring."

            MCname "Alive."

            Aubrey "Debatable."

        "Depends who's asking.":

            $ add_relationship_points("Aubrey", 2)

            MCname "You interviewing me?"

            Aubrey "Maybe."

    
    MCname "What are you doing?"

    Aubrey "Shh."

    MCname "Were you hiding?"

    Aubrey "Maybe."

    MCname "Why?"

    Aubrey "Long story."
    Aubrey "Also a funny one."

    MCname "Should I be concerned?"

    Aubrey "Probably."

    MCname "..."
    MCname "Why?"

    Aubrey "Some perfectionist is gonna spend all day thinking about that."

    MCname "You're evil."

    Aubrey "Thank you."

    Aubrey "Damn."

    MCname "Late?"

    Aubrey "Very."

    MCname "Then why are you just standing here?"

    Aubrey "Because I was already late."

    MCname "...That's terrible logic."

    Aubrey "Works every time."

    Aubrey "See ya around, freshman."

    MCname "You're not even going the right direction."

    Aubrey "Details."

    hide aubrey
    with dissolve

    MCname "(She's either the most confident person on campus...)"
    MCname "(...or the biggest menace.)"
    MCname "(Honestly... probably both.)"

    jump ep2_classroom_morning

label ep2_jess_morning:

    $ add_relationship_points("Jess", 2)

    scene campus_coffee_shop
    with dissolve

    MCname "(If anyone's making a coffee run this early...)"

    show jess casual smile at center
    with dissolve

    Jess "Well, look who survived day one."

    MCname "Barely."

    Jess "That seems to be the freshman motto."

    MCname "You heading to class?"

    Jess "Eventually."
    Jess "First, coffee delivery."

    MCname "That many cups?"

    Jess "One's mine."
    Jess "One's for my roommate."
    Jess "...And one's for Nick."

    MCname "You bring him coffee?"

    Jess "He's hopeless before nine."

    Jess "Want to walk with me?"

    MCname "Sure."

    scene campus_path
    with dissolve

    show jess casual neutral at right

    Jess "So..."
    Jess "How are you holding up?"

    MCname "Honestly?"
    MCname "Still trying to remember where half my classes are."

    Jess "Everyone gets lost."
    Jess "Some people just get lost with more confidence."

    MCname "That sounds oddly specific."

    Jess "Experience."

    Student "Thank you!"

    Jess "You're okay."
    Jess "First week's rough."

    Jess "It gets easier."

    MCname "You do that a lot?"

    Jess "Help people?"

    MCname "Yeah."

    Jess "If I can make someone's day a little less stressful..."
    Jess "...why wouldn't I?"

    menu:
    
        "That's one of the nicest things I've heard all week.":

            $ add_relationship_points("Jess", 1)

            MCname "The campus could use more people like you."

            Jess "That's sweet."

        "You're the mom friend, aren't you?":

            $ add_relationship_points("Jess", 1)

            MCname "You carry emergency coffee."
            MCname "You help strangers."
            MCname "You're absolutely the mom friend."

            Jess "...I've been called worse."

        "Must get exhausting always looking after everyone.":

            $ add_relationship_points("Jess", 1)

            Jess "Sometimes."
            Jess "But everyone deserves someone looking out for them."
    
    Jess "I should get these delivered before Nick starts texting me dramatic complaints."

    MCname "He does that?"

    Jess "He once texted me..."
    Jess "\"I've seen the light, Jess."
    Jess "\"Unfortunately it was because I opened the fridge and there wasn't any coffee.\""

    MCname "That sounds exactly like him."

    Jess "Anyway..."

    Jess "I'm glad we ran into each other."

    MCname "Me too."

    Jess "See you in class?"

    MCname "Wouldn't miss it."

    hide jess
    with dissolve

    MCname "(Jess is different.)"
    MCname "(She's the kind of person who quietly makes everyone's day better... even if they don't always notice.)"

    jump ep2_classroom_morning

label ep2_nick_morning:

    scene dorm_morning
    with dissolve

    $ add_relationship_points("Nick", 5)

    show nick grin at center
    with dissolve

    Nick "Changed your mind already?"

    MCname "About what?"

    Nick "Going out."
    Nick "You were halfway out the door."

    MCname "Figured I'd hang around for a bit."

    Nick "Good."
    Nick "I'd hate to drink this terrible instant coffee alone."

    MCname "That... smells illegal."

    Nick "Pain builds character."

    MCname "Pretty sure that's just burnt coffee."

    Nick "Probably."

    MCname "So..."
    MCname "How'd you end up here?"

    Nick "Scholarship."
    Nick "A little luck."
    Nick "A lot of paperwork."

    MCname "That's less exciting than I expected."

    Nick "What?"
    Nick "You thought I was recruited because I'm devastatingly handsome?"

    MCname "The thought crossed my mind."

    Nick "Correct answer."

    Nick "You settling in okay?"

    MCname "Trying to."

    Nick "First week always feels weird."
    Nick "Then one day you'll be walking across campus wondering where the semester went."

    MCname "Easy for you to say."

    Nick "Nah."
    Nick "I was exactly where you are last year."

    Nick "Have you seen the guys with the blue and gold shirts around campus?"

    MCname "Yeah."

    Nick "That's Alpha Delta."
    Nick "One of the fraternities."

    MCname "You thinking about joining?"

    Nick "Thinking?"
    Nick "I've been planning to rush since senior year."

    MCname "Really?"

    Nick "My cousin was an Alpha."
    Nick "Best years of his life, according to him."

    MCname "I always figured fraternities were just parties."

    Nick "That's what everybody thinks."
    Nick "Yeah, they throw parties."
    Nick "But they also have alumni connections, intramurals, charity events..."
    Nick "...and a built-in group of people who always have your back."

    MCname "Sounds nice."

    Nick "College's a lot easier when you've got people in your corner."

    MCname "(He's got a point.)"

    menu:
    
        "Maybe I'll rush too.":

            MCname "Could be fun."

            Nick "Hell yeah."
            Nick "Imagine us getting in together."

        "I'm not really the frat type.":

            MCname "At least... I don't think I am."

            Nick "Neither do half the guys who end up joining."

        "I'll keep an open mind.":

            MCname "Depends on what they're actually like."

            Nick "That's the right attitude."
    
    Nick "Rush week isn't for a while anyway."
    Nick "You'll meet the different houses."
    Nick "Figure out who you click with."

    MCname "Plural?"

    Nick "Oh yeah."
    Nick "Every house thinks they're the best."

    MCname "Because Alpha Delta?"

    Nick "Now you're catching on."

    MCname "You've never even been a member."

    Nick "Details."

    Nick "...Yep."

    MCname "What?"

    Nick "We're gonna be late if we don't leave now."

    MCname "Whose fault is that?"

    Nick "Definitely yours."

    MCname "How?"

    Nick "I haven't figured that part out yet."

    MCname "(I'm starting to think living with Nick is never going to be boring.)"

    hide nick
    with dissolve

    jump ep2_classroom_morning

label ep2_classroom_morning:

    scene classroom_morning
    with dissolve

    MCname "(Made it in one piece.)"
    MCname "(That's becoming my morning goal.)"

    scene classroom_morning

    show kaia casual smile at left
    show tiff casual neutral at right

    Kaia "Hey!"
    Kaia "Over here."

    MCname "Mind if I sit here?"

    Kaia "Only if you're planning on stealing my notes."

    MCname "Bold of you to assume I'd understand them."

    #Kaia laughs.
    #Tiff smirks.

    Tiff "At least he's honest."

    MCname "(Guess these two adopted me.)"

    show professor_hart happy at center
    with dissolve

    ProfessorHart "Good morning, everyone."
    ProfessorHart "I'm Professor Hart."
    ProfessorHart "And before anyone asks..."

    #ProfessorHart raises a travel mug.

    ProfessorHart "...yes, this is coffee."
    ProfessorHart "...and no, you can't have any."

    #The class chuckles.

    ProfessorHart "Let's try this again."
    ProfessorHart "How many of you got at least eight hours of sleep?"

    #Three students raise their hands.

    ProfessorHart "Excellent."
    ProfessorHart "Liars usually reveal themselves early."

    #The room laughs.

    ProfessorHart "It's only the second day."
    ProfessorHart "You're still figuring this place out."

    # Frat guys enter
    show fratguy1 grin
    show fratguy2 grin
    show fratguy3 smile

    FratGuy1 "Morning, Professor."

    ProfessorHart "You're two minutes late."

    FratGuy2 "Technically we're all here now."

    ProfessorHart "And technically..."
    ProfessorHart "...you're still late."

    #The class laughs.

    ProfessorHart "Sit down before I start charging admission."

    FratGuy3 "Worth a shot."

    #Kaia leans toward you.

    Kaia "Those guys think they're celebrities."

    Tiff "Half the campus agrees."

    MCname "Who are they?"

    Kaia "Upperclassmen."
    Kaia "They're in Pi Kappa Alpha."

    Tiff "You'll know the fraternity guys."
    Tiff "They make sure everyone does."

    #ProfessorHart claps once.

    ProfessorHart "Eyes up here."

    ProfessorHart "Yesterday we covered the syllabus."
    ProfessorHart "Today we're talking about something much more important."

    #ProfessorHart writes on the board:

    ProfessorHart "Your degree matters."
    ProfessorHart "But so do the people sitting around you."

    ProfessorHart "Some of you will meet lifelong friends here."
    ProfessorHart "Some of you will discover careers you never considered."
    ProfessorHart "Some of you..."
    ProfessorHart "...will probably date someone in this room."

    #The class laughs.

    Kaia "Well this just got interesting."

    #Tiff rolls her eyes.
    #MCname laughs.

    ProfessorHart "Don't hide in your dorm."
    ProfessorHart "Join clubs."
    ProfessorHart "Go to campus events."
    ProfessorHart "Meet people who aren't exactly like you."

    #ProfessorHart points toward the quad.

    ProfessorHart "Tomorrow afternoon the student organization fair opens."
    ProfessorHart "Clubs."
    ProfessorHart "Volunteer organizations."
    ProfessorHart "Sports."
    ProfessorHart "...and yes..."

    #ProfessorHart glances at the fraternity guys.

    ProfessorHart "...the fraternities and sororities."

    #FratGuy1 gives a smug grin.

    ProfessorHart "Mr. Carter."

    FratGuy1 "Yes?"

    ProfessorHart "If I hear the phrase..."
    ProfessorHart "'Best house on campus'..."
    ProfessorHart "...before lunch..."
    ProfessorHart "...I'm assigning extra reading."

    #The frat guys laugh.

    FratGuy1 "Message received."

    #bell

    ProfessorHart "That's enough excitement for one morning."
    ProfessorHart "Enjoy the rest of your day."
    ProfessorHart "College is what you make of it."

    hide professor_hart
    with dissolve

    Kaia "You guys wanna hang at the Flaunt house tomorrow?"

    Tiff "I'm game."

    Kaia "You should come too."

    #FratGuy2 passes by with a confident grin.

    FratGuy2 "We'll see you there, freshman."

    MCname "(Looks like tomorrow just got a lot more interesting.)"

    jump ep2_after_class

label ep2_after_class:

    

    
    

    
    
    

                
    

