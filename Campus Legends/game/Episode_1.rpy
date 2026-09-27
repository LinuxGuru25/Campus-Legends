
###############################################
# TUESDAY MORNING — EPISODE 1 START
###############################################

label tuesday_morning:

    scene dorm_room_morning

    MCname "{i}(Tuesday. First real day...){/i}"
    MCname "{i}(Mixer’s on Friday...){/i}"
    MCname "{i}(No pressure, right?){/i}"

    show Malik

    Malik "Morning, bro. You ready for day one?"
    MCname "Does a bear shit in the woods and....."

    Malik "I feel like a pround dad sending his son to school in the morning."

    MCname "hahah well dad i neeed 18 years of child support to get through this semester."

    Malik "Oh—i think we're outta milk son."
    Malik "haha but seiously go my friend be a social butterfly and make some new friends."

    MCname "{i}(Alright, time to bounce... should I take Malik's advice and look for one of the ladies before class?){/i}"


    menu:
        "Look for Sienna.":
            $ add_personality("Confident", 1)
            $ walkthrough("Confident +1")
            $ morning_route = "sienna"
            MCname "{i}(Let’s see if Sienna’s around. She’s probably already up.){/i}"
            jump look_for_sienna_tuesday

        "Look for Jess.":
            $ mc_adjust_growth(1)
            $ walkthrough("Growth +1")
            $ morning_route = "jess"
            MCname "{i}(Jess seemed calm yesterday… maybe I’ll run into her.){/i}"
            jump look_for_jess_tuesday

        "Just go to class.":
            $ mc_adjust_anxiety(1)
            $ walkthrough("Anxiety +1")
            $ morning_route = "class"
            MCname "{i}(I should probably just head to class before I overthink everything.){/i}"
            jump class_intro



###############################################
# SIENNA ENCOUNTER — FULL SCENE
###############################################

