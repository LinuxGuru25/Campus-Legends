##############################################
## ROMANCE SYSTEMS LAYER
## Helpers, Gossip, Jealousy, Route Evolution
##############################################

init python:

    ############################################################
    ## 1. ROUTE HELPERS
    ############################################################

    def is_locked(name):
        return relationship_api.get_status(name) == "locked"

    def is_active_route(name):
        return relationship_api.get_status(name) in ("dating", "exclusive")

    def lock_if_cheated_too_much(name):
        """
        Optional: lock route if severity is very high.
        """
        sev = relationship_api.get_severity(name)
        if sev >= 80:
            relationship_api.lock_route(name)

    def unlock_if_reconciled(name):
        """
        Optional: unlock route after reconciliation.
        """
        if relationship_api.get_status(name) == "dating":
            # Clear any 'locked' style flags in metadata if you use them
            meta = relationship_api.get_metadata(name)
            if "hard_lock" in meta:
                del meta["hard_lock"]
                relationship_api.set_metadata(name, meta)


    ############################################################
    ## 2. AFFECTION MILESTONES
    ############################################################

    def check_affection_milestones(name):
        """
        Call this after changing affection to trigger milestone scenes.
        """
        aff = relationship_api.get_affection(name)
        meta = relationship_api.get_metadata(name)

        milestones = meta.get("affection_milestones_triggered", set())
        if not isinstance(milestones, set):
            milestones = set()

        def mark(m):
            milestones.add(m)
            meta["affection_milestones_triggered"] = milestones
            relationship_api.set_metadata(name, meta)

        # Example thresholds – tweak as you like
        if aff >= 10 and "10" not in milestones:
            renpy.call_in_new_context("affection_milestone_10", name)
            mark("10")

        if aff >= 20 and "20" not in milestones:
            renpy.call_in_new_context("affection_milestone_20", name)
            mark("20")

        if aff >= 30 and "30" not in milestones:
            renpy.call_in_new_context("affection_milestone_30", name)
            mark("30")


    ############################################################
    ## 3. METADATA CLEANUP
    ############################################################

    def sanitize_relationship_metadata():
        """
        Optional: run this on load or via debug to keep metadata tidy.
        """
        for name, data in relationship_api.characters.items():
            meta = data.get("metadata", {})
            # Example: remove obsolete flags
            obsolete = [k for k in meta.keys() if k.startswith("old_")]
            for k in obsolete:
                del meta[k]
            relationship_api.set_metadata(name, meta)


    ############################################################
    ## 4. GOSSIP & RUMOR SYSTEM (CHEAT-DRIVEN)
    ############################################################

    def gossip_on_cheat(name, severity, **kwargs):
        """
        Triggered on cheat; uses chaos reputation to decide how loud the gossip is.
        """
        global_meta = relationship_api.get_global_metadata()
        rep = global_meta.get("reputation", {
            "social": 0,
            "romantic": 0,
            "loyalty": 0,
            "chaos": 0,
        })
        chaos = rep["chaos"]

        # Light gossip
        if chaos >= 10 and chaos < 25:
            renpy.call_in_new_context("cheating_rumors", name)

        # Heavy rumor storm
        if chaos >= 25:
            renpy.call_in_new_context("cheating_rumors", name)
            renpy.call_in_new_context("world_reacts_to_breakup", name)


    ############################################################
    ## 5. DYNAMIC JEALOUSY SYSTEM
    ############################################################

    def check_dynamic_jealousy(primary, others):
        """
        Compare affection between primary LI and others.
        If someone is being 'overtaken', trigger jealousy scenes.
        Call this after big affection changes.
        """
        primary_aff = relationship_api.get_affection(primary)

        for other in others:
            other_aff = relationship_api.get_affection(other)
            # If other is gaining on primary or surpasses them
            if other_aff >= primary_aff - 2:
                # Trigger a jealousy scene label if you want per-character
                renpy.call_in_new_context("jealousy_scene", primary, other)


    ############################################################
    ## 6. ROUTE EVOLUTION SYSTEM
    ############################################################

    def update_route_state(name):
        """
        Evolves route based on affection, trust, and severity.
        Call this after major events or periodically.
        """
        relationship_api.ensure(name)

        aff = relationship_api.get_affection(name)
        tr = relationship_api.get_trust(name)
        sev = relationship_api.get_severity(name)
        status = relationship_api.get_status(name)

        # Hard fail: too much severity → broken_up or locked
        if sev >= 80:
            relationship_api.set_status(name, "broken_up")
            relationship_api.lock_route(name)
            return

        # Early crush → dating
        if aff >= 10 and tr >= 5 and status in ("neutral", "friends"):
            relationship_api.set_status(name, "dating")

        # Strong bond → exclusive
        if aff >= 20 and tr >= 15 and status == "dating":
            relationship_api.set_status(name, "exclusive")

        # Post-reconciliation cleanup
        if status == "dating" and sev == 0:
            unlock_if_reconciled(name)


    ############################################################
    ## 7. HOOK REGISTRATION FOR SYSTEMS
    ############################################################

    # Gossip reacts to cheating
    relationship_api.on("cheat", gossip_on_cheat)
