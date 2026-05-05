default rumor_level = 0
default mc_anxiety = 0
default mc_depression = 0

screen phone_stats():

    modal True

    window:
        style "phone_bg"

        viewport:
            xpos 13
            yalign 0.3
            xsize 450
            ysize 750
            scrollbars "vertical"
            draggable True
            mousewheel True

            frame:
                xalign 0.5
                yalign 0.5
                background None

                vbox:
                    spacing 20
                    align (0.5, 0.0)

                    text "MC Stats" size 40 color "#FFFFFF" xalign 0.5

                    # -------------------------
                    # PERSONALITY
                    # -------------------------
                    $ pdata = get_personality_data()

                    text "Personality" size 30 color "#FFD700"
                    text "Confident: [pdata['Confident']]" size 22
                    text "Caring: [pdata['Caring']]" size 22
                    text "Selfish: [pdata['Selfish']]" size 22
                    text "Dominant: [mc_personality]" size 22

                    null height 20

                    # -------------------------
                    # RELATIONSHIPS
                    # -------------------------
                    text "Relationships" size 30 color "#FFD700"

                    for girl in ["sienna", "jess", "aubrey", "zoey", "kaia", "misty", "tiffany"]:
                        $ rel = relationship_api.get(girl)
                        $ tier = rel["evolution"]["stage"]

                        text "[girl.capitalize()]" size 26 color "#FFFFFF"
                        text "Affection: [rel['affection']]" size 22
                        text "Trust: [rel['trust']]" size 22
                        text "Tier: [tier]" size 22

                        null height 10

                    null height 20

                    # -------------------------
                    # ROUTE STATUS
                    # -------------------------
                    text "Route Status" size 30 color "#FFD700"

                    for girl in ["sienna", "jess", "aubrey", "zoey", "kaia", "misty", "tiffany"]:
                        $ state = relationship_api.get(girl).get("route_state", "open")

                        if state == "open":
                            $ color = "#00FFAA"
                        elif state == "exclusive":
                            $ color = "#00A2FF"
                        elif state == "soft_locked":
                            $ color = "#FFCC00"
                        elif state == "locked":
                            $ color = "#FF8800"
                        elif state == "closed":
                            $ color = "#FF4444"
                        else:
                            $ color = "#FFFFFF"

                        text "[girl.capitalize()]: [state.capitalize()]" size 22

                    null height 20

                    # -------------------------
                    # JEALOUSY
                    # -------------------------
                    text "Jealousy Levels" size 30 color "#FFD700"

                    for girl in ["sienna", "jess", "aubrey", "zoey", "kaia", "misty", "tiffany"]:
                        $ j = relationship_api.get(girl).get("jealousy", 0)
                        text "[girl.capitalize()]: [j]" size 22

                    null height 20

                    # -------------------------
                    # RUMOR LEVEL
                    # -------------------------
                    text "Campus Rumor Level" size 30 color "#FFD700"
                    text "[rumor_level]" size 22

                    null height 20

                    # -------------------------
                    # MC EMOTIONAL STATE
                    # -------------------------
                    text "MC Emotional State" size 30 color "#FFD700"
                    text "Anxiety: [mc_anxiety]" size 22
                    text "Depression: [mc_depression]" size 22

                    null height 20

                    # -------------------------
                    # EXCLUSIVE ROUTE
                    # -------------------------
                    text "Exclusive Route" size 30 color "#FFD700"

                    $ excl = relationship_api.get_global_metadata().get("exclusive_with", None)

                    if excl:
                        text "Exclusive with: [excl.capitalize()]" size 22
                    else:
                        text "No exclusive route active" size 22
    vbox:                       
        align(0.5, 0.9)
        textbutton "Back":
            action [Hide(screen=None), Show("phone_home")]