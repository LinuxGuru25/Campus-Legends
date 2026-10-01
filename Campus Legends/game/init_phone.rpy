init offset = 0

label init_phone:
    python:
        phone_state = PhoneState()
        
        if not phone_state.initialized:
            phone_state.initialized = True

            phone_state.apps = [
                App("Messages", "contacts", "images/phone/icons/message_icon.png"),
                App("Relationships", "phone_stats", "images/phone/icons/stats_icon.png"),
                App("Twatter", "feed", "images/phone/icons/twatter_icon.png")
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

        renpy.block_rollback()
    return