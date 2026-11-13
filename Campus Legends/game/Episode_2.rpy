default checked_kaia_out = False
default talked_Aubrey = False

label episode_2_start:

    scene dorm_morning
    with dissolve

    MCname "(Day two.)"
    MCname "(Still weird waking up somewhere that isn't home... but it's starting to feel a little less strange.)"

    #show Malik grin
    #with dissolve

    Malik "Morning good sir"

    MCname "Coffee"

    Malik "I got you bro there's a spot not to far from here that has fantastic coffee"

    MCname "Gonna shower first"

    Malik "Good idea man you're becoming a little pungent"

    MCname "Room already smelled a little pungent haha"

    Malik "Haha"

    #MC takes a shower

    #MC finshes shower and gets dressed

    MCname "Alright man lets go coffee is calling my name"

    #they make it to the diner and grab a table

    #waitress walks over to the table

    mystery "Hi! How are you doing today? Can we start with some coffee or water?"

    #Malik looks at the waitress

    Malik "Yeah let me..."
    Malik "Tiff?"

    Tiff "Oh, hey Malik!!!"

    Malik "I didnt know you worked here!!"

    Tiff "Yeah, i need the money to be honest."

    Malik "felt"
    Malik "Let me introduce my new bestie [MCname]"

    MCname "Hi"

    Tiff "You guys ready to order?"

    MCname "I'll start with a coffee"

    Tiff "How do you like your coffee?"

    MCname "2 creams 3 sugars please"

    #show her writing the order down

    Malik "I'll have mine black please"

    Tiff "Alright one black and one with 2 creams and 3 sugars coming up"

    #She walks away

    Malik "The breakfast platter is actually pretty bomb bro,you should give it a try."

    MCname "Once again i'll trust you on this one."

    #Tiff returns with the coffee

    Tiff "You boys ready to order?"

    MCname "Yeah i'll take the breakfast platter,2 eggs,grits,susage,pancakes"

    Tiff "OK, one breakfast platter and for you Malik"

    Malik "I'll have the same!!"

    Tiff "make that 2 platters, alright give me a few minutes ill have that right out to you guys"

    Malik "Thanks Tiff you're the bestest"

    #Tiff smirks at Malik

    Malik "Cute right?"

    menu:

        "Yeah, she's hot.\n{color=#00ff00}{i}[Tiff +1]{/i}{/color}":
            $ relationship_api.add_affection("Tiff", 1)
            $ walkthrough("Tiff +1")
            MCname "Yeah, she's definitely cute."
            Malik "Haha I knew you'd say that."

        "Nah, not my type.\n{color=#ff0000}{i}[Tiff -1]{/i}{/color}":
            $ relationship_api.add_affection("Tiff", -1)
            $ walkthrough("Tiff -1")
            MCname "She’s cool, but not really my type."
            Malik "Damn, tough crowd."

    Malik "She might be at the party tonight and as far as i know she's single as a pringle"

    MCname "Looking foward to this party actually i could use a distraction"

    Malik "Truer words have never been spoken!!"

    #Tiff returns with the food

    Tiff "Alright guys 2 platters and if you guys need anything just hollar"

    MCname "Looks pretty damn good"

    Malik "Trust me it is dude"

    #30 minutes later

    MCname "Damn that was good!!"

    Malik "Best breakfast spot in town if you ask me"

    #Tiff comes back to the table

    Tiff "You gents ready for the bill?"

    MCname "Absolutly and it was damn good"

    Malik "Compliments to the chef!!!"

    #Tiff walks away to grab the bill and she returns with it

    menu:

        # PLAYER PAYS
        "Pay the bill yourself.\n{color=#ff0000}{i}[-$20]{/i}{/color}\n{color=#00ff00}{i}[Tiff +1]{/i}{/color}":
            if money_api.spend(20):
                $ walkthrough("-$20")
                $ relationship_api.add_affection("Tiff", 1)
                $ walkthrough("Tiff +1")

                MCname "I got it."
                "I've been saving a little… I can cover this."
                Malik "Okay, big spender. Respect."
                Tiff "That's really sweet of you."

                # TIP MENU
                menu:
                    "Leave a $5 tip.\n{color=#ff0000}{i}[-$5]{/i}{/color}\n{color=#00ff00}{i}[Tiff +1]{/i}{/color}":
                        if money_api.spend(5):
                            $ walkthrough("-$5")
                            $ relationship_api.add_affection("Tiff", 1)
                            $ walkthrough("Tiff +1")
                            "I can spare five bucks."
                            Tiff "Thank you, sweetheart."

                    "Leave a $10 tip.\n{color=#ff0000}{i}[-$10]{/i}{/color}\n{color=#00ff00}{i}[Tiff +2]{/i}{/color}":
                        if money_api.spend(10):
                            $ walkthrough("-$10")
                            $ relationship_api.add_affection("Tiff", 2)
                            $ walkthrough("Tiff +2")
                            "Ten bucks isn't too bad."
                            Tiff "Wow… that's really generous."

                    "Leave a $20 tip.\n{color=#ff0000}{i}[-$20]{/i}{/color}\n{color=#00ff00}{i}[Tiff +5]{/i}{/color}":
                        if money_api.spend(20):
                            $ walkthrough("-$20")
                            $ relationship_api.add_affection("Tiff", 5)
                            $ walkthrough("Tiff +5")
                            "I've been saving… I can afford to go big."
                            Tiff "Oh my god… thank you! That means a lot."

                    "Skip the tip.":
                        "I should save my money."
                        Tiff "No worries, hun."

            else:
                MCname "…I don't have enough."
                Malik "Bro, you're tapped out?"
                Tiff "It's alright, he can cover it."
                Malik "I'll take care of it."

        # MALIK PAYS
        "Let Malik pay.":
            MCname "You got this one?"
            Malik "Yeah, I'll cover it."
            Tiff "Thanks, sweetheart."
            "Probably better to save my cash anyway."

    Malik "Shit i gotta bounce man,sorry to dine and dash on you"
    MCname "All good bro"
    Malik "BE ready by 8 ill meet you back at the dorm"
    MCname "10-4 copy boss"
    #Malik is shown leaving in a hurry
    "I should figure out what to do next… hit the gym or head to the library."

    menu:
        "Go to the gym.":
            "A workout wouldn't hurt. Might help clear my head."
            jump gym_scene

        "Go to the library.":
            "Probably smart to get ahead on some work."
            jump library_scene

label library_scene:
    "I spend some time in the library getting ahead on my coursework."
    "By the time I head back to the dorm, it's almost time to get ready for the party."
    jump pre_party_scene

label gym_scene:

    scene gym_day with dissolve

    #mc arrives at the gym

    #mc enters the front doors
    "{i}(Huh......){/i}"
    #Kaia is busy texting on her phone she doesnt hear the mc
    mystery "Brad, seriously?"
    pause 0.5
    mystery "You promised you'd call me back!"
    pause 0.5
    mystery "I can't believe you forgot our date!"
    pause 0.5
    mystery "Dont even try to turn this around on me, you're the one who forgot!"
    pause 0.5
    "She rubs her forehead"
    mystery "I'm not asking you for every second of the day."
    pause 0.5
    mystery "You know what Brad...I'M DONE ARGUING WITH YOU!"
    "{i}(damn...){/i}"
    #She hangs up the phone and slams it on the counter. She looks up and sees me standing there.
    mystery "WHAT"
    MCname "........."
    mystery "i'm sorry..."
    MCname "It's all good, people get frustrated sometimes."
    mystery "I assume you heard at least some of that.."
    MCname "Yeah, I did. It sounded like you were having a rough time."
    mystery "Yeah, I guess you could say that."
    mystery "Anyway...I'm Kaia, nice to meet you."
    MCname "Nice to meet you too Kaia, I'm [MCname]"
    MCname "I'm actually here to work out, but I can wait if you need a moment."
    Kaia "No, it's fine. Are you a student here?"
    MCname "Yeah, I am."
    Kaia "Do you have your student ID on you?"
    MCname "Yeah, I do."
    #hands her student ID
    Kaia "Thanks, I just need to put this in the system and then you can get started."
    Kaia "Okay one second...Alright, you're all set. The gym is open from 6 AM to 10 PM, and the locker rooms are just down the hall to your left."
    MCname "Thanks Kaia, I appreciate it."
    Kaia "Hold your horses for a sceond!!! If you want i can give you the grand tour of the gym, show you where everything is?"
    Kaia "Or if you want to just get started, we can skip the tour and you can just start working out?"
    menu:
        "Accept Kaia's offer to tour the gym {color=#00ff00}{i}[Kaia +2]{/i}{/color}":
            $ relationship_api.add_points("Kaia", 2)
            $ walkthrough("Kaia +2")
            MCname "Sure, a tour sounds great."
            Kaia "Awesome! Follow me, and I'll show you around."
            jump gym_tour

        "Decline for now":
            MCname "Maybe another time. I just want to get started with my workout."
            Kaia "No problem. The locker rooms are just down the hall to your left. Enjoy your workout!"
            jump gym_workout