label look_for_sienna_tuesday:

    $ relationship_api.add_points("Sienna", 1)
    $ walkthrough("Sienna +1")

    MCname "{i}(Wonder if I'll run into Sienna...){/i}"

    scene campus_path
    show Sienna

    # MC walking past the Flaunt house

    Sienna "Morning, freshman."

    MCname "Oh—hey. Didn't expect to see you out this early."

    Sienna "Really? I've been awake for hours."

    MCname "It's not even eight."

    Sienna "Exactly. Half the campus is still unconscious."

    menu:
        "Tease her back.":
            $ add_personality("Confident", 1)
            $ walkthrough("Confident +1")
            $ relationship_api.add_points("Sienna", 1)
            $ walkthrough("Sienna +1")

            MCname "So ambition or caffeine addiction?"
            Sienna smirk "Why are you acting like those are different things?"

        "Act impressed.":
            $ relationship_api.add_points("Sienna", 1)
            $ walkthrough("Sienna +1")
            MCname "Seriously? I barely made it out of bed."
            Sienna eyebrow "Trust me, I noticed."

        "Play it cool.":
            $ add_personality("Confident", 1)
            $ walkthrough("Confident +1")
            MCname "Guess somebody has to keep the campus running."
            Sienna "Good thing I'm here, then."

    Sienna "Anyway, I'm doing some rush week prep."

    MCname "Already?"

    Sienna "Yup. Rush week is next week, so if you're gonna join a frat now is the time to make that decision known."

    MCname "Malik did ask me if I wanted to join the Kappas."

    Sienna "Well?"

    MCname "I mean... I'd be lying if I said it hasn't been on my mind."

    Sienna "You're off to a good start if the VP is vetting you."

    MCname "I'm confused... I only know Mal... wait!!! He's the fuckin' VP??"

    Sienna "Ding ding, he finally figures it out, haha."

    MCname "That sneaky mofo, he just said he's a part of it!!!"

    Sienna "Technically he didn't lie, he just kinda omitted some information."

    Sienna "Anyway, all I know is this coming week is gonna be hell for us..."

    menu:
        "Ask about Flaunt.":
            $ relationship_api.add_points("Sienna", 1)
            $ walkthrough("Sienna +1")
            MCname "So what does Flaunt actually do on campus?"
            Sienna "For starters, we aren't what people think we are... just a bunch of chicks who party, drink, and fuck frat boys."
            Sienna "I mean sure, some of us do enjoy some extracurricular activities, but that's not our main focus."
            Sienna "We also look to make young women into future leaders in their chosen industry, we feed the homeless every weekend, we do volunteer work in the community and so on."
            MCname "Wow, and you coordinate all this shit?"
            Sienna smirk "Indeed I do, freshie."
            MCname "Sounds like a lot."
            Sienna "It is."
            pause 0.2
            Sienna "Worth it, though."

        "Joke about joining.":
            $ add_personality("Selfish", 1)
            $ walkthrough("Selfish +1")
            MCname "Think they'd let me join?"
            Sienna "Maybe."
            MCname "That's not exactly reassuring."
            Sienna "You'd be a project."
            pause 0.2
            Sienna smirk "A fun project, though."

        "Playfully acknowledge her role.":
            $ add_personality("Confident", 1)
            $ walkthrough("Confident +1")
            MCname "Presidential duties never stop, huh?"
            Sienna "Not when you're good at them."
            MCname "Wow, and humble too!!"
            Sienna smirk "You say that like I've got a reason to be modest."

    if get_points("Anxiety") >= 3:

        Sienna "You look tense."
        MCname "Do I?"
        Sienna "A little."
        MCname "First day jitters."
        Sienna nod "Fair."
        Sienna "For what it's worth, nobody here knows what they're doing."
        MCname "That supposed to help?"
        Sienna "Maybe."
        Sienna smirk "Some people are just better at pretending."

    elif get_points("Depression") >= 3:

        Sienna "You look tired."
        MCname "Didn't sleep great."
        Sienna "No, I mean tired tired."
        MCname "..."
        Sienna neutral "Then don't let today steamroll you."
        MCname "Easy for you to say."
        Sienna "Maybe."
        Sienna "But you only get one first day. Might as well make it count."

    elif get_points("Confident") >= 3:

        Sienna "You're walking around like you already belong here."
        MCname "That a bad thing?"
        Sienna "Not at all."
        Sienna smirk "Confidence is basically currency on this campus."
        MCname "Good thing I'm rich, then."
        Sienna laugh "We'll see."

    else:

        Sienna "You've got that new‑kid look."
        MCname "What's that supposed to mean?"
        Sienna "Like you're constantly checking for emergency exits."
        MCname "Is it really that obvious?"
        Sienna "Painfully."

    menu:
        "Flirt lightly.":
            $ relationship_api.add_points("Sienna", 5)
            $ walkthrough("Sienna +5")
            MCname "You know, I didn't expect you to be this easy to talk to."
            Sienna raise_eyebrow "That's what you get for listening to Malik."
            MCname "Hahaha, how'd you know?"
            Sienna "He tells everyone I'm some kind of man-eater or something. He's just mad I shot down his friends from the frat."
            MCname "So one could say you're a hot commodity."
            Sienna "Haha... barely. I don't even have time to myself, let alone maintain a relationship with all the sorority shit going down."
            MCname "That actually sucks... you're a beautiful woman, you deserve to have someone."
            Sienna "You sound like you have someone in mind."
            MCname "Maybe I do?"
            # Sienna stops what she is doing and approaches you
            Sienna "You sure you wanna go that route, [MCname]?"
            "(......)"
            Sienna smirk "Cat got your tongue?"
            MCname "Umm, no, I..."
            Sienna "Hahaha, cute...."

        "Ask her for advice about day one.":
            $ relationship_api.add_points("Sienna", 1)
            $ walkthrough("Sienna +1")
            MCname "Got any advice for surviving day one?"
            Sienna "Don't be forgettable."
            MCname "That's it?"
            Sienna "People remember confidence."
            pause 0.2
            Sienna "Or chaos."
            Sienna smirk "Ideally the fun kind."

        "Challenge her a little.":
            $ add_personality("Confident", 1)
            $ walkthrough("Confident +1")
            MCname "You talk like you've got everyone figured out."
            Sienna "Maybe I do."
            MCname "That's a dangerous amount of confidence."
            Sienna smirk "Then prove me wrong."
            "Sienna glances at her phone."


    Sienna "Anyway, go to class before you get lost."

    MCname "That likely?"

    Sienna "For you? Very."

    MCname "Wow."

    Sienna smirk "See you around, [MCname]."

    MCname "{i}(She somehow manages to be encouraging and insulting at the same time.){/i}"

    jump class_intro



###############################################
# JESS ENCOUNTER — NEW FULL SCENE
###############################################

label look_for_jess_tuesday:

    $ change_points("Jess", +1)
    $ walkthrough("Jess +1")

    scene campus_hallway

    MCname "{i}(Hopefully I'll run into Jess along the way.){/i}"

    # MC runs into Jess in the library

    Jess "[MCname], hey, how are you?"

    MCname "I'm doing great, how's the morning treating you?"
    Jess "It could be better..."
    MCname "Something wrong?"
    Jess "Just the stress of this coming rush week."
    MCname "Shit, I can imagine... but it'll be over soon enough and you'll be free!!"
    Jess "I keep telling myself that."
    MCname "Hey, don't you worry. If things get too stressful, you call us and we'll come rescue you!!"
    Jess "Haha, thanks. How's Malik?"
    MCname "Just as goofy as ever, but I'm glad he's my roomie."
    Jess "He's a good guy, stick with him."
    MCname "I plan to."
    # Jess lets out a content sigh
    Jess "I like quiet mornings. Less noise, less chaos."

    menu:
        "Be friendly.":
            $ change_points("Jess", +1)
            $ walkthrough("Jess +1")
            MCname "Campus is kinda peaceful right now."
            Jess "It won't last too much longer though, sadly."

        "Be flirty.":
            $ add_personality("Confident", 1)
            $ walkthrough("Confident +1")
            MCname "I'm really glad I ran into you this morning."
            Jess "Why's that?"
            MCname "You're such a calming influence on people, it's actually refreshing."
            Jess blush "That's so sweet, [MCname]..."
            Jess "Thank you."

    Jess "Are you heading to class?"

    MCname "Yup, I think I'm headed in the right direction, haha."
    Jess "What do you need to go?"
    MCname "English Comp."
    Jess "Ahh, you're in Prof Hart's class!!! She's an amazing prof!! You'll love her."
    Jess "Just keep going down the hall and take a right, it's the second door on the left."
    MCname "You, my friend, are a scholar and a lady!!!"
    Jess "Haha."
    Jess "Anyway… I should get going. Don’t be late to class."

    hide Jess with dissolve

    MCname "{i}(She’s definitely different from Sienna… quieter, but sharp.){/i}"



