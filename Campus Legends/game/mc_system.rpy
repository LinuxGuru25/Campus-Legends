##############################################
## MC EMOTIONAL SYSTEM 
## Anxiety, Depression, Emotional Load, Growth
##############################################

init python:

    ############################################################
    ## 0. MC STATE CONTAINER
    ############################################################

    if not hasattr(store, "mc_state"):
        mc_state = {
            "anxiety": 0,          # 0–100
            "depression": 0,       # 0–100
            "emotional_load": 0,   # 0–100
            "coping_style": "avoidance",  # avoidance, humor, honesty, self_blame, distraction, openness
            "growth": 0,           # -100 (regressing) to +100 (healing)
            "internal_severity": 0, # how bad he feels about his actions
            "flags": set(),        # mc_had_panic_attack, mc_shut_down, mc_opened_up, etc.
        }


    ############################################################
    ## 1. HELPERS: GET / SET / CLAMP
    ############################################################

    def mc_get(key, default=None):
        return mc_state.get(key, default)

    def mc_set(key, value):
        mc_state[key] = value

    def mc_add(key, delta, min_val=None, max_val=None):
        val = mc_state.get(key, 0) + delta
        if min_val is not None:
            val = max(min_val, val)
        if max_val is not None:
            val = min(max_val, val)
        mc_state[key] = val
        return val

    def mc_flag(flag):
        f = mc_state.get("flags", set())
        if not isinstance(f, set):
            f = set(f)
        f.add(flag)
        mc_state["flags"] = f

    def mc_has_flag(flag):
        f = mc_state.get("flags", set())
        return flag in f


    ############################################################
    ## 2. CORE METERS: ANXIETY / DEPRESSION / EMOTIONAL LOAD
    ############################################################

    def mc_adjust_anxiety(amount, source=None):
        """
        Increase/decrease MC anxiety.
        """
        val = mc_add("anxiety", amount, 0, 100)
        mc_add("emotional_load", amount // 2, 0, 100)
        mc_maybe_trigger_events(source=source)
        return val

    def mc_adjust_depression(amount, source=None):
        """
        Increase/decrease MC depression.
        """
        val = mc_add("depression", amount, 0, 100)
        mc_add("emotional_load", amount // 2, 0, 100)
        mc_maybe_trigger_events(source=source)
        return val

    def mc_adjust_emotional_load(amount, source=None):
        """
        Directly adjust emotional load.
        """
        val = mc_add("emotional_load", amount, 0, 100)
        mc_maybe_trigger_events(source=source)
        return val


    ############################################################
    ## 3. INTERNAL SEVERITY & GROWTH
    ############################################################

    def mc_adjust_internal_severity(amount, source=None):
        """
        How bad the MC feels about his actions.
        """
        val = mc_add("internal_severity", amount, 0, 100)
        # Internal severity feeds anxiety/depression
        mc_adjust_anxiety(amount // 2, source=source)
        mc_adjust_depression(amount // 3, source=source)
        return val

    def mc_adjust_growth(amount, source=None):
        """
        Growth > 0 = healing, < 0 = regressing.
        """
        val = mc_add("growth", amount, -100, 100)
        return val


    ############################################################
    ## 4. COPING STYLE (PLAYER-DRIVEN)
    ############################################################

    def mc_set_coping_style(style):
        """
        style: avoidance, humor, honesty, self_blame, distraction, openness
        """
        if style in ("avoidance", "humor", "honesty", "self_blame", "distraction", "openness"):
            mc_set("coping_style", style)
        return mc_get("coping_style")

    def mc_coping_modifiers():
        """
        Returns dict of modifiers based on coping style.
        Used to tweak anxiety, depression, detection, etc.
        """
        style = mc_get("coping_style", "avoidance")
        mods = {
            "anxiety_mult": 1.0,
            "depression_mult": 1.0,
            "detection_mult": 1.0,
            "growth_mult": 1.0,
        }

        if style == "avoidance":
            mods["anxiety_mult"] = 1.2
            mods["depression_mult"] = 1.1
            mods["growth_mult"] = 0.8
        elif style == "humor":
            mods["anxiety_mult"] = 0.9
            mods["depression_mult"] = 1.0
            mods["growth_mult"] = 1.0
        elif style == "honesty":
            mods["anxiety_mult"] = 1.1
            mods["depression_mult"] = 0.9
            mods["growth_mult"] = 1.2
        elif style == "self_blame":
            mods["anxiety_mult"] = 1.3
            mods["depression_mult"] = 1.3
            mods["growth_mult"] = 0.7
        elif style == "distraction":
            mods["anxiety_mult"] = 0.95
            mods["depression_mult"] = 1.1
            mods["growth_mult"] = 0.9
        elif style == "openness":
            mods["anxiety_mult"] = 1.0
            mods["depression_mult"] = 0.9
            mods["growth_mult"] = 1.3

        return mods


    ############################################################
    ## 5. EVENT THRESHOLDS & TRIGGERS
    ############################################################

    def mc_maybe_trigger_events(source=None):
        """
        Check anxiety / depression / emotional_load and trigger scenes.
        Called automatically whenever those meters change.
        """
        anxiety = mc_get("anxiety", 0)
        depression = mc_get("depression", 0)
        load = mc_get("emotional_load", 0)

        # Panic attack threshold
        if anxiety >= 75 and load >= 60 and not mc_has_flag("mc_had_panic_attack"):
            mc_flag("mc_had_panic_attack")
            renpy.call_in_new_context("mc_panic_attack_scene", source)

        # Shutdown threshold
        if load >= 80 and not mc_has_flag("mc_shut_down_once"):
            mc_flag("mc_shut_down_once")
            renpy.call_in_new_context("mc_shutdown_scene", source)

        # Deep depression reflection
        if depression >= 70 and not mc_has_flag("mc_depression_reflection"):
            mc_flag("mc_depression_reflection")
            renpy.call_in_new_context("mc_depression_reflection_scene", source)


    ############################################################
    ## 6. INTEGRATION HELPERS FOR GAME EVENTS
    ############################################################

    def mc_on_cheat(severity, detected=False):
        """
        Called when MC cheats (before or after detection).
        severity: 1–3
        detected: bool
        """
        # Internal severity always rises
        mc_adjust_internal_severity(10 * severity, source="cheat")

        # Anxiety & depression spikes
        mods = mc_coping_modifiers()
        mc_adjust_anxiety(int(8 * severity * mods["anxiety_mult"]), source="cheat")
        mc_adjust_depression(int(5 * severity * mods["depression_mult"]), source="cheat")

        # If detected, emotional load spikes harder
        if detected:
            mc_adjust_emotional_load(15 * severity, source="cheat_detected")

    def mc_on_breakup(initiated_by_mc=False):
        """
        Called when a breakup happens.
        """
        mods = mc_coping_modifiers()
        base_anx = 15
        base_dep = 20

        if initiated_by_mc:
            base_anx += 5
            base_dep += 10

        mc_adjust_anxiety(int(base_anx * mods["anxiety_mult"]), source="breakup")
        mc_adjust_depression(int(base_dep * mods["depression_mult"]), source="breakup")
        mc_adjust_emotional_load(20, source="breakup")

    def mc_on_reconciliation():
        """
        Called when reconciliation happens.
        """
        mods = mc_coping_modifiers()
        mc_adjust_anxiety(int(-10 * mods["anxiety_mult"]), source="reconcile")
        mc_adjust_depression(int(-8 * mods["depression_mult"]), source="reconcile")
        mc_adjust_emotional_load(-10, source="reconcile")
        mc_adjust_growth(int(10 * mods["growth_mult"]), source="reconcile")
        mc_flag("mc_opened_up")


    ############################################################
    ## 7. OPTIONAL: HOOK INTO RELATIONSHIP API EVENTS
    ############################################################

    def mc_relationship_event_listener(event, **kwargs):
        """
        Generic listener if you want to hook MC reactions
        into the same event bus as the girls.
        """
        if event == "cheat":
            name = kwargs.get("name")
            severity = kwargs.get("severity", 1)
            detected = kwargs.get("detected", False)
            mc_on_cheat(severity, detected=detected)

        elif event == "breakup":
            name = kwargs.get("name")
            initiated_by_mc = kwargs.get("initiated_by_mc", False)
            mc_on_breakup(initiated_by_mc=initiated_by_mc)

        elif event == "reconcile":
            name = kwargs.get("name")
            mc_on_reconciliation()

    # If you want this wired in:
    # relationship_api.on("cheat", lambda name, severity, **k: mc_on_cheat(severity, detected=k.get("detected", False)))
    # relationship_api.on("breakup", lambda name, **k: mc_on_breakup(initiated_by_mc=k.get("initiated_by_mc", False)))
    # relationship_api.on("reconcile", lambda name, **k: mc_on_reconciliation())