label gym_tour:

    scene gym_tour with dissolve

    Kaia "Alright, let's start with the cardio area. We have treadmills, ellipticals, and stationary bikes here."
    #you guys walk past the cardio area and into the weightlifting section.
    Kaia "Next, we have the weightlifting section. We have free weights, benches, and machines for all your strength training needs."
    #you guys walk past the weightlifting section and into the stretching and yoga area.
    Kaia "Over here is the stretching and yoga area. We have mats and space for you to do your stretches or yoga routines."
    #you guys walk past the stretching and yoga area and into the locker rooms and showers.
    Kaia "Finally, we have the locker rooms and showers. You can change and freshen up after your workout. Just remember to bring your own towel and toiletries."
    Kaia "And i suggest some shower shoes as well, the floors can get a little slippery."
    Kaia "That's the grand tour of the gym! If you have any questions or need assistance, feel free to ask me or any of the staff."
    MCname "Thanks for the tour, Kaia. I appreciate it."
    Kaia "You're welcome! Enjoy your workout!!!"
    Kaia "Oh and you seem smart enough so i dont need to tell you this but just in case, please remember to wipe down the equipment after use and put weights back where they belong"
    Kaia "And for fucks sake no recording yourself for socials or toktoks, this is a gym not a social media studio."
    MCname "HAHA, got it. Thanks for the heads up."
    Kaia "Alright duty calls so i'll leave you to it."
    $ relationship_api.add_points("Kaia", 1)
    $ walkthrough("Kaia +1")

    jump gym_workout

label gym_workout:

    scene gym_workout with dissolve

    "{i}(Alright..time to hit the weights){/i}"

    #MC walks over to the weightlifting section and starts his workout routine. He focuses on his form and pushes himself to lift heavier weights. After a while, he takes a break and wipes down the equipment.
    "{i}(Damn i feel kinda outta shape..){/i}"
    mystery "Hey, you doing alright over there?"
    MCname "Yeah, I'm good. Just taking a break."
    mystery "You know, if you want, I can give you some tips on your form and technique. I used to be a personal trainer."
    MCname "i mean why not."
    #Kai walks over and introduces himself
    mystery "I'm Kai, and I used to be a personal trainer here."
    MCname "Nice to meet you, Kai. I'm [MCname]."
    Kai "Nice to meet you too, [MCname]. So bench today? you trying to max out or just get a good workout in?"
    MCname "Just trying to get a good workout in, but i wouldnt mind maxing out if i can."
    Kai "Alright, let's start with a warm-up set to get your muscles ready. Then we can move on to heavier weights. Remember to keep your back flat and your feet planted firmly on the ground."
    #the workout continues with Kai giving tips and encouragement. After a while, MC finishes his workout and thanks Kai for the help.
    #Kaia walks past
    menu:
        "Check her out {color=#00ff00}{i}[Kaia +1]{/i}{/color}":
            $ relationship_api.add_points("Kaia", 1)
            $ walkthrough("Kaia +1")
            $ checked_kaia_out = True
            jump Kaia_notice

        "Focus on your workout":
            "I should stay focused on my workout and not get distracted."
            jump gym_workout_end

label Kaia_notice:

    scene Kaia_notice with dissolve

    #Kaia notices you checking her out and gives you a playful smile. She walks over to you.
    #As she walks past she delivers a playful line
    Kaia "You know, staring at me won't make you stronger. But I appreciate the attention."
    #Kaia keeps walking
    Kai "Bro she's taken, you should probably focus on your workout."
    MCname "Yeah, i know man..."
    Kai "Just trying to be a good friend and look out for you."
    Kai "Brad is a bit of a douche canoe..."
    MCname "I can see that, but i dont know the whole story."
    Kai "Well, let's just say he doesn't treat Kaia the way she deserves. You should probably steer clear of him."
    MCname "Thanks for the heads up, Kai. I appreciate it."
    MCname "If it's the same Brad i meet earlier then its to late ,he already invited to a party tonight and i accepted."
    Kai "Figures he'd be trying to recruit you, we could use a few new brothers"
    MCname "Ahh so you're an Alpha?"
    Kai "Damn you say that like its a bad thing haha"
    MCname "Haha naw homie just teasing you, i know a few Alphas and they are all good people...well most of them anyway"
    Kai "Yeah, we have our ups and downs but we look out for each other."
    Kai "It's a brotherhood, and we take care of our own."
    "{i}(It does seem like a tight-knit group, maybe I should join them){/i}"

    jump gym_workout_end

label gym_workout_end:

    scene gym_day with dissolve

    "{i}(Alright, time to hit the showers and get ready for the party tonight.){/i}"
    "{i}(I should probably head back to the dorms and get cleaned up.){/i}"
    MCname "Thanks for the help, Kai. I appreciate it."
    Kai "No problem, [MCname]. It was great working out with you. See you around!"
    #Show mc taking a shower in the locker room
    "{i}(This shower is actually feeling pretty damn good, I could get used to this.){/i}"
    "{i}(Why can't our showers be like this?){/i}"
    #MC finishes showering and gets dressed

    #show mc walking past front desk
    Kai "Hey, [MCname]! How was your workout?"
    MCname "It was great!!"

    if checked_kaia_out:
        Kaia "Hey, [MCname]! I noticed you checking me out earlier. Just remember, I'm taken."
        MCname "Yeah, I know. I was just admiring your dedication to fitness."
        "Kaia blushes, trying to hide it with a quick glance away."
        Kaia "I'll catch you later. {i}…never noticed how cute he really is...{/i}"

    MCname "You going to the party tonight?"
    Kaia "Yeah, I might swing by for a bit. But I have to be up early tomorrow for a training session, so I won't stay too long."
    Kaia "I'll be there to support Brad, but I won't be staying for the whole thing."
    Kaia "Anyway, I should get BACK TO WORK . See you around, [MCname]!"
    jump pre_party_scene

label pre_party_scene:

    #MC geta text from Malik "Yo bro, you ready for the party tonight? It's gonna be lit!"
    MCname "I just finished up and I'm heading back to the dorms to get cleaned up and dressed. I'll be ready by 8."
    Malik "Sweet, see you then!"
    #MC walks back to the dorms
    Malik "Yoooo was good Broseph Stalin, get dressed and reasy to mingle like a Pringle!!!"
    MCname "Haha, you got it bro. I'll be ready by 8."
    #MC starts to get dressed
    "{i}(This should do the trick.){/i}"
    Malik "Damn bro, you clean up nice. I like the fit."
    MCname "Thanks, man. I appreciate it."
    Malik "I got us a few pre party drinks, so we can get the night started right."
    MCname "My man what you got?"
    Malik "I got us some whiskey, some vodka, and a few beers. What do you want to start with?"
    MCname "Lets take a few shots of whiskey and then head out,,i dont wanna be smashed before we get to the party haha."
    #they take a few shots of whiskey
    Malik "Yo man how about a friendly wager?"
    MCname "Why do i feel like this is a bad idea?"
    Malik "Naw man its just a friendly wager."
    MCname "Alright, what are we betting on?"
    Malik "Alright,if you can get a chicks number at the party, you win."
    Malik "Not to hard right?"
    MCname "I mean, i guess not. But what if i dont want to get a girls number?"
    Malik "Then you lose and you gotta do 10 shots of vodka."
    MCname "Damn bro, that is a steep price to pay."
    Malik "I know right, but it makes it more fun. So what do you say?"
    MCname "Alright, you're on. Let's see if I can get a girl's number at the party."

    jump rush_party_start