###############################################
# CLASS INTRO — FIRST CLASS OF THE YEAR
###############################################

label class_intro:

    scene classroom_morning with dissolve

    MCname "{i}(First class of freshman year... alright. Deep breath. Try not to say anything stupid.){/i}"

    # Optional callback depending on who you looked for
    if morning_route == "sienna":
        MCname "{i}(Running into Sienna definitely woke me up. She has... a lot of energy.){/i}"
    elif morning_route == "jess":
        MCname "{i}(Jess made the morning a little less intimidating. That was nice.){/i}"
    else:
        MCname "{i}(Definitely should've grabbed coffee. I'm barely functioning.){/i}"

    play sound "classroom_murmur.ogg"

    MCname "{i}(The room buzzes with nervous conversations. Some people already know each other. Most are pretending they do.){/i}"

    show prof

    # Professor Hart enters the room

    "Damnnn son she's hot... yeah bwoi!"

    prof "Morning, everyone."

    prof "Welcome to English Comp."

    prof "I'm Professor Hart."

    prof "Some of you enrolled because the course title sounded interesting."

    prof "Some of you because it fit your schedule."

    prof "And a few of you probably think this is going to be an easy A."

    pause 0.4

    prof "Those students usually stop showing up around midterms."

    MCname "{i}(Well... she wasted absolutely no time setting the tone.){/i}"

    prof "This semester, we're going to focus on something we all use every day."

    prof "Language."

    prof "How we communicate."

    prof "How we persuade."

    prof "And how the words we choose shape the way people see us."

    prof "Because writing isn't just about putting words on a page."

    prof "It's about understanding your audience."

    prof "Building an argument."

    prof "And learning how to make your ideas matter."

    MCname "{i}(Okay... that's actually more interesting than I expected.){/i}"

    prof "We'll be reading, writing, discussing, and occasionally questioning why the hell English has so many unnecessary rules."

    pause 0.4

    prof "But first..."

    prof "Let's get the awkward part out of the way."

    prof "Stand up, tell us your name, and share one thing you hope to improve or learn this semester."

    MCname "{i}(Of course. Icebreakers. The true enemy of higher education.){/i}"

menu:

    "Be confident.\n{color=#00ff00}{i}(Confident +1){/i}{/color}":
        $ add_personality("Confident", 1)
        $ walkthrough("Confident +1")

        MCname "I'm [MCname]. I'd like to take my writing to the next level!!!"

        prof "Confidence is useful."
        prof "Just make sure it's earned."

    "Be modest.\n{color=#00ff00}{i}(Growth +1){/i}{/color}":
        $ mc_adjust_growth(1)
        $ walkthrough("Growth +1")

        MCname "I'm [MCname]. Honestly... I'm mostly hoping to improve my writing a little."

        prof "A realistic goal."
        prof "College has a way of humbling everyone."

    "Be funny.\n{color=#00ff00}{i}(Selfish +1){/i}{/color}":
        $ change_points("Selfish", 1)
        $ walkthrough("Selfish +1")

        MCname "My name is Buck, I drive a truck, and I like to—"

        prof "Nope, don't you finish that sentence."
        prof "Now that it's out of your system, tell us your name and what you hope to learn this semester."

        MCname "I'm [MCname]. I hope to learn how to write better essays and not get lost in the library."

        prof "Funny. Now sit down."
        prof "I'll have my eye on you..."

    "Be awkward.\n{color=#00ff00}{i}(Anxiety +1){/i}{/color}":
        $ mc_adjust_anxiety(1)
        $ walkthrough("Anxiety +1")

        MCname "I'm... [MCname]."
        MCname "...I actually don't know yet."

        prof "That's an acceptable answer."
        prof "If you already knew everything you wanted to learn, you wouldn't need college."


prof "Good."

prof "Here's one thing you'll discover over the next few months."

prof "Everyone wants to be understood."

prof "Very few people know how to understand someone else."

prof "Pay attention in here, and you might learn something useful."

MCname "{i}(She's definitely more interesting than I expected.){/i}"

if get_points("Confident") >= 3:

    prof "Confidence opens doors."

    prof "Arrogance closes them."

    MCname "{i}(...Was that aimed at me?){/i}"

elif get_points("Anxiety") >= 3:

    prof "And if public speaking makes you nervous..."

    prof "Congratulations."

    prof "You're human."

    MCname "{i}(...That actually makes me feel a little better.){/i}"

