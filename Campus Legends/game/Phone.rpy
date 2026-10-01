default viewing_photo = False
default current_photo = None
default feed = []
default back_post = None

init -10 python:

#====================================
# CLASSES
#====================================

    class PhoneState(NoRollback):
        def __init__(self):
            self.initialized = False
            self.apps = []
            self.contacts = []
            self.all_profiles = []

        def reset(self):
            self.initialized = False
            self.apps = []
            self.contacts = []
            self.feed = []
            self.all_profiles = []

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
                
            if player_text or player_image:
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
            new_sms(contact, None, self.text, self.image)
            contact.chat.append(self.response)
            self.response.delay = 1.0
#====================================
# TWATTER CLASSES
#====================================
    
    class Profile:
        def __init__(self, username, followers=0, following=0, pfp="images/phone/icon.png", description=None):
            self.username = username
            self.followers = followers
            self.following = following
            self.pfp = pfp
            self.description = description
            self.posts = []
            self.visible = False
            self.added = False

        def show_profile(self):
            self.visible = True
    
    
    class Post:
        def __init__(self, owner=None, text=None, image=None, follow_up=None, initial_likes=0, initial_retwats=0, from_player=False):
            self.owner = owner
            self.text = text
            self.image = image
            self.follow_up = follow_up
            self.initial_likes = initial_likes
            self.initial_retwats = initial_retwats
            self.from_player = from_player
            self.comments = []
            self.comment_choices = []
            self.player_liked = False
            self.player_retwat = False
            self.resolved = False
            self.visible = False

        def mark_resolved(self):
            self.resolved = True

        def toggle_likes(self):
            self.player_liked = not self.player_liked
        
        def toggle_retwats(self):
            self.player_retwat = not self.player_retwat
        
        def get_likes(self):
            return str(self.initial_likes +(1 if self.player_liked else 0))

        def get_retwats(self):
            return str(self.initial_retwats +(1 if self.player_retwat else 0))
        
        def get_comments(self):
            return str(len(self.comments))
        
        def new_comment(self, owner, text=None, image=None):
            from_player = owner is None
            comment = Comment(owner=owner, text=text, image=image, from_player=from_player)       
            self.comments.append(comment)
            comment.show_comment()

            return comment

        def show_comment_choices(self):
            for comment in self.comment_choices:
                if not comment.chosen:
                    comment.show_comment()
        
        def hide_comment_choices(self):
            for comment in self.comment_choices:
                if self.resolved:
                    comment.hide_comment()

        def comment_chain(self, player_text=None, npc_text=None, player_image=None, npc_image=None):
            if npc_image:
                npc_response = Comment(self.owner, image=npc_image)
            elif npc_text:
                npc_response = Comment(self.owner, text=npc_text)
            elif npc_text and npc_image:
                npc_response = Comment(self.owner, text=npc_text, image=npc_image)
            
            if player_image:
                player_comment = Comment(owner=None, image=player_image, response=npc_response)
            elif player_text:
                player_comment = Comment(owner=None, text=player_text,  response=npc_response)
            elif player_text and player_image:
                player_comment = Comment(owner=None, text=player_text, image=player_image, response=npc_response)

            if player_text or player_image or player_text and player_image:
                self.comment_choices.append(player_comment)    

                if self.visible:
                    player_comment.show_comment()
            else:
                self.follow_up = npc_response

            return npc_response
        

    class Comment(Post):
        def __init__(self, owner=None, text=None, image=None, from_player=False, response=None):
            super().__init__(owner=owner, text=text, image=image, from_player=from_player)
            self.response = response
            self.chosen = False

        def hide_comment(self):
            self.visible = False
        
        def show_comment(self):
            self.visible = True


        def choose(self, post):
            self.chosen = True
            post.new_comment(owner=self.owner, text=self.text, image=self.image)
            if self.response:
                post.comments.append(self.response)
                self.response.visible = True

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

    def new_post(owner, text=None, image=None):
        from_player = owner is None
        post = Post(owner=owner, text=text, image=image, from_player=from_player)   
        owner.posts.append(post)   
        feed.append(post)
        post.visible = True
        return post

    
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

style post_bg:
    xalign 0.5
    yalign 0.5
    xfill True
    yfill False
    yminimum 0
    xminimum 0
    background "#FFFFFF"
    padding(15,10)

