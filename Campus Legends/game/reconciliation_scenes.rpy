##############################################
## CAMPUS LEGENDS — RECONCILIATION SCENES
## With Hard Fail Logic + Permanent Route Lock
##############################################

############################################################
## SIENNA
############################################################

label scene_reconcile_sienna:

    $ name = "Sienna"
    $ trust = relationship_api.get_trust(name)
    $ meta = relationship_api.get_metadata(name)
    $ scars = meta.get("emotional_scars", [])
    $ rebuild = meta.get("rebuild_progress", 0)
    $ stage = meta.get("rebuild_stage", 0)
    $ personality = meta.get("personality", "balanced")
    $ difficulty = calculate_reconcile_difficulty(name)
    $ required_trust = 30 + difficulty * 5
    $ personality_block = (personality in ["guarded", "volatile"] and stage < 3)

    scene dorm_evening
    with fade

    "The hallway outside Sienna's room is unusually quiet."

    MCname "{i}(No perfect time for this…){/i}"

    "You knock."

    pause

    Sienna "It's open."

    show sienna neutral at center

    Sienna "You actually came."

    if "major" in scars:
        Sienna "You made it seem like losing me wouldn’t change anything."
    elif "moderate" in scars:
        Sienna "You kept disappearing."
    else:
        Sienna "You messed up. But you're here."

    ############################################
    ## HARD FAIL CHECK — PERMANENT LOCK
    ############################################

    if trust < required_trust or ("major" in scars and rebuild < 25) or personality_block:

        jump scene_reconcile_fail_sienna

    ############################################
    ## SUCCESS BRANCH
    ############################################

    if trust >= 60:
        Sienna "You're different today."
        Sienna "You’re not hiding behind jokes."
        "Her walls crack."
        Sienna "I'm willing to try again."
    else:
        Sienna "I believe you."
        Sienna "But trust comes after."

    $ reconcile(name)

    return


label scene_reconcile_fail_sienna:

    show sienna neutral at center

    Sienna "No."
    Sienna "You haven’t shown me enough."
    Sienna "And I’m not waiting for you to change."

    Sienna "This isn’t a delay."
    Sienna "This is goodbye."

    # PERMANENT LOCK
    $ meta = relationship_api.get_metadata("Sienna")
    $ meta["reconciliation_locked"] = True
    $ relationship_api.set_metadata("Sienna", meta)

    return


############################################################
## JESS
############################################################

label scene_reconcile_jess:

    $ name = "Jess"
    $ trust = relationship_api.get_trust(name)
    $ meta = relationship_api.get_metadata(name)
    $ scars = meta.get("emotional_scars", [])
    $ rebuild = meta.get("rebuild_progress", 0)
    $ stage = meta.get("rebuild_stage", 0)
    $ personality = meta.get("personality", "balanced")
    $ difficulty = calculate_reconcile_difficulty(name)
    $ required_trust = 30 + difficulty * 5
    $ personality_block = (personality in ["guarded", "volatile"] and stage < 3)

    scene campus_green_night
    with fade

    show jess sad at center

    Jess "...Hey."

    if "major" in scars:
        Jess "I kept wondering what I did wrong."
    elif "moderate" in scars:
        Jess "I stopped making excuses for you disappearing."
    else:
        Jess "You hurt me."

    ############################################
    ## HARD FAIL CHECK — PERMANENT LOCK
    ############################################

    if trust < required_trust or ("major" in scars and rebuild < 25) or personality_block:

        jump scene_reconcile_fail_jess

    ############################################
    ## SUCCESS BRANCH
    ############################################

    if trust >= 55:
        Jess "I just wanted a message."
        Jess "Anything."
        Jess "I believe you."
    else:
        Jess "Show me. Not with promises. With consistency."

    $ reconcile(name)

    return


label scene_reconcile_fail_jess:

    show jess sad at center

    Jess "I can’t do this again."
    Jess "I can’t keep hoping you’ll stay."

    Jess "I’m done."

    # PERMANENT LOCK
    $ meta = relationship_api.get_metadata("Jess")
    $ meta["reconciliation_locked"] = True
    $ relationship_api.set_metadata("Jess", meta)

    return


############################################################
## AUBREY
############################################################

label scene_reconcile_aubrey:

    $ name = "Aubrey"
    $ trust = relationship_api.get_trust(name)
    $ meta = relationship_api.get_metadata(name)
    $ scars = meta.get("emotional_scars", [])
    $ rebuild = meta.get("rebuild_progress", 0)
    $ stage = meta.get("rebuild_stage", 0)
    $ personality = meta.get("personality", "balanced")
    $ difficulty = calculate_reconcile_difficulty(name)
    $ required_trust = 30 + difficulty * 5
    $ personality_block = (personality in ["guarded", "volatile"] and stage < 3)

    scene gym_late
    with fade

    show aubrey annoyed at center

    Aubrey "You gonna stand there looking guilty all night?"

    if "major" in scars:
        Aubrey "You left me wondering where I stood."
    elif "moderate" in scars:
        Aubrey "Mixed signals. Constantly."
    else:
        Aubrey "You messed up. But you owned it."

    ############################################
    ## HARD FAIL CHECK — PERMANENT LOCK
    ############################################

    if trust < required_trust or ("major" in scars and rebuild < 25) or personality_block:

        jump scene_reconcile_fail_aubrey

    ############################################
    ## SUCCESS BRANCH
    ############################################

    if trust >= 65:
        Aubrey "I care about habits."
        Aubrey "Not speeches."
        Aubrey "If this works, it's because you kept showing up."
    else:
        Aubrey "Consistency. That’s what I need."

    $ reconcile(name)

    return


