screen phone_stats():

    frame:
        style_prefix "phone"
        xfill True
        yfill True

        viewport:
            draggable True
            mousewheel True

            frame:
                xpadding 20
                ypadding 20

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
                        $ tier = evolution.get_tier(girl)

                        text "[girl.capitalize()]" size 26 color "#FFFFFF"
                        text "Affection: [rel.affection]" size 22
                        text "Trust: [rel.trust]" size 22
                        text "Tier: [tier]" size 22

                        null height 10

                    null height 20

                    # -------------------------
                    # ROUTE STATUS
                    # -------------------------
                    text "Route Status" size 30 color "#FFD700"

                    for girl in ["sienna", "jess", "aubrey", "zoey", "kaia", "misty", "tiffany"]:
                        $ state = relationship_api.get_route_state(girl)

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

                        text "[girl.capitalize()]: [state.capitalize()]" size 22 color color

                    null height 20

                    # -------------------------
                    # JEALOUSY
                    # -------------------------
                    text "Jealousy Levels" size 30 color "#FFD700"

                    for girl in ["sienna", "jess", "aubrey", "zoey", "kaia", "misty", "tiffany"]:
                        $ j = jealousy.get(girl)
                        text "[girl.capitalize()]: [j]" size 22

                    null height 20

                    # -------------------------
                    # RUMOR LEVEL
                    # -------------------------
                    text "Campus Rumor Level" size 30 color "#FFD700"
                    text "[rumor.get()]" size 22

                    null height 20

                    # -------------------------
                    # MC EMOTIONAL STATE
                    # -------------------------
                    text "MC Emotional State" size 30 color "#FFD700"
                    text "Anxiety: [mc_emotion.get_anxiety()]" size 22
                    text "Depression: [mc_emotion.get_depression()]" size 22

                    null height 20

                    # -------------------------
                    # EXCLUSIVE ROUTE
                    # -------------------------
                    text "Exclusive Route" size 30 color "#FFD700"

                    if exclusive.exclusive_with:
                        text "Exclusive with: [exclusive.exclusive_with.capitalize()]" size 22
                    else:
                        text "No exclusive route active" size 22



