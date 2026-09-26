## RUMOR & GOSSIP SYSTEM
## Campus Legends — API Compatible
## Integrates with Jealousy, Breakups, Cheating, Personality

init python:

    class RumorSystem:

        def __init__(self):
            # Global rumor score (campus-wide)
            self.global_key = "campus_rumor_score"

            # How fast rumors decay per day
            self.decay_rate = 1

            # Rumor thresholds
            self.levels = {
                "clean": 0,
                "whispers": 15,
                "talked_about": 30,
                "problematic": 50,
                "infamous": 75,
            }

        # ---------------------------------------------------------
        # GET RUMOR SCORE
        # ---------------------------------------------------------
        def get(self):
            meta = relationship_api.get_global_metadata()
            if self.global_key not in meta:
                meta[self.global_key] = 0
                relationship_api.set_global_metadata(meta)
            return meta[self.global_key]

        # ---------------------------------------------------------
        # SET RUMOR SCORE
        # ---------------------------------------------------------
        def set(self, value):
            meta = relationship_api.get_global_metadata()
            meta[self.global_key] = max(0, value)
            relationship_api.set_global_metadata(meta)

        # ---------------------------------------------------------
        # ADD RUMOR POINTS
        # ---------------------------------------------------------
        def add(self, amount):
            current = self.get()
            self.set(current + amount)
            return current + amount

        # ---------------------------------------------------------
        # DECAY RUMORS
        # ---------------------------------------------------------
        def decay(self):
            current = self.get()
            self.set(current - self.decay_rate)

        # ---------------------------------------------------------
        # PERSONALITY MODIFIER
        # ---------------------------------------------------------
        def personality_modifier(self):
            """
            Caring MC reduces rumor spread.
            Selfish MC increases rumor spread.
            Confident MC reduces rumor impact.
            """
            data = get_personality_data()

            mod = 0

            if data["Caring"] >= 25:
                mod -= 2

            if data["Selfish"] >= 25:
                mod += 3

            if data["Confident"] >= 25:
                mod -= 1

            return mod

        # ---------------------------------------------------------
        # JEALOUSY INTEGRATION
        # ---------------------------------------------------------
        def jealousy_modifier(self, girl):
            """
            High jealousy from a girl increases rumor spread.
            """
            value = jealousy.get(girl)

            if value >= 50:
                return 5
            if value >= 25:
                return 2
            return 0

        # ---------------------------------------------------------
        # CHEATING INTEGRATION
        # ---------------------------------------------------------
        def cheating_modifier(self, severity):
            """
            Severity 1 = mild cheating
            Severity 2 = caught cheating
            Severity 3 = public cheating
            """
            if severity == 1:
                return 10
            if severity == 2:
                return 20
            if severity == 3:
                return 35
            return 0

        # ---------------------------------------------------------
        # TRIGGER RUMOR EVENT
        # ---------------------------------------------------------
        def trigger(self, source, severity=1):
            """
            Called when something rumor-worthy happens.
            source = girl or event name
            severity = 1–3
            """
            base = 5 * severity

            # Add personality influence
            base += self.personality_modifier()

            # If source is a girl, add jealousy influence
            if source in jealousy.base_jealousy:
                base += self.jealousy_modifier(source)

            # Apply rumor
            self.add(base)

            # Trigger reactions
            self.react()

        # ---------------------------------------------------------
        # RUMOR REACTION LOGIC
        # ---------------------------------------------------------
        def react(self):
            """
            Determines what happens when rumor score rises.
            """
            value = self.get()

            if value >= self.levels["whispers"] and value < self.levels["talked_about"]:
                renpy.call_in_new_context("rumor_whispers")

            elif value >= self.levels["talked_about"] and value < self.levels["problematic"]:
                renpy.call_in_new_context("rumor_talked_about")

            elif value >= self.levels["problematic"] and value < self.levels["infamous"]:
                renpy.call_in_new_context("rumor_problematic")

            elif value >= self.levels["infamous"]:
                renpy.call_in_new_context("rumor_infamous")


    rumor = RumorSystem()

label rumor_whispers:
    # People whisper when MC walks by
    return

label rumor_talked_about:
    # Girls lose a little trust
    $ relationship_api.add_trust("sienna", -1)
    $ relationship_api.add_trust("jess", -1)
    return

label rumor_problematic:
    # Some scenes lock, jealousy rises faster
    $ jealousy.add("aubrey", 5)
    return

label rumor_infamous:
    # Major consequences: breakups, confrontations, social media blowups
    return

