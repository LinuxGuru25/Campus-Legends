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
            
            #====================================
            # OBJECT INSTANCES
            #====================================
            sms = SMS()

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


        #renpy.block_rollback()