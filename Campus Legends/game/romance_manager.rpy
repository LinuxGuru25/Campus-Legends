##############################################
## romance_manager.rpy
## Unified Romance Engine — Campus Legends
##############################################

default characters = {}


default relationship_points = {
    "Sienna": 0,
    "Jess": 0,
    "Aubrey": 0,
    "Norah": 0,
    "Misty": 0,
    "Kaia": 0,
    "Tiff": 0,
}

default romance_threshold = {
    "Sienna": 50,
    "Jess": 50,
    "Aubrey": 59,
    "Norah": 59,
    "Misty": 50,
    "Kaia": 50,
    "Tiff": 50,
}

default romance_personality_bonus = {
    "Sienna": "confident",
    "Jess": "caring",
    "Aubrey": "selfish",
    "Norah": "caring",
    "Misty": "caring",
    "Kaia": "confident",
    "Tiff": "confident",
}

default girlfriend = {
    "Sienna": False,
    "Jess": False,
    "Aubrey": False,
    "Norah": False,
    "Misty": False,
    "Kaia": False,
    "Tiff": False,
}

default girlfriend_bonuses = {
    "Sienna": {"confident": 1},
    "Jess": {"caring": 1},
    "Aubrey": {"selfish": 1},
    "Norah": {"caring": 1},
    "Misty": {"caring": 1},
    "Kaia": {"confident": 1},
    "Tiff": {"confident": 1},
}