elif get_points("Depression") >= 3:

    prof "If you're exhausted already..."

    prof "Don't assume you're the only one."

    prof "College is an adjustment."

    MCname "{i}(Huh... that's surprisingly reassuring.){/i}"

prof "That's enough philosophy for one morning."

prof "Your syllabus and first assignment will be online tonight."

prof "Read them."

prof "Unlike most professors..."

prof "...I can tell when you didn't."

prof "Now I'm going to pass around a small quiz to evaluate your level of understanding."

prof "You have until the end of class to finish."

# MC receives his test
"Your professor hands you the test."

if mini_games_enabled:
    call english_comp_quiz1
else:
    "You skip the diagnostic quiz."


prof "See you Wednesday."

MCname "{i}(Well... that could've gone a lot worse.){/i}"

MCname "{i}(One class down. Only... a few hundred more to go.){/i}"

jump campus_after_class



###############################################
# AFTER CLASS — MINI FREE ROAM HUB
###############################################

label campus_after_class:

    scene campus_path with dissolve

    MCname "{i}(Class wasn’t bad… might as well look around before heading out.){/i}"
    MCname "{i}(Looks like a few people are still hanging around.){/i}"

    call screen hallway_free_roam
    return



###############################################
# FREE ROAM SCREEN — CLICK TO TALK
###############################################

screen hallway_free_roam:

    # Background hallway
    add "campus_hallway.webp"

    # Sienna & Jess together
    imagebutton:
        idle "sienna_jess_idle.webp"
        hover "sienna_jess_hover.webp"
        xpos 150
        ypos 300
        action Jump("fr_sienna_jess")

    # Norah
    imagebutton:
        idle "norah_idle.webp"
        hover "norah_hover.webp"
        xpos 600
        ypos 320
        action Jump("fr_norah")

    # Malik
    imagebutton:
        idle "Malik_idle.webp"
        hover "Malik_hover.webp"
        xpos 950
        ypos 310
        action Jump("fr_Malik")

    # Continue down hallway → Aubrey scene
    imagebutton:
        idle "hallway_arrow_idle.webp"
        hover "hallway_arrow_hover.webp"
        xpos 1200
        ypos 400
        action Jump("aubrey_hallway_scene")



###############################################
# SIENNA + JESS
# PART 1
###############################################

label fr_sienna_jess:

    $ talked_sj = True

    scene campus_hallway with dissolve
    play ambience "audio/ambience/campus_hallway.ogg" fadein 1.5

    show Sienna casual smirk at left
    show Jess casual smile at right


    Sienna "I'm telling you, that's absolutely cheating."

    "Jess laughs."

    Jess "It isn't cheating."

    Sienna "Bringing homemade cookies to recruit people into your sorority is bribery!!"

    Jess "It's hospitality."

    Sienna "It's sugar."

    Jess "People like sugar."

    Sienna "Exactly."

    "Jess shakes her head, trying not to smile."

    MCname "{i}(...Do I interrupt?){/i}"

    "Jess notices you first."
    "Jess smiles."

    Jess "Hey."

    "Sienna glances over."

    Sienna "Well, well, well."
    Sienna "Look what we have here!!!"

    MCname "Hello to you too, Sienna."

    Sienna "Hey, handsome."

    MCname "Does Professor Hart ever smile?"

    "Jess thinks for a second."

    Jess "I've seen it."

    Sienna "Liar."

    "Jess laughs."

    Jess "I have!"

    Sienna "That was probably indigestion."

    MCname "{i}(I can't help but chuckle.){/i}"

    MCname "She isn't that bad, tbh."

    Sienna "Oh, she's awful."

    Jess "She's exaggerating."

    Sienna "No, I'm being charitable."

    "Jess nudges Sienna with her shoulder."

    Jess "Ignore her."
    Jess "She enjoys scaring freshmen."

    Sienna "Correction."

    Sienna "I enjoy watching freshmen scare themselves."

    MCname "There's a difference?"

    Sienna "Huge difference."
    Sienna "I don't create the chaos."

    "Sienna grins."

    Sienna "I simply appreciate it."

    MCname "{i}(She's impossible to get a straight answer out of.){/i}"

    "Jess notices your expression."

    Jess "Don't worry."
    Jess "She's actually nicer than she pretends."

    "Sienna gasps dramatically."

    Sienna "Jess."
    Sienna "You're ruining my reputation."

    Jess "What reputation?"

    "Sienna places a hand over her heart."

    Sienna "You wound me, madam!!!"

    Jess "Debatable."

    Sienna "Intimidating."

    Jess "Debatable."

    Sienna "Mysterious."

    "Jess tilts her head."

    Jess "That one I'll allow."

    MCname "{i}(I can't help but laugh.){/i}"

    MCname "You two have known each other a while?"

    Jess "Since freshman orientation."

    Sienna "Longest two years of my life."

    "Jess smiles sweetly."

    Jess "Yet you still keep me around."

    Sienna "Someone has to stop you from feeding strangers."

    "Jess looks genuinely confused."

    Jess "Why is that a bad thing?"

    "Sienna points toward you."

    Sienna "See?"
    Sienna "She'd probably bake you cookies if you looked hungry."

    "Jess glances toward you."

    Jess "...Would that be weird?"

    MCname "Nope!!!"

    "Jess hides a smile."

    Jess "Good."

    "Sienna smirks."

    Sienna "You're too nice, Jess."

    "Jess quietly laughs."

    "A group of students rushes past, nearly clipping one another as they argue over which building their next lecture is in."
    "The three of you instinctively step aside."

    MCname "{i}(Campus somehow feels less overwhelming when you're standing with people instead of wandering around alone.){/i}"

    "Sienna notices you looking around."

    Sienna "I thought we moved past the lost puppy phase?"

    MCname "Trying to."
    MCname "This place is bigger than I expected."

    Jess "Everyone gets lost their first week."

    Sienna "Some people keep getting lost."

    "Jess smiles knowingly."

    Jess "You're talking about yourself."

    Sienna "Allegedly."

    Jess "You called me because you couldn't find the library."

    "Sienna scoffs."

    Sienna "Ugh, I call you one time and I never hear the end of it."

    Jess "Twas adorable though."

    MCname "That makes me feel better."

    Sienna "See?"
    Sienna "I'm inspirational."

    MCname "I don't think that's the word."

    "Sienna grins."

    Sienna "It's close enough."

    "A comfortable silence settles over the group as students continue filing through the hallway."

    Jess "So..."
    Jess "How's your first day really going?"

    menu:
        "Honestly? Better than I expected.":

            $ add_personality("Confident", 1)
            $ walkthrough("Confident +1")

            MCname "Honestly?"
            MCname "Better than I expected."
            MCname "I figured I'd spend the whole day embarrassing myself."

            Sienna "The day's still young."

            Jess "You really can't help yourself."

            Sienna "I prefer honesty."

            MCname "{i}(I laugh despite myself.){/i}"

            "Jess smiles."

            Jess "It's good you're settling in."

            Sienna "Tomorrow is when reality kicks in."

            MCname "Thanks..."
            MCname "...I think."

            $ mc_adjust_anxiety(-1)
            $ walkthrough("Anxiety -1")

            "Sienna crosses her arms."

            MCname "{i}(I can't help but smile.){/i}"

            jump fr_sienna_jess_part2



