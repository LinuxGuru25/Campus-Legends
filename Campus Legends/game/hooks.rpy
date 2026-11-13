
label world_reacts_to_breakup(name):

    if reputation["chaos"] >= 20:
        "You overhear students whispering about your breakup."

    if reputation["loyalty"] <= -10:
        "Someone posts a vague tweet about untrustworthy guys."

    if rep_with[name] <= -15:
        "[name] avoids eye contact when she sees you."

    return

label social_media_breakup_shift(name):

    if reputation["chaos"] >= 20:
        "Your feed fills with memes about campus drama."

    if reputation["loyalty"] <= -10:
        "Someone subtweets: 'Some people never change.'"

    return


label jealousy_after_breakup(name):

    if get_dominant_personality() == "Confident":
        "[name] glances at the girl you're talking to… then looks away."

    if get_dominant_personality() == "Caring":
        "[name] looks hurt more than angry."

    if get_dominant_personality() == "Selfish":
        "Rumors spread that you moved on instantly."

    return


label affection_milestone_10(name):

    $ renpy.notify(name + " opens up a little more.")

    return


label affection_milestone_20(name):

    scene black with fade
    pause 0.3

    "[name] finds excuses to stay near you."

    "[name] \"Promise me you won't disappear on me?\""

    "Something between you two has shifted."

    return


label affection_milestone_30(name):

    scene black with fade
    pause 0.3

    "[name] looks at you like you're the only person in the room."

    "[name] \"I'm really glad I met you.\""

    "This one feels different. Real."

    return


label cheating_rumors(name):

    scene black with fade
    pause 0.3

    "Whispers follow you across campus."

    "[name] heard the rumors too."

    "[name] \"People are talking. I'm trying not to listen.\""

    return


label jealousy_scene(primary, other):

    scene black with fade
    pause 0.3

    "[primary] notices how much time you spend with [other]."

    "[primary] \"You two seem close.\""

    "The words come out light. The look doesn't."

    return