label rush_party_start:
    #MC and Malik arrive at the party, which is in full swing. The music is loud, people are dancing, and the atmosphere is electric. The party is filled with students from the campus, and everyone seems to be having a great time.
    #Shwo front of frat house with people drinking and talking outside.
    Malik "We have arrived at our destination!!"
    MCname "Damn this place is nice"
    Malik "Right"
    Malik "Well the world is your oyster so i'll see you inside."
    "{i}(Alright, lets see what i can get into.){/i}"
    #Brad spots the MC and signals for him to join him
    Brad "My man!!! glad you could make it!!"
    MCname "Seems like the party is in full swing already"
    Brad "Hell yeah dude go ahead inside and enjoy yourself"
    MCname "I think i....."
    Brad "Get this man a beer asap"
    #a frat bro hands the mc a beer
    Brad "Now you're set to go have fun bro"
    #Brad turns away and starts mingling before you can even respond
    "{i}(Well shit...i guess ill just head inside.){/i}"

    jump rush_party_free_roam

    ###############################################
    # RUSH PARTY — FREE ROAM HUB
    ###############################################

label rush_party_free_roam:

    scene party_main_room
    play music "party_mix.ogg"

    $ talked_sienna = False
    $ talked_jess = False
    $ talked_kaia = False
    $ talked_misty = False
    $ talked_kai = False
    $ talked_malik = False
    $ talked_Aubrey = False

label rush_party_hub:

    if talked_sienna and talked_jess and talked_kaia and talked_misty and talked_kai and talked_malik and talked_Aubrey:
        jump rush_party_finish

    menu:
        "Who do you want to talk to?"

        "Talk to Sienna" if not talked_sienna:
            jump party_sienna_scene

        "Talk to Jess" if not talked_jess:
            jump party_jess_scene

        "Talk to Kaia" if not talked_kaia:
            jump party_kaia_scene

        "Talk to Misty" if not talked_misty:
            jump party_misty_scene

        "Talk to Kai" if not talked_kai:
            jump party_kai_scene

        "Talk to Malik" if not talked_malik:
            jump party_malik_scene

        "Talk to Aubrey" if not talked_Aubrey and talked_sienna and talked_jess and talked_kaia and talked_misty and talked_kai and talked_malik:
            jump party_aubrey_scene

label party_sienna_scene:
    $ talked_sienna = True

    #MC notices Sienna sitting at a table drinking alone with her eyes observing the environment and walks up to her confidently

    MCname "Hey. What you doing sitting here all alone?"
    Sienna "Oh hey. I did my fair share of networking with all the important leaders and what not"
    Sienna "Now I'm just observing their behaviors. What kind of drinks they like... how they react to one another and the recruits"
    MCname "Damn you don't fuck around"
    Sienna "Listen. If I'm gonna join a sorority. I need to know what I'm getting into"
    Sienna "I don't want to just be in some club. I want to be somewhere I know I will belong and feel welcomed."
    MCname "Yeah. I feel that"
    Sienna "What about you?"

    #MC blushingly chuckles

    MCname "What you mean? What about me?"
    Sienna "What are you expecting out of joining the Kappas"
    MCname "{i}(Damn I haven't thought about that. Why do I wanna be a Kappa?){/i}"

    menu:
        "For the parties":
            jump mc_kappas_parties

        "Community outreach":
            jump mc_kappas_outreach

label mc_kappas_parties:
    MCname "I wanna join the Kappas for moments like these"
    MCname "Fun parties, networking, and you know the fine ladies is a bonus"

    $ add_personality("Selfish", 1)

    #MC winks flirtingly at Sienna

    $ relationship_api.add_affection("Sienna", -1)

    #Sienna folds her arms in disappointment

    Sienna "Parties are good for the social aspects and all, but it's also important to have meaningful reasoning that serves a purpose"
    Sienna "Malik isn't just VP because he's cool and popular. He's a great leader and is very charismatic"
    MCname "Damn you got me there. But for real though, I want to be a Kappa because I want to be more social overall"
    MCname "And not just with anyone, but with people I know who will get me where I wanna be and help me break down any obstacles in my way"

    #Sienna smiles impressed and playfully slaps MC on the shoulder

    $ relationship_api.add_trust("Sienna", 1)

    Sienna "Okay papi. I hear that."

    jump sienna_number_setup

label mc_kappas_outreach:
    MCname "I really love all the community outreach that comes with being a Kappa"
    Sienna "Oh for sure. That's one of the major reasons for me too"
    Sienna "People tend to only think about the partying and drinking stereotypes that comes with sororities and fraternities"
    Sienna "They never think about the toy drives and charity events"
    MCname "Exactly. I want to provide outreach to help get the word out for fundraising during charity campaigns"
    MCname "You know. Pass the message along for benefactors and to inspire future Kappas by showing them why it's important to make a difference"

    $ add_personality("Caring", 1)
    $ relationship_api.add_affection("Sienna", 1)

    Sienna "Si, si papi. Now you're speaking my language."

label sienna_number_setup:
    MCname "I like it when you say Papi like that"

    #Sienna looks away smiling blushingly

    Sienna "Well play your cards right and you could be hearing it more often"
    MCname "Damn. Okay okay. I see how it is"
    Sienna "Yeah? And what is it that you see?"
    Sienna "I'm just telling it like it is"
    MCname "Well I see a smart, beautiful queen"
    MCname "And I respect that. You laying your cards out like that"

    #Sienna lets out a light chuckle

    Sienna "You definitely know how to make a compliment"
    MCname "I'm just tryna play the hand that I'm dealt with"
    Sienna "And I appreciate that you're making an initiative and listening"
    Sienna "A lot of dudes don't do that"
    MCname "I'm not like those dudes"
    Sienna "I'm learning that now"

    #MC makes a big smile

    MCname "{i}(We seem to be hitting it off. I should probably ask for her number right?){/i}"

    menu:
        "Ask confidently":
            jump mc_sienna_number_confident

        "Ask shyly":
            jump mc_sienna_number_shy

        "Ask carefully":
            jump mc_sienna_number_careful

label mc_sienna_number_confident:
    MCname "Since we're playing our cards and all that, how about I go all in"

    #Sienna cackles

    Sienna "And what do you mean by that?"
    MCname "Give me your number and you can find out"
    Sienna "Damn! I see, I see"
    Sienna "Not gonna lie, I'm loving the confidence"

    $ add_personality("Confident", 1)

    MCname "Thank you. thank you"

    #Sienna sucks her teeth flirtingly

    Sienna "Well? Are you gonna bask in the moment or are you going to give me your phone?"

    #MC hands his phone to Sienna and she grabs it, puts her number in and hands it back

    Sienna "Now don't be texting me at 2 am talking bout, you up?"

    #MC chuckles

    MCname "Nah I won't. I'm not like that"
    Sienna "Yeah we'll see about that"
    MCname "I swear I'm not. For real"
    Sienna "I know I'm messing with you"
    MCname "Cool. Cool"
    Sienna "Well I gotta be going"
    MCname "See you"
    Sienna "You better call me"
    MCname "Don't worry I will"
    Sienna "Yeah alright"

    #Sienna walks away slowly

    jump rush_party_hub

label mc_sienna_number_shy:
    MCname "So um I was wondering...since we're getting to know each other and all"
    Sienna "Yeah? What are you wondering in that brain of yours?"
    MCname "What if I um, had a way to um, get to know you more"
    Sienna "Ay dios mio! Are you trying to ask for my number?"
    MCname "Mayyybe?"

    #Sienna chuckles lightly

    MCname "Was it that obvious?"
    Sienna "Well you look like you're about to pass out sweating"
    Sienna "Am I making you nervous?"
    MCname "Little bit, little bit. Not gonna lie"
    Sienna "Awww that's cute"
    MCname "Cute! I'm not tryna be cute"
    Sienna "Well too bad. I's too damn late"

    $ relationship_api.add_affection("Sienna", 1)

    #MC laughs

    Sienna "Don't worry, it's a good thing"

    #Sienna pulls her hand out and MC hands her his phone, she puts her number in and hands it back

    Sienna "You better call me"
    MCname "I will. I will. I promise"
    Sienna "Okay cool"
    Sienna "And don't be too shy. I don't bite"

    #Sienna walks away slowly

    jump rush_party_hub