label scene_reconcile_fail_aubrey:

    show aubrey annoyed at center

    Aubrey "Stop."
    Aubrey "You haven’t earned this."
    Aubrey "And I’m not waiting around hoping you will."

    Aubrey "We’re done."

    # PERMANENT LOCK
    $ meta = relationship_api.get_metadata("Aubrey")
    $ meta["reconciliation_locked"] = True
    $ relationship_api.set_metadata("Aubrey", meta)

    return


############################################################
## MISTY
############################################################

label scene_reconcile_misty:

    $ name = "Misty"
    $ trust = relationship_api.get_trust(name)
    $ meta = relationship_api.get_metadata(name)
    $ scars = meta.get("emotional_scars", [])
    $ rebuild = meta.get("rebuild_progress", 0)
    $ stage = meta.get("rebuild_stage", 0)
    $ personality = meta.get("personality", "balanced")
    $ difficulty = calculate_reconcile_difficulty(name)
    $ required_trust = 30 + difficulty * 5
    $ personality_block = (personality in ["guarded", "volatile"] and stage < 3)

    scene cafe_evening
    with fade

    show misty sad at center

    misty "You're late."

    if "major" in scars:
        misty "You made me feel like I was too much."
    elif "moderate" in scars:
        misty "You pulled away when I needed you most."
    else:
        misty "You hurt me."

    ############################################
    ## HARD FAIL CHECK — PERMANENT LOCK
    ############################################

    if trust < required_trust or ("major" in scars and rebuild < 25) or personality_block:

        jump scene_reconcile_fail_misty

    ############################################
    ## SUCCESS BRANCH
    ############################################

    if trust >= 55:
        misty "Let me matter."
        "She lets you take her hand."
    else:
        misty "I want to forgive you."
        misty "But wanting isn’t the same as being ready."

    $ reconcile(name)

    return


label scene_reconcile_fail_misty:

    show misty sad at center

    misty "I can’t."
    misty "The hurt is too deep."
    misty "I don’t want to try again."

    # PERMANENT LOCK
    $ meta = relationship_api.get_metadata("Misty")
    $ meta["reconciliation_locked"] = True
    $ relationship_api.set_metadata("Misty", meta)

    return


############################################################
## KAIA
############################################################

label scene_reconcile_kaia:

    $ name = "Kaia"
    $ trust = relationship_api.get_trust(name)
    $ meta = relationship_api.get_metadata(name)
    $ scars = meta.get("emotional_scars", [])
    $ rebuild = meta.get("rebuild_progress", 0)
    $ stage = meta.get("rebuild_stage", 0)
    $ personality = meta.get("personality", "balanced")
    $ difficulty = calculate_reconcile_difficulty(name)
    $ required_trust = 30 + difficulty * 5
    $ personality_block = (personality in ["guarded", "volatile"] and stage < 3)

    scene rooftop_night
    with fade

    show kaia neutral at center

    kaia "Bold move coming up here."

    if "major" in scars:
        kaia "You made me feel stupid for believing you'd stay."
    elif "moderate" in scars:
        kaia "You used 'I'm fine' like a shield."
    else:
        kaia "You hurt me."

    ############################################
    ## HARD FAIL CHECK — PERMANENT LOCK
    ############################################

    if trust < required_trust or ("major" in scars and rebuild < 25) or personality_block:

        jump scene_reconcile_fail_kaia

    ############################################
    ## SUCCESS BRANCH
    ############################################

    if trust >= 60:
        kaia "If we’re doing this, we’re doing it honestly."
        "She rests her forehead against yours."
    else:
        kaia "You’re here."
        kaia "That’s more than I expected."

    $ reconcile(name)

    return


label scene_reconcile_fail_kaia:

    show kaia neutral at center

    kaia "Not this time."
    kaia "Not anymore."

    kaia "You didn’t show me enough."
    kaia "And I’m not giving out infinite chances."

    # PERMANENT LOCK
    $ meta = relationship_api.get_metadata("Kaia")
    $ meta["reconciliation_locked"] = True
    $ relationship_api.set_metadata("Kaia", meta)

    return


############################################################
## TIFFANY
############################################################

