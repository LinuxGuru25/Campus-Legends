##############################################
## CHARACTER-SPECIFIC BREAKUP REACTIONS
## Campus Legends — API-Compatible
##############################################

init python:

    ############################################################
    ## Helper: Set a breakup flag safely in API metadata
    ############################################################
    def set_breakup_flag(name, flag):
        meta = relationship_api.get_metadata(name)
        meta[flag] = True
        relationship_api.set_metadata(name, meta)


    ############################################################
    ## GENERIC FALLBACK REACTION
    ############################################################
    def generic_breakup_reaction(name, severity, **kwargs):
        if severity >= 3:
            renpy.notify(f"{name} is deeply hurt by the breakup.")
        else:
            renpy.notify(f"{name} seems distant after the breakup.")


    ############################################################
    ## SIENNA
    ############################################################
    def sienna_breakup_reaction(name, severity, **kwargs):
        if name != "Sienna":
            return

        if severity >= 3:
            renpy.notify("Sienna shuts down emotionally after the breakup.")
            set_breakup_flag("Sienna", "sienna_post_breakup_freeze")
        else:
            renpy.notify("Sienna keeps things polite but cold.")
            set_breakup_flag("Sienna", "sienna_polite_cold")


    ############################################################
    ## JESS
    ############################################################
    def jess_breakup_reaction(name, severity, **kwargs):
        if name != "Jess":
            return

        if severity >= 3:
            renpy.notify("Jess stops reaching out entirely.")
            set_breakup_flag("Jess", "jess_total_withdrawal")
        else:
            renpy.notify("Jess replies slower and with shorter messages.")
            set_breakup_flag("Jess", "jess_slow_fade")


    ############################################################
    ## AUBREY
    ############################################################
    def aubrey_breakup_reaction(name, severity, **kwargs):
        if name != "Aubrey":
            return

        if severity >= 3:
            renpy.notify("Aubrey has a sharp, emotional confrontation before pulling away.")
            set_breakup_flag("Aubrey", "aubrey_final_confrontation")
        else:
            renpy.notify("Aubrey becomes sarcastic and guarded around you.")
            set_breakup_flag("Aubrey", "aubrey_guarded_post_breakup")


    ############################################################
    ## MISTY
    ############################################################
    def misty_breakup_reaction(name, severity, **kwargs):
        if name != "Misty":
            return

        if severity >= 3:
            renpy.notify("Misty avoids you completely after the breakup.")
            set_breakup_flag("Misty", "misty_total_avoidance")
        else:
            renpy.notify("Misty seems fragile but tries to stay friendly.")
            set_breakup_flag("Misty", "misty_fragile_friendly")


    ############################################################
    ## KAIA
    ############################################################
    def kaia_breakup_reaction(name, severity, **kwargs):
        if name != "Kaia":
            return

        if severity >= 3:
            renpy.notify("Kaia cuts you off with brutal clarity.")
            set_breakup_flag("Kaia", "kaia_hard_cutoff")
        else:
            renpy.notify("Kaia keeps things strictly business.")
            set_breakup_flag("Kaia", "kaia_business_only")


    ############################################################
    ## TIFFANY
    ############################################################
    def tiffany_breakup_reaction(name, severity, **kwargs):
        if name != "Tiffany":
            return

        if severity >= 3:
            renpy.notify("Tiffany makes it very public that she's 'done with drama'.")
            set_breakup_flag("Tiffany", "tiffany_public_breakup")
            relationship_api.add_reputation("romantic", -2)
            relationship_api.add_reputation("chaos", 3)
        else:
            renpy.notify("Tiffany remains polite but clearly distant.")
            set_breakup_flag("Tiffany", "tiffany_polite_breakup")


    ############################################################
    ## NORAH
    ############################################################
    def norah_breakup_reaction(name, severity, **kwargs):
        if name != "Norah":
            return

        if severity >= 3:
            renpy.notify("Norah quietly walls herself off emotionally.")
            set_breakup_flag("Norah", "norah_walled_off")
        else:
            renpy.notify("Norah stays kind, but there's a new distance.")
            set_breakup_flag("Norah", "norah_soft_distance")


    ############################################################
    ## REGISTER ALL BREAKUP HOOKS
    ############################################################

    relationship_api.on("breakup", generic_breakup_reaction)
    relationship_api.on("breakup", sienna_breakup_reaction)
    relationship_api.on("breakup", jess_breakup_reaction)
    relationship_api.on("breakup", aubrey_breakup_reaction)
    relationship_api.on("breakup", misty_breakup_reaction)
    relationship_api.on("breakup", kaia_breakup_reaction)
    relationship_api.on("breakup", tiffany_breakup_reaction)
    relationship_api.on("breakup", norah_breakup_reaction)
