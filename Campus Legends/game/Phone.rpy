init offset = 1
default force_phone = False
default viewing_photo = False
default current_photo = None


init -10 python:
    
    class App(NoRollback):
        def __init__(self, app_screen, name, icon):
            self.app_screen = app_screen # What screen will show when the app is clicked
            self.name = name # The app's name
            self.icon = icon # The app's icon
    # Apps in order of index [0] = First app, [1] = Second app, etc.
    apps = [
            App("contacts", "Messages", "images/phone/icon.png"),            
            App("feed", "Twatter", "images/phone/icon.png")
        ]
    class Contact(NoRollback):
        def __init__(self, contact_id, contact_name, pfp):
            self.contact_id = contact_id
            self.contact_name = contact_name
            self.pfp = pfp
            self.chat = []
            self.has_unread = False
            self.convo_done = False

        def mark_unread(self):
            """ Mark this contact as having unread messages """
            self.has_unread = True
        
        def mark_read(self):
            """ Mark this contact's messages as read """
            self.has_unread = False
        
        def add_sms(self, text):
            """ Add message to the chat """
            self.chat.append(text)
    
    sienna = Contact("sienna_dm", "Sienna", "images/phone/icon.png")
    nick = Contact("nick_dm", "Nick", "images/phone/icon.png")
    
    # Contacts in order of index [0] = First app, [1] = Second contact, etc.
    contacts = [
            sienna,
            nick,
        ]
    
    
    
    class SMS(NoRollback):
        def __init__(self, sender, text="", image=None, is_image=False, from_player=False, resolved=False):
            self.sender = sender
            self.text = text
            self.image = image
            self.is_image = is_image
            self.choices = []
            self.from_player = from_player
            self.resolved = resolved
            self.visible = False
            self.show_at = None
            self.expires_epoch = None
            self.responded_to = False

        def show_text(self):
            """ Shows the text """
            self.visible = True
        
        def hide_text(self):
            """ Hides the text """
            self.visible = False

        def add_choice(self, choice):
            """ Adds a choice """
            self.choices.append(choice)
        
        def resolve(self):
            self.resolved = True

        def player_replied(self):
            """ Marks that the player has replied to this message """
            self.responded_to = True

        def show_choices(self):
            for choice in self.choices:
                if not choice.chosen:
                    choice.show_choice()

        def can_expire(self):
            """
            Example:
                [message set up]
                msg.show_text()
                msg.can_expire()

                [Message Choices]

                works with chaining as well
            """
            self.expires_epoch = phone_epoch

        def chain(self, player_text, npc_text=None, npc_image=None):
            """
            Example:
                msg = SMS(sender, "message text")
                sender.add_sms(msg)
                msg.show_text()
                
                level2 = msg.chain("player response", "Npc follow-up")
                level3 = level2.chain("Player response", "Npc follow-up")
                level4 = level3.chain("Player response", "Npc follow-up")
                level5 = level4.chain("Player response", npc_image="path/to/image.png")
            """
            if npc_image:
                npc_response = SMS(self.sender, image=npc_image, is_image=True)
            else:
                npc_response = SMS(self.sender, npc_text)
            
            player_choice = Choice(player_text, npc_text or "", response_sms=npc_response)
            self.add_choice(player_choice)
            
            if self.visible:
                player_choice.show_choice()

            return npc_response

        def chain_end(self, player_text, npc_response=None, followup_npc_text=None, followup_npc_image=None, followup_choices=None, npc_response_image=None):
            """
            Args:
                player_text: What player says
                npc_response: NPC's immediate text response (optional if using image)
                followup_npc_text: NPC's follow-up text message (optional if using image)
                followup_npc_image: NPC's follow-up image path (optional)
                followup_choices: List of (player_text, npc_text) for final choices
                npc_response_image: NPC's immediate image response (optional)
            """
            if npc_response_image:
                npc_response_sms = SMS(self.sender, image=npc_response_image, is_image=True)
            else:
                npc_response_sms = SMS(self.sender, npc_response or "")
            
            player_choice = Choice(player_text, npc_response or "", response_sms=npc_response_sms)
            

            if followup_npc_image:
                player_choice.followup_is_image = True
                player_choice.followup_image = followup_npc_image
                player_choice.followup_text = ""
            else:
                player_choice.followup_is_image = False
                player_choice.followup_text = followup_npc_text or ""
            
            player_choice.followup_choices = followup_choices or []
            
            self.add_choice(player_choice)
            if self.visible:
                player_choice.show_choice()
            
            return npc_response_sms

        

        def expiry_old_reply_windows(self):
            """
            Hides choices on messages that are now "too old" to reply to,
            and marks those SMS as resolved so they don't block anything.
            """
            for contact in contacts:
                for sms in contact.chat:
                    if not sms.visible:
                        continue
                    if sms.resolved:
                        continue
                    if not sms.choices:
                        continue

                    # if this SMS was meant to expire and it's from an older epoch
                    if getattr(sms, "expires_epoch", None) is not None:
                        if phone_epoch >= sms.expires_epoch:
                            for choice in sms.choices:
                                choice.hide_choice()
                            sms.resolve()

        def advance_expired(self):
            """
            Call when story context advances (end of a scene / time jump / new day).
            It will expire old optional reply choices.
            """
            global phone_epoch
            phone_epoch +=1
            self.expiry_old_reply_windows()

    class Choice(NoRollback):
        def __init__(self, text, response, response_sms=None, chosen=False):
            self.text = text
            self.response = response
            self.response_sms = response_sms
            self.chosen = chosen
            self.visible = False

        def show_choice(self):
            """ Shows the choice """
            self.visible = True
        
        def hide_choice(self):
            """ Hides the choice """
            self.visible = False
        
        def choose(self, contact):
            self.chosen = True
            player_reply = SMS(None, self.text, from_player=True)
            
            if hasattr(self, 'response_sms') and self.response_sms:
                npc_response = self.response_sms
                if not npc_response.text:
                    npc_response.text = self.response
            else:
                npc_response = SMS(contact, self.response)
            
            contact.add_sms(player_reply)
            contact.add_sms(npc_response)
            player_reply.show_text()
            
            import time
            npc_response.show_at = time.time() + 1.0
            
            if hasattr(self, 'followup_text') or hasattr(self, 'followup_image'):
                npc_response.has_followup = True
                
                # Check if follow-up is an image or text
                if hasattr(self, 'followup_is_image') and self.followup_is_image:
                    npc_response.followup_is_image = True
                    npc_response.followup_image = getattr(self, 'followup_image', None)
                    npc_response.followup_text = ""
                else:
                    npc_response.followup_is_image = False
                    npc_response.followup_text = getattr(self, 'followup_text', "")
                
                npc_response.followup_choices = getattr(self, 'followup_choices', [])
                npc_response.followup_sender = contact

            renpy.restart_interaction()

# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
    def has_any_unread_messages():
        """ Checks if any messages are unread """
        return any(contact.has_unread for contact in contacts)
    
    def not_responded():
        """ Checks if any messages are waiting for a response """
        for contact in contacts:
            for sms in contact.chat:
                if sms.visible and not sms.resolved and len(sms.choices) > 0:
                    return True
        return False

    def view_photo(photo_path):
        """Open a photo in fullscreen view"""
        global viewing_photo, current_photo
        viewing_photo = True
        current_photo = photo_path

    def close_photo():
        """Close the photo view"""
        global viewing_photo, current_photo
        viewing_photo = False
        current_photo = None
        renpy.hide_screen("photo_viewer")

    def check_delayed_messages(contact):
        """Check if any messages should be revealed based on their show_at timestamp"""
        import time
        current_time = time.time()

        for sms in contact.chat:
            if not sms.visible and sms.show_at and current_time >= sms.show_at:
                sms.show_text()
                sms.show_at = None

                for choice in sms.choices:
                    choice.show_choice()
        
                if hasattr(sms, 'has_followup') and sms.has_followup:
                    if hasattr(sms, 'followup_is_image') and sms.followup_is_image:
                        followup = SMS(sms.followup_sender, image=sms.followup_image, is_image=True)
                    else:
                        followup = SMS(sms.followup_sender, sms.followup_text)
                    
                    contact.add_sms(followup)
                    followup.show_at = time.time() + 1.0
                    
                    for choice_text, choice_response in sms.followup_choices:
                        choice = Choice(choice_text, choice_response)
                        followup.add_choice(choice)
                    
                    sms.has_followup = False
                
                renpy.restart_interaction()

    chat_yadj = ui.adjustment()

    def message(contact, sms):
        contact.mark_unread()
        contact.add_sms(sms)
        sms.show_text()
        sms.show_choices()
# ------------------------------------------------------------
# STYLES
# ------------------------------------------------------------
style gray_bg:
    xalign 0.0
    xmaximum 400
    background "#DDDDDD"
    padding(15,10)

style blue_bg:
    xalign 1.0
    xmaximum 400
    background "#0066FF"
    padding(15,10)

style gray_photo:
    xalign 0.0
    xmaximum 400
    background "#DDDDDD"
    padding (5, 5)

style blue_photo:
    xalign 1.0
    xmaximum 400
    background "#0066FF"
    padding (5, 5)

# ------------------------------------------------------------
# SCREENS
# ------------------------------------------------------------

screen phone_button():
    textbutton "Phone":
        xalign 1.0
        action [Show("phone_home"), Hide("phone_button")]

screen phone_home():
    modal True

    window:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 1000
        background "#1d1d1d"
        
        frame:
            xalign 0.5
            yalign 0.5
            xysize (550, 950)
            background "#ffffff"
            grid 4 4:
                spacing 10
                xalign 0.5
                yalign 0.5
                for app in apps:
                    button:
                        xysize (100, 100)
                        vbox:
                            add app.icon
                            text app.name
                        align(0.5, 0.5)
                        action [Show(f"{app.app_screen}"), Hide("phone_home")]
    vbox:
        align(0.5, 0.95)
        textbutton "Close":
            action [Hide("phone_home"), Show("phone_button")]

