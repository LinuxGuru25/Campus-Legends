default persistent.replay_unlocks = {}

init python:

    REPLAY_DATA = {
        "Aubrey": [
            ("Label Name", "thumbnail.png"),
        ],

        "Jess": [
            ("Label Name", "thumbnail.png"),
        ],

        "Kaia": [
            ("Label Name", "thumbnail.png"),
        ],

        "Misty": [
            ("Label Name", "thumbnail.png"),
        ],

        "Norah": [
            ("Label Name", "thumbnail.png"),
        ],

        "Sienna": [
            ("Label Name", "thumbnail.png"),
        ],

        "Tiffany": [
            ("Label Name", "thumbnail.png"),
        ],

        "Others": [
            ("Label Name", "thumbnail.png"),
        ],
    }

    def is_unlocked(label_name):
        if persistent.replay_unlocks is None:
            return False
        return persistent.replay_unlocks.get(label_name, False)

    def unlock_replay(label_name):
        if persistent.replay_unlocks is None:
            persistent.replay_unlocks = {}
        persistent.replay_unlocks[label_name] = True
        renpy.save_persistent()

    def unlock_all_replays():
        if persistent.replay_unlocks is None:
            persistent.replay_unlocks = {}
        for character, items in REPLAY_DATA.items():
            for label_name, thumbnail in items:
                persistent.replay_unlocks[label_name] = True
        renpy.save_persistent()

    def setReplay():
        global MCname
        global player_name

        if persistent.MCname:
            MCname = persistent.MCname
        else:
            MCname = "Emanuel"


label galleryname:
    
    scene black
    if not persistent.gallerynamechange:
        $ persistent.galleryname = renpy.input("Enter your name:", allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz").strip()
        if persistent.galleryname == "":
            $ persistent.galleryname = "Emanuel"
        $ persistent.gallerynamechange = True
        return
    elif True:
        return

label galleryrename:

    scene black
    $ persistent.galleryname = renpy.input("Enter your name:", allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz").strip()
    if persistent.galleryname == "":
        $ persistent.galleryname = "Emanuel"
    $ persistent.gallerynamechange = True
    return

screen character_select():
    tag menu

    add "gallery_images/bg_gallery.png"

    hbox:
        yalign 0.5
        xalign 0.5

        grid 4 2:
            spacing 15

            for character, item in REPLAY_DATA.items():
                for label_name, thumbnail in items:
                    vbox:
                        spacing 15

                        button:
                            add "thumbnail.png"
                            xsize 380
                            ysize 200
                            xalign 0.5
                            action ShowMenu("replay_screen", character=character), Hide("character_select")

                        text character size 20 xalign 0.5 yalign 1.0
    
    textbutton "Return":
        text_size 40
        xalign 0.05
        yalign 0.95
        action Return()

    textbutton "Change Name":
        text_size 40  
        yalign 0.95 
        xalign 0.95 
        action [ui.callsinnewcontext("galleryrename")]

screen replay_screen(character):
    tag menu

    add "gallery_images/bg_gallery.png"

    $ items = REPLAY_DATA[character]

    hbox:
        yalign 0.5
        xalign 0.5

        vbox:
            spacing 15

            for label_name, thumbnail in items:
                $ unlocked = is_unlocked(label_name)
                if unlocked:
                    vbox:
                        spacing 15
                        button:           
                            add thumbnail
                            xsize 380
                            ysize 200
                            xalign 0.5
                            yalign 0.5
                            action Replay(label_name, scope={"player_name": persistent.galleryname or "Emanuel"})
                        
                        text label_name size 20 xalign 0.5 yalign 1.0
                
                else:
                    button:
                        background gui.accent_color
                        text "????" size 40 xalign 0.5 yalign 0.5
                        xsize 300
                        ysize 200
                        xalign 0.5
                        yalign 0.5
                        action NullAction()

    vbox:
        xalign 0.0
        yalign 0.95
        textbutton "Unlock All":
            text_size 40
            xalign 0.95
            yalign 0.95
            action Function(unlock_all_replays)


        textbutton "Back":
            text_size 40
            xalign 0.05
            yalign 0.95
            action ShowMenu("character_select"), Hide("replay_screen")
