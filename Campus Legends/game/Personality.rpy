# ============================================================
# CAMPUS LEGENDS - PERSONALITY MANAGER
# ============================================================

# ------------------------------------------------------------
# MC PERSONALITY
# ------------------------------------------------------------

default mc_personality = {
    "Confident": 3,
    "Caring": 0,
    "Selfish": 0,
}

default dominant_personality = "Neutral"

# ------------------------------------------------------------
# PERSONALITY SETTINGS
# ------------------------------------------------------------

init python:

    PERSONALITY_THRESHOLD = 10
    PERSONALITY_EVOLUTION_THRESHOLD = 30

    PERSONALITY_DEFAULTS = {
        "Confident": 3,
        "Caring": 0,
        "Selfish": 0,
    }

    PERSONALITY_TRAITS = [
        "Confident",
        "Caring",
        "Selfish",
    ]

    # Each girl's preferred MC personality traits.
    preferred_personality = {
        "sienna": ["Confident", "Caring"],
        "jess": ["Caring"],
        "aubrey": ["Selfish"],
        "norah": ["Caring"],
        "misty": ["Caring"],
        "kaia": ["Caring", "Confident"],
        "tiff": ["Confident"],
    }

    # --------------------------------------------------------
    # PERSONALITY POINTS
    # --------------------------------------------------------

    def _ensure_personality_data():
        data = store.mc_personality

        if isinstance(data, dict):
            return data

        migrated = PERSONALITY_DEFAULTS.copy()

        if isinstance(data, str):
            legacy_trait = next(
                (trait for trait in PERSONALITY_TRAITS
                 if trait.lower() == data.strip().lower()),
                None
            )

            if legacy_trait:
                migrated[legacy_trait] = PERSONALITY_THRESHOLD
            elif data.strip().lower() not in ("", "neutral"):
                renpy.log(
                    "Unrecognized legacy mc_personality value: {!r}".format(data)
                )
        else:
            renpy.log(
                "Invalid mc_personality value of type {}; restoring defaults.".format(
                    type(data).__name__
                )
            )

        store.mc_personality = migrated
        return migrated

    def get_personality_data():
        return _ensure_personality_data()

    def save_personality_data(data):
        if not isinstance(data, dict):
            raise TypeError("Personality data must be a dictionary.")
        store.mc_personality = data
        update_mc_dominant_trait()

    def get_points(trait):
        return _ensure_personality_data().get(trait, 0)

    def add_personality(trait, amount=1):

        if trait not in PERSONALITY_TRAITS:
            raise ValueError(
                "Unknown personality trait: {}".format(trait)
            )

        personality = _ensure_personality_data()
        personality[trait] = personality.get(trait, 0) + amount

        update_mc_dominant_trait()

        return personality[trait]

    # --------------------------------------------------------
    # DOMINANT PERSONALITY
    # --------------------------------------------------------

    def update_mc_dominant_trait():

        personality = _ensure_personality_data()

        if not personality:
            store.dominant_personality = "Neutral"
            return

        highest_trait = max(
            PERSONALITY_TRAITS,
            key=lambda trait: personality.get(trait, 0)
        )

        highest_value = personality.get(highest_trait, 0)

        if highest_value < PERSONALITY_THRESHOLD:
            store.dominant_personality = "Neutral"
        else:
            store.dominant_personality = highest_trait

    def get_dominant_personality():
        return store.dominant_personality

    # --------------------------------------------------------
    # GIRL PERSONALITY PREFERENCES
    # --------------------------------------------------------

    def get_preferred_traits(girl):

        return preferred_personality.get(
            girl.lower(),
            []
        )

    # --------------------------------------------------------
    # PERSONALITY BONUSES
    # --------------------------------------------------------

    def personality_bonus(girl, base_amount):

        # Bonuses only apply to positive relationship gains.
        if base_amount <= 0:
            return base_amount

        bonus = 0

        for trait in get_preferred_traits(girl):

            if get_points(trait) >= PERSONALITY_THRESHOLD:
                bonus += 1

        return base_amount + bonus

    def personality_locked(girl):

        # Returns True when no preferred trait has reached 10.
        for trait in get_preferred_traits(girl):

            if get_points(trait) >= PERSONALITY_THRESHOLD:
                return False

        return True

    def personality_allows_exclusive(girl):

        return not personality_locked(girl)

    # --------------------------------------------------------
    # RELATIONSHIP INTEGRATION
    # --------------------------------------------------------

    def add_affection_with_personality(girl, base_amount):

        final_amount = personality_bonus(girl, base_amount)

        relationship_api.add_affection(
            girl,
            final_amount,
            apply_personality=False
        )

        return final_amount

    def add_trust_with_personality(girl, base_amount):

        final_amount = personality_bonus(girl, base_amount)

        relationship_api.add_trust(
            girl,
            final_amount,
            apply_personality=False
        )

        return final_amount

    # --------------------------------------------------------
    # PERSONALITY EVOLUTION
    # --------------------------------------------------------

    def personality_evolution_modifier(girl):

        caring = get_points("Caring")
        selfish = get_points("Selfish")

        if caring >= PERSONALITY_EVOLUTION_THRESHOLD:
            return - 5

        if selfish >= PERSONALITY_EVOLUTION_THRESHOLD:
            return 5

        return 0
