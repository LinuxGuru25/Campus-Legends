define Aubrey = Character("Aubrey")
define Tiffany = Character("Tiff")
define mystery = Character("???")
label episode_2_start:

    scene dorm_morning
    with dissolve

    MCname "(Day two.)"
    MCname "(Still weird waking up somewhere that isn't home... but it's starting to feel a little less strange.)"

    show Malik grin at left
    with dissolve

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
            "I’ve been saving a little… I can cover this."
            Malik "Okay, big spender. Respect."
            Tiff "That’s really sweet of you."

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
                        "Ten bucks isn’t too bad."
                        Tiff "Wow… that’s really generous."

                "Leave a $20 tip.\n{color=#ff0000}{i}[-$20]{/i}{/color}\n{color=#00ff00}{i}[Tiff +5]{/i}{/color}":
                    if money_api.spend(20):
                        $ walkthrough("-$20")
                        $ relationship_api.add_affection("Tiff", 5)
                        $ walkthrough("Tiff +5")
                        "I’ve been saving… I can afford to go big."
                        Tiff "Oh my god… thank you! That means a lot."

                "Skip the tip.":
                    "I should save my money."
                    Tiff "No worries, hun."

        else:
            MCname "…I don’t have enough."
            Malik "Bro, you’re tapped out?"
            Tiff "It’s alright, he can cover it."
            Malik "I’ll take care of it."

    # MALIK PAYS
    "Let Malik pay.":
        MCname "You got this one?"
        Malik "Yeah, I’ll cover it."
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
        "A workout wouldn’t hurt. Might help clear my head."
        jump gym_scene

    "Go to the library.":
        "Probably smart to get ahead on some work."
        jump library_scene

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
kaia "Do you have your student ID on you?"
MCname "Yeah, I do."
#hands her student ID
Kaia "Thanks, I just need to put this in the system and then you can get started."
Kaia "Okay one second...Alright, you're all set. The gym is open from 6 AM to 10 PM, and the locker rooms are just down the hall to your left."
MCname "Thanks Kaia, I appreciate it."
Kaia "Hold your horses for a sceond!!! If you want i can give you the grand tour of the gym, show you where everything is?"
kaia "Or if you want to just get started, we can skip the tour and you can just start working out?"
menu:
    "Accept Kaia's offer to tour the gym {color=#00ff00}{i}[Kaia +2]{/i}{/color}":
        $ relationship_api.add_points("Kaia", 2)
        $ walkthrough("Kaia +2")
        MCname "Sure, a tour sounds great."
        Kaia "Awesome! Follow me, and I'll show you around."
        jump gym_tour

    "Decline for now":
        mc "Maybe another time. i just want to get started with my workout."
        kaia "No problem. The locker rooms are just down the hall to your left. Enjoy your workout!"
        jump gym_workout

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
        $ checked_kaia_out = true
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
"[i](Why cant our showers be like this?){/i}"
#MC finishes showering and gets dressed

#show mc walking past front desk
Kai "Hey, [MCname]! How was your workout?"
MCname "It was great!!"

if checked_kaia_out:
    Kaia "Hey, [MCname]! I noticed you checking me out earlier. Just remember, I'm taken."
    MCname "Yeah, I know. I was just admiring your dedication to fitness."
    "Kaia blushes, trying to hide it with a quick glance away."
    kaia "I'll catch you later. {i}…never noticed how cute he really is...{/i}"

MCname "You going to the party tonight?"
Kaia "Yeah, I might swing by for a bit. But I have to be up early tomorrow for a training session, so I won't stay too long."
Kaia "I'll be there to support Brad, but I won't be staying for the whole thing."
Kaia "Anyway, I should get BACK TO WORK . See you around, [MCname]!"
jump pre_party_scene

label pre_party_scene:

#MC geta text from Malik "Yo bro, you ready for the party tonight? It's gonna be lit!"
MCname "I just left the gym and im on my way back to the dorms to get cleaned up and dressed. I'll be ready by 8."
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
Malik "Alright im gonna give you a list."
Malik "Complete the list at the party and you become a legend, nobody has ever completed the entire list."
# Activate objectives AFTER the conversation
$ rush_obj_blowie = active
$ rush_obj_handjob = active
$ rush_obj_kiss = active
$ rush_obj_panties = active
$ rush_obj_drink_5_shots = active
$ rush_obj_have_sex = active

"{i}(A list? This already sounds like a setup…){/i}"
jump rush_party_start    

label rush_party_start:
    show screen rush_objectives
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

    show screen rush_objectives
    call screen rush_party_free_roam_screen
    return



###############################################
# RUSH PARTY FREE ROAM SCREEN — CLICK TO TALK
###############################################

screen rush_party_free_roam_screen:

    # Background party render
    add "party_main_room.png"

    # Sienna
    imagebutton:
        idle "sienna_party_idle.png"
        hover "sienna_party_hover.png"
        xpos 200
        ypos 350
        action Jump("party_sienna_scene")

    # Jess
    imagebutton:
        idle "jess_party_idle.png"
        hover "jess_party_hover.png"
        xpos 900
        ypos 120
        action Jump("party_jess_scene")

    # Malik
    imagebutton:
        idle "malik_party_idle.png"
        hover "malik_party_hover.png"
        xpos 1100
        ypos 400
        action Jump("party_malik_scene")

    # Kaia
    imagebutton:
        idle "kaia_party_idle.png"
        hover "kaia_party_hover.png"
        xpos 350
        ypos 120
        action Jump("party_kaia_scene")

    # Misty
    imagebutton:
        idle "misty_party_idle.png"
        hover "misty_party_hover.png"
        xpos 750
        ypos 250
        action Jump("party_misty_scene")

    # Kai
    imagebutton:
        idle "kai_party_idle.png"
        hover "kai_party_hover.png"
        xpos 500
        ypos 500
        action Jump("party_kai_scene")

    # Random people
    imagebutton:
        idle "party_crowd_idle.png"
        hover "party_crowd_hover.png"
        xpos 650
        ypos 420
        action Jump("party_random_people")

    # Exit
    imagebutton:
        idle "exit_party_idle.png"
        hover "exit_party_hover.png"
        xpos 1200
        ypos 600
        action Jump("rush_party_summary")













    

        
        



        
        

    


 



    

    
    

    
    
    

                
    