label mc_sienna_number_careful:
    MCname "I have a question. If you don't mind me asking."
    Sienna "Yeah sure. What's up?"
    MCname "I was wondering if I could have your number?"

    #Sienna giggles flirtingly

    Sienna "Well I can't say I'm surprised that's what you asked"
    Sienna "But I do respect that you were all polite about it"

    $ relationship_api.add_affection("Sienna", 1)

    MCname "I wanted to ask in a way that made you feel relaxed and comfortable"
    Sienna "Damn. Look at you being a gentleman"
    MCname "I am a man of many honors and I will always respect a queen"
    Sienna "Okay you don't need to say all of that. I was already convinced"
    MCname "I'm just speaking facts"
    Sienna "Yeah okay. Give me your phone"

    #MC hands his phone to Sienna and she grabs it, puts her number in and hands it back

    Sienna "Here you go lover boy"
    MCname "Appreciate it"
    Sienna "I appreciate you being so respectful"
    MCname "Of course. I couldn't imagine ever disrespecting you"

    #Sienna gazes down shyly

    $ relationship_api.add_points("Sienna", 1)

    Sienna "Alright I gotta go. A girl needs her beauty sleep"
    MCname "Goodnight Sienna"
    Sienna "Buenos noches papi"

    #Sienna walks away slowly

    jump rush_party_hub

label party_jess_scene:

    $ talked_jess = True
    MCname "There you are!!"
    Jess "Hey. enjoying the party?"
    MCname "Yeah, its been interesting"
    Jess "Just interesting?"
    #A loud chug chug chug rings through the house
    MCname "....See interesting"
    Jess "Hahaha and they're just getting started"
    MCname "I think i'll stay back here with you"
    Jess "Haha no no you need to have fun."
    MCname "What about you? why are you hiding?"
    Jess "Not hiding, this is a tactical positioning"
    MCname "So your camping?"
    #Jess laughs hysterically
    Jess "Haha Gotta get my chopper gunner"
    MCname "Ohhh shit we have a gamer!!!"
    Jess "Guilty!! been playing Modern Gunplay for a long time!!"
    MCname "Any good?"
    Jess "Better than you"
    MCname "Woooow, its like that?"
    Jess "Damn right it is!!"
    menu:
        "Challenge her to a 1v1 {color=#00ff00}{i}[Jess +3]{/i}{/color}":
            $ relationship_api.add_points("Jess", 3)
            $ walkthrough("Jess +3")
            MCname "1 v 1 me bro!!!"
            #Jess laughs out loud again
            Jess "Give me your number we'll set it up noob"
            #MC puts his number in her phone
            MCname "When i 360 no scope you dont cry to Malik"
            Jess "...."
            MCname "What no more trahtalk?"
            Jess "No...i was thinkig, how about we up the stakes some"
            MCname "Do tell do tell"
            Jess "Loser has to do whatever challenge the winner gives them"
            "{i}(She is way to confident this seems like a trap...){/i}"
            MCname "You're on girlie!!!"

        "Leave it alone":
            MCname "Alright im gonna go do my rounds"
            Jess "Ok, ill talk to you later"

    jump rush_party_hub

label party_kaia_scene:
    $ talked_kaia = True
    #Kaia is sitting all alone on the couch when a few feet in front of her Brad is laughing it up with a frat bro
    #MC notices her alone and grabs her a drink ,then he approches
    MCname "Hey,i brought you a party favor."
    #Kaia looks up from her phone suprised and disappointed
    Kaia "...Thanks"
    MCname "You look like you're having the time of your life."
    Kaia "Oh, absolutely. Best night ever..."
    MCname "That good huh?"
    Kaia "I'm fine...."
    MCname "Didn't say you weren't"
    #She looks at him, slightly surprised. Most people would either push her to explain or pretend not to notice.
    Kaia "You're learning when to keep your mouth shut. That's a good quality."
    MCname "I'll put it on my résumé."
    #Kaia laughs despite herself
    #Brad starts talking and laughing with a girl that joined conversation
    "{i}(Brad is such an idiot....){/i}"
    MCname "Hey i was wondering is the gym open on Sunday?"
    Kaia "Yup!! open 7 days a week"
    MCname "Good because i really need to work on my cardio"
    Kaia "I usaully run a few miles every other day to get my cardio in"
    MCname "Sheesh Kaia a few miles??"
    #Kaia giggles
    Kaia "Yup, light work!!"
    "{i}(She is on great shape....){/i}"
    #The girl hugs Brad and lingers and Kaia scowls at the sight
    "{i}(Shit i better so something....){/i}"
    MCname "HEY BRAD"
    #Brad turns towards you guys and walks over
    Brad "There you are. Been looking all over for you"
    Kaia "Really? That's funny. I've been sitting in the same spot for twenty minutes."
    Brad "Kaia, come on. dont start this shit again..im working the room"
    Kaia "You're doing a great job. Especially with the girls you've been working"
    #You feel the tension rising
    Brad "Can we not do this here?"
    Kaia "You mean can I stop embarrassing you in front of your brothers?"
    Brad "I mean, can you stop turning everything into a fucking problem?"
    #That hits harder than he intended. Kaia goes quiet.
    #Brad notices the MC watching
    Brad "What? You got something to say, freshman?"

    menu:
        "Stand up for her {color=#00ff00}{i}[+4 Kaia]{/i}{/color}":
            $ relationship_api.add_points("Kaia", 4)
            $ walkthrough("Kaia +4")
            #MC STANDS UP
            MCname "Yeah actually i do"
            Brad "What motherfucker"
            "{i}(dont beat this dudes ass....){/i}"
            #Malik comes over and steps between us
            Malik "Hey hey hey guys lets chill"
            MCname "......"
            #Malik drags brad away
            Kaia "You shouldn't have done that...but i appreciate it"
            MCname "He was being a douche canoe"
            Kaia "You know what..since you seem to have all this pent up energy, how about you join me on one of my runs?"
            MCname "Yeah i'd like that"
            #a genuine smile from kaia
            jump kaia_convo_end

        "Give her an out {color=#00ff00}{i}[+3 Kaia]{/i}{/color}":
            $ relationship_api.add_points("Kaia", 3)
            $ walkthrough("Kaia +3")
            MCname "Kaia didn't you say you wanted to show me where they keep the good drinks "
            #She catches on immediately.
            Kaia "I did, actually. Brad, entertain your guests."
            #You walk away together, leaving Brad standing there.
            #Once you're out of earshot, she exhales.
            Kaia "Thanks. I didn't need you to fight my battles. I just needed a reason to get away from him."
            MCname "All in a days service madam"
            jump kaia_convo_end

        "Keep it light {color=#00ff00}{i}[+2 Kaia]{/i}{/color}":
            $ relationship_api.add_points("Kaia", 2)
            $ walkthrough("Kaia +2")
            MCname "Nothing, man. Just trying to figure out if the party president gets paid by the hour."
            #Malik, listening nearby, snorts into his drink
            #Brad rolls his eyes and leaves to deal with another group.
            Kaia "You're an idiot."
            MCname "But a charming idiot"
            Kaia "Let's not get ahead of ourselves."
            jump kaia_convo_end

        "Stay out of it":
            jump kaia_brad_argument

label kaia_brad_argument:
    Kaia "WTF IS YOUR PROBLEM BRAD,LEAVE HIM ALONE"
    Brad "Now you're sticking up for this asshole"
    Kaia "He said nothing to you.."
    Brad "why are sitting with him then?"
    Kaia "FUCKIN UNBELIEVABLE..YOU'RE MAD BECAUSE HE IS TALKING TO ME WHEN YOU HAVE THIS BITCH ALL OVER YOU"
    #Kaia gets up extremly frustarated
    Kaia "IM DONE, GO FUCK YOURSELF, DONT BOTHER LOOKING FOR ME"
    #kaia stomps away towards the balcony
    jump kaia_convo_end

