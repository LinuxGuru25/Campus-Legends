
init python:

    class Bio:
        def __init__(self, name, pfp="images/phone/icon.png"):
            self.name = name
            self.pfp = pfp
            self.stats = {
                "age": "?",
                "sex": "?",
                "height": "?",
                "weight": "?"
            }
            self.entries = []
            self.visible = True #False

    class Entry:
        def __init__(self, owner, text=None):
            self.owner = owner
            self.text = text
            self.visible = False

    def add_entry(owner, text):
        entry = Entry(owner=owner, text=text)
        owner.entries.append(entry)
        entry.visible = True

screen bios_home():
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
                yfill False
                
                vpgrid:
                    cols 3
                    spacing 15
                    xfill True
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    xalign 0.5
                    yalign 0.5
                    

                    for bio in phone_state.bios:
                        if bio.visible:
                            button:                            
                                action [Show("bio_screen", bio=bio), Hide(screen=None)]
                                
                                vbox:
                                    add bio.pfp:
                                        size(100, 100)
                                    
                                    text bio.name:
                                        style "readable"
                                        xalign 0.5

 
    vbox:
        align(0.5, 0.93)
        textbutton "Back":
            action [Show("phone_home"), Hide(screen=None)]

screen bio_screen(bio):
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
                    yalign 0.0
                    spacing 15
                    
                    add bio.pfp:
                        xalign 0.5
                        size (120, 120)

                    text bio.name color "#000000" size 40 xalign 0.5

                    frame:
                        background "#CCCCCC"
                        xfill True
                        ysize 1
                    
                    text (f"Age: {bio.stats["age"]}") color "#000000" size 30
                    text (f"Sex: {bio.stats["sex"]}") color "#000000" size 30
                    text (f"Height: {bio.stats["height"]}") color "#000000" size 30
                    text (f"Weight: {bio.stats["weight"]} lbs") color "#000000" size 30

                    frame:
                        background "#CCCCCC"
                        xfill True
                        ysize 1

                    for entry in bio.entries:
                        vbox:
                            spacing 15
                            xalign 0.0

                            text (f"-{entry.text}") color "#000000" size 25

    vbox:
        align(0.5, 0.93)
        textbutton "Back":
            action [Show("bios_home"), Hide(screen=None)]