screen contacts():
    modal True

    window:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 1000
        background "#1d1d1d"
        
        viewport:
            xalign 0.5
            yalign 0.5
            xysize (550, 950)
            scrollbars "vertical"
            mousewheel True
            add "#ffffff"

            vbox:
                for contact in contacts:
                    button:
                        action [
                            Show("chat_screen", contact=contact),
                            Hide(screen=None),
                            Function(contact.mark_read)
                        ]

                        hbox:
                            spacing 15
                            xalign 0.0
                            yalign 0.5

                            add contact.pfp:
                                size (60,60)

                            vbox:
                                text contact.contact_name:
                                    size 28
                                    font "DejaVuSans.ttf"
                                    outlines [(0, "#000000", 0, 0)]
                                    color "#000000"
                                if contact.has_unread:
                                    text "New message!" size 18 color "#FF0000" font "DejaVuSans.ttf"
                            
                                null height 10
                                frame:
                                    background "#CCCCCC"
                                    xfill True
                                    ysize 1
    vbox:                       
        align(0.5, 0.95)
        textbutton "Back":
            action [Hide(screen=None), Show("phone_home")]

screen chat_screen(contact):
    modal True

    timer 0.1 repeat True action Function(check_delayed_messages, contact)

    window:
        xalign 0.5
        yalign 0.5
        xysize (600, 1000)
        background "#1d1d1d"
    
        # python:
        #     _msg_count = sum(1 for _s in contact.chat if _s.visible)
        #     if not hasattr(chat_yadj, '_last_count') or chat_yadj._last_count != _msg_count:
        #         chat_yadj._last_count = _msg_count
        #         chat_yadj.value = float("inf")



        viewport:
            xalign 0.5
            yalign 0.5
            xysize (550, 950)
            scrollbars "vertical"
            mousewheel True
            draggable True
            #yadjustment chat_yadj
            add "#FFFFFF"
            vbox:
                spacing 15
                xfill True
                for sms in contact.chat:
                    if sms.visible:
                        if sms.is_image:
                            if sms.from_player:
                                frame:
                                    style "blue_bg"
                                    vbox:
                                        spacing 5
                                        imagebutton:
                                            idle Transform(sms.image, fit="contain", xsize=280, ysize=200)
                                            hover Transform(sms.image, fit="contain", xsize=280, ysize=200)
                                            action [SetVariable("viewing_photo", True), SetVariable("current_photo", sms.image)]
                            else:
                                frame:
                                    style "gray_bg"
                                    vbox:
                                        spacing 5
                                        imagebutton:
                                            idle Transform(sms.image, fit="contain", xsize=280, ysize=200)
                                            hover Transform(sms.image, fit="contain", xsize=280, ysize=200)
                                            action [SetVariable("viewing_photo", True), SetVariable("current_photo", sms.image)]

                        elif sms.text:
                            if sms.from_player:
                                frame:
                                    style "blue_bg"
                                    vbox:
                                        spacing 15
                                        text sms.text:
                                            size 20
                                            font "DejaVuSans.ttf"
                                            outlines [(0, "#000000", 0, 0)]
                                            color "#FFFFFF"
                            else:
                                frame:
                                    style "gray_bg"

                                    vbox:
                                        spacing 15
                                        text sms.text:
                                            size 20
                                            font "DejaVuSans.ttf"
                                            outlines [(0, "#000000", 0, 0)]
                                            color "#000000"

                    
                        for choice in sms.choices:
                            if choice.visible and not sms.resolved and not choice.chosen:
                                frame:
                                    xalign 0.5
                                    xmaximum 400
                                    background "#0066FF"
                                    padding (5, 5)
                                    vbox:
                                        button:
                                            text choice.text:
                                                size 20
                                                font "DejaVuSans.ttf"
                                                idle_color "#FFFFFF"
                                                hover_color "#6d6d6d"
                                            action [
                                                Function(choice.choose, contact), 
                                                Function(sms.resolve), 
                                                Function(sms.player_replied),
                                                Function(renpy.block_rollback)
                                            ]
    if viewing_photo:
        use photo_viewer()                               
    else:
        vbox:
            align(0.5, 0.95)
            button:
                text "Back":
                    idle_color "#a8a8a8"
                    hover_color "#0099cc"
                    font "DejaVuSans.ttf"
                action [Hide(screen=None), Show("contacts")]
screen photo_viewer():
        modal True
        zorder 1000

        button:
            xfill True
            yfill True
            background "#00000080"
            action SetVariable("viewing_photo", False), SetVariable("current_photo", None), Hide("photo_viewer")

        if current_photo:
            add current_photo:
                xalign 0.5
                yalign 0.5
                xsize 1280
                ysize 720

                fit "contain"