##########################################################
# SIENNA + JESS
# PART 2
##########################################################

label fr_sienna_jess_part2:

    "Jess looks down the hallway as another wave of students pours out of a nearby classroom."

    Jess "It's funny."

    MCname "What is?"

    Jess "This place feels enormous during your first week."
    Jess "Then one day you realize you keep seeing the same faces everywhere."

    Sienna "That's when you learn campus isn't actually that big."

    MCname "Or everyone just has the same schedule."

    "Sienna points at you."

    Sienna "See?"
    Sienna "He's adapting already."

    "Jess smiles."

    Jess "You'll settle in faster than you think."

    MCname "I hope so."

    "Sienna tilts her head."

    Sienna "So..."
    Sienna "Have you figured out what you're actually doing here?"

    MCname "Besides trying not to get lost?"

    Sienna "That doesn't count."

    MCname "I'm still figuring things out."
    MCname "I didn't exactly come in with my entire life planned."

    Jess "Honestly?"
    Jess "Most people don't."

    Sienna "Some pretend they do."

    "Jess glances toward her."

    Jess "You included."

    "Sienna places a hand against her chest."

    Sienna "Excuse me."
    Sienna "The nerve of her!!! I don't know why I put up with you."

    MCname "That's... actually true."

    "Sienna smiles proudly."

    "Jess giggles."

    Jess "Looking confident and having a plan aren't the same thing."

    Sienna "...You didn't have to expose me like that."

    "The three of you laugh."

    "A student rushes by carrying far too many textbooks."
    "Halfway down the hall, the stack slips from his arms, scattering books across the floor."

    "Without thinking, Jess takes a step forward."

    "Another student is already helping gather everything."
    "Jess relaxes."

    "Sienna notices."

    Sienna "You were about to help."

    Jess "He looked like he needed it."

    "Sienna smiles knowingly."

    Sienna "See?"
    Sienna "That's exactly what I was talking about."

    Jess "What?"

    Sienna "You physically cannot ignore someone that needs help."

    "Jess laughs softly."

    Jess "I don't think that's a bad thing."

    Sienna "It's not."
    Sienna "Just don't let people take advantage of it."

    "Jess's smile softens."

    Jess "I know."

    MCname "{i}(There's a lot more history between these two than they're letting on.){/i}"

    "A comfortable silence settles over the group."
    "Instead of feeling awkward..."
    "...it feels easy."

    Sienna "Alright."
    Sienna "Important question."

    MCname "Uh oh."

    "Jess laughs."

    Jess "You say that every time."

    Sienna "What's been your favorite part of today?"

    menu:
        "Meeting new people.":
            $ relationship_api.add_points("Jess", 1)
            $ walkthrough("Jess +1")
            $ relationship_api.add_points("Sienna", 1)
            $ walkthrough("Sienna +1")
            $ add_personality("Caring", 1)
            $ walkthrough("Caring +1")

            MCname "Honestly..."
            MCname "Meeting people."
            MCname "It's made the campus feel a lot less intimidating."

            "Jess smiles warmly."
            Jess "I'm glad."
            Jess "College's a lot more fun when you don't try to do everything alone."

            Sienna "Besides..."
            "Sienna smirks."
            Sienna "You seem decent."

            MCname "That's the nicest thing you've said to me."
            Sienna "Don't get used to it."

        "Surviving Professor Hart.":
            $ add_personality("Confident", 1)
            $ walkthrough("Confident +1")
            $ relationship_api.add_points("Sienna", 2)
            $ walkthrough("Sienna +2")

            MCname "Making it out of Hart's classroom alive."

            "Sienna laughs."
            "Jess shakes her head."

            Jess "You're both so dramatic."
            Sienna "Says the girl who looked terrified on her first day."

            "Jess smiles sheepishly."
            Jess "I was."

        "It's too early to decide.":
            $ add_personality("Selfish", 1)
            $ walkthrough("Selfish +1")
            $ relationship_api.add_points("Jess", 1)
            $ walkthrough("Jess +1")

            MCname "Ask me next week."
            MCname "I'm still processing everything."

            Jess "Fair answer."
            Sienna "Responsible answer."

            MCname "You sound disappointed."
            Sienna "A little."

            "Jess laughs."


    "Sienna glances toward the windows."

    Sienna "Speaking of surviving..."

    Sienna "We've got somewhere to be."

    "Jess checks the time on her phone."

    Jess "We're going to be late."

    Sienna "Technically."

    "Jess gives her a look."

    Sienna "Fine."

    "Sienna looks back at you."

    Sienna "One piece of free advice."

    MCname "Let's hear it."

    Sienna "Say yes to things."
    Sienna "Join a club."
    Sienna "Go to events."
    Sienna "Talk to people."
    Sienna "College gets really boring if all you do is go to class and go home."

    "Jess smiles."

    Jess "She's right."
    Jess "You'll make the best memories when you least expect them."

    MCname "I'll keep that in mind."

    "Sienna starts walking backward."

    Sienna "Good."
    Sienna "I'd hate for you to waste perfectly good tuition."

    MCname "{i}(I laugh despite myself.){/i}"

    "Jess shakes her head."

    Jess "Don't mind her."

    Sienna "You absolutely should mind me."

    Jess "Bye."

    MCname "See you both around."

    "Jess smiles."

    Jess "See you."

    "Sienna turns one last time before disappearing down the hallway."

    Sienna "Oh..."

    MCname "Yeah?"

    "Sienna grins."

    Sienna "Try not to look so lost tomorrow."

    MCname "No promises."

    "Sienna laughs quietly before continuing down the hall beside Jess."

    hide Sienna with dissolve
    hide Jess with dissolve

    MCname "{i}(They're... fun.){/i}"
    MCname "{i}(Completely different people... but somehow they balance each other out.){/i}"
    MCname "{i}(Something tells me today won't be the last time our paths cross.){/i}"

    call screen hallway_free_roam
    return



