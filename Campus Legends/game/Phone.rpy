default viewing_photo = False
default current_photo = None

init -10 python:

#====================================
# CLASSES
#====================================

    class PhoneState(NoRollback):
        def __init__(self):
            self.initialized = False
            self.apps = []
            self.contacts = []

        def reset(self):
            self.initialized = False
            self.apps = []
            self.contacts = []

    class App(NoRollback):
        def __init__(self, name, screen, icon=None):
            self.name = name
            self.screen = screen
            self.icon = icon

    class Contact:
        def __init__(self, name, pfp="images/phone/icon.png"):
            self.name = name
            self.pfp = pfp
            self.chat = []
            self.has_unread = False
            self.visible = False

        def show_contact(self):
            self.visible = True
        
        def mark_read(self):
            self.has_unread = False

        def mark_unread(self):
            self.has_unread = True
        
        def add_sms(self, sms):
            self.chat.append(sms)
        
        def kill_choices(self):
            for sms in self.chat:
                sms.mark_resolved()
                sms.hide_choices()


    class SMS:
        def __init__(self, sender=None, text="", image=None, follow_up=None, from_player=False):
            self.sender = sender
            self.text = text
            self.image = image
            self.follow_up = follow_up
            self.from_player = from_player
            self.choices = []
            self.visible = False
            self.resolved = False
            self.replied_to  = False
            self.delay = None

        def reveal(self, contact): # make message appear
            self.visible = True
            self.show_choices()
            self.delay = None
            self.schedule_follow_up(contact)

        def schedule_follow_up(self, contact): # prepare next automatic message
            if self.follow_up:
                contact.chat.append(self.follow_up)
                self.follow_up.delay = 1.0

        def player_replied(self):
            self.replied_to = True

        def show_choices(self):
            for choice in self.choices:
                if not choice.chosen:
                    choice.show_choice()
        
        def hide_choices(self):
            for choice in self.choices:
                if self.resolved:
                    choice.hide_choice()
        
        def mark_resolved(self):
            self.resolved = True

        def show_text(self):
            self.visible = True
        
        def add_choice(self, choice):
            self.choices.append(choice)
        
        def chain(self, player_text=None, npc_text=None, player_image=None, npc_image=None): # connect messages together
            if npc_image:
                npc_response = SMS(self.sender, image=npc_image)
            else:
                npc_response = SMS(self.sender, text=npc_text)
            
            if player_image:
                player_choice = Choice(image=player_image, response=npc_response)
            else:
                player_choice = Choice(text=player_text, response=npc_response)
                
            if player_text:
                self.add_choice(player_choice)
                
                if self.visible:
                    player_choice.show_choice()
            else:
                self.follow_up = npc_response

            return npc_response

    class Choice:
        def __init__(self, text="", response=None, image=None):
            self.text = text
            self.image = image
            self.response = response
            self.chosen = False
            self.visible = False

        def show_choice(self):
            self.visible = True

        def hide_choice(self):
            self.visible = False

        def choose(self, contact):
            self.chosen = True
            player_reply = new_sms(contact, None, self.text, self.image)
            player_reply.visible = True
            contact.chat.append(self.response)
            self.response.delay = 1.0

#====================================
# FUNCTIONS
#====================================

    def phone_open():
        config.rollback_enabled = False

    def phone_close():
        config.rollback_enabled = True

    chat_yadj = ui.adjustment()

    def new_sms(contact, sender, text=None, image=None): # Create/start a conversation
        from_player = sender is None
        sms = SMS(sender=sender, text=text, image=image, from_player=from_player)
        contact.chat.append(sms)
        sms.reveal(contact)
        if not from_player:
            contact.mark_unread()
        return sms

#====================================
# STYLES
#====================================
style phone_bg:
    xalign 0.5
    yalign 0.5
    xsize 476
    ysize 970
    background "images/phone/base.png"

