##############################################
## CHEATING DETECTION SYSTEM — HYBRID MODEL
## Campus Legends — API-Compatible
##############################################

init python:

    ############################################################
    ## 1. BASE DETECTION CHANCE (SYSTEMIC)
    ############################################################

    def base_detection_chance(name, severity):
        """
        Returns a % chance the cheating is discovered immediately.
        Influenced by:
        - character reaction profile
        - MC personality
        - severity
        - chaos reputation
        """
        profile, p_scale = relationship_api.personality_scale_for(name)

        # Start with reaction profile strictness
        if profile is renpy.store.reaction_profiles["strict"]:
            chance = 35
        elif profile is renpy.store.reaction_profiles["balanced"]:
            chance = 20
        else:
            chance = 10

        # Severity increases risk
        chance += severity * 5

        # MC personality modifies risk
        mc = relationship_api.get_mc_personality()
        if mc == "Selfish":
            chance += 10
        elif mc == "Caring":
            chance -= 5

        # Chaos reputation increases risk
        rep = relationship_api.get_global_metadata().get("reputation", {})
        chaos = rep.get("chaos", 0)
        chance += chaos // 5

        # Clamp
        return max(0, min(chance, 95))


    ############################################################
    ## 2. PLAYER CHOICE MODIFIERS
    ############################################################

    def apply_player_choice_modifier(base, choice):
        """
        Player choices modify detection chance.
        """
        if choice == "hide":
            return base - 15
        if choice == "lie":
            return base - 5
        if choice == "confess":
            return 0
        if choice == "distract":
            return base - 10
        if choice == "avoid":
            return base - 8

        return base


    ############################################################
    ## 3. FINAL DETECTION ROLL
    ############################################################

    def cheating_detection_roll(name, severity, choice):
        """
        Returns True if caught, False if not.
        Also sets metadata flags for future consequences.
        """
        base = base_detection_chance(name, severity)
        final = apply_player_choice_modifier(base, choice)

        import random
        roll = random.randint(1, 100)

        meta = relationship_api.get_metadata(name)

        if roll <= final:
            meta["cheating_caught"] = True
            relationship_api.set_metadata(name, meta)
            return True

        # Not caught immediately — but maybe later
        meta["cheating_hidden"] = True
        meta["cheating_rumor_pending"] = True
        relationship_api.set_metadata(name, meta)

        return False


    ############################################################
    ## 4. RUMOR-BASED LATE DETECTION
    ############################################################

    def process_late_detection(name):
        """
        If cheating wasn't caught immediately, gossip may expose it later.
        """
        meta = relationship_api.get_metadata(name)

        if not meta.get("cheating_rumor_pending", False):
            return

        rep = relationship_api.get_global_metadata().get("reputation", {})
        chaos = rep.get("chaos", 0)

        # Chance gossip exposes the cheating
        chance = min(chaos * 2, 60)

        import random
        roll = random.randint(1, 100)

        if roll <= chance:
            meta["cheating_caught_late"] = True
            relationship_api.set_metadata(name, meta)
            renpy.call_in_new_context("cheating_exposed_late", name)
        else:
            # Rumor fizzles out
            meta["cheating_rumor_pending"] = False
            relationship_api.set_metadata(name, meta)


    ############################################################
    ## 5. JEALOUSY-BASED DETECTION
    ############################################################

    def jealousy_detection_check(name, others):
        """
        If another LI has high affection, they may notice cheating.
        """
        primary_aff = relationship_api.get_affection(name)

        for other in others:
            other_aff = relationship_api.get_affection(other)

            if other_aff >= primary_aff - 1:
                # Jealousy exposes cheating
                meta = relationship_api.get_metadata(name)
                meta["cheating_caught_jealousy"] = True
                relationship_api.set_metadata(name, meta)

                renpy.call_in_new_context("cheating_exposed_by_jealousy", name, other)
                return


    ############################################################
    ## 6. HOOK: When cheating happens
    ############################################################

    def hybrid_cheat_handler(name, severity, **kwargs):
        """
        Called automatically when cheating occurs.
        Prompts player choice → runs detection roll.
        """

        # Ask player how they handle it
        result = renpy.call_in_new_context("cheating_player_choice", name)

        caught = cheating_detection_roll(name, severity, result)

        if caught:
            renpy.call_in_new_context("cheating_caught_scene", name)
        else:
            renpy.call_in_new_context("cheating_hidden_scene", name)


    relationship_api.on("cheat", hybrid_cheat_handler)