###############################################
# NORAH — FREE ROAM
###############################################

label fr_norah:

    $ talked_norah = True

    scene campus_hallway with dissolve

    MCname "{i}(...Damn, who is that???){/i}"

    MCname "{i}(...I don't know, but I'm about to find out.){/i}"

    MCname "Hey."

    Norah "Hey."

    MCname "You're in Hart's class."

    Norah "Yeah."

    MCname "I'm—"

    Norah "The new guy."

    "MCname laughs."
    MCname "That obvious?"

    show norah casual neutral
    Norah "You keep looking at the room numbers."

    "MCname instinctively glances toward one."

    show norah casual smirk
    Norah "Case in point."

    "MCname laughs."
    MCname "Okay... fair."

    show norah casual neutral
    Norah "Look, new guy... I'm kinda busy, so if you don't mind?"

    MCname "Yeah... sure."

    "Norah shakes her head."
    Norah "Animal shelter."

    MCname "{i}(...Wasn't expecting that.){/i}"

    MCname "Huh?"

    Norah "If you wanna help out, I volunteer at the local animal shelter on weekends."

    MCname "That's actually really cool of you."

    "Norah shrugs."
    Norah "I love animals and I'd be glad to help out if I can."

    "MCname smiles."
    MCname "That's... actually a pretty good reason."

    show norah casual soft
    MCname "{i}(I think that's the first time she's smiled.){/i}"

    # Freshman drops papers
    show norah casual neutral
    $ renpy.pause(0.2)

    "A freshman hurries past, accidentally dropping a folder. Papers scatter everywhere."
    "Before the student can react—"

    show norah casual kneel with dissolve
    "Norah is already kneeling, collecting pages."

    Freshman "Oh my gosh, thank you."

    show norah casual neutral
    Norah "Try holding it from the bottom."

    Freshman "Right. Thanks."

    "The student rushes away."
    "MCname watches."
    "Norah brushes dust from her hands."


    menu:

        "Compliment her kindness.":

            $ relationship_api.add_affection("Norah", 1)
            $ walkthrough("Norah +1")
            $ add_personality("Caring", 1)
            $ walkthrough("Caring +1")

            MCname "You're nicer than you let on."

            # show norah casual raisedbrow
            Norah "Who said I was trying to hide it?"

            "MCname laughs."
            MCname "Fair enough."

        "Tease her.":

            $ add_personality("Confident", 1)
            $ walkthrough("Confident +1")
            $ relationship_api.add_affection("Norah", 1)
            $ walkthrough("Norah +1")

            MCname "Careful."
            MCname "People might start thinking you're nice."

            show norah casual neutral
            Norah "That would ruin my image."

            "MCname laughs."

            $ renpy.pause(0.4)
            show norah casual smirk
            "A beat later, the corner of her mouth curls into a tiny smile."

        "Ask about the shelter.":

            $ relationship_api.add_affection("Norah", 3)
            $ walkthrough("Norah +3")

            MCname "What's it like?"

            show norah casual soft
            Norah "Loud."
            Norah "Messy."
            Norah "Worth it."

            MCname "Sounds like you enjoy it."

            Norah "I do."

    # Exit
    show norah casual neutral
    "Norah checks her phone."

    Norah "I should get going."

    MCname "Volunteer shift?"

    Norah "Tomorrow."

    show norah casual walk
    "Norah starts walking."

    $ renpy.pause(0.5)

    show norah casual back
    "After a few steps, she stops."

    Norah "Welcome to campus."

    MCname "Thanks."

    show norah casual back
    "She gives a small wave over her shoulder before disappearing into the crowd."

    hide norah with dissolve

    MCname "{i}(She's hard to read.){/i}"
    MCname "{i}(...But I don't think she's nearly as cold as she wants people to believe.){/i}"

    call screen hallway_free_roam
    return