style phone_screen:
    xalign 0.5
    yalign 0.5
    xsize 450
    ysize 800
    background "#FFFFFF"

style gray_bg:
    xalign 0.0
    xmaximum 400
    yfill False
    xfill False
    yminimum 0
    xminimum 0
    background "#DDDDDD"
    padding(15,10)

style blue_bg:
    xalign 1.0
    xmaximum 400
    yfill False
    xfill False
    yminimum 0
    xminimum 0
    background "#0066FF"
    padding(15,10)

#====================================
# SCREENS
#====================================

screen phone_button():

    imagebutton auto "phone/phone_button_%s.png":
        focus_mask True
        action [Show("phone_home"), Hide("phone_button")]


screen phone_home():
    modal True

    on "show" action Function(phone_open)
    on "hide" action Function(phone_close)

    button:
        xfill True
        yfill True
        background "#00000080"
        action NullAction()

    window:
        style "phone_bg"

        frame:
            style "phone_screen"

            vbox:
                align (0.5, 0.5)

                grid 4 4:
                    for app in phone_state.apps:
                        button:
                            add app.icon
                            action [Show(screen=app.screen), Hide(screen=None)]

    vbox:
        align (0.5, 0.93)
        textbutton "Close":
            action [Hide(screen=None), Show("phone_button")]

screen contacts():
    modal True

    on "show" action Function(phone_open)
    on "hide" action Function(phone_close)

    button:
        xfill True
        yfill True
        background "#00000080"
        action NullAction()

    window:
        style "phone_bg"

        frame:
            style "phone_screen"
            
            vbox:
                xalign 0.5

                spacing 15

                for contact in phone_state.contacts:
                    if contact.visible:
                        button:
                            xfill True
                            action [Show("chat_screen", contact=contact), Hide(screen=None), Function(contact.mark_read)]
                            hbox:
                                add contact.pfp:
                                    size (60, 60)
                                text contact.name:
                                    if contact.has_unread:
                                        color "#cc0000"
                                        bold True
                                    else:
                                        color "#000000"
                                    size 24
                                    yalign 0.5


                        frame:
                            background "#CCCCCC"
                            xfill True
                            ysize 1

    vbox:
        align (0.5, 0.93)
        textbutton "Back":
            action[Show("phone_home"), Hide(screen=None)]

screen chat_screen(contact):
    modal True
    on "show" action Function(phone_open)
    on "hide" action Function(phone_close)

    button:
        xfill True
        yfill True
        background "#00000080"
        action NullAction()

    window:
        style "phone_bg"

        python:
            _msg_count = sum(1 for _s in contact.chat)
            if not hasattr(chat_yadj, "_last_count") or chat_yadj._last_count != _msg_count:
                chat_yadj._last_count = _msg_count
                chat_yadj.value = float("inf")

        frame:
            style "phone_screen"

            viewport:
                xalign 0.5
                yalign 0.5
                xsize 450
                ysize 800
                scrollbars "vertical"
                mousewheel True
                draggable True
                yadjustment chat_yadj

                hbox:
                    vbox:
                        spacing 15
                        xfill True

                        for sms in contact.chat:

                            if sms.delay is not None and not sms.visible:
                                timer sms.delay action Function(sms.reveal, contact)

                            $ bubble_style = "blue_bg" if sms.from_player else "gray_bg"
                            $ text_color = "#FFFFFF" if sms.from_player else "#000000"

                            if sms.visible:
                                
                                if sms.image:
                                    frame:
                                        style bubble_style

                                        vbox:
                                            spacing 5
                                            imagebutton:
                                                idle Transform(sms.image, fit="contain", xsize=280, ysize=200)
                                                hover Transform(sms.image, fit="contain", xsize=280, ysize=200)
                                                action [SetVariable("viewing_photo", True), SetVariable("current_photo", sms.image)]
                                
                                elif sms.text:        
                                    frame:
                                        style bubble_style
                                        vbox:
                                            spacing 15
                                            text sms.text style "default":
                                                size 20
                                                color text_color

    if viewing_photo:
        use photo_viewer()

    vbox:
        align(0.5, 0.93)
        textbutton "Back":
            action [Show("contacts"), Hide(screen=None)]
    
    frame:
        xpos 1230
        yalign 0.5
        xsize 450
        ysize 800
        background None
        padding (20, 20)

        vbox:
            spacing 15
            for sms in contact.chat:
                for choice in sms.choices:
                    if choice.visible:
                        button:
                            xfill True
                            hover_background "#0066FF"
                            idle_background "#999999"
                            padding (10, 10)
                            text choice.text:
                                size 20
                                idle_color "#000000"
                                hover_color "#FFFFFF"
                            action [
                                Function(choice.choose, contact),
                                Function(sms.mark_resolved),
                                Function(sms.hide_choices),
                                Function(sms.player_replied)
                            ]

