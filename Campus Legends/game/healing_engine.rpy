##############################################
## mc_healing_system.rpy
## MC Emotional Support & Healing Engine
##############################################

init python:

    ############################################################
    ## 1. CORE HEALING FUNCTION
    ############################################################

    def mc_receive_support(source, strength=1, kind="general"):
        """
        Emotional support for the MC from friends/partners.

        source: character name string (e.g. "Sienna", "Aubrey")
        strength: 1–3 (light, medium, strong)
        kind: "general", "grounding", "reassurance", "comfort", "distraction"
        """

        # Base healing values
        heal_anx = 0
        heal_dep = 0
        heal_load = 0
        growth = 0

        if kind == "general":
            heal_anx = 5 * strength
            heal_dep = 4 * strength
            heal_load = 5 * strength
            growth = 3 * strength

        elif kind == "grounding":
            heal_anx = 8 * strength
            heal_load = 6 * strength
            growth = 4 * strength

        elif kind == "reassurance":
            heal_anx = 6 * strength
            heal_dep = 6 * strength
            growth = 5 * strength

        elif kind == "comfort":
            heal_dep = 8 * strength
            heal_load = 5 * strength
            growth = 6 * strength

        elif kind == "distraction":
            heal_anx = 4 * strength
            heal_load = 4 * strength
            growth = 2 * strength

        # Apply healing to MC emotional system
        mc_adjust_anxiety(-heal_anx, source=f"support_{source}")
        mc_adjust_depression(-heal_dep, source=f"support_{source}")
        mc_adjust_emotional_load(-heal_load, source=f"support_{source}")
        mc_adjust_growth(growth, source=f"support_{source}")

        # Track who has supported the MC
        mc_flag(f"supported_by_{source}")

        return {
            "anxiety_healed": heal_anx,
            "depression_healed": heal_dep,
            "load_healed": heal_load,
            "growth_gain": growth
        }


    ############################################################
    ## 2. AUTO SUPPORT TRIGGER (WHEN MC IS STRUGGLING)
    ############################################################

    def mc_support_auto_trigger(name):
        """
        Call this when a friend/partner is present in a scene.
        If MC is clearly struggling, they may step in to help.
        """
        anxiety = mc_get("anxiety")
        depression = mc_get("depression")
        load = mc_get("emotional_load")

        # Thresholds for visible struggle
        if anxiety >= 60 or depression >= 60 or load >= 70:
            renpy.call_in_new_context("mc_support_scene", name)


    ############################################################
    ## 3. HOOKS FOR RELATIONSHIP EVENTS
    ############################################################

    def mc_support_on_reconcile(name):
        """
        When reconciliation happens, partner provides emotional support.
        """
        mc_receive_support(name, strength=2, kind="reassurance")

    def mc_support_on_breakup(name):
        """
        After a breakup, a friend or another character can step in.
        You decide who in script; this just calls the scene.
        """
        renpy.call_in_new_context("mc_friend_support_after_breakup", name)


    # OPTIONAL: wire into relationship_api if desired
    # relationship_api.on("reconcile", lambda name, **k: mc_support_on_reconcile(name))
    # relationship_api.on("breakup",   lambda name, **k: mc_support_on_breakup(name))

##############################################
## 4. WIRE HEALING ENGINE INTO RELATIONSHIP API
##############################################

init python:

    # When reconciliation happens, partner provides emotional support
    relationship_api.on(
        "reconcile",
        lambda name, **k: mc_support_on_reconcile(name)
    )

    # When a breakup happens, a friend or partner may step in
    relationship_api.on(
        "breakup",
        lambda name, **k: mc_support_on_breakup(name)
    )

    # When cheating is detected, partner may offer emotional support later
    relationship_api.on(
        "cheat",
        lambda name, severity, detected=False, **k:
            mc_support_auto_trigger(name)
    )