#################################################
# Malik — FREE ROAM
#################################################

label fr_Malik:

    $ talked_Malik = True

    scene campus_hallway with dissolve

    show Malik grin at center

    MCname "{i}(Malik's leaning against one of the lockers, absentmindedly spinning a basketball on his finger.){/i}"
    MCname "{i}(He's somehow making standing in a hallway look like a scheduled activity.){/i}"

    "Before you can say anything—"

    Malik "There he is!"
    "Malik points dramatically."
    Malik "The man."
    Malik "The myth."
    Malik "The freshman."

    "MCname laughs."
    MCname "I was wondering when that title would stop following me."

    Malik "Give it..."
    "Malik pretends to check an invisible watch."
    Malik "Two weeks."
    Malik "Maybe three."

    MCname "Comforting."

    "Malik lets the basketball bounce once before catching it."

    Malik "So."
    Malik "Scale of one to ten."
    Malik "How lost are you?"

    menu:

        "Completely lost.":

            $ mc_adjust_anxiety(-1)
            $ walkthrough("Anxiety -1")

            MCname "Honestly?"
            MCname "Like an eight."

            "Malik nods seriously."
            Malik "Respect."
            Malik "Admitting it is step one."

        "I'm figuring it out.":

            $ add_personality("Confident", 1)
            $ walkthrough("Confident +1")

            MCname "I'm adapting."

            "Malik squints."
            Malik "Confident answer."
            "Malik grins."
            Malik "Suspiciously confident."

        "I've been pretending I know where I'm going.":

            $ add_personality("Selfish", 1)
            $ walkthrough("Selfish +1")

            MCname "I've mastered walking with purpose."
            MCname "People assume I belong."

            "Malik bursts out laughing."
            Malik "That's literally what I did."

    "Malik spins the basketball again."

    Malik "Little secret."
    "Malik leans closer."
    Malik "Nobody knows what they're doing."

    MCname "Really?"

    Malik "Upperclassmen just walk faster."

    "MCname laughs."

    Malik "That's the trick."
    Malik "Confidence."
    Malik "If you look like you belong..."
    "Malik shrugs."
    Malik "...people stop asking questions."

    MCname "{i}(He's got a point.){/i}"

    # Passing students
    Student "Hey Malik!"
    "Malik waves back."
    Malik "Hey!"

    "Thirty seconds later—"

    Malik "Yo, Tyler!"
    "Tyler gives him a fist bump without slowing down."

    MCname "Do you know everyone?"

    "Malik thinks."
    Malik "No."
    "Malik pauses."
    Malik "Just... a concerning percentage."

    "MCname laughs."

    MCname "How?"

    "Malik shrugs."
    Malik "Talk to people."
    Malik "Remember names."
    Malik "Don't be weird."

    "MCname raises an eyebrow."

    Malik "Okay..."
    "Malik grins."
    Malik "Be the fun kind of weird."

    "Both laugh."

    "Malik bounces the basketball again."

    Malik "Speaking of..."
    "Malik points toward you."
    Malik "You're my roommate."

    MCname "Guess you're stuck with me."

    "Malik sighs dramatically."
    Malik "Yeah."
    Malik "Housing really dropped the ball."

    MCname "You seem devastated."

    "Malik smiles."
    Malik "I'm coping."
    Malik "Barely."

    "They both laugh."

    Malik "Seriously though..."
    "Malik's tone softens."
    Malik "I'm glad they paired us."

    "MCname looks surprised."

    "Malik shrugs."
    Malik "Starting college's a lot easier when you've got somebody in your corner."

    "MCname smiles."
    MCname "Yeah."
    MCname "I appreciate that."

    "Malik nods."
    Malik "Besides..."
    "Malik smirks."
    Malik "If you're gonna embarrass yourself..."
    Malik "I'd rather have front-row seats."

    "MCname laughs."
    MCname "There it is."

    Malik "Had to end on brand."

    "Malik's phone buzzes."
    "Malik checks it."

    Malik "Crap."
    Malik "I've gotta run."

    "Malik starts walking backward."
    Malik "Don't disappear."

    MCname "I wasn't planning on it."

    "Malik points at you."
    Malik "Good."
    Malik "We've got a whole year of bad decisions ahead of us."

    "MCname laughs."
    MCname "That somehow sounded reassuring."

    "Malik grins."
    Malik "It was."
    Malik "See you back at the dorm."

    hide Malik with dissolve

    $ relationship_api.add_affection("Malik", 2)
    $ walkthrough("Malik +2")

    MCname "{i}(He's ridiculously easy to talk to.){/i}"
    MCname "{i}(If this is what college friendships are supposed to feel like... maybe I'm gonna be alright.){/i}"

    call screen hallway_free_roam
    return



