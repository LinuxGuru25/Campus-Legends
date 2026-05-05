
##############################################
## PERSONALITY SYSTEM — API Compatible
## Campus Legends
##############################################

default mc_personality = "Neutral"

init python:

    ############################################################
    ## 1. PERSONALITY STORAGE (API METADATA)
    ############################################################

    def get_personality_data():
        """
        Returns the MC personality dictionary stored in API metadata.
        """
        meta = relationship_api.get_global_metadata()
        if "personality" not in meta:
            meta["personality"] = {
                "Confident": 0,
                "Caring": 0,
                "Selfish": 0,
            }
            relationship_api.set_global_metadata(meta)
        return meta["personality"]


    def save_personality_data(data):
        meta = relationship_api.get_global_metadata()
        meta["personality"] = data
        relationship_api.set_global_metadata(meta)


    ############################################################
    ## 2. ADD PERSONALITY POINTS
    ############################################################

    def add_personality(trait, amount=1):
        """
        Adds personality points and updates MC dominant trait.
        Also applies reputation modifiers.
        """
        data = get_personality_data()
        data[trait] += amount
        save_personality_data(data)

        # Reputation modifiers
        if trait == "Confident":
            relationship_api.add_reputation("social", amount)
            relationship_api.add_reputation("romantic", amount * 0.5)

        elif trait == "Caring":
            relationship_api.add_reputation("loyalty", amount)
            relationship_api.add_reputation("romantic", amount * 0.25)

        elif trait == "Selfish":
            relationship_api.add_reputation("loyalty", -amount)
            relationship_api.add_reputation("chaos", amount)

        update_mc_personality()


    ############################################################
    ## 3. GET PERSONALITY VALUE
    ############################################################

    def get_personality(trait):
        return get_personality_data()[trait]


    ############################################################
    ## 4. UPDATE DOMINANT PERSONALITY
    ############################################################

    def update_mc_personality():
        global mc_personality
        data = get_personality_data()
        mc_personality = max(data, key=data.get)
        return mc_personality


    ############################################################
    ## 5. PERSONALITY-BASED ROMANCE BONUS
    ############################################################

    def personality_bonus_for(name):
        """
        Returns +1 if MC personality matches the character's preferred type.
        """
        prefs = renpy.store.preferred_personality
        if name in prefs and prefs[name] == mc_personality:
            return 1
        return 0