screen photo_viewer():
        modal True
        on "show" action Function(phone_open)
        on "hide" action Function(phone_close)
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
screen feed():
    modal True

    window:
        style "phone_bg"

        vbox:
            
            null height 65
            spacing 5

            viewport:
                xpos 13
                yalign 0.5
                xsize 450
                ysize 750
                scrollbars "vertical"
                draggable True
                mousewheel True
                
                vbox:
                    frame:
                        xpos 0.05
                        yalign 0.5
                        background None
                        xfill True
                        ysize 100
                        hbox:
                            button:
                                add player_pf.pfp:
                                    size (75, 75)
                                action [Show("profile_screen", profile=player_pf), Hide(screen=None)]

                            null width 85
                            
                            text "Feed" size 35 color "#000000" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)] xalign 0.5 yalign 0.5
                            
                        frame:
                            background "#CCCCCC"
                            xfill True
                            ysize 3

                        for post in all_posts:
                            if post.visible:
                                $ _author = post.author  # profile object

                                frame:
                                    style "post_bg"
                                    
                                    hbox:
                                        spacing 10

                                        vbox:
                                            yalign 0.0
                                            button:
                                                add _author.pfp:
                                                    size (60, 60)
                                                action [Show("profile_screen", profile=_author), Hide(screen=None)]


                                        vbox:
                                            spacing 8
                                            xmaximum 370

                                            
                                            textbutton _author.get_username():
                                                text_hover_color "#646464"
                                                text_idle_color "#000000"
                                                text_font "DejaVuSans.ttf"
                                                text_outlines [(0, "#000000", 0, 0)]
                                                text_size 25
                                                xalign 0.0

                                                action Show("profile_screen", profile=_author), Hide(screen=None)

                                            
                                            if post.text:
                                                text post.text:
                                                    size 20
                                                    color "#000000"
                                                    font "DejaVuSans.ttf"
                                                    outlines [(0, "#000000", 0, 0)]

                                            
                                            if post.image is not None:
                                                imagebutton:
                                                    idle Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                    hover Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                    action [
                                                        SetVariable("viewing_photo", True),
                                                        SetVariable("current_photo", post.image),
                                                        Show("photo_viewer")
                                                    ]

                                frame:
                                    background "#CCCCCC"
                                    xfill True
                                    ysize 3

    vbox:
        align(0.5, 0.9)
        textbutton "Back":
            text_font "DejaVuSans.ttf"
            text_outlines [(0, "#000000", 0, 0)]
            action [Show("phone_home"), Hide(screen=None)]

screen profile_screen(profile, back_screen="feed"):
    modal True

    window:
        style "phone_bg"

        viewport:
            xpos 13
            yalign 0.3
            xsize 450
            ysize 750
            scrollbars "vertical"
            mousewheel True
            draggable True
            
            vbox:
                spacing 15
                xfill True
                
                text "Profile"

                if profile.visible:
                    pass
                
                grid 3 10:
                    for post in profile.posts:
                        if post.visible:
                            pass

    vbox:
        align(0.5, 0.9)
        textbutton "Back":
            text_font "DejaVuSans.ttf"
            text_outlines [(0, "#000000", 0, 0)]
            action [Show("feed"), Hide(screen=None)]

