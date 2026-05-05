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

            player_r1 = sienna_m1.chain("Not much", "Nice")
            player_r1a = sienna_m1.chain("Doing homework", "Sounds fun")

            sienna_m2 = SMS(sienna, "How's it going?")

            player_r2 = sienna_m2.chain("Boring, big test", "Sorry to hear that")
            player_r2a = sienna_m2.chain("Good, I aced my test", "Great to hear")

            player_r3 = player_r2.chain("test text", "test text 2")
            player_r3a = player_r2a.chain("test text 3", "test text 4")


            player_r4 = player_r3.chain("Picture?", npc_image="images/phone/jeff.png")
            player_r4a = player_r3a.chain("Send a picture", npc_image="images/phone/jeff.png")
        

            # --------------------------------------------
            # POSTS
            # --------------------------------------------

            feed_visible = True

            
            player_pf = Profile(f"{player_username}", "images/phone/icon.png", None, 282, 53)
            player_pf.show_profile()

            sienna_pf = Profile("sienna_username", "images/phone/icon.png", "Test", 300, 90)
            nick_pf = Profile("nick_username", "images/phone/icon.png", "words", 200, 17)

            sienna_post1 = Post(sienna_pf, "What's up yall?", None, 70, 52)
            player_post = Post(player_pf, "Player text", "images/phone/jeff.png", 30, 24)
            


        #renpy.block_rollback()