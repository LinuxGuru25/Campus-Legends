init offset = 1
default force_phone = False
default viewing_photo = False
default current_photo = None
default feed_visible = False
default profile_tile = (120, 120)
default player_username = f"@{player_name}_123"
default phone_epoch = 0

init -10 python:

    class App(NoRollback):
        def __init__(self, app_screen, name, icon):
            self.app_screen = app_screen # What screen will show when the app is clicked
            self.name = name # The app's name
            self.icon = icon # The app's icon
    
    # Apps in order of index [0] = First app, [1] = Second app, etc.
    apps = [
            App("contacts", "Messages", "images/phone/icons/message_icon.png"),            
            App("feed", "Twatter", "images/phone/icons/twatter_icon.png")
        ]
    class Contact(NoRollback):
        def __init__(self, contact_id, contact_name, pfp):
            self.contact_id = contact_id
            self.contact_name = contact_name
            self.pfp = pfp
            self.chat = []
            self.has_unread = False
            self.convo_done = False
            self._initialized = False

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
            self.added = False

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
            """ Will expire old optional reply choices """
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

    class Profile(NoRollback):
        def __init__(self, user_id, username, pfp=None, bio="", starting_followers=0, following=0):
            self.user_id = user_id
            self.username = username
            self.pfp = pfp
            self.bio = bio
            self.starting_followers = starting_followers
            self.following = following
            self.posts = []
            self.visible = False
            self._initialized = False
            

        def get_user_id(self):
            """ Returns user id as a string """
            return str(self.user_id)

        def get_username(self):
            """ Adds @ in front of username and returns as string """
            return (f"@{self.username}")

        def add_post(self, post):
            """ Adds a post to this post """
            self.posts.append(post)
        
        def get_posts(self):
            """ Get total number of posts """
            return len(self.posts)
        
        def show_profile(self):
            self.visible = True
        
        def hide_profile(self):
            self.visible = False
    
    class Post(NoRollback):
        def __init__(self, post_id, author, image, caption="", starting_likes=0):
            self.post_id = post_id
            self.author = author
            self.image = image
            self.caption = caption
            self.starting_likes = starting_likes
            self.player_liked = False
            self.visible = False
            self.comments = []
            self.added = False

        def toggle_like(self):
            """Toggles if the player clicks like"""
            self.player_liked = not self.player_liked
        
        def get_post_id(self):
            """ Returns post id as a string """
            return str(self.post_id)

        def get_likes(self):
            return self.starting_likes +(1 if self.player_liked else 0)

        def show_post(self):
            self.visible = True
        
        def hide_post(self):
            self.visible = False

        def add_comment(self, comment):
            """ Adds a comment to this post """
            self.comments.append(comment)
        
        def get_comments(self):
            """ Get total number of comments """
            return len(self.comments)

    all_posts = []

    class Comment(NoRollback):
        def __init__(self, comment_id, author, text, pfp=None, starting_likes=0):
            self.comment_id = comment_id
            self.author = author
            self.text = text
            self.pfp = pfp
            self.starting_likes = starting_likes
            self.player_liked = False
            self.visible = False
            self.added = False
        
        def toggle_like(self):
            self.player_liked = not self.player_liked
        
        def get_likes(self):
            return self.starting_likes + (1 if self.player_liked else 0)
        
        def show_comment(self):
            self.visible = True
        
        def hide_comment(self):
            self.visible = False
    
    class PhoneState(NoRollback):
        def __init__(self):
            self.initialized = False

        def reset(self):
            self.initialized = False
            all_posts.clear()
            for contact in contacts:
                contact.chat.clear()
                contact.has_unread = False
                contact.convo_done = False

    phone_state = PhoneState()

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
        if not sms.added:
            sms.added = True
            contact.mark_unread()
            contact.add_sms(sms)
            sms.show_text()
            sms.show_choices()

    def add_feed(post):
        all_posts.append(post)

    def new_post(profile, post):
        if not post.added:
            post.added = True
            profile.show_profile()
            profile.add_post(post)
            post.show_post()
            add_feed(post)

    def new_comment(post, comment):
        if not comment.added:
            comment.added = True
            comment.show_comment()
            post.add_comment(comment)



    
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

style post_bg:
    xalign 0.5
    xmaximum 760
    background "#ffffff"
    padding (5, 5)