init -10 python:

    class RelationshipAPI:

        def __init__(self):
            self.characters = {}
            self.global_meta = {}
            self.hooks = {
                "cheat": [],
                "breakup": [],
                "reconcile": [],
                "forgive": [],
                "reputation_change": [],
                "rebuild_milestone": [],
            }

        ############################################################
        ## CORE REGISTRY / METADATA
        ############################################################

        def ensure(self, name):
            if name not in store.characters:
                store.characters[name] = {
                    "caring": 0,
                    "name_as": name,
                    "relationship_state": "stable",
                    "status": "single",
                    "dating": False,
                    "broken_up": False,
                    "emotion": "neutral",
                    "severity": 0,
                    "emotional_scar": False,
                    "reconciliation_available": True,
                    "caught_cheating": False,
                    "trust": 0,
                    "affection": 0,
                    "cheated_on": False,
                    "personality": {
                        "confident": 0,
                        "caring": 0,
                        "selfish": 0,
                    },
                    "evolution": {
                        "stage": 0,
                        "history": [],
                    },
                    "breakup_reason": None,
                    "reaction_style": "neutral",
                    "breakup_severity_tier": "soft",
                    "rebuild_progress": 0,
                    "first_contact_done": False,
                    "rebuild_stage": 0,
                    "meta": {},
                }
            return store.characters[name]

        def get(self, name):
            return self.ensure(name)

        def get_all_names(self):
            return list(store.characters.keys())

        def get_global_metadata(self):
            return self.global_meta

        def set_global_metadata(self, data):
            self.global_meta = data

        def get_metadata(self, name):
            return self.ensure(name)["meta"]

        def set_metadata(self, name, data):
            self.ensure(name)["meta"] = data

        ############################################################
        ## BASIC GETTERS / SETTERS
        ############################################################

        def get_status(self, name):
            return self.ensure(name)["status"]

        def set_status(self, name, status):
            c = self.ensure(name)
            c["status"] = status

        def get_severity(self, name):
            return self.ensure(name)["severity"]

        def get_affection(self, name):
            return self.ensure(name)["affection"]

        def set_affection(self, name, value):
            c = self.ensure(name)
            c["affection"] = max(-100, min(100, value))

        def get_trust(self, name):
            return self.ensure(name)["trust"]

        def set_trust(self, name, value):
            c = self.ensure(name)
            c["trust"] = max(-100, min(100, value))
            self.update_relationship_state(name)

        ############################################################
        ## ROUTE LOCKING
        ############################################################

        def lock_route(self, name):
            c = self.ensure(name)
            c["status"] = "locked"

        def unlock_route(self, name):
            c = self.ensure(name)
            if c["status"] == "locked":
                c["status"] = "single"

        ############################################################
        ## HOOKS
        ############################################################

        def on(self, event_name, callback):
            if event_name in self.hooks:
                self.hooks[event_name].append(callback)

        def trigger(self, event_name, **kwargs):
            if event_name in self.hooks:
                for callback in self.hooks[event_name]:
                    callback(**kwargs)

        ############################################################
        ## TRUST / AFFECTION
        ############################################################

        TRUST_PERSONALITY_MODIFIERS = {
            "soft":        {"gain": +2, "loss": -1},
            "warm":        {"gain": +1, "loss": -1},
            "balanced":    {"gain": 0,  "loss": 0},
            "guarded":     {"gain": -1, "loss": +1},
            "volatile":    {"gain": -2, "loss": +2},
        }

        def _get_personality_label(self, name):
            meta = self.get_metadata(name)
            return meta.get("personality", "balanced")

        def add_trust(self, name, amount):
            c = self.ensure(name)
            c["trust"] += amount
            c["trust"] = max(-100, min(100, c["trust"]))
            self.update_relationship_state(name)
            return c["trust"]

        def add_trust_raw(self, name, amount):
            return self.add_trust(name, amount)

        def add_trust_scaled(self, name, amount):
            personality = self._get_personality_label(name)
            p_mod = self.TRUST_PERSONALITY_MODIFIERS.get(
                personality, self.TRUST_PERSONALITY_MODIFIERS["balanced"]
            )

            if amount > 0:
                amount += p_mod["gain"]
            elif amount < 0:
                amount += p_mod["loss"]

            return self.add_trust(name, amount)

        def add_trust_event_support(self, name, intensity=1):
            return self.add_trust_scaled(name, +5 * intensity)

        def add_trust_event_betrayal(self, name, intensity=1):
            return self.add_trust_scaled(name, -8 * intensity)

        def add_trust_event_absence(self, name, intensity=1):
            return self.add_trust_scaled(name, -5 * intensity)

        def add_trust_event_vulnerability(self, name, intensity=1):
            return self.add_trust_scaled(name, +4 * intensity)

        def add_trust_event_repair(self, name, intensity=1):
            return self.add_trust_scaled(name, +3 * intensity)

        def add_affection(self, name, amount):
            c = self.ensure(name)
            c["affection"] += amount
            c["affection"] = max(-100, min(100, c["affection"]))
            self.check_affection_milestones(name)
            self.update_route_state(name)
            return c["affection"]

        ############################################################
        ## DATING FLAGS
        ############################################################

        def set_dating(self, name, value=True):
            c = self.ensure(name)
            c["dating"] = value
            if value:
                c["status"] = "dating"
            self.update_relationship_state(name)

        def set_exclusive(self, name):
            c = self.ensure(name)
            c["status"] = "exclusive"

        def set_broken_up(self, name, value=True):
            c = self.ensure(name)
            c["broken_up"] = value
            if value:
                c["status"] = "broken_up"
            self.update_relationship_state(name)

        ############################################################
        ## ROMANCE POINTS / GIRLFRIEND
        ############################################################

        def add_points(self, name, amount):
            if name not in store.relationship_points:
                store.relationship_points[name] = 0

            store.relationship_points[name] += amount
            store.relationship_points[name] = max(0, store.relationship_points[name])

            self.check_romance_unlock(name)
            return store.relationship_points[name]

        def set_girlfriend(self, name):
            girlfriend[name] = True
            self.set_dating(name, True)

            if name in girlfriend_bonuses:
                for trait, bonus in girlfriend_bonuses[name].items():
                    if trait in store.mc_personality:
                        store.mc_personality[trait] += bonus

            for other in girlfriend:
                if other != name:
                    self.lock_route(other)

        def check_romance_unlock(self, name):
            if girlfriend.get(name, False):
                return False

            points = store.relationship_points.get(name, 0)
            threshold = romance_threshold[name]

            preferred_trait = romance_personality_bonus.get(name, None)
            if preferred_trait and store.mc_personality.get(preferred_trait, 0) >= 3:
                threshold -= 2

            if self.get_status(name) == "locked":
                return False

            if points >= threshold:
                self.set_girlfriend(name)
                return True

            return False

        ############################################################
        ## PERSONALITY‑ADJUSTED SEVERITY
        ############################################################

        def personality_adjusted_severity(self, name, base_severity):
            c = self.ensure(name)
            p = c["personality"]
            severity = base_severity

            if p["confident"] >= 5:
                if base_severity in [1, 2]:
                    severity -= 1

            if p["caring"] >= 5:
                if base_severity in [1, 2, 3]:
                    severity += 1

            if p["selfish"] >= 5:
                if base_severity in [2, 3]:
                    severity += 1

            severity = max(0, min(4, severity))
            return severity

        def map_severity_to_tier(self, severity):
            if severity <= 1:
                return "soft"
            elif severity <= 3:
                return "hard"
            else:
                return "catastrophic"

        def assign_reaction_style(self, name):
            c = self.ensure(name)
            p = c["personality"]

            if p["confident"] >= 5 and p["selfish"] < 5:
                return "cold"

            if p["caring"] >= 5 and p["selfish"] < 5:
                return "emotional"

            if p["selfish"] >= 5:
                return "explosive"

            if p["caring"] >= 3 and p["confident"] <= 3:
                return "passive"

            return "avoidant"

        ############################################################
        ## EMOTIONAL STATE / CONSEQUENCES
        ############################################################

        def calculate_emotional_state(self, name, severity):
            c = self.ensure(name)
            p = c["personality"]

            base_map = {
                0: "soft",
                1: "hurt",
                2: "distant",
                3: "confront",
                4: "broken",
            }

            emotion = base_map.get(severity, "broken")

            if p["confident"] >= 5:
                if emotion == "broken":
                    emotion = "confront"
                elif emotion == "confront":
                    emotion = "distant"

            if p["caring"] >= 5:
                if emotion == "distant":
                    emotion = "confront"

            if p["selfish"] >= 5:
                if emotion in ["hurt", "distant"]:
                    emotion = "confront"

            return emotion

        def apply_emotional_consequences(self, name, emotion, severity):
            c = self.ensure(name)

            trust_penalty = {
                "soft": 0,
                "hurt": -5,
                "distant": -10,
                "confront": -20,
                "broken": -35,
            }

            self.add_trust(name, trust_penalty.get(emotion, -10))

            if severity >= 3:
                c["emotional_scar"] = True

            cooldown_map = {
                "soft": 0,
                "hurt": 1,
                "distant": 2,
                "confront": 3,
                "broken": 5,
            }

            c["meta"]["cooldown_days"] = cooldown_map.get(emotion, 1)

        ############################################################
        ## RELATIONSHIP STATE MACHINE
        ############################################################

        def update_relationship_state(self, name):
            c = self.ensure(name)
            trust = c["trust"]
            severity = c["severity"]
            emotion = c["emotion"]
            scar = c["emotional_scar"]

            if c["relationship_state"] == "stable":
                if trust < -10 or emotion in ["hurt", "distant", "confront"]:
                    c["relationship_state"] = "unstable"

            if c["relationship_state"] == "unstable":
                if severity >= 3 or trust < -25 or emotion == "broken":
                    c["relationship_state"] = "broken"
                    c["broken_up"] = True
                    c["dating"] = False
                    c["status"] = "broken_up"

            if c["relationship_state"] == "broken":
                if trust > -5 and not scar and c["reconciliation_available"]:
                    c["relationship_state"] = "rebuilding"

            if c["relationship_state"] == "rebuilding":
                if trust >= 20 and emotion in ["soft", "hurt"]:
                    c["relationship_state"] = "stable"
                    c["broken_up"] = False
                    c["dating"] = True
                    c["status"] = "dating"

            return c["relationship_state"]

        ############################################################
        ## FORGIVENESS / RECONCILIATION
        ############################################################

        def calculate_forgiveness_difficulty(self, name):
            c = self.ensure(name)
            p = c["personality"]

            base = c["severity"]

            if c["emotional_scar"]:
                base += 1

            if c["trust"] < -10:
                base += 1
            if c["trust"] < -25:
                base += 1

            if p["caring"] >= 5:
                base += 1

            if p["confident"] >= 5:
                base -= 1

            if p["selfish"] >= 5 and c["severity"] >= 2:
                base += 1

            tier = c.get("breakup_severity_tier", "soft")
            if tier == "hard":
                base += 1
            elif tier == "catastrophic":
                base += 2

            difficulty = max(1, min(5, base + 1))
            c["meta"]["forgiveness_difficulty"] = difficulty
            return difficulty

        def can_forgive(self, name):
            c = self.ensure(name)
            difficulty = self.calculate_forgiveness_difficulty(name)

            required_trust = {
                1: -20,
                2: -10,
                3: 0,
                4: 10,
                5: 20,
            }

            cooldown_days = c["meta"].get("cooldown_days", 0)

            if c["cheated_on"] and cooldown_days > 0:
                return False

            if c["trust"] < required_trust[difficulty]:
                return False

            return True

        def can_reconcile(self, name):
            c = self.ensure(name)

            if c["relationship_state"] not in ["broken", "rebuilding"]:
                return False

            if c["emotional_scar"] and c["trust"] < 0:
                return False

            cooldown_days = c["meta"].get("cooldown_days", 0)
            if cooldown_days > 0 and c["relationship_state"] == "broken":
                return False

            if c["trust"] < -15:
                return False

            return True

        ############################################################
        ## DIALOGUE ROUTING
        ############################################################

        def get_emotional_reaction_scene(self, name, context_prefix):
            c = self.ensure(name)
            emotion = c["emotion"]
            state = c["relationship_state"]

            if emotion not in ["soft", "hurt", "distant", "confront", "broken"]:
                emotion = "soft"

            return f"{context_prefix}_{emotion}_{state}"

        def get_breakup_scene(self, name):
            c = self.ensure(name)
            emotion = c["emotion"]
            style = c["reaction_style"]

            if emotion not in ["soft", "hurt", "distant", "confront", "broken"]:
                emotion = "soft"
            if style not in ["cold", "emotional", "avoidant", "explosive", "passive"]:
                style = "neutral"

            return f"breakup_{emotion}_{style}"

        def get_reconciliation_scene(self, name):
            c = self.ensure(name)
            emotion = c["emotion"]
            style = c["reaction_style"]

            if emotion not in ["soft", "hurt", "distant", "confront", "broken"]:
                emotion = "soft"
            if style not in ["cold", "emotional", "avoidant", "explosive", "passive"]:
                style = "neutral"

            return f"reconcile_{emotion}_{style}"

        def get_confrontation_scene(self, name):
            c = self.ensure(name)
            trust = c["trust"]

            if trust < -25:
                return "scene_breakup_confrontation"
            elif trust < -10:
                return "scene_angry_confrontation"
            else:
                return "scene_cold_silence"

        ############################################################
        ## CHEATING / BREAKUP
        ############################################################

        def cheat(self, name, severity=1, detected=False):
            severity = self.personality_adjusted_severity(name, severity)

            c = self.ensure(name)
            c["cheated_on"] = True
            c["severity"] = severity

            emotion = self.calculate_emotional_state(name, severity)
            c["emotion"] = emotion

            self.apply_emotional_consequences(name, emotion, severity)
            self.update_relationship_state(name)

            self.trigger("cheat", name=name, severity=severity, detected=detected)

        def breakup(self, name, initiated_by_mc=False, severity=4, reason="unspecified"):
            severity = self.personality_adjusted_severity(name, severity)

            c = self.ensure(name)

            c["breakup_reason"] = reason
            c["reaction_style"] = self.assign_reaction_style(name)
            c["breakup_severity_tier"] = self.map_severity_to_tier(severity)

            c["broken_up"] = True
            c["dating"] = False
            c["status"] = "broken_up"
            c["severity"] = severity

            emotion = self.calculate_emotional_state(name, severity)
            c["emotion"] = emotion

            self.apply_emotional_consequences(name, emotion, severity)
            self.update_relationship_state(name)

            self.trigger(
                "breakup",
                name=name,
                initiated_by_mc=initiated_by_mc,
                severity=severity,
                tier=c["breakup_severity_tier"],
                reaction_style=c["reaction_style"],
                reason=reason,
            )

        ############################################################
        ## RECONCILIATION (ADVANCED)
        ############################################################

        def calculate_rebuild_difficulty(self, name):
            c = self.ensure(name)

            base = 1

            tier = c.get("breakup_severity_tier", "soft")
            if tier == "hard":
                base += 1
            elif tier == "catastrophic":
                base += 2

            if c["emotional_scar"]:
                base += 1

            style = c.get("reaction_style", "neutral")
            if style in ["cold", "avoidant"]:
                base += 1
            if style == "explosive":
                base += 2

            if c["trust"] < -10:
                base += 1
            if c["trust"] < -25:
                base += 1

            return max(1, min(5, base))

        def add_rebuild_progress(self, name, amount):
            c = self.ensure(name)

            difficulty = self.calculate_rebuild_difficulty(name)
            adjusted = int(amount / difficulty) if difficulty > 0 else amount

            c["rebuild_progress"] += adjusted
            c["rebuild_progress"] = max(0, min(100, c["rebuild_progress"]))

            self.update_rebuild_stage(name)
            return c["rebuild_progress"]

        def update_rebuild_stage(self, name):
            c = self.ensure(name)
            p = c["rebuild_progress"]

            old_stage = c["rebuild_stage"]

            if p >= 75:
                c["rebuild_stage"] = 3
            elif p >= 40:
                c["rebuild_stage"] = 2
            elif p >= 15:
                c["rebuild_stage"] = 1
            else:
                c["rebuild_stage"] = 0

            if c["rebuild_stage"] != old_stage:
                self.trigger("rebuild_milestone", name=name, stage=c["rebuild_stage"])

        def can_trigger_first_contact(self, name):
            c = self.ensure(name)

            if c["first_contact_done"]:
                return False

            if c["relationship_state"] != "broken":
                return False

            cooldown = c["meta"].get("cooldown_days", 0)
            if cooldown > 0:
                return False

            return True

        def complete_first_contact(self, name):
            c = self.ensure(name)
            c["first_contact_done"] = True
            self.add_rebuild_progress(name, 10)

        def reconcile(self, name):
            c = self.ensure(name)

            if not self.can_reconcile(name):
                return False

            c["broken_up"] = False
            c["dating"] = True
            c["status"] = "dating"

            self.add_trust(name, +20)

            c["rebuild_progress"] = 0
            c["rebuild_stage"] = 0
            c["first_contact_done"] = False

            self.update_relationship_state(name)
            self.trigger("reconcile", name=name)

            return True

        def forgive(self, name):
            c = self.ensure(name)

            if not self.can_forgive(name):
                return False

            c["cheated_on"] = False
            c["severity"] = 0

            self.add_trust(name, +15)

            c["emotion"] = self.calculate_emotional_state(name, c["severity"])
            self.update_relationship_state(name)

            self.trigger("forgive", name=name)
            return True

        ############################################################
        ## ROUTE EVOLUTION / JEALOUSY / GOSSIP / MILESTONES
        ############################################################

        def is_locked(self, name):
            return self.get_status(name) == "locked"

        def is_active_route(self, name):
            return self.get_status(name) in ("dating", "exclusive")

        def lock_if_cheated_too_much(self, name):
            sev = self.get_severity(name)
            if sev >= 80:
                self.lock_route(name)

        def unlock_if_reconciled(self, name):
            if self.get_status(name) == "dating":
                meta = self.get_metadata(name)
                if "hard_lock" in meta:
                    del meta["hard_lock"]
                    self.set_metadata(name, meta)

        def check_affection_milestones(self, name):
            aff = self.get_affection(name)
            meta = self.get_metadata(name)

            milestones = meta.get("affection_milestones_triggered", set())
            if not isinstance(milestones, set):
                milestones = set()

            def mark(m):
                milestones.add(m)
                meta["affection_milestones_triggered"] = milestones
                self.set_metadata(name, meta)

            if aff >= 10 and "10" not in milestones:
                renpy.call_in_new_context("affection_milestone_10", name)
                mark("10")

            if aff >= 20 and "20" not in milestones:
                renpy.call_in_new_context("affection_milestone_20", name)
                mark("20")

            if aff >= 30 and "30" not in milestones:
                renpy.call_in_new_context("affection_milestone_30", name)
                mark("30")

        def sanitize_relationship_metadata(self):
            for name, data in store.characters.items():
                meta = data.get("meta", {})
                obsolete = [k for k in meta.keys() if k.startswith("old_")]
                for k in obsolete:
                    del meta[k]
                self.set_metadata(name, meta)

        def gossip_on_cheat(self, name, severity, **kwargs):
            global_meta = self.get_global_metadata()
            rep = global_meta.get("reputation", {
                "social": 0,
                "romantic": 0,
                "loyalty": 0,
                "chaos": 0,
            })
            chaos = rep["chaos"]

            if chaos >= 10 and chaos < 25:
                renpy.call_in_new_context("cheating_rumors", name)

            if chaos >= 25:
                renpy.call_in_new_context("cheating_rumors", name)
                renpy.call_in_new_context("world_reacts_to_breakup", name)

        def check_dynamic_jealousy(self, primary, others):
            primary_aff = self.get_affection(primary)

            for other in others:
                other_aff = self.get_affection(other)
                if other_aff >= primary_aff - 2:
                    renpy.call_in_new_context("jealousy_scene", primary, other)

        def update_route_state(self, name):
            self.ensure(name)

            aff = self.get_affection(name)
            tr = self.get_trust(name)
            sev = self.get_severity(name)
            status = self.get_status(name)

            if sev >= 80:
                self.set_broken_up(name, True)
                self.lock_route(name)
                return

            if aff >= 10 and tr >= 5 and status in ("single", "neutral", "friends"):
                self.set_dating(name, True)

            if aff >= 20 and tr >= 15 and status == "dating":
                self.set_exclusive(name)

            if status == "dating" and sev == 0:
                self.unlock_if_reconciled(name)

        ############################################################
        ## TRUST DECAY / DEBUG
        ############################################################

        TRUST_DECAY_RATE = 1
        TRUST_DECAY_MIN = 20

        def decay_trust_tick(self):
            for name in self.get_all_names():
                current = self.get_trust(name)
                if current > self.TRUST_DECAY_MIN:
                    self.add_trust(name, -self.TRUST_DECAY_RATE)

        def get_trust_percent(self, name):
            trust = self.get_trust(name)
            return max(0, min(100, trust))

        def debug_relationship(self, name):
            meta = self.get_metadata(name)
            data = {
                "affection": self.get_affection(name),
                "trust": self.get_trust(name),
                "status": self.get_status(name),
                "severity": self.get_severity(name),
                "reconciliation_locked": meta.get("reconciliation_locked", False),
                "rebuild_stage": meta.get("rebuild_stage", 0),
                "rebuild_progress": meta.get("rebuild_progress", 0),
            }
            renpy.log(f"[REL DEBUG] {name}: {data}")

        ############################################################
        ## HOOK REGISTRATION
        ############################################################

        def register_default_hooks(self):
            self.on("cheat", self.gossip_on_cheat)

init -10 python:
    relationship_api = RelationshipAPI()
    relationship_api.register_default_hooks()

    










