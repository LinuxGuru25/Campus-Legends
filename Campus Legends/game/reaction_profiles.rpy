##############################################
## CHARACTER REACTION PROFILES
##############################################

init python:

    def setup_reaction_profiles():
        mapping = {
            "Sienna": "strict",
            "Jess": "forgiving",
            "Aubrey": "balanced",
            "Norah": "balanced",
            "Tiffany": "strict",
            "Kaia": "strict",
            "Misty": "forgiving",
        }

        for name, profile in mapping.items():
            relationship_api.ensure(name)
            meta = relationship_api.get_metadata(name)
            meta["reaction_profile"] = profile
            relationship_api.set_metadata(name, meta)


label setup_relationship_profiles:
    $ setup_reaction_profiles()
    return


default reaction_profiles = {
    "forgiving": {
        "cheating_multiplier": 0.6,
        "breakup_threshold": 25,
        "reconcile_difficulty": 0.7,
        "anger_spike": 5,
    },
    "balanced": {
        "cheating_multiplier": 1.0,
        "breakup_threshold": 40,
        "reconcile_difficulty": 1.0,
        "anger_spike": 10,
    },
    "strict": {
        "cheating_multiplier": 1.4,
        "breakup_threshold": 60,
        "reconcile_difficulty": 1.4,
        "anger_spike": 20,
    },
}

##############################################
## CHARACTER-SPECIFIC CHEAT REACTIONS
## Campus Legends — API-Compatible 
##############################################

init python:

    ############################################################
    ## Helper: Set a metadata flag safely
    ############################################################
    def set_flag(name, flag):
        """
        Stores a character-specific reaction flag inside the API's metadata.
        """
        meta = relationship_api.get_metadata(name)
        meta[flag] = True
        relationship_api.set_metadata(name, meta)


    ############################################################
    ## 1. NORAH
    ############################################################
    def norah_cheat_reaction(name, severity, **kwargs):
        if name != "Norah":
            return

        renpy.notify("Norah found out. She won’t forget this.")
        set_flag("Norah", "nora_cold_shoulder")


    ############################################################
    ## 2. SIENNA
    ############################################################
    def sienna_cheat_reaction(name, severity, **kwargs):
        if name != "Sienna":
            return

        if severity >= 3:
            renpy.notify("Sienna shuts down completely.")
            set_flag("Sienna", "sienna_freeze_out")
        else:
            renpy.notify("Sienna keeps her distance, trying not to show she's hurt.")
            set_flag("Sienna", "sienna_distant")


    ############################################################
    ## 3. JESS
    ############################################################
    def jess_cheat_reaction(name, severity, **kwargs):
        if name != "Jess":
            return

        if severity >= 3:
            renpy.notify("Jess stops replying to your messages.")
            set_flag("Jess", "jess_silent_treatment")
        else:
            renpy.notify("Jess becomes noticeably quieter around you.")
            set_flag("Jess", "jess_withdrawn")


    ############################################################
    ## 4. AUBREY
    ############################################################
    def aubrey_cheat_reaction(name, severity, **kwargs):
        if name != "Aubrey":
            return

        if severity >= 3:
            renpy.notify("Aubrey confronts you with raw emotion.")
            set_flag("Aubrey", "aubrey_confrontation")
        else:
            renpy.notify("Aubrey gives you sharp, clipped responses.")
            set_flag("Aubrey", "aubrey_snappy")


    ############################################################
    ## 5. MISTY
    ############################################################
    def misty_cheat_reaction(name, severity, **kwargs):
        if name != "Misty":
            return

        if severity >= 3:
            renpy.notify("Misty avoids eye contact and keeps to herself.")
            set_flag("Misty", "misty_avoiding")
        else:
            renpy.notify("Misty seems hurt but tries to act normal.")
            set_flag("Misty", "misty_masking")


    ############################################################
    ## 6. KAIA
    ############################################################
    def kaia_cheat_reaction(name, severity, **kwargs):
        if name != "Kaia":
            return

        if severity >= 3:
            renpy.notify("Kaia shuts you out with cutting precision.")
            set_flag("Kaia", "kaia_shutout")
        else:
            renpy.notify("Kaia becomes sarcastic and guarded.")
            set_flag("Kaia", "kaia_guarded")


    ############################################################
    ## 7. TIFFANY
    ############################################################
    def tiffany_cheat_reaction(name, severity, **kwargs):
        if name != "Tiffany":
            return

        if severity >= 3:
            renpy.notify("Tiffany makes sure people know she's 'done with drama'.")
            set_flag("Tiffany", "tiffany_public_reaction")
            relationship_api.add_reputation("romantic", -3)
        else:
            renpy.notify("Tiffany becomes politely distant.")
            set_flag("Tiffany", "tiffany_polite_distance")


    ############################################################
    ## REGISTER ALL HOOKS WITH THE NEW API
    ############################################################

    relationship_api.on("cheat", norah_cheat_reaction)
    relationship_api.on("cheat", sienna_cheat_reaction)
    relationship_api.on("cheat", jess_cheat_reaction)
    relationship_api.on("cheat", aubrey_cheat_reaction)
    relationship_api.on("cheat", misty_cheat_reaction)
    relationship_api.on("cheat", kaia_cheat_reaction)
    relationship_api.on("cheat", tiffany_cheat_reaction)