style readable:
    font "DejaVuSans.ttf"
    color "#000000"
    size 20
    outlines [(0, "#000000", 0, 0)]

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
                                            text sms.text style "readable":
                                                size 20
                                                color text_color

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
                            action [
                            Function(choice.choose, contact),
                            Function(sms.mark_resolved),
                            Function(sms.player_replied),
                            Function(sms.hide_choices)
                            ]
                            xfill True
                            hover_background "#0066FF"
                            idle_background "#999999"
                            padding (10, 10)
                            
                            if choice.text and not choice.image:
                                text choice.text:
                                    style "readable"
                                    idle_color "#000000"
                                    hover_color "#FFFFFF"
                            
                            elif choice.image and not choice.text: 
                                add choice.image:
                                    size (280, 200)
    if viewing_photo:
        use photo_viewer()
                        

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

            viewport:
                xalign 0.5
                yalign 0.5
                xsize 450
                ysize 800
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 5
                    button:
                        xfill True
                        background "#dddddd"
                        action [Show("profile_screen", profile=player_profile), Hide(screen=None)]
                        hbox:
                            add player_profile.pfp:
                                size (60, 60)
                            text player_profile.username:
                                color "#000000"
                                size 24
                                yalign 0.5
                    frame:
                        background "#CCCCCC"
                        xfill True
                        ysize 1
                    
                    for post in feed:
                        if post.visible and (post.owner is player_profile or post.owner.visible):
                            vbox:     
                                hbox:
                                    button:
                                        xfill True
                                        background "#FFFFFF"
                                        action [Show("profile_screen", profile=post.owner), Hide(screen=None)]
                                        hbox:
                                            add post.owner.pfp:
                                                size (40, 40)
                                            text post.owner.username:
                                                color "#000000"
                                                size 24
                                                yalign 0.5
                                        
                                if post.image and not post.text:
                                    frame:
                                        style "post_bg"
                            
                                        vbox:
                                            spacing 5
                                            xalign 0.5
                                            imagebutton:
                                                idle Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                hover Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                action [SetVariable("viewing_photo", True), SetVariable("current_photo", post.image)]
                                            
                                elif post.text and not post.image:        
                                    frame:
                                        style "post_bg"
                                        
                                        vbox:
                                            spacing 15
                                            xalign 0.5
                                            text post.text style "readable"
                                                        
                                        
                                elif post.text and post.image:
                                    frame:
                                        style "post_bg"

                                        vbox:
                                            xalign 0.5
                                            text post.text style "readable":
                                                xalign 0.5
                                                    
                                            vbox:
                                                spacing 5
                                                xalign 0.5
                                                imagebutton:
                                                    idle Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                    hover Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                    action [SetVariable("viewing_photo", True), SetVariable("current_photo", post.image)]

                                frame:
                                    style "post_bg"
                                    hbox:
                                        xalign 0.5
                                        button:
                                            hbox:
                                                add "images/phone/icons/comment_icon.png":
                                                    size (35,35)
                                                        
                                                text [post.get_comments()]:
                                                    style "readable"
                                            action [Show("post_comments", post=post, back_screen="feed"), Hide(screen=None)]

                                        if post.player_retwat:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/retwat_icon.png":
                                                        size (35, 35)

                                                    text [post.get_retwats()]:
                                                        style "readable"
                                                action Function(post.toggle_retwats)

                                        else:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/retwat_icon.png":
                                                        size (35, 35)

                                                    text [post.get_retwats()]:
                                                        style "readable"
                                                action Function(post.toggle_retwats)
                                                
                                        if post.player_liked:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/red_heart_icon.png":
                                                        size (35, 35)

                                                    text [post.get_likes()]:
                                                        style "readable"
                                                action Function(post.toggle_likes)
                                                
                                        else:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/white_heart_icon.png":
                                                        size (35, 35)

                                                    text [post.get_likes()]:
                                                        style "readable"
                                                action Function(post.toggle_likes)

                                        
                            frame:
                                background "#CCCCCC"
                                xfill True
                                ysize 1

    vbox:
        align(0.5, 0.93)
        textbutton "Back":
            action [Show("phone_home"), Hide(screen=None)]
    
    if viewing_photo:
        use photo_viewer