style username:
    xalign 0.5
    xmaximum 300
    idle_color "#000000"
    hover_color "#646464"
    size 20
    background None
    padding (5, 5)

style like_count:
    color "#000000"
    size 25

style comment:
    color "#000000"
    size 18

style pl_username:
    xalign 0.5
    xmaximum 300
    idle_color "#000000"
    hover_color "#646464"
    size 25
    bold True
    padding (5, 5)
# ------------------------------------------------------------
# SCREENS
# ------------------------------------------------------------

screen phone_button():
    imagebutton:
        auto "phone/Phone_button_%s.png"
        focus_mask True 
        action [Show("phone_home"), Hide("phone_button")]

screen phone_home():
    modal True

    window:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 1000
        background "images/phone/base.png"
        
        frame:
            xalign 0.5
            yalign 0.5
            xsize 450
            ysize 775
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
                            text app.name:
                                font "DejaVuSans.ttf"
                                size 20
                                outlines [(1, "#000000", 0, 0)]
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
        background "images/phone/base.png"
        
        text "Contacts" size 40 color "#000000" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)] xalign 0.5 yalign 0.07

        viewport:
            xalign 0.5
            yalign 0.5
            xsize 450
            ysize 775
            scrollbars "vertical"
            draggable True
            mousewheel True
            

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
                            
                                null height 5
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
        xsize 600
        ysize 1000
        background "images/phone/base.png"
    
        python:
            _msg_count = sum(1 for _s in contact.chat if _s.visible)
            if not hasattr(chat_yadj, '_last_count') or chat_yadj._last_count != _msg_count:
                chat_yadj._last_count = _msg_count
                chat_yadj.value = float("inf")



        viewport:
            xalign 0.5
            yalign 0.5
            xsize 450
            ysize 775
            scrollbars "vertical"
            mousewheel True
            draggable True
            yadjustment chat_yadj
            
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
                                        text sms.text style "default":
                                            size 20
                                            font "DejaVuSans.ttf"
                                            outlines [(0, "#000000", 0, 0)]
                                            color "#FFFFFF"
                            else:
                                frame:
                                    style "gray_bg"

                                    vbox:
                                        spacing 15
                                        text sms.text style "default":
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
                                                Function(sms.player_replied)
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


screen feed():
    modal True

    window:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 1000
        background "images/phone/base.png"

        text "Feed" size 40 color "#000000" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)] xalign 0.5 yalign 0.07

        viewport:
                xalign 0.5
                yalign 0.5
                xsize 450
                ysize 775
                scrollbars "vertical"
                draggable True
                mousewheel True
                
                
                if feed_visible:
                    vbox:
                        # Player profile button
                        frame:
                            align (0.0, 0.5)
                            background None
                            xfill True
                            ysize 100

                            hbox:
                                add player_pf.pfp:
                                    size (65, 65)
                                textbutton "Your Profile":
                                    text_style "pl_username"
                                    text_font "DejaVuSans.ttf"
                                    text_outlines [(0, "#000000", 0, 0)]
                                    action [Show("profile_screen", profile=player_pf), Hide(screen=None)]
                            
                        # Divider
                        frame:
                            background "#CCCCCC"
                            xfill True
                            ysize 3
                        vbox:
                            xalign 0.5
                            for post in all_posts:
                                if post.visible:
                                    frame:
                                        style "post_bg"
                                        vbox:
                                            spacing 5
                                            # Posted image (Square images look the best)
                                            imagebutton:
                                                idle Transform(post.image, fit="contain", xsize=280, ysize=280)
                                                hover Transform(post.image, fit="contain", xsize=280, ysize=280)
                                                action [SetVariable("viewing_photo", True), SetVariable("current_photo", post.image), Show("photo_viewer")]
                                            xfill True

                                            hbox:
                                                spacing 10
                                                xalign 0.0
                                                # Author pfp and username
                                                add post.author.pfp:
                                                    size (65, 65)

                                                textbutton post.author.get_username():
                                                    padding (5, 5)
                                                    text_style "username"
                                                    text_font "DejaVuSans.ttf"
                                                    text_outlines [(0, "#000000", 0, 0)]
                                                    action [Show("profile_screen", profile=post.author), Hide(screen=None)]
                                            hbox:
                                                
                                                # Like button
                                                if post.player_liked:
                                                    textbutton "❤️ [post.get_likes()]":
                                                        text_font "DejaVuSans.ttf"
                                                        text_outlines [(0, "#000000", 0, 0)]
                                                        text_size 25
                                                        text_color "#000000"
                                                        background None
                                                        action Function(post.toggle_like)
                                                else:
                                                    textbutton "🤍 [post.get_likes()]":
                                                        text_font "DejaVuSans.ttf"
                                                        text_outlines [(0, "#000000", 0, 0)]
                                                        text_size 25
                                                        text_color "#000000"
                                                        background None
                                                        action Function(post.toggle_like)
                                                # Comments button
                                                textbutton "💬 [post.get_comments()]" :
                                                    text_font "DejaVuSans.ttf"
                                                    text_outlines [(0, "#000000", 0, 0)]
                                                    text_size 25
                                                    text_color "#000000"        
                                                    background None
                                                    action [Show("post_comments", post=post, back_screen="feed"), Hide(screen=None)]
                                # Divider
                                null height 5
                                frame:
                                    background "#CCCCCC"
                                    xfill True
                                    ysize 3
    vbox:
        align(0.5, 0.95)
        textbutton "Back":
            text_font "DejaVuSans.ttf"
            text_outlines [(0, "#000000", 0, 0)]
            action [Show("phone_home"), Hide(screen=None)]

