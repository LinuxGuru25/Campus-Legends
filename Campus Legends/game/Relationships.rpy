##############################################
## RELATIONSHIPS.rpy — Campus Legends
## Unified Relationship API Integration
## Clean, Modern, Conflict-Free
##############################################

default characters = {}

init python:

    ############################################################
    ## 1. CHARACTER REGISTRATION
    ############################################################

    def register_character(name, personality="Neutral"):
        """
        Ensures the character exists in the API registry.
        Safe to call multiple times.
        """
        if name not in characters:
            characters[name] = {
                "personality": personality,
            }

        # Register with the Relationship API
        relationship_api.ensure(name)


    ############################################################
    ## 2. SAFE WRAPPERS FOR AFFECTION / TRUST
    ############################################################

    def add_affection(name, amount):
        """
        Adds affection using the API.
        """
        relationship_api.add_affection(name, amount)

    def add_trust(name, amount):
        """
        Adds trust using the API.
        """
        relationship_api.add_trust(name, amount)

    def get_affection(name):
        return relationship_api.get_affection(name)

    def get_trust(name):
        return relationship_api.get_trust(name)


    ############################################################
    ## 3. ROUTE / STATUS HELPERS
    ############################################################

    def is_dating(name):
        return relationship_api.get_status(name) == "dating"

    def is_exclusive(name):
        return relationship_api.get_status(name) == "exclusive"

    def is_broken_up(name):
        return relationship_api.get_status(name) == "broken_up"

    def lock_route(name):
        relationship_api.lock_route(name)

    def unlock_route(name):
        relationship_api.unlock_route(name)


    ############################################################
    ## 4. CHEATING / BREAKUP / FORGIVENESS HOOKS
    ############################################################

    def on_cheat(name, severity, **kwargs):
        """
        Triggered automatically by the API when cheating occurs.
        Routes to story labels.
        """
        renpy.call_in_new_context("cheating_reaction", name)
        renpy.call_in_new_context("cheating_rumors", name)
        renpy.call_in_new_context("cheating_jealousy", name)

    def on_breakup(name, severity, **kwargs):
        """
        Triggered automatically by the API when a breakup occurs.
        """
        renpy.call_in_new_context("world_reacts_to_breakup", name)
        renpy.call_in_new_context("social_media_breakup_shift", name)
        renpy.call_in_new_context("jealousy_after_breakup", name)

    def on_reconcile(name, **kwargs):
        """
        Triggered when forgiveness threshold is reached.
        """
        renpy.call_in_new_context("reconciliation_scene", name)


    ############################################################
    ## 5. REGISTER HOOKS WITH THE API
    ############################################################

    relationship_api.on("cheat", on_cheat)
    relationship_api.on("breakup", on_breakup)
    relationship_api.on("reconcile", on_reconcile)


    ############################################################
    ## 6. OPTIONAL DEBUGGING UTILITIES
    ############################################################

    def debug_relationship(name):
        """
        Prints all relationship data for debugging.
        """
        data = {
            "affection": relationship_api.get_affection(name),
            "trust": relationship_api.get_trust(name),
            "status": relationship_api.get_status(name),
            "severity": relationship_api.get_severity(name),
        }
        renpy.log(f"[REL DEBUG] {name}: {data}")