screen profile_screen(profile, back_screen="feed", back_args=None):
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

            viewport:
                xalign 0.5
                yalign 0.5
                xsize 450
                ysize 800
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 5

                    frame:
                        xfill True
                        yfill False
                        background "#dddddd"
                        vbox:
                            spacing 15
                            hbox:
                                spacing 5
                                add profile.pfp:
                                    size (75,75)
                                
                                text profile.username:
                                    style "readable"
                                    yalign 0.5
                            
                            if profile.description:
                                text profile.description:
                                    style "readable"

                            hbox:
                                spacing 15

                                text f"{profile.following} Following":
                                    style "readable"
                                
                                text f"{profile.followers} Followers":
                                    style "readable"
                    
                    frame:
                        background "#CCCCCC"
                        xfill True
                        ysize 1

                    for post in profile.posts:
                        if post.visible:
                            vbox:
                                
                                hbox:
                                    button:
                                        xfill True
                                        background "#FFFFFF"
                                        action NullAction()
                                        hbox:
                                            add profile.pfp:
                                                size (40, 40)
                                            text profile.username:
                                                color "#000000"
                                                size 24
                                                yalign 0.5
                                
                                if post.image and not post.text:
                                            frame:
                                                style "post_bg"
                            
                                                vbox:
                                                    spacing 5
                                                    xalign 0.5
                                                    imagebutton:
                                                        idle Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                        hover Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                        action [SetVariable("viewing_photo", True), SetVariable("current_photo", post.image)]
                                            
                                elif post.text and not post.image:        
                                    frame:
                                        style "post_bg"
                                
                                        vbox:
                                            spacing 15
                                            xalign 0.5
                                            text post.text style "readable"
                                                
                                
                                elif post.text and post.image:
                                    frame:
                                        style "post_bg"

                                        vbox:
                                            xalign 0.5
                                            text post.text style "readable":
                                                xalign 0.5
                                            
                                            vbox:
                                                spacing 5
                                                xalign 0.5
                                                imagebutton:
                                                    idle Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                    hover Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                    action [SetVariable("viewing_photo", True), SetVariable("current_photo", post.image)]

                                frame:
                                    style "post_bg"
                                    hbox:
                                        xalign 0.5
                                        button:
                                            hbox:
                                                add "images/phone/icons/comment_icon.png":
                                                    size (35,35)
                                                
                                                text [post.get_comments()]:
                                                    style "readable"
                                            action [Show("post_comments", post=post, back_screen="profile_screen", back_args={"profile": profile, "back_screen": back_screen, "back_args": back_args}), Hide(screen=None)]

                                        if post.player_retwat:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/retwat_icon.png":
                                                        size (35, 35)

                                                    text [post.get_retwats()]:
                                                        style "readable"
                                                action Function(post.toggle_retwats)

                                        else:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/retwat_icon.png":
                                                        size (35, 35)

                                                    text [post.get_retwats()]:
                                                        style "readable"
                                                action Function(post.toggle_retwats)
                                        
                                        if post.player_liked:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/red_heart_icon.png":
                                                        size (35, 35)

                                                    text [post.get_likes()]:
                                                        style "readable"
                                                action Function(post.toggle_likes)
                                        
                                        else:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/white_heart_icon.png":
                                                        size (35, 35)

                                                    text [post.get_likes()]:
                                                        style "readable"
                                                action Function(post.toggle_likes)

                                        
                                frame:
                                    background "#CCCCCC"
                                    xfill True
                                    ysize 1

    vbox:
        align(0.5, 0.93)
        textbutton "Back":
            action [Show(back_screen, **(back_args or {})), Hide(screen=None)]

    if viewing_photo:
        use photo_viewer

