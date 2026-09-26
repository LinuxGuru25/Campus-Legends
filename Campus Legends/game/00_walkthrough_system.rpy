init python:
    # Walkthrough text character
    WT = Character(
        None,
        what_prefix="{size=22}{color=#00ff00}{i}",
        what_suffix="{/i}{/color}{/size}"
    )

    # Walkthrough function
    def walkthrough(msg):
        if renpy.store.walkthrough_enabled:
            renpy.say(WT, msg)