label kaia_convo_end:
    #you go to the balcony to check on kaia
    #she doesnt turn but she hears you coming
    Kaia "You know what's funny?"
    MCname "Clowns?"
    #KAIA turns towards the mc with a smirk on her face trying to fight a laugh
    Kaia "Not funny"
    MCname "Thats not what that smile is saying"
    Kaia "Ok maybe a little."
    Kaia "But seriously"
    Kaia "When we first started dating, he used to make time for me. Didn't matter what he had going on. He'd show up just to see me for five minutes."
    MCname "And now?"
    Kaia "Now I have to book an appointment."
    "She laughs, but there's no real humor behind it."
    Kaia "Everyone thinks we're this perfect couple. Brad, the big man on campus, and his gorgeous girlfriend. Must be nice, right?"
    MCname "You know what,Humility has always been your strongest suit, Kaia."
    "kaia giggles"
    MCname "But seriously is that what you think?"
    Kaia "I think I'm getting pretty good at pretending."

    menu:
        "You deserve someone who actually shows up for you.\n{color=#00ff00}{i}[Kaia Romance +1]{/i}{/color}":

            MCname "You know, you deserve someone who actually shows up for you."
            $ relationship_api.add_points("Kaia", 1)
            $ walkthrough("Kaia Romance +1")
            Kaia "..."
            Kaia "Are you flirting with me?"
            MCname "Would it be a problem if I was?"
            Kaia "You know I'm taken, right?"
            MCname "Yeah. I'm aware."
            Kaia "Then you should probably be careful with what you say."
            MCname "Just stating the obvious. Doesn't mean I'm expecting anything."
            Kaia "Good. Because my relationship is complicated enough without some freshman trying to swoop in."
            MCname "Freshman? Damn. I thought we were having a moment."
            Kaia "*laughs softly* You're unbelievable."
            "For the first time tonight, Kaia looks genuinely amused."
            Kaia "Now, if you'll excuse me, I should probably check on my boyfriend."
            "The way she says 'boyfriend' makes it sound more like an obligation than a term of endearment."

        "Sounds exhausting, having to pretend everything's perfect.\n{color=#00ff00}{i}[Kaia Trust +1]{/i}{/color}":
            MCname "Honestly? Sounds exhausting, having to pretend everything's perfect all the time."
            $ relationship_api.add_points("Kaia", 1)
            $ walkthrough("Kaia Trust +1")
            Kaia "*sighs* You have no idea."
            MCname "You don't have to tell me anything. Just figured you could use someone who'd listen."
            Kaia "That's the thing. Everyone wants to know what's going on, but nobody actually wants to hear the answer."
            MCname "Well, I'm listening."
            "Kaia studies you for a moment, as if trying to decide whether she believes you."
            Kaia "Thanks. I mean that."
            "Her expression softens before she glances back toward the party."
            Kaia "Don't make me regret saying that, okay?"
            MCname "Wouldn't dream of it."

        "Maybe you two just need to talk honestly.\n{color=#00ff00}{i}[Kaia Trust +1]{/i}{/color}":

            MCname "Maybe you two just need to have an honest conversation."

            $ relationship_api.add_points("Kaia", 1)
            $ walkthrough("Kaia Trust +1")
            Kaia "Maybe."
            Kaia "Though talking only works when both people actually want to listen."
            MCname "Fair point."
            Kaia "Besides, it's not like I haven't tried."
            MCname "Then it's on him to meet you halfway."
            "Kaia gives you a thoughtful look."
            Kaia "You know, most guys would've used this opportunity to tell me what a piece of shit Brad is."
            MCname "I'm not dating him. I don't know the whole story."
            Kaia "Exactly."
            "She gives you a small, appreciative smile."
            Kaia "That's actually pretty refreshing."

    jump rush_party_hub

label party_misty_scene:

    $ talked_misty = True

    # MC notices Misty hanging outside while exploring the party.

    "{i}(Wow... she's kinda hot.){/i}"
    "{i}(Maybe I should go talk to her.){/i}"
    "{i}(Looks like she could use a drink... so could I.){/i}"

    # MC grabs two drinks and takes a sip to calm his nerves.

    MCname "Hey, I'm [MCname]. Mind if I join you?"

    Misty "If you must. Trying to get away from the noise too?"

    MCname "Yeah, it can be kind of a lot sometimes. Not a fan of the loud yourself?"

    Misty "Nah, I love the music, but I also love being able to hear another day."

    Misty "And the night air smells better than whatever is going on in there."

    # MC and Misty laugh.

    menu:

        "Offer her a drink {color=#00ff00}{i}[Misty +2]{/i}{/color}":
            $ relationship_api.add_points("Misty", 2)
            $ walkthrough("Misty +2")
            MCname "Here, I brought you something."
            Misty "Oh? How thoughtful. Thanks."
            Misty "So, what brings you to the party?"
            MCname "Just trying to meet some new people and have a good time. How about you?"
            Misty "Same here. It's always nice to get out and socialize a bit."
            MCname "Definitely. So, what do you like to do for fun?"
            Misty "What a curious question."
            Misty "Well, I enjoy moonlit nights, taking long walks on the beach, knitting, and unicorns."
            Misty "In fact, I once took a seaside stroll on a moonlit night and discovered a unicorn."
            Misty "I proceeded to stab it in the throat with a crochet needle."
            Misty "I am a woman of refined, yet simple tastes."
            MCname "........."
            MCname "I'm just trying to figure out if you're messing with me."
            Misty "Would you prefer that I was?"
            MCname "Honestly? I'm not sure."
            Misty "Good. Uncertainty keeps life interesting."
            MCname "So, what's your story?"
            Misty "My story? How much time do you have?"
            MCname "Depends. Is it going to involve more dead unicorns?"
            Misty "Only if you're lucky."
            MCname "I'll keep that in mind."
            Misty "I'm just a girl trying to survive college, avoid unnecessary human interaction, and occasionally remind people that life is meaningless."
            MCname "Wow. And here I thought I was having a good night."
            Misty "Oh, don't worry. You're doing great. You're still smiling."
            MCname "I think that's just nervousness."
            Misty "Same thing, really."
            MCname "You always this cheerful?"
            Misty "Only on special occasions."
            MCname "And what's so special about tonight?"
            Misty "I haven't decided yet."
            # Misty takes a sip of her drink.
            Misty "So, you're new around here?"
            MCname "That obvious?"
            Misty "A little. You have that look."
            MCname "What look?"
            Misty "The 'I have absolutely no idea what I'm doing here' look."
            MCname "Damn. Is it really that bad?"
            Misty "Don't worry. Most people here are pretending they know what they're doing."
            MCname "That's reassuring."
            Misty "Welcome to college."
            # Misty glances toward the party.
            Misty "Well, I should probably head back in before someone starts looking for me."
            MCname "You don't seem particularly eager."
            Misty "I'm not. But disappearing for too long tends to make people ask questions."
            MCname "Fair enough."
            Misty "It was nice meeting you, [MCname]."
            MCname "You too, Misty."
            Misty "Try not to have too much fun in there. It would ruin your reputation."
            MCname "I'll do my best."
            # Misty heads back toward the party.
            "{i}(Okay... she's definitely an interesting one.){/i}"
            "{i}(Not exactly what I expected, but I think I like her.){/i}"

        "Just introduce yourself":

            MCname "I figured I'd come say hello. You looked like you could use some company."

            Misty "That's either very thoughtful or a terrible read of the situation."

            MCname "I'll let you decide."

            Misty "How generous of you."

            MCname "I'm [MCname], by the way."

            Misty "Misty."

            MCname "Nice to meet you."

            Misty "We'll see."

    jump rush_party_hub

