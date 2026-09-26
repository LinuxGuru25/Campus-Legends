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
            "anxiety": 0,            # 0–100
            "depression": 0,         # 0–100
            "emotional_load": 0,     # 0–100
            "coping_style": "avoidance",  # avoidance, humor, honesty, self_blame, distraction, openness
            "growth": 0,             # -100 (regressing) to +100 (healing)
            "internal_severity": 0,  # how bad he feels about his actions
            "flags": set(),          # mc_had_panic_attack, mc_shut_down, mc_opened_up, etc.
        }


    ############################################################
    ## 1. HELPERS: GET / SET / CLAMP
    ############################################################

    def mc_get(key, default=None):
        return mc_state.get(key, default)

    def mc_set(key, value):
        mc_state[key] = value
        return value

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
        return f

    def mc_has_flag(flag):
        f = mc_state.get("flags", set())
        return flag in f


    ############################################################
    ## 2. CORE METERS: ANXIETY / DEPRESSION / EMOTIONAL LOAD
    ############################################################

    def mc_adjust_anxiety(amount, source=None):
        val = mc_add("anxiety", amount, 0, 100)
        mc_add("emotional_load", amount // 2, 0, 100)
        mc_maybe_trigger_events(source=source)
        return val

    def mc_adjust_depression(amount, source=None):
        val = mc_add("depression", amount, 0, 100)
        mc_add("emotional_load", amount // 2, 0, 100)
        mc_maybe_trigger_events(source=source)
        return val

    def mc_adjust_emotional_load(amount, source=None):
        val = mc_add("emotional_load", amount, 0, 100)
        mc_maybe_trigger_events(source=source)
        return val


    ############################################################
    ## 3. INTERNAL SEVERITY & GROWTH
    ############################################################

    def mc_adjust_internal_severity(amount, source=None):
        val = mc_add("internal_severity", amount, 0, 100)
        mc_adjust_anxiety(amount // 2, source=source)
        mc_adjust_depression(amount // 3, source=source)
        return val

    def mc_adjust_growth(amount, source=None):
        return mc_add("growth", amount, -100, 100)


    ############################################################
    ## 4. COPING STYLE (PLAYER-DRIVEN)
    ############################################################

    def mc_set_coping_style(style):
        if style in ("avoidance", "humor", "honesty", "self_blame", "distraction", "openness"):
            mc_set("coping_style", style)
        return mc_get("coping_style")

    def mc_coping_modifiers():
        style = mc_get("coping_style", "avoidance")
        mods = {
            "anxiety_mult": 1.0,
            "depression_mult": 1.0,
            "growth_mult": 1.0,
        }

        if style == "avoidance":
            mods["anxiety_mult"] = 1.2
            mods["depression_mult"] = 1.1
            mods["growth_mult"] = 0.8

        elif style == "humor":
            mods["anxiety_mult"] = 0.9
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

        elif style == "openness":
            mods["depression_mult"] = 0.9
            mods["growth_mult"] = 1.3

        return mods


    ############################################################
    ## 5. EVENT THRESHOLDS & TRIGGERS
    ############################################################

    def mc_maybe_trigger_events(source=None):
        anxiety = mc_get("anxiety", 0)
        depression = mc_get("depression", 0)
        load = mc_get("emotional_load", 0)

        if anxiety >= 75 and load >= 60 and not mc_has_flag("mc_had_panic_attack"):
            mc_flag("mc_had_panic_attack")
            renpy.call_in_new_context("mc_panic_attack_scene", source)

        if load >= 80 and not mc_has_flag("mc_shut_down_once"):
            mc_flag("mc_shut_down_once")
            renpy.call_in_new_context("mc_shutdown_scene", source)

        if depression >= 70 and not mc_has_flag("mc_depression_reflection"):
            mc_flag("mc_depression_reflection")
            renpy.call_in_new_context("mc_depression_reflection_scene", source)


    ############################################################
    ## 6. MC REACTIONS TO RELATIONSHIP EVENTS
    ############################################################

    def mc_on_cheat(severity, detected=False):
        mods = mc_coping_modifiers()

        mc_adjust_internal_severity(10 * severity, source="cheat")
        mc_adjust_anxiety(int(8 * severity * mods["anxiety_mult"]), source="cheat")
        mc_adjust_depression(int(5 * severity * mods["depression_mult"]), source="cheat")

        if detected:
            mc_adjust_emotional_load(15 * severity, source="cheat_detected")
            mc_flag("mc_got_caught_cheating")
        else:
            mc_adjust_emotional_load(8 * severity, source="cheat_hidden")
            mc_flag("mc_hiding_cheating")

    def mc_on_breakup(initiated_by_mc=False, severity=2):
        mods = mc_coping_modifiers()

        base_anx = 12 + (severity * 3)
        base_dep = 15 + (severity * 4)

        if initiated_by_mc:
            base_anx += 5
            base_dep += 10
            mc_flag("mc_initiated_breakup")
        else:
            mc_flag("mc_got_dumped")

        mc_adjust_anxiety(int(base_anx * mods["anxiety_mult"]), source="breakup")
        mc_adjust_depression(int(base_dep * mods["depression_mult"]), source="breakup")
        mc_adjust_emotional_load(20, source="breakup")

    def mc_on_reconciliation():
        mods = mc_coping_modifiers()

        mc_adjust_anxiety(int(-10 * mods["anxiety_mult"]), source="reconcile")
        mc_adjust_depression(int(-8 * mods["depression_mult"]), source="reconcile")
        mc_adjust_emotional_load(-10, source="reconcile")
        mc_adjust_growth(int(10 * mods["growth_mult"]), source="reconcile")
        mc_flag("mc_opened_up")

    def mc_on_forgive():
        mods = mc_coping_modifiers()

        mc_adjust_internal_severity(-15, source="forgive")
        mc_adjust_emotional_load(-12, source="forgive")
        mc_adjust_growth(int(12 * mods["growth_mult"]), source="forgive")
        mc_flag("mc_was_forgiven")


    ############################################################
    ## 7. SIMPLE WRAPPER FUNCTION (for script compatibility)
    ############################################################

    def add_confidence(amount):
        """
        Simple wrapper so old script calls like:
            $ add_confidence(1)
        still work.
        Confidence = positive growth.
        """
        return mc_adjust_growth(amount, source="confidence")


    ############################################################
    ## 8. HOOK INTO RELATIONSHIP API EVENTS
    ############################################################

    def _mc_register_relationship_hooks():
        try:
            relationship_api.on("cheat", lambda name, severity, detected=False: mc_on_cheat(severity, detected))
            relationship_api.on("breakup", lambda name, initiated_by_mc=False, severity=2: mc_on_breakup(initiated_by_mc, severity))
            relationship_api.on("reconcile", lambda name: mc_on_reconciliation())
            relationship_api.on("forgive", lambda name: mc_on_forgive())
        except Exception:
            pass

    _mc_register_relationship_hooks()


