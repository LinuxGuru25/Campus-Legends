init offset = 0

label init_phone:
    python:
        phone_state.reset()
        
        if not phone_state.initialized:
            phone_state.initialized = True

            # --------------------------------------------
            # TEXTS
            # --------------------------------------------
            sienna_m1 = SMS(sienna, "What's up pussy?")
            sienna.add_sms(sienna_m1)
            sienna_m1.show_text()
            sienna_m1.can_expire()

            player_r1 = sienna_m1.chain("Who you callin pussy?", "You, dumb fuck")
            player_r1a = sienna_m1.chain("Callin me a pussy?", "Who else would I be talkin to?")

            sienna_m2 = SMS(sienna, "How's it going bitch?")
            

            player_r2 = sienna_m2.chain("I see you talkin to yourself again", "EXCUSE ME?")
            player_r2a = sienna_m2.chain("Prob better than you, hoe", "You da bitch ass hoe tho")

            player_r3 = player_r2.chain("Keep it coming hoe, you know what I said", "Imma bitch slap the shit outta you")
            player_r3a = player_r2a.chain("Said nobody", "That's right, bitch aint go no friends. my bad.")


            player_r4 = player_r3.chain("Picture?", npc_image="images/phone/jeff.png")
            player_r4a = player_r3a.chain("Send a picture", npc_image="images/phone/jeff.png")
        

            # --------------------------------------------
            # POSTS
            # --------------------------------------------

            feed_visible = True

            

            player_pf = Profile(f"{player_username}", "images/phone/icon.png", None ,282, 53)
            player_pf.show_profile()

            sienna_pf = Profile("sienna_username", "images/phone/icon.png","Test", 300, 90)
            nick_pf = Profile("nick_username", "images/phone/icon.png","words", 200, 17)

            sienna_post1 = Post("sienna_post1", sienna_pf, "images/phone/jeff.png", "Lmao", 54)
            sienna_post2 = Post("sienna_post2", sienna_pf, "images/phone/run.png", "2", 45)
            sienna_post3 = Post("sienna_post3", sienna_pf, "images/phone/test2.png", "3", 90)
            sienna_post4 = Post("sienna_post4", sienna_pf, "images/phone/test3.png", "4", 57)

            si_p1_c1 = Comment(nick_pf, "comment text", "images/phone/icon.png", 50)


        #renpy.block_rollback()