label party_kai_scene:
    $ talked_kai = True

    #You spot Kai and Malik chatting
    Malik "Bro, welcome to your first Alpha party!!"
    MCname "You guys always throw parties like this?"
    Malik "Nah. Sometimes we throw bigger ones."
    MCname "Of course you do."
    "Malik laughs and nods toward the kitchen"
    Malik "I'm gonna grab us something to drink. Don't get kidnapped by a pledge challenge while I'm gone."
    MCname "Roger that."
    "Malik disappears into the crowd. As the MC looks around, someone suddenly claps him on the shoulder"
    Kai "BRO!"
    "The MC turns to find Kai grinning at him"
    MCname "Kai? The hell are you doing here?"
    Kai "Living my best life!!!"
    Kai "Last time I saw you, you were trying to turn yourself into a Greek statue on the bench press."
    MCname "Pretty sure you were the one giving me unsolicited coaching."
    Kai "And look at you now. Out here living your best life. Clearly, my wisdom changed you."
    MCname "Yeah, I'm thinking of getting your face tattooed on my chest."
    Kai "Make sure you get my good side."
    "You both laugh"
    Kai "So, you came to check out the Alphas?"
    MCname "Brad invited me. Figured I'd see what the hype was about."
    Kai "Brad invited you? Shit, that's a pretty good sign."
    MCname "Meaning?"
    Kai "Meaning our fearless president doesn't invite just anybody to these things. Or maybe he just needs more bodies to make the party look good."
    MCname "There it is. Knew you couldn't stay serious for more than five seconds."
    Kai "Serious is for exams and funerals, bro. Everything else is negotiable."
    Kai "Come on. Since you're here, I'm officially making you my responsibility tonight."
    MCname "Should I be worried?"
    Kai "Abo-fuckin-lutly"
    "Kai leads the MC toward a table where a group of brothers and rush candidates are gathered around a beer-pong setup. A few guys are shouting at a particularly competitive match"
    Kai "Gentlemen! I found us another victim."
    MCname "Victim? I thought we were friends."
    Kai "We are. That's why I'm giving you the opportunity to embarrass yourself in front of everybody I know."
    MCname "That's touching, man."
    Kai "I know right"
    "A tall pledge with a backward cap turns toward you"
    Ace "You playing or just here to admire the table?"
    MCname "Depends. You guys any good?"
    "The group erupts in laughter"
    Kai "OH! Gym bro came with some heat!"
    Ace "Talk is cheap, freshman."
    Kai "He's got a point. Let's see if those muscles come with any hand-eye coordination."
    "Kai grabs a ping-pong ball and tosses it to the MC"
    Kai "Your call, bro. You wanna put these clowns in their place, or you wanna take the scenic route and enjoy the party?"
    MCname "Let's do this!!"
    #show them winning the game
    "After the game, you and Kai step away from the table. The music is still pounding, and a couple of Alphas are arguing over who cheated during the last round."
    MCname "So, is every night with the Alphas this fun?"
    Kai "Nah. Sometimes it's better."
    MCname "Comforting."
    Kai "Hey, you wanted to see what Alpha was about. This is the authentic experience."
    MCname "I thought the authentic experience involved brotherhood, academic excellence, and personal growth."
    Kai "Yeah, we do all that shit, too."
    MCname "Sure you do."
    Kai "I'm serious, bro! We have standards....kinda"
    MCname "And beer pong?"
    Kai "Beer pong builds character."
    "You both laugh as Kai grabs a drink from a nearby cooler."
    Kai "For real, though. Being an Alpha's been one of the best decisions I've made here."
    MCname "Yeah? What makes it so good?"
    Kai "It's the people, man. You find your crew. Guys who'll have your back when shit gets rough, call you out when you're being an idiot, and still show up when you need them."
    MCname "Sounds like you got lucky with your brothers."
    Kai "Maybe. Or maybe I just know a good thing when I see it."
    "He takes a sip, glancing toward the living room where a couple of his fraternity brothers are hyping up another game."
    Kai "Don't get me wrong. The parties are a nice bonus. But when college gets stressful, having people in your corner makes a difference."
    MCname "Didn't know you had such a sentimental side."
    Kai "Whoa, whoa. Keep that shit between us. I've got a reputation as a dumbass to maintain."
    MCname "Your secret's safe with me."
    "You both laugh."
    Kai "Speaking of which, you thinking about joining Alpha yourself?"
    MCname "Still figuring things out."
    Kai "Fair enough. Just don't choose a house because somebody tells you it's the place to be. Find people you actually fuck with."
    MCname "Fuckin Confucius over here."
    Kai "To meet girl in park is good but to park meat in girl is better."
    "You both laugh"
    "Kai bumps his fist against yours."
    Kai "Anyway, enough of this emotional bullshit. Come on. There's a party going on, and I know at least three people here who need to get their asses kicked at beer pong."
    MCname "You go ahead man i'll holla at you bro."

    jump rush_party_hub

label party_malik_scene:
    $ talked_malik = True
    "You spot Malik near the kitchen, standing beside a table covered in drinks. He's staring suspiciously at a plastic cup."
    # Scene 1 — The drink situation
    "You spot Malik near the kitchen, standing beside a table covered in drinks. He's staring suspiciously at a plastic cup."
    Malik "Bro, we got a problem."
    MCname "What'd you do?"
    Malik "Why do you automatically assume I did something?"
    MCname "Because I know you."
    Malik "Damn. We've been roommates for two days and you're already judging me."
    MCname "So what's the problem?"
    Malik "I put my drink down for literally ten seconds, and now I don't know which cup is mine."
    "You look at the table. There are about twenty identical red cups."
    MCname "Tragic. Should we call campus security?"
    Malik "I'm being serious, man. One of these could belong to a stranger."
    MCname "God forbid."
    Malik "Exactly! I don't know where that dude's mouth has been."
    MCname "Malik, 19 of those belong to a stranger."
    MCname "Your odds kinda suck."
    MCname "You might wanna emotionally prepare yourself."
    "Malik shakes his head and points at you."
    Malik "See, this is why I need you around. You keep me grounded."
    MCname "I'm pretty sure I'm making you worse."
    Malik "Same thing."
    "You both laugh."
    "Malik turns back to the table, studying the cups like he's trying to crack a murder case."
    Malik "All right. Let's think about this logically."
    MCname "Oh, good. We're doomed."
    Malik "I remember putting it down right here."
    "He points to the table."
    Malik "Then somebody must've moved it."
    MCname "Or—and hear me out—you forgot which cup you picked up."
    Malik "That is not a theory I'm willing to entertain."
    MCname "Of course not."
    "Malik picks up one of the cups and gives it a cautious sniff."
    MCname "Bro. What the hell are you doing?"
    Malik "Checking."
    MCname "Checking what? The cup's criminal record?"
    Malik "I'm trying to see if it smells familiar."
    MCname "You think your drink has a signature scent?"
    Malik "You got a better idea?"
    MCname "Yeah. Get another drink."
    Malik "And let whoever stole my cup win? Absolutely not."
    MCname "Nobody stole your damn cup!"
    Malik "You don't know that."
    "He puts the cup down and starts examining the others."
    MCname "I'm gonna leave you to it before this turns into a full investigation."
    Malik "Fine. You check the kitchen. I'll look around the living room."
    MCname "We're splitting up over a red Solo cup?"
    Malik "It's not about the cup anymore. It's about principle."
    MCname "Right. The principle of being an idiot."
    Malik "Keep talking, and you're sleeping on the floor tonight."
    MCname "You can't kick me out of my own bed."
    Malik "Watch me."
    "Malik marches toward the living room, leaving you by the kitchen counter."
    "You glance behind a stack of paper plates sitting beside a half-empty bowl of chips."
    "There's a red Solo cup tucked right behind them."
    MCname "..."
    "You pick it up and inspect it."
    MCname "No fucking way."
    "Malik reappears from the living room, looking even more frustrated."
    Malik "Anything?"
    MCname "I think I found your missing suspect."
    "You hold up the cup."
    "Malik freezes."
    Malik "..."
    MCname "Wallet, phone, keys. But somehow you forgot the one thing you came into this kitchen holding."
    Malik "Okay, in my defense—"
    MCname "Oh, this should be good."
    Malik "I put it down."
    MCname "Incredible detective work."
    Malik "Shut up."
    MCname "You spent ten minutes investigating cups when yours was sitting three feet away from you."

    Malik "I was checking the other possibilities first."
    MCname "You smelled a stranger's drink, Malik."
    Malik "That is classified information."
    MCname "I'm telling everybody."
    Malik "I'm changing the Wi-Fi password."
    MCname "YOU DON'T EVEN KNOW HOW!"
    "You both burst out laughing."
    Malik "I swear to God, living with you is gonna be a nightmare."
    MCname "You love me, man."
    Malik "Unfortunately."
    "He snatches the cup from your hand and takes a suspicious look inside."
    MCname "Now what?"
    Malik "Now I need a new drink. I've lost trust in this one."
    MCname "YOU JUST FOUND IT!"
    Malik "Yeah, but where's it been?"
    "You stare at him for a moment before bursting out laughing again."
    MCname "You're unbelievable, bro."
    Malik "And yet, you're stuck with me."
    "He throws an arm around your shoulder and steers you back into the party, still holding his supposedly suspicious cup."
    Malik "I'm gonna go sit down and guard my drink...."
    MCname "Please. For the sake of everyone here."

    jump rush_party_hub

label party_aubrey_scene:
    $ talked_Aubrey = True

    ##############################################
    # AUBREY & TIFF - OPERATION FIREWORKS
    ##############################################