screen tile_screen(post, back_screen="profile_screen"):
    frame:
        xysize profile_tile
        background None
        padding (5, 5)

        imagebutton:
            idle Transform(post.image, fit="cover", xysize=profile_tile)
            hover Transform(post.image, fit="cover", xysize=profile_tile)
            action [Show("post_comments", post=post, back_screen=back_screen), Hide(screen=None)]

screen profile_info(profile):
    vbox:
        xsize 430
        xalign 0.25
        yalign 0.25
        # pfp and bio text
        vbox:
            spacing 5
            frame:
                background None
                xfill True
                yalign 0.5
                hbox:
                    add profile.pfp xysize (150,150)
                    vbox:
                        if len(profile.posts) > 1 or len(profile.posts) == 0:
                            text f"{len(profile.posts)}" size 20 color "#000000" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)]
                            text "Posts" size 20 color "#000000" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)]
                        elif len(profile.posts) == 1:
                            text f"{len(profile.posts)}" size 20 color "#000000" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)]
                            text "Post" size 20 color "#000000"
                        
                        
                    null width 15
                    vbox:
                        text f"{profile.starting_followers}"  size 20 color "#000000" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)]
                        text "Followers" size 20 color "#000000" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)]
                    null width 15
                    vbox:
                        text f"{profile.following}" size 20 color "#000000" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)]
                        text "Following" size 20 color "#000000" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)]

            text f"{profile.username}" color "#000000" font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)] size 23
            text f"{profile.bio}" color "#000000" size 20 font "DejaVuSans.ttf" outlines [(0, "#000000", 0, 0)]
        frame:
            background "#CCCCCC"
            xfill True
            ysize 3

screen profile_screen(profile, back_screen="feed"):
    modal True

    window:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 1000
        background "images/phone/base.png"

        viewport:
            xalign 0.5
            yalign 0.5
            xsize 450
            ysize 775
            scrollbars "vertical"
            mousewheel True
            draggable True
            
            vbox:
                spacing 15
                xfill True
                
                if profile.visible:
                    use profile_info(profile)
                
                grid 3 10:
                    for post in profile.posts:
                        if post.visible:
                            use tile_screen(post, back_screen="profile_screen")

    vbox:
        align(0.5, 0.95)
        textbutton "Back":
            text_font "DejaVuSans.ttf"
            text_outlines [(0, "#000000", 0, 0)]
            action [Show("feed"), Hide(screen=None)]

screen post_comments(post, back_screen="feed"):
    modal True

    window:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 1000
        background "images/phone/base.png"

        viewport:
            xalign 0.5
            yalign 0.5
            xsize 450
            ysize 775
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
        align(0.5, 0.95)
        textbutton "Back":
            text_font "DejaVuSans.ttf"
            text_outlines [(0, "#000000", 0, 0)]
            action If(
                back_screen == "profile_screen",
                [Show("profile_screen", profile=post.author, back_screen="feed"), Hide(screen=None)],
                [Show(back_screen), Hide(screen=None)]
            )

