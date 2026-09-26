
## PERSONALITY SYSTEM (API-BASED)
## Campus Legends — Option 1 Upgrade
## Traits: Confident, Caring, Selfish

default mc_personality = "Neutral"

init python:

    # ---------------------------------------------------------
    # 1. PERSONALITY STORAGE (API METADATA)
    # ---------------------------------------------------------

    def get_personality_data():
        """
        Returns the MC personality dictionary stored in API metadata.
        Creates it if missing.
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
        """
        Saves the updated personality dictionary back into API metadata.
        """
        meta = relationship_api.get_global_metadata()
        meta["personality"] = data
        relationship_api.set_global_metadata(meta)


    # ---------------------------------------------------------
    # 2. ADD PERSONALITY POINTS
    # ---------------------------------------------------------

    def add_personality(trait, amount=1):
        """
        Adds personality points and updates MC dominant trait.
        Also triggers personality drift and evolution checks.
        """
        data = get_personality_data()

        if trait not in data:
            return

        data[trait] += amount
        save_personality_data(data)

        update_mc_dominant_trait()
        apply_personality_drift()
        return data[trait]


    # ---------------------------------------------------------
    # 3. DOMINANT PERSONALITY CALCULATION
    # ---------------------------------------------------------

    def update_mc_dominant_trait():
        """
        Updates the MC's dominant personality string.
        """
        data = get_personality_data()

        highest = max(data, key=data.get)
        value = data[highest]

        if value < 10:
            store.mc_personality = "Neutral"
        else:
            store.mc_personality = highest


    # ---------------------------------------------------------
    # 4. PERSONALITY DRIFT (Optional but AAA-feel)
    # ---------------------------------------------------------

    def apply_personality_drift():
        """
        Slowly shifts MC personality toward the dominant trait.
        Prevents the MC from becoming 'everything at once'.
        """
        data = get_personality_data()
        dominant = store.mc_personality

        if dominant == "Neutral":
            return

        for trait in data:
            if trait != dominant and data[trait] > 0:
                data[trait] -= 0.1

        save_personality_data(data)


    # ---------------------------------------------------------
    # 5. PREFERRED PERSONALITY PER GIRL
    # ---------------------------------------------------------

    preferred_personality = {
        "sienna": ["Confident", "Caring"],
        "jess": ["Caring"],
        "aubrey": ["Confident"],
        "kaia": ["Caring", "Confident"],
    }


    # ---------------------------------------------------------
    # 6. PERSONALITY MATCH BONUS
    # ---------------------------------------------------------

    def personality_bonus(girl, base_amount):
        """
        Returns base_amount + bonus if MC matches girl's preferred traits.
        """
        data = get_personality_data()
        prefs = preferred_personality.get(girl, [])

        bonus = 0
        for trait in prefs:
            if data.get(trait, 0) >= 20:
                bonus += 1

        return base_amount + bonus


    # ---------------------------------------------------------
    # 7. PERSONALITY LOCK CHECK
    # ---------------------------------------------------------

    def personality_locked(girl):
        """
        Returns True if MC does NOT meet any of the girl's preferred traits.
        Used for personality-locked scenes.
        """
        data = get_personality_data()
        prefs = preferred_personality.get(girl, [])

        for trait in prefs:
            if data.get(trait, 0) >= 20:
                return False

        return True


    # ---------------------------------------------------------
    # 8. INTEGRATION WITH AFFECTION/TRUST
    # ---------------------------------------------------------

    def add_affection_with_personality(girl, base_amount):
        """
        Adds affection but applies personality bonus automatically.
        """
        final = personality_bonus(girl, base_amount)
        relationship_api.add_affection(girl, final)
        return final


    def add_trust_with_personality(girl, base_amount):
        """
        Adds trust but applies personality bonus automatically.
        """
        final = personality_bonus(girl, base_amount)
        relationship_api.add_trust(girl, final)
        return final


    # ---------------------------------------------------------
    # 9. EXCLUSIVE ROUTE INTEGRATION
    # ---------------------------------------------------------

    def personality_allows_exclusive(girl):
        """
        Exclusive routes require at least one preferred trait at threshold.
        """
        return not personality_locked(girl)


    # ---------------------------------------------------------
    # 10. GIRLFRIEND EVOLUTION INTEGRATION
    # ---------------------------------------------------------

    def personality_evolution_modifier(girl):
        """
        Returns a modifier for girlfriend evolution thresholds.
        Example: Caring MC makes forgiveness easier.
        """
        data = get_personality_data()

        if data["Caring"] >= 30:
            return -5  # easier evolution
        if data["Selfish"] >= 30:
            return +5  # harder evolution

        return 0