screen post_comments(post, back_screen="feed"):
    modal True

    window:
        style "phone_bg"

        viewport:
            xalign 0.2
            yalign 0.3
            xsize 450
            ysize 750
            draggable True
            scrollbars "vertical"
            mousewheel True
                
            vbox:
                spacing 15
                xalign 0.5
                
                # Show the post at the top
                frame:
                    xsize 430
                    background "#ffffff"
                    padding (10, 10)
                    
                    vbox:
                        spacing 8
                        
                        # Post author info
                        hbox:
                            spacing 10
                            
                            add post.author.pfp:
                                size (65, 65)
                            
                            style "post_bg"
                            vbox:
                                # align (0.5, 0.5)
                                text post.author.get_username():
                                    size 20
                                    font "DejaVuSans.ttf"
                                    outlines [(0, "#000000", 0, 0)]
                                    color "#000000"
                                    bold True

                                imagebutton:
                                    idle Transform(post.image, fit="contain", xsize=280, ysize=280)
                                    hover Transform(post.image, fit="contain", xsize=280, ysize=280)
                                    action [SetVariable("viewing_photo", True), SetVariable("current_photo", post.image), Show("photo_viewer")]
                                
                                text post.caption:
                                    xalign 0.0
                                    font "DejaVuSans.ttf"
                                    outlines [(0, "#000000", 0, 0)]
                                    size 20
                                    color "#000000"
                        

                # Divider
                frame:
                    background "#CCCCCC"
                    xfill True
                    ysize 3
                
                # Comments section
                if len(post.comments) > 1 or len(post.comments) == 0:
                    text f"{post.get_comments()} Comments" size 22 color "#666666" xalign 0.0 font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)]
                elif len(post.comments) == 1:
                    text f"{post.get_comments()} Comment" size 22 color "#666666" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)] xalign 0.0
                
                # Loop through comments
                for comment in post.comments:
                    if comment.visible:
                        frame:
                            style "comment"
                            xsize 430
                            
                            vbox:
                                spacing 8
                            
                                hbox:
                                    xfill True
                                    
                                    hbox:
                                        spacing 10
                                        xalign 0.0
                                        
                                        add comment.author.pfp:
                                            size (50, 50)
                                        
                                        text comment.author.get_username():
                                            size 20
                                            font "DejaVuSans.ttf"
                                            outlines [(0, "#000000", 0, 0)]
                                            color "#000000"

                                    
                                    hbox:
                                        xalign 1.0
                                        
                                        if comment.player_liked:
                                            textbutton "❤️ [comment.get_likes()]":
                                                text_size 20
                                                text_font "DejaVuSans.ttf"
                                                text_outlines [(0, "#000000", 0, 0)]
                                                text_color "#000000"
                                                background None
                                                action Function(comment.toggle_like)
                                        else:
                                            textbutton "🤍 [comment.get_likes()]":
                                                text_size 20
                                                text_font "DejaVuSans.ttf"
                                                text_outlines [(0, "#000000", 0, 0)]
                                                text_color "#000000"
                                                background None
                                                action Function(comment.toggle_like)
                                
                                # Comment text
                                text comment.text:
                                    font "DejaVuSans.ttf"
                                    outlines [(0, "#000000", 0, 0)]
                                    size 20
                                    color "#000000"
                                    xmaximum 400

    vbox:
        align(0.5, 0.9)
        textbutton "Back":
            text_font "DejaVuSans.ttf"
            text_outlines [(0, "#000000", 0, 0)]
            action If(
                back_screen == "profile_screen",
                [Show("profile_screen", profile=post.author, back_screen="feed"), Hide(screen=None)],
                [Show(back_screen), Hide(screen=None)]
            )