screen post_comments(post, back_screen="feed", back_args=None):
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

            viewport:
                xalign 0.5
                yalign 0.5
                xsize 450
                ysize 800
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 5

                    frame:
                        style "post_bg"

                        if post.visible:
                            vbox:
                                if post.image and not post.text:
                                    frame:
                                        style "post_bg"
                    
                                        vbox:
                                            spacing 5
                                            xalign 0.5
                                            imagebutton:
                                                idle Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                hover Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                action [SetVariable("viewing_photo", True), SetVariable("current_photo", post.image)]
                                            
                                elif post.text and not post.image:        
                                    frame:
                                        style "post_bg"
                                
                                        vbox:
                                            spacing 15
                                            xalign 0.5
                                            text post.text style "readable"
                                                
                                
                                elif post.text and post.image:
                                    frame:
                                        style "post_bg"

                                        vbox:
                                            xalign 0.5
                                            text post.text style "readable":
                                                xalign 0.5
                                            
                                            vbox:
                                                spacing 5
                                                xalign 0.5
                                                imagebutton:
                                                    idle Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                    hover Transform(post.image, fit="contain", xsize=280, ysize=200)
                                                    action [SetVariable("viewing_photo", True), SetVariable("current_photo", post.image)]

                                frame:
                                    style "post_bg"
                                    hbox:
                                        xalign 0.5
                                        button:
                                            hbox:
                                                add "images/phone/icons/comment_icon.png":
                                                    size (35,35)
                                                
                                                text [post.get_comments()]:
                                                    style "readable"
                                            action NullAction()

                                        if post.player_retwat:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/retwat_icon.png":
                                                        size (35, 35)

                                                    text [post.get_retwats()]:
                                                        style "readable"
                                                action Function(post.toggle_retwats)

                                        else:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/retwat_icon.png":
                                                        size (35, 35)

                                                    text [post.get_retwats()]:
                                                        style "readable"
                                                action Function(post.toggle_retwats)
                                        
                                        if post.player_liked:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/red_heart_icon.png":
                                                        size (35, 35)

                                                    text [post.get_likes()]:
                                                        style "readable"
                                                action Function(post.toggle_likes)
                                        
                                        else:
                                            button:
                                                hbox:
                                                    add "images/phone/icons/white_heart_icon.png":
                                                        size (35, 35)

                                                    text [post.get_likes()]:
                                                        style "readable"
                                                action Function(post.toggle_likes)
  
                                frame:
                                    background "#CCCCCC"
                                    xfill True
                                    ysize 1

                                for comment in post.comments:
                                    if comment.visible:
                                        frame:
                                            style "post_bg"
                                            vbox:
                                                xfill True
                                                spacing 5
                                            
                                                    
                                                button:
                                                    action [Show("profile_screen", profile=(player_profile if comment.from_player else comment.owner), back_screen="post_comments", back_args={"post": post, "back_screen": back_screen, "back_args": back_args}), Hide(screen=None)]
                                                    hbox:
                                                        $ profile_picture = player_profile.pfp if comment.from_player else comment.owner.pfp
                                                        $ profile_username = player_profile.username if comment.from_player else comment.owner.username
                                                        
                                                        add profile_picture:
                                                            size (75,75)
                                                        
                                                        text profile_username:
                                                            style "readable"
                                                            yalign 0.5
                                                

                                                if comment.text and not comment.image:
                                                    text comment.text:
                                                        style "readable"
                                                
                                                elif comment.image and not comment.text:
                                                    imagebutton:
                                                        idle Transform(comment.image, fit="contain", xsize=280, ysize=200)
                                                        hover Transform(comment.image, fit="contain", xsize=280, ysize=200)
                                                        action [SetVariable("viewing_photo", True), SetVariable("current_photo", comment.image)]
                                                
                                                elif comment.text and comment.image:
                                                    text comment.text:
                                                        style "readable"
                                                    
                                                    imagebutton:
                                                        idle Transform(comment.image, fit="contain", xsize=280, ysize=200)
                                                        hover Transform(comment.image, fit="contain", xsize=280, ysize=200)
                                                        action [SetVariable("viewing_photo", True), SetVariable("current_photo", comment.image)]

                                        frame:
                                            background "#CCCCCC"
                                            xfill True
                                            ysize 1

    vbox:
        align(0.5, 0.93)
        textbutton "Back":
            action [Show(back_screen, **(back_args or {})), Hide(screen=None)]

    frame:
        xpos 1230
        yalign 0.5
        xsize 450
        ysize 800
        background None
        padding (20, 20)

        vbox:
            spacing 15
            for comment in post.comment_choices:
                if comment.visible:
                    vbox:
                        spacing 5
                        button:
                            action [
                                Function(comment.choose, post),
                                Function(post.mark_resolved),
                                Function(post.hide_comment_choices)
                                    
                                ]
                            xfill True
                            hover_background "#0066FF"
                            idle_background "#999999"
                            padding (10, 10)
    
                            if comment.text and not comment.image:
                                text comment.text:
                                    style "readable"
                                    idle_color "#000000"
                                    hover_color "#FFFFFF"
                                
                            elif comment.image and not comment.text:
                                
                                add comment.image:
                                    size (280, 200)
                            
                            elif comment.text and comment.image:
                                
                                text comment.text:
                                    style "readable"
                                    idle_color "#000000"
                                    hover_color "#FFFFFF"
                                
                                add comment.image:
                                    size (280, 200)

    if viewing_photo:
        use photo_viewer                        