#################################################
# AUBREY — FIRST APPEARANCE
#################################################

label aubrey_hallway_scene:

    scene campus_hallway with dissolve

    stop ambience fadeout 1.0

    MCname "{i}(I should probably head back before I get lost again.){/i}"

    play sound "footsteps.ogg"

    MCname "{i}(...Someone's coming.){/i}"

    show aubrey neutral at right with dissolve

    MCname "{i}She moves through the hallway like she has somewhere to be, but she's in no hurry to get there.{/i}"
    MCname "{i}Dark ink traces along one arm beneath the sleeve of her jacket—just enough to catch your eye before disappearing again.{/i}"

    "A couple of students step aside without being asked."
    "Aubrey barely seems to notice."
    "She passes you..."
    "..."
    "..."
    "Then stops."

    Aubrey "You're standing in front of the campus map."

    "MCname looks behind himself."
    MCname "...I am."

    Aubrey "People might actually need it."

    "MCname quickly steps aside."
    MCname "Right."
    MCname "Sorry."

    "Aubrey walks over, glances at the map for barely a second, then starts to leave again."

    MCname "{i}(That's it?){/i}"

    MCname "Wait."

    "Aubrey pauses."

    MCname "Can I ask you something?"

    "She turns just enough to acknowledge you."

    Aubrey "Depends."

    MCname "Is this campus really as confusing as it feels..."
    MCname "...or am I just having a rough first day?"

    "Aubrey studies you for a moment."

    Aubrey "First day?"

    "MCname nods."

    Aubrey "That explains it."

    MCname "Explains what?"

    Aubrey "You still stop every time you hear a bell."

    "MCname blinks."

    Aubrey "You'll stop doing that."

    "MCname laughs."
    MCname "You noticed?"

    Aubrey "I notice a lot."

    "A beat passes."

    MCname "So..."
    MCname "Any advice?"

    "Aubrey considers the question."

    Aubrey "Don't spend all your time trying to impress people."
    Aubrey "Most of them are too busy trying to impress each other."

    "MCname nods slowly."
    MCname "That's... actually good advice."

    show aubrey soft
    Aubrey "I know."

    "Her phone buzzes. She glances at the screen."

    Aubrey "I've got to go."

    MCname "Thanks."

    "Aubrey starts walking."

    "After a few steps—"

    Aubrey "Oh."

    MCname "Yeah?"

    "Aubrey looks back over her shoulder."

    Aubrey "The Arts Building?"

    MCname "What about it?"

    Aubrey "Third floor."

    "MCname frowns."
    MCname "I didn't ask where it was."

    Aubrey "No."
    Aubrey "But you were going to."

    "She walks away before you can answer."

    hide aubrey with dissolve

    MCname "{i}(...Okay.){/i}"
    MCname "{i}She somehow answered a question I hadn't asked yet.{/i}"
    MCname "{i}(I still don't know her name... but I have a feeling she won't stay a stranger for long.){/i}"

    jump end_of_day_transition


label end_of_day_transition:

    scene black with dissolve
    $ renpy.pause(0.5)

    "That night, campus finally starts to feel a little less overwhelming."

    "You survived your first day."

    scene dorm_night with dissolve
    $ renpy.pause(0.5)

    "And tomorrow?"

    "Your first real day."

    jump episode_2_start

    
    
            
    
    
    
    