label aubrey_tiff_interaction:

    # Rush party free roam encounter
    scene

    # MC notices a crowd gathering around Aubrey and Tiff.

    MCname "Aubrey? Tiff? What's going on?"

    Aubrey "Well, well. Look who decided to join the fun."

    Aubrey "Hey, handsome. Wanna cause a little trouble?"

    Tiff "Oh, thank God you're here. We need more people if this is going to work."

    MCname "That sounds reassuring."

    MCname "What exactly are you two planning?"

    # Aubrey turns back toward the small crowd.

    Aubrey "Okay, where was I?"

    Tiff "You were explaining how we're about to make tonight legendary."

    Aubrey "Right."

    Aubrey "So, here's the plan. There's a building on the other side of campus with a pretty decent rooftop."

    Aubrey "If we can get up there, we can set off some fireworks and give everyone a proper end to the night."

    MCname "You want to set off fireworks on campus?"

    Tiff "When you say it like that, it sounds bad."

    MCname "Because it IS bad."

    Aubrey "Oh, come on. Where's your sense of adventure?"

    menu:
        "I'm in. Let's make this night memorable.":
            jump aubrey_tiff_join

        "Are you two completely crazy?":
            jump aubrey_tiff_question

    ##############################################
    # MC QUESTIONS THE PLAN
    ##############################################

label aubrey_tiff_question:
    Aubrey "Now, handsome. Don't tell me you're a chicken."
    Tiff "Come on, MC! Live a little!"
    MCname "I'm just trying to understand how either of you thought this was a good idea."
    Aubrey "Because we're visionaries."
    MCname "You're criminals."
    Tiff "Okay, technically, we haven't done anything yet."
    Aubrey "And we won't if you keep standing there asking questions."
    menu:
        "Fine. I'm in.":
            jump aubrey_tiff_join

        "Nah. I'm not getting arrested tonight.":
            jump aubrey_tiff_decline

    ##############################################
    # MC DECLINES
    ##############################################

label aubrey_tiff_decline:
    MCname "You two have fun. I'm going to enjoy the rest of the party without a criminal record."
    Aubrey "Boo! You're no fun."
    Tiff "Honestly, I don't blame you."
    Aubrey "Don't encourage him!"
    MCname "Good luck, ladies. Try not to burn the university down."
    Aubrey "No promises, handsome."
    # MC heads back toward the party.
    "{i}You decide that some adventures aren't worth the consequences.{/i}"

    jump rush_party_phase_2

    ##############################################
    # THE PLAN
    ##############################################

label aubrey_tiff_join:

    MCname "Alright. I'm in."
    Tiff "YES!"
    Aubrey "That's what I like to hear."
    MCname "But where are we getting the fireworks?"
    Aubrey "Leave that part to me."
    Aubrey "All I need is a few people to help get them to the roof."
    MCname "And what about campus security?"
    Tiff "We were hoping they wouldn't notice."
    MCname "That's not exactly a plan."
    Aubrey "Which is why you're here, handsome."
    MCname "We're going to need two teams. Movers and distractions."
    MCname "One group gets the fireworks upstairs. The other keeps security occupied."
    Aubrey "Look at you. Pretty face and a functioning brain."
    MCname "I try."
    Tiff "Okay! You heard him. Let's get moving!"
    Aubrey "Alright, people! Operation Fireworks is officially underway!"
    "{i}The group breaks into smaller teams and heads across campus.{/i}"
    "{i}For a few minutes, everything seems to be going according to plan.{/i}"
    "{i}That is, until MC spots two campus security officers near the building entrance.{/i}"
    Tiff "Oh, you've got to be kidding me."
    Aubrey "Well, that's inconvenient."
    MCname "You think?"
    Aubrey "You're up, handsome. We need a distraction."
    MCname "Right now?"
    Aubrey "Unless you have a better idea."
    menu:
        "Pretend to collapse. Make them think it's an emergency.":
            jump aubrey_tiff_distraction_success

        "Walk up and ask them for directions.":
            jump aubrey_tiff_distraction_fail

    ##############################################
    # DISTRACTION 1 - THE FAKE EMERGENCY
    ##############################################

label aubrey_tiff_distraction_success:
    MCname "Okay. Get the others behind those bushes."
    Tiff "What are you going to do?"
    MCname "Trust me."
    "{i}Half the group disappears behind the nearby bushes while MC and Tiff remain in the open.{/i}"
    MCname "Alright... here goes nothing."
    # MC suddenly collapses to the ground.
    Tiff "OH MY GOD!"
    Tiff "MC! Are you okay?!"
    "{i}The two security officers immediately rush over.{/i}"
    "Campus Security 1" "What's going on here?"
    Tiff "I don't know! We were just talking and he suddenly collapsed!"
    "Campus Security 2" "Seriously? During our shift?"
    "Campus Security 1" "Hey, kid. Can you hear me?"
    MCname "..."
    Tiff "That's it?! He's unconscious! Can somebody PLEASE do something?!"
    "Campus Security 1" "Alright, alright. Calm down."
    "Campus Security 2" "I think something might actually be wrong with him."
    MCname "{i}(Come on... come on...){/i}"
    "Campus Security 2" "Hey! Wake up, kid!"
    "{i}The officer gives MC a gentle shake.{/i}"
    # A loud whistle suddenly echoes across campus.
    "{i}BOOM!{/i}"
    "{i}A brilliant burst of color explodes across the night sky.{/i}"
    "{i}More fireworks follow, lighting up the campus.{/i}"
    MCname "WHOA!"
    "{i}MC suddenly sits upright.{/i}"
    MCname "Oh, hey. I'm good."
    "Campus Security 1" "What the hell?!"
    MCname "Yeah, this happens sometimes."
    MCname "Thanks for checking on me, though."
    Tiff "Oh my God, you scared me half to death!"
    "{i}Tiff grabs MC's arm and helps him to his feet.{/i}"
    "Campus Security 2" "You know what? I don't even want to ask."
    "Campus Security 1" "Come on. We need to find out where those fireworks are coming from."
    "{i}The two officers hurry toward the fireworks display.{/i}"
    "{i}Tiff watches them disappear before turning back to MC with a huge grin.{/i}"
    Tiff "You absolute idiot."
    MCname "An idiot who just saved the mission."
    Tiff "I can't believe that actually worked!"
    MCname "Neither can I."
    "{i}The two of you hurry back toward the party.{/i}"
    jump aubrey_tiff_fireworks_aftermath

    ##############################################
    # DISTRACTION 2 - THE TERRIBLE EXCUSE
    ##############################################

label aubrey_tiff_distraction_fail:
    MCname "Alright. I've got this."
    Tiff "You do?"
    MCname "Absolutely."
    "{i}MC walks toward the security officers with Tiff and another student following behind.{/i}"
    MCname "Uh, hey. Sorry to bother you guys."
    "Campus Security 1" "Can we help you?"
    MCname "Yeah, actually. We're a little lost."
    "Campus Security 2" "Lost?"
    MCname "We're trying to find our dorms. I kind of forgot which building I'm in."
    "{i}Tiff slowly turns toward MC.{/i}"
    Tiff "{i}(Seriously?){/i}"
    "Campus Security 1" "You forgot where you live?"
    MCname "Well, when you put it like that..."
    "Campus Security 2" "And your friends?"
    Tiff "I'm mostly just trying to help him."
    MCname "Yeah. I'm pretty hopeless."
    "{i}MC lets out an awkward laugh while subtly motioning for the others to move along.{/i}"
    "Campus Security 2" "Hold on."
    "{i}The officer notices movement near the building.{/i}"
    "Campus Security 2" "Hey! What are those people doing over there?"
    MCname "What people?"
    "Campus Security 1" "Don't play dumb. Stop right there!"
    Tiff "Aw, man. SCATTER!"
    "{i}The group immediately breaks in every direction.{/i}"
    "{i}Unfortunately, the distraction has completely fallen apart.{/i}"
    "{i}A few minutes later, MC and Tiff find themselves sitting in the campus security office.{/i}"
    Tiff "What kind of distraction was that?!"
    MCname "I thought it was pretty convincing."
    Tiff "You told them you forgot where you live!"
    MCname "I panicked!"
    Aubrey "Well, well. Look what we have here."
    "{i}Aubrey leans against the doorway, shaking her head.{/i}"
    Aubrey "I should've known you were just a pretty face."
    MCname "Nice to see you too."
    Tiff "Don't look at me. This was his plan."
    Aubrey "Oh, I know."
    MCname "Are you two seriously going to leave me here?"
    Aubrey "Wouldn't dream of it, handsome."
    "{i}Aubrey gives MC a playful wink before walking away.{/i}"
    MCname "I hate this place."
    "{i}Somehow, the night has gotten even more complicated.{/i}"

    jump rush_party_phase_2

    ##############################################
    # FIREWORKS AFTERMATH
    ##############################################

