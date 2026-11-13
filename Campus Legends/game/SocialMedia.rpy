############################################################
# SOCIAL MEDIA SYSTEM
# Campus Legends
#
# Classes and profile definitions
# Initialization is handled by init_phone .rpy
############################################################


############################################################
# SOCIAL MEDIA CLASSES
############################################################

init -9 python:

    class Profile(NoRollback):
        def __init__(self, username, display_name=None, pfp="images/phone/icon.png"):
            self.username = username
            self.display_name = display_name if display_name else username
            self.pfp = pfp
            self.posts = []
            self.visible = True

        def get_username(self):
            return self.username


    class Post(NoRollback):
        def __init__(
            self,
            author,
            text="",
            image=None,
            caption="",
            comments=None,
            visible=True
        ):
            self.author = author
            self.text = text
            self.image = image
            self.caption = caption if caption else text
            self.comments = comments if comments else []
            self.visible = visible

        def get_comments(self):
            return len(self.comments)


    class Comment(NoRollback):
        def __init__(
            self,
            author,
            text="",
            likes=0,
            visible=True
        ):
            self.author = author
            self.text = text
            self.likes = likes
            self.visible = visible
            self.player_liked = False

        def get_likes(self):
            return self.likes

        def toggle_like(self):

            if self.player_liked:
                self.likes -= 1
                self.player_liked = False

            else:
                self.likes += 1
                self.player_liked = True


############################################################
# PROFILES
############################################################

default player_pf = Profile(
    "New Student",
    "New Student",
    "images/phone/icon.png"
)

default sienna_pf = Profile(
    "Sienna",
    "Sienna",
    "images/phone/icon.png"
)

default jess_pf = Profile(
    "Jess",
    "Jess",
    "images/phone/icon.png"
)

default malik_pf = Profile(
    "Malik",
    "Malik",
    "images/phone/icon.png"
)

default norah_pf = Profile(
    "Norah",
    "Norah",
    "images/phone/icon.png"
)

default tiffany_pf = Profile(
    "Tiff",
    "Tiffany",
    "images/phone/icon.png"
)

default misty_pf = Profile(
    "Misty",
    "Misty",
    "images/phone/icon.png"
)

default kaia_pf = Profile(
    "Kaia",
    "Kaia",
    "images/phone/icon.png"
)

default aubrey_pf = Profile(
    "Aubrey",
    "Aubrey",
    "images/phone/icon.png"
)