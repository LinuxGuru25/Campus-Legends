
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

    if mc_personality == "Confident":
        "[name] glances at the girl you're talking to… then looks away."

    if mc_personality == "Caring":
        "[name] looks hurt more than angry."

    if mc_personality == "Selfish":
        "Rumors spread that you moved on instantly."

    return



