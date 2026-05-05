##############################################
## CHARACTER-SPECIFIC RECONCILIATION REACTIONS
## Campus Legends — API-Compatible
##############################################

init python:

    ############################################################
    ## Helper: Set reconciliation flags in metadata
    ############################################################
    def set_reconcile_flag(name, flag):
        meta = relationship_api.get_metadata(name)
        meta[flag] = True
        relationship_api.set_metadata(name, meta)


    ############################################################
    ## GENERIC FALLBACK REACTION
    ############################################################
    def generic_reconcile_reaction(name, **kwargs):
        renpy.notify(f"You and {name} slowly rebuild trust.")


    ############################################################
    ## SIENNA
    ############################################################
    def sienna_reconcile_reaction(name, **kwargs):
        if name != "Sienna":
            return

        renpy.notify("Sienna lets out a long breath… 'Okay. Let's try again.'")
        set_reconcile_flag("Sienna", "sienna_softening")


    ############################################################
    ## JESS
    ############################################################
    def jess_reconcile_reaction(name, **kwargs):
        if name != "Jess":
            return

        renpy.notify("Jess gives a small smile. 'I missed talking to you.'")
        set_reconcile_flag("Jess", "jess_warm_reconnect")


    ############################################################
    ## AUBREY
    ############################################################
    def aubrey_reconcile_reaction(name, **kwargs):
        if name != "Aubrey":
            return

        renpy.notify("Aubrey nudges your shoulder. 'Don't make me regret this.'")
        set_reconcile_flag("Aubrey", "aubrey_guard_down")


    ############################################################
    ## MISTY
    ############################################################
    def misty_reconcile_reaction(name, **kwargs):
        if name != "Misty":
            return

        renpy.notify("Misty hugs you tightly. 'I just… needed time.'")
        set_reconcile_flag("Misty", "misty_reconnected")


    ############################################################
    ## KAIA
    ############################################################
    def kaia_reconcile_reaction(name, **kwargs):
        if name != "Kaia":
            return

        renpy.notify("Kaia crosses her arms, then softens. 'Alright. Clean slate.'")
        set_reconcile_flag("Kaia", "kaia_clean_slate")


    ############################################################
    ## TIFFANY
    ############################################################
    def tiffany_reconcile_reaction(name, **kwargs):
        if name != "Tiffany":
            return

        renpy.notify("Tiffany sighs. 'Fine… but no more drama, okay?'")
        set_reconcile_flag("Tiffany", "tiffany_reopens_door")

        # Reputation boost for public reconciliation
        relationship_api.add_reputation("romantic", 2)
        relationship_api.add_reputation("social", 1)


    ############################################################
    ## NORAH
    ############################################################
    def norah_reconcile_reaction(name, **kwargs):
        if name != "Norah":
            return

        renpy.notify("Norah smiles softly. 'Thank you for trying… it means a lot.'")
        set_reconcile_flag("Norah", "norah_heart_open")


    ############################################################
    ## REGISTER ALL RECONCILIATION HOOKS
    ############################################################

    relationship_api.on("reconcile", generic_reconcile_reaction)
    relationship_api.on("reconcile", sienna_reconcile_reaction)
    relationship_api.on("reconcile", jess_reconcile_reaction)
    relationship_api.on("reconcile", aubrey_reconcile_reaction)
    relationship_api.on("reconcile", misty_reconcile_reaction)
    relationship_api.on("reconcile", kaia_reconcile_reaction)
    relationship_api.on("reconcile", tiffany_reconcile_reaction)
    relationship_api.on("reconcile", norah_reconcile_reaction)
