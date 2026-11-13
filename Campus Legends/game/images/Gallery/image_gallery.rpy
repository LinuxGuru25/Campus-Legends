###############################################
# CENTRALIZED GALLERY SYSTEM
###############################################

# Persistent unlock dictionary
default persistent.gallery_unlocks = {}

###############################################
# GALLERY DATA 
###############################################

init python:

    GALLERY_DATA = {
        "Aubrey": [
            ("aubrey1", "aubrey_1.webp"),
            ("aubrey2", "aubrey_2.webp"),
        ],

        "Jess": [
            ("jess1", "jess_1.webp"),
        ],

        "Kaia": [
            ("kaia1", "kaia_1.webp"),
        ],

        "Misty": [
            ("misty1", "misty_1.webp"),
        ],

        "Norah": [
            ("norah1", "norah_1.webp"),
        ],

        "Sienna": [
            ("sienna1", "sienna_1.webp"),
        ],

        "Tiffany": [
            ("tiffany1", "tiffany_1.webp"),
        ],

        "Others": [
            ("hart1", "hart_1.webp"),
        ],
    }

###############################################
# GALLERY OBJECT — AUTO‑GENERATED BUTTONS
###############################################

init python:

    gallery = Gallery()
    gallery.transition = dissolve

    for character, items in GALLERY_DATA.items():
        for button_name, image_file in items:
            gallery.button(button_name)
            gallery.unlock_image(image_file.replace(".webp", ""))
            gallery.condition(f"persistent.gallery_unlocks.get('{button_name}', False)")

###############################################
# UNLOCK FUNCTION 
###############################################

init python:
    def unlock_gallery(button_name):
        persistent.gallery_unlocks[button_name] = True

###############################################
# MAIN GALLERY SCREEN 
###############################################

screen gallery_screen():
    tag menu
    add "images/gallery_images/bg_gallery.png"

    vbox:
        xalign 0.25
        yalign 0.5

        for character in GALLERY_DATA.keys():
            textbutton character:
                action ShowMenu("gallery_character", character=character)

        textbutton "Return":
            action Return()

###############################################
# GENERIC GALLERY PAGE
###############################################

screen gallery_character(character):
    tag menu
    add "images/gallery_images/bg_gallery.png"

    $ items = GALLERY_DATA[character]

    hbox:
        yalign 0.5
        xalign 0.5

        grid 3 2:
            spacing 25

            for button_name, image_file in items:
                add gallery.make_button(
                    button_name,
                    unlocked = im.Scale(f"gallery_images/{image_file}", 234, 132),
                    locked = "gallery_images/locked.jpg"
                )

    textbutton "Back":
        text_size 45
        xalign 0.05
        yalign 0.95
        action ShowMenu("gallery_screen")


