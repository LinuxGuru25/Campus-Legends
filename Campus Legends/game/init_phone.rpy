init offset = 0

label init_phone:
    python:
        phone_state = PhoneState()
        
        if not phone_state.initialized:
            phone_state.initialized = True

            phone_state.apps = [
                App("Messages", "contacts", "images/phone/icons/message_icon.png"),
                App("Relationships", "phone_stats", "images/phone/icons/stats_icon.png"),
                App("Twatter", "feed", "images/phone/icons/twatter_icon.png"),
                App("Bios", "bios_home", "images/phone/icon.png")
            ]

            feed = []

            

            #====================================
            # OBJECT INSTANCES
            #====================================
            sms = SMS()
            post = Post()
            

            # will add pfp images later
            aubrey_contact = Contact("Aubrey")
            jess_contact = Contact("Jess")
            kaia_contact = Contact("Kaia")
            malik_contact = Contact("Malik")
            misty_contact = Contact("Misty")
            norah_contact = Contact("Norah")
            sienna_contact = Contact("Sienna")
            tiffany_contact  = Contact("Tiffany")

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

            # will add pfp images later
            player_profile = Profile("new_student", 0, 0)
            aubrey_profile = Profile("Aubrey_username", 0, 0)
            jess_profile = Profile("Jess_username", 0, 0)
            kaia_profile = Profile("kaia_username", 0, 0)
            malik_profile = Profile("malik_username", 0, 0, description="This is a description")
            misty_profile = Profile("misty_username", 0, 0)
            norah_profile = Profile("Norah_username", 0, 0)
            sienna_profile = Profile("Sienna_username", 0, 0)
            tiffany_profile = Profile("Tiffany_username", 0, 0)


            phone_state.all_profiles = [
                player_profile,
                aubrey_profile,
                jess_profile,
                kaia_profile,
                malik_profile,
                misty_profile,
                norah_profile, 
                sienna_profile,
                tiffany_profile
            ]

            player_bio = Bio("You")
            player_bio.stats={
                    "age": "20",
                    "sex": "M",
                    "height": "6'2",
                    "weight": "210"
            }
            aubrey_bio = Bio("Aubrey")
            jess_bio = Bio("Jess")
            kaia_bio = Bio("Kaia")
            malik_bio = Bio("Malik")
            misty_bio = Bio("Misty")
            norah_bio  = Bio("Norah")
            sienna_bio = Bio("Sienna")
            sienna_bio.stats = {
                "age": "26",
                "sex": "F",
                "height": "5'11",
                "weight": "145"
            }
            tiffany_bio = Bio("Tiffany")

            phone_state.bios = [
                player_bio,
                aubrey_bio,
                jess_bio,
                kaia_bio,
                malik_bio,
                misty_bio,
                norah_bio,
                sienna_bio,
                tiffany_bio
            ]

        renpy.block_rollback()
    return