label aubrey_tiff_fireworks_aftermath:
    # MC returns to the rush party.
    # The fireworks are lighting up the sky.
    "{i}The entire party has spilled outside to watch the fireworks.{/i}"
    "{i}People cheer as another explosion of color fills the sky.{/i}"
    MCname "{i}(Okay... I'll admit. That was pretty awesome.){/i}"
    "{i}Tiff catches up with MC, still riding the adrenaline.{/i}"
    Tiff "That was INCREDIBLE!"
    MCname "Yeah. I think I aged about five years in the last two minutes."
    Tiff "You should've seen your face when that security guy started shaking you!"
    MCname "I was committed to the performance."
    Tiff "You were one second away from getting CPR!"
    MCname "That's called dedication."
    "{i}Tiff laughs and playfully nudges MC.{/i}"
    "{i}Across the crowd, Aubrey catches MC's eye and raises her cup in a little toast.{/i}"
    Tiff "So..."
    Tiff "What do you say? Worth the trouble?"
    menu:
        "Stay with Tiff.":
            jump aubrey_tiff_tiff_ending

        "Go talk to Aubrey.":
            jump aubrey_tiff_aubrey_ending

    ##############################################
    # ENDING A - TIFF
    ##############################################

label aubrey_tiff_tiff_ending:

    # Relationship reward can be adjusted to your system.
    $ relationship_api.add_affection("Tiff", 1)
    Tiff "That was seriously one of the craziest things I've ever done."
    MCname "And somehow, I think you enjoyed every second of it."
    Tiff "Maybe a little."
    MCname "We would've been caught if it weren't for your award-winning acting."
    Tiff "Excuse me? YOU were the one lying on the ground!"
    MCname "And you sold it beautifully."
    Tiff "Okay, fine. We make a pretty good team."
    MCname "I'd say so."
    "{i}Tiff looks up at the fireworks, smiling as another burst lights up the sky.{/i}"
    Tiff "You know, I didn't think you'd actually go along with us."
    MCname "Why not?"
    Tiff "You seemed like the sensible type."
    MCname "I am sensible."
    Tiff "You literally pretended to pass out in front of campus security."
    MCname "A temporary lapse in judgment."
    Tiff "Sure."
    "{i}She laughs, then looks back at MC.{/i}"
    Tiff "I'm glad you came along tonight."
    MCname "Me too."
    Tiff "We should do something together again sometime."
    MCname "Something that doesn't involve campus security?"
    Tiff "No promises."
    "{i}Tiff smiles and turns her attention back to the fireworks.{/i}"
    "{i}For the rest of the display, the two of you stay together, enjoying the chaos you helped create.{/i}"

    jump rush_party_phase_2

label rush_party_phase_2:
    "The party winds down, and you head back to the dorm."
    jump rush_party_finish

    ##############################################
    # ENDING B - AUBREY
    ##############################################

label aubrey_tiff_aubrey_ending:
    # Relationship reward can be adjusted to your system.
    $ relationship_api.add_affection("Aubrey", 1)
    "{i}MC makes his way through the crowd toward Aubrey.{/i}"
    Aubrey "Well, look who survived."
    MCname "Barely. I think I deserve a medal."
    Aubrey "A medal? I was thinking more along the lines of a kiss."
    MCname "That's a pretty generous reward."
    Aubrey "Don't get ahead of yourself, handsome."
    MCname "So, how'd I do?"
    Aubrey "Not bad."
    MCname "Not bad?"
    Aubrey "You followed orders, didn't completely ruin the plan, and managed to entertain me."
    Aubrey "I'd say that's a successful first mission."
    MCname "First mission?"
    Aubrey "Oh, honey. You didn't think this was going to be our last adventure, did you?"
    MCname "Should I be worried?"
    Aubrey "Probably."
label aubrey_reward_scene:
    "{i}Aubrey takes a sip of her drink, watching the fireworks light up the night sky.{/i}"
    Aubrey "You know, I wasn't sure you'd actually have the guts to go through with it."
    MCname "I'm full of surprises."
    Aubrey "Clearly."
    "{i}She turns toward him, a mischievous smile slowly spreading across her face.{/i}"
    Aubrey "And I have to admit... I'm impressed."
    MCname "Careful. Keep talking like that and I'll start thinking you like me."
    Aubrey "Don't get ahead of yourself, handsome."
    "{i}She steps a little closer, lowering her voice.{/i}"
    Aubrey "Although... I do think you deserve a little reward for tonight."
    MCname "As do I."
    Aubrey "Oh? Someone's feeling confident."
    MCname "You haven't exactly given me a reason not to be."
    "{i}Aubrey laughs, then glances toward the party before looking back at him.{/i}"
    Aubrey "How about we sneak away and find somewhere a little more private?"
    MCname "Say less."
    "{i}She takes his hand, leading him away from the crowd. The music gradually fades behind them, leaving only the distant sounds of the party and fireworks overhead.{/i}"
    "{i}Once they're alone, Aubrey turns to face him.{/i}"
    MCname "So... what now?"
    Aubrey "Well, handsome..."
    "{i}She steps closer, looking him up and down with an amused smile.{/i}"
    Aubrey "I think we should stop talking for a little while."
    "{i}She pulls him into a kiss, her playful teasing giving way to something considerably more intimate.{/i}"
    Aubrey "Well, [MCname]..."
    Aubrey "Handsome AND a troublemaker, i can work with that."
    MCname "I could say the same about you."
    Aubrey "Careful. Compliments will get you everywhere."
    MCname "Something tells me you wouldn't mind."
    Aubrey "Maybe I wouldn't."
    #She kisses him again, this time with a little more intensity, before pulling back and giving him a sly grin.
    Aubrey "So, what do you say we make this a night to remember?"
    menu:
        "Kiss her back.":
            jump aubrey_reward_kiss

        "Pull away and suggest leaving.":
            jump aubrey_reward_reject

label aubrey_reward_kiss:
    "{i}MC leans in, returning her kiss with equal fervor. The world around them seems to fade away as they share a passionate moment, the fireworks above providing a spectacular backdrop.{/i}"
    #Aubrey pulls back slightly, her eyes sparkling with mischief and desire.
    Aubrey "Good boy."
    #Aubrey begins taking off his pants
    #she begins to rub his erection through his boxers
    #grabs her rear and kisses her neck while she continues to rub his erection
    #she begins to unbutton her shirt and takes off her bra
    #after she takes off her bra, he begins to rub her breasts and she begins to rub his erection through his boxer
    #she takes his member out of his boxer and begins to rub it while he continues to rub her breasts
    #she drops to her knees and begins to give him a blowjob while she plays with herself with one hand and rubs his balls with the other
    MCname "{i}(Ok she's a little to good at this i gotta focus on something else before this ends quickly){/i}"
    #seeing your struggle she resoubles her effort and begins to suck harder and faster while she continues to play with herself.
    MCname "{i}(ohhh shit...kittens,grandma,who won the football game...){/i}"
    #sensing his fight she begins to deep throat him and he begins to moan.
    MCname "ohhh shit...ohhh shit...ohhh shit..."
    #Aubrey release his member from her mouth and begins to rub his member with her hand while she continues to play with herself.
    Aubrey "Whats wrong handsome? You look like your about to cum."
    #MC Struggling
    MCname "......"
    #She begins to suck again
    menu:
        "Cum in her mouth":
            jump aubrey_reward_leave

        "Pull away and cum on her face":
            jump aubrey_reward_leave

label aubrey_reward_leave:
    #you both finish and she begins to clean herself up and you begin to put your pants back on
    Aubrey "Well, that was fun."
    MCname "Yeah, it was."
    Aubrey "Dont let it get to your head."
    Aubrey "And no we wont be doing that again."
    Aubrey "I have a reputation to maintain."
    #she finshes getting dressed
    #she leaves and leaves you alone to get dressed and head back to your dorm

    jump rush_party_finish

label aubrey_reward_reject:
    MCname "I think I should head back to the party."
    Aubrey "Fair enough. I'll see you out there, handsome."

    jump rush_party_finish

label rush_party_finish:
    "{i}You head back to your dorm, the sounds of the party fading behind you.{/i}"
    MCname "{i}(What a night... I can't believe everything that happened.){/i}"
    MCname "{i}(I wonder what tomorrow will bring....){/i}"
    jump ep2_to_ep3

label ep2_to_ep3:

    stop music fadeout 2.0
    scene black with fade

    centered "{size=+40}End of Episode 2{/size}"

    pause 2.0

    centered "{size=+40}Episode 3{/size}"

    pause 2.0

    jump episode_3_start
