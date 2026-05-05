##############################################
## 00_romance_manager.rpy
## Unified Romance Engine — Campus Legends
##############################################

init python:

    ############################################################
    ## RELATIONSHIP API CLASS
    ############################################################

    class RelationshipAPI:

        def __init__(self):
            self.characters = {}
            self.global_meta = {}

            # Event hooks for other systems (MC emotional system, healing, UI, etc.)
            self.hooks = {
                "cheat": [],
                "breakup": [],
                "reconcile": [],
                "forgive": [],
                "reputation_change": [],
            }

        ############################################################
        ## CHARACTER INITIALIZATION
        ############################################################

        def ensure(self, name):
            """
            Ensures a character exists in the relationship system.
            Creates default values if missing.
            """
            if name not in store.characters:
                store.characters[name] = {
                    "trust": 0,
                    "affection": 0,
                    "cheated_on": False,
                    "dating": False,
                    "broken_up": False,
                    "severity": 0,
                    "personality": {
                        "volatility": 0.5,
                        "type": "Neutral",
                    },
                    "evolution": {
                        "stage": 0,
                        "history": [],
                    },
                    "meta": {},
                }
            return store.characters[name]

        ############################################################
        ## BASIC GETTER (REQUIRED FOR STATS APP)
        ############################################################

        def get(self, name):
            """
            Returns the character data dictionary.
            Auto‑creates the character if missing.
            """
            return self.ensure(name)

        ############################################################
        ## GLOBAL METADATA ACCESS (REQUIRED FOR STATS APP)
        ############################################################

        def get_global_metadata(self):
            """
            Returns the global metadata dictionary used by the Stats App.
            """
            return self.global_meta

        ############################################################
        ## HOOK REGISTRATION
        ############################################################

        def on(self, event_name, callback):
            """
            Register a callback for an event.
            Example: relationship_api.on("cheat", my_function)
            """
            if event_name in self.hooks:
                self.hooks[event_name].append(callback)

        def trigger(self, event_name, **kwargs):
            """
            Trigger an event and notify all listeners.
            """
            if event_name in self.hooks:
                for callback in self.hooks[event_name]:
                    callback(**kwargs)

        ############################################################
        ## CORE RELATIONSHIP FUNCTIONS
        ############################################################

        def add_trust(self, name, amount):
            c = self.ensure(name)
            c["trust"] += amount
            c["trust"] = max(-100, min(100, c["trust"]))
            return c["trust"]

        def add_affection(self, name, amount):
            c = self.ensure(name)
            c["affection"] += amount
            c["affection"] = max(-100, min(100, c["affection"]))
            return c["affection"]

        def set_dating(self, name, value=True):
            c = self.ensure(name)
            c["dating"] = value

        def set_broken_up(self, name, value=True):
            c = self.ensure(name)
            c["broken_up"] = value

        ############################################################
        ## CHEATING SYSTEM (API SIDE)
        ############################################################

        def cheat(self, name, severity=1, detected=False):
            """
            Called when MC cheats on a character.
            """
            c = self.ensure(name)
            c["cheated_on"] = True
            c["severity"] = severity

            # Trust hit
            trust_loss = -10 * severity
            self.add_trust(name, trust_loss)

            # Trigger event for MC emotional system, healing system, etc.
            self.trigger("cheat", name=name, severity=severity, detected=detected)

        ############################################################
        ## BREAKUP SYSTEM
        ############################################################

        def breakup(self, name, initiated_by_mc=False):
            c = self.ensure(name)
            c["broken_up"] = True
            c["dating"] = False

            # Trust drop
            self.add_trust(name, -20)

            # Trigger event
            self.trigger("breakup", name=name, initiated_by_mc=initiated_by_mc)

        ############################################################
        ## RECONCILIATION SYSTEM
        ############################################################

        def reconcile(self, name):
            c = self.ensure(name)
            c["broken_up"] = False
            c["dating"] = True

            # Trust boost
            self.add_trust(name, +10)

            # Trigger event
            self.trigger("reconcile", name=name)

        ############################################################
        ## FORGIVENESS SYSTEM
        ############################################################

        def forgive(self, name):
            c = self.ensure(name)
            c["cheated_on"] = False
            c["severity"] = 0

            self.add_trust(name, +15)

            self.trigger("forgive", name=name)

        ############################################################
        ## PERSONALITY SYSTEM
        ############################################################

        def set_personality(self, name, ptype, volatility=0.5):
            c = self.ensure(name)
            c["personality"]["type"] = ptype
            c["personality"]["volatility"] = volatility

        ############################################################
        ## EVOLUTION SYSTEM
        ############################################################

        def evolve(self, name, stage):
            c = self.ensure(name)
            c["evolution"]["stage"] = stage
            c["evolution"]["history"].append(stage)

        ############################################################
        ## CONFRONTATION ROUTING
        ############################################################

        def get_confrontation_scene(self, name):
            c = self.ensure(name)
            trust = c["trust"]
            vol = c["personality"]["volatility"]

            if trust < -25:
                return "scene_breakup_confrontation"
            elif trust < -10:
                return "scene_angry_confrontation"
            elif vol > 0.7:
                return "scene_volatile_reaction"
            else:
                return "scene_cold_silence"


############################################################
## INSTANTIATE THE API (CRITICAL)
############################################################

init python:
    relationship_api = RelationshipAPI()