label scene_reconcile_tiffany:

    $ name = "Tiffany"
    $ trust = relationship_api.get_trust(name)
    $ meta = relationship_api.get_metadata(name)
    $ scars = meta.get("emotional_scars", [])
    $ rebuild = meta.get("rebuild_progress", 0)
    $ stage = meta.get("rebuild_stage", 0)
    $ personality = meta.get("personality", "balanced")
    $ difficulty = calculate_reconcile_difficulty(name)
    $ required_trust = 30 + difficulty * 5
    $ personality_block = (personality in ["guarded", "volatile"] and stage < 3)

    scene party_aftermath
    with fade

    show tiffany tired at center

    tiffany "You missed the dramatic part."

    if "major" in scars:
        tiffany "You made me feel like I was only fun when you needed a distraction."
    elif "moderate" in scars:
        tiffany "You kept me at arm’s length."
    else:
        tiffany "You hurt me."

    ############################################
    ## HARD FAIL CHECK — PERMANENT LOCK
    ############################################

    if trust < required_trust or ("major" in scars and rebuild < 25) or personality_block:

        jump scene_reconcile_fail_tiffany

    ############################################
    ## SUCCESS BRANCH
    ############################################

    if trust >= 50:
        tiffany "I already see the parts of you that aren’t fun."
        tiffany "And I stayed anyway."
    else:
        tiffany "I want to forgive you."
        tiffany "But I need consistency."

    $ reconcile(name)

    return


label scene_reconcile_fail_tiffany:

    show tiffany tired at center

    tiffany "I can’t keep doing this."
    tiffany "You haven’t earned my trust."
    tiffany "And I’m done pretending you might."

    # PERMANENT LOCK
    $ meta = relationship_api.get_metadata("Tiffany")
    $ meta["reconciliation_locked"] = True
    $ relationship_api.set_metadata("Tiffany", meta)

    return


############################################################
## NORAH
############################################################

label scene_reconcile_norah:

    $ name = "Norah"
    $ trust = relationship_api.get_trust(name)
    $ meta = relationship_api.get_metadata(name)
    $ scars = meta.get("emotional_scars", [])
    $ rebuild = meta.get("rebuild_progress", 0)
    $ stage = meta.get("rebuild_stage", 0)
    $ personality = meta.get("personality", "balanced")
    $ difficulty = calculate_reconcile_difficulty(name)
    $ required_trust = 30 + difficulty * 5
    $ personality_block = (personality in ["guarded", "volatile"] and stage < 3)

    scene library_night
    with fade

    show norah soft at center

    norah "I wondered when you'd come."

    if "major" in scars:
        norah "You made me feel like my care was a burden."
    elif "moderate" in scars:
        norah "You dragged me into your darkness without talking to me."
    else:
        norah "You hurt me."

    ############################################
    ## HARD FAIL CHECK — PERMANENT LOCK
    ############################################

    if trust < required_trust or ("major" in scars and rebuild < 25) or personality_block:

        jump scene_reconcile_fail_norah

    ############################################
    ## SUCCESS BRANCH
    ############################################

    if trust >= 60:
        norah "Love costs something."
        norah "I just needed to know you weren’t spending mine carelessly."
        norah "Take my hand."
        "You do."
    else:
        norah "I forgive easily."
        norah "But trust takes time."

    $ reconcile(name)

    return


label scene_reconcile_fail_norah:

    show norah soft at center

    norah "I forgive easily."
    norah "But I don’t trust easily."
    norah "And I don’t trust this."

    norah "I’m closing this door."

    # PERMANENT LOCK
    $ meta = relationship_api.get_metadata("Norah")
    $ meta["reconciliation_locked"] = True
    $ relationship_api.set_metadata("Norah", meta)

    return


############################################################
## GENERIC FALLBACK
############################################################

label scene_reconcile_generic:

    $ name = _return if _return else "Unknown"
    $ trust = relationship_api.get_trust(name)
    $ meta = relationship_api.get_metadata(name)
    $ scars = meta.get("emotional_scars", [])
    $ rebuild = meta.get("rebuild_progress", 0)
    $ stage = meta.get("rebuild_stage", 0)
    $ personality = meta.get("personality", "balanced")
    $ difficulty = calculate_reconcile_difficulty(name)
    $ required_trust = 30 + difficulty * 5
    $ personality_block = (personality in ["guarded", "volatile"] and stage < 3)

    scene campus_night
    with fade

    "[name]" "So. This is the part where you say you're sorry."

    ############################################
    ## HARD FAIL CHECK — PERMANENT LOCK
    ############################################

    if trust < required_trust or ("major" in scars and rebuild < 25) or personality_block:

        jump scene_reconcile_fail_generic

    ############################################
    ## SUCCESS BRANCH
    ############################################

    "[name]" "Then start by staying."

    $ reconcile(name)

    return


label scene_reconcile_fail_generic:

    "[name]" "No."
    "[name]" "This isn’t happening."
    "[name]" "Not now. Not ever."

    # PERMANENT LOCK
    $ meta = relationship_api.get_metadata(name)
    $ meta["reconciliation_locked"] = True
    $ relationship_api.set_metadata(name, meta)

    return



            