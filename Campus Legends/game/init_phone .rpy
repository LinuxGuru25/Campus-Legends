init offset = 0

label init_phone:
    python:
        phone_state = PhoneState()

        #====================================
        # PLAYER PROFILE
        #====================================

        player_pf.username = player_name if player_name else "New Student"
        player_pf.display_name = player_name if player_name else "New Student"


        #====================================
        # PHONE INITIALIZATION
        #====================================

        if not phone_state.initialized:
            phone_state.initialized = True

            phone_state.apps = [
                App(
                    "Messages",
                    "contacts",
                    "images/phone/icons/message_icon.png"
                ),

                App(
                    "Relationships",
                    "phone_stats",
                    "images/phone/icons/stats_icon.png"
                ),

                App(
                    "Twatter",
                    "feed",
                    "images/phone/icons/twatter_icon.png"
                )
            ]


            #====================================
            # CLEAR SOCIAL MEDIA DATA
            #====================================

            all_posts.clear()
            twatter_posts.clear()

            sienna_pf.posts.clear()
            jess_pf.posts.clear()
            malik_pf.posts.clear()
            norah_pf.posts.clear()
            tiffany_pf.posts.clear()
            misty_pf.posts.clear()
            kaia_pf.posts.clear()
            aubrey_pf.posts.clear()
            player_pf.posts.clear()


            #====================================
            # SIENNA POST
            #====================================

            sienna_post_1 = Post(
                sienna_pf,
                text="First week at SSU and already running around like crazy.",
                caption="First week at SSU and already running around like crazy.",
                visible=True
            )

            sienna_comment_1 = Comment(
                jess_pf,
                "You mean running around making everyone else do the work 😂",
                likes=4
            )

            sienna_post_1.comments.append(sienna_comment_1)
            sienna_pf.posts.append(sienna_post_1)
            all_posts.append(sienna_post_1)


            #====================================
            # JESS POST
            #====================================

            jess_post_1 = Post(
                jess_pf,
                text="Trying to survive another semester.",
                caption="Trying to survive another semester.",
                visible=True
            )

            jess_comment_1 = Comment(
                sienna_pf,
                "You'll survive. Probably.",
                likes=2
            )

            jess_post_1.comments.append(jess_comment_1)
            jess_pf.posts.append(jess_post_1)
            all_posts.append(jess_post_1)


            #====================================
            # MALIK POST
            #====================================

            malik_post_1 = Post(
                malik_pf,
                text="New year. Same chaos.",
                caption="New year. Same chaos.",
                visible=True
            )

            malik_comment_1 = Comment(
                jess_pf,
                "Please don't make this year worse than last year.",
                likes=3
            )

            malik_post_1.comments.append(malik_comment_1)
            malik_pf.posts.append(malik_post_1)
            all_posts.append(malik_post_1)


            #====================================
            # NORAH POST
            #====================================

            norah_post_1 = Post(
                norah_pf,
                text="SSU is already getting interesting.",
                caption="SSU is already getting interesting.",
                visible=True
            )

            norah_pf.posts.append(norah_post_1)
            all_posts.append(norah_post_1)


            #====================================
            # TIFFANY POST
            #====================================

            tiffany_post_1 = Post(
                tiffany_pf,
                text="Coffee first. Everything else later.",
                caption="Coffee first. Everything else later.",
                visible=True
            )

            tiffany_pf.posts.append(tiffany_post_1)
            all_posts.append(tiffany_post_1)


            #====================================
            # MISTY POST
            #====================================

            misty_post_1 = Post(
                misty_pf,
                text="Who else is already counting down to Friday?",
                caption="Who else is already counting down to Friday?",
                visible=True
            )

            misty_pf.posts.append(misty_post_1)
            all_posts.append(misty_post_1)


            #====================================
            # KAIA POST
            #====================================

            kaia_post_1 = Post(
                kaia_pf,
                text="New semester. New memories.",
                caption="New semester. New memories.",
                visible=True
            )

            kaia_pf.posts.append(kaia_post_1)
            all_posts.append(kaia_post_1)


            #====================================
            # AUBREY POST
            #====================================

            aubrey_post_1 = Post(
                aubrey_pf,
                text="Friday can't come soon enough.",
                caption="Friday can't come soon enough.",
                visible=True
            )

            aubrey_pf.posts.append(aubrey_post_1)
            all_posts.append(aubrey_post_1)


            #====================================
            # TWATTER POSTS
            #====================================

            twatter_posts.extend(all_posts)


            #====================================
            # CONTACTS
            #====================================

            aubrey_contact = Contact(
                "Aubrey",
                "images/phone/icon.png"
            )

            jess_contact = Contact(
                "Jess",
                "images/phone/icon.png"
            )

            kaia_contact = Contact(
                "Kaia",
                "images/phone/icon.png"
            )

            malik_contact = Contact(
                "Malik",
                "images/phone/icon.png"
            )

            misty_contact = Contact(
                "Misty",
                "images/phone/icon.png"
            )

            norah_contact = Contact(
                "Norah",
                "images/phone/icon.png"
            )

            sienna_contact = Contact(
                "Sienna",
                "images/phone/icon.png"
            )

            tiffany_contact = Contact(
                "Tiffany",
                "images/phone/icon.png"
            )


            phone_state.contacts = [
                aubrey_contact,
                jess_contact,
                kaia_contact,
                malik_contact,
                misty_contact,
                norah_contact,
                sienna_contact,
                tiffany_contact
            ]


            #====================================
            # CONTACT LIST
            #====================================

            contacts_list.clear()

            contacts_list.extend([
                aubrey_contact,
                jess_contact,
                kaia_contact,
                malik_contact,
                misty_contact,
                norah_contact,
                sienna_contact,
                tiffany_contact
            ])


        renpy.block_rollback()

    return