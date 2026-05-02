init offset = 0

label init_phone:
    python:

        sienna_m1 = SMS(sienna, "What's up pussy?")
        sienna.add_sms(sienna_m1)
        sienna_m1.show_text()

        player_r1 = sienna_m1.chain("Who you callin pussy?", "You, dumb fuck")
        player_r1a = sienna_m1.chain("Callin me a pussy?", "Who else would I be talkin to?")

        sienna_m2 = SMS(sienna, "How's it going bitch?")
        

        player_r2 = sienna_m2.chain("I see you talkin to yourself again", "EXCUSE ME?")
        player_r2a = sienna_m2.chain("Prob better than you, hoe", "You da bitch ass hoe tho")

        player_r3 = player_r2.chain("Keep it coming hoe, you know what I said", "Imma bitch slap the shit outta you")
        player_r3a = player_r2a.chain("Said nobody", "That's right, bitch aint go no friends. my bad.")

        renpy.block_rollback()