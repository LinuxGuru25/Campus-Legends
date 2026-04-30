
# ============================================================
# PERSONALITY SYSTEM
# ============================================================

default reputation = {
    "social": 0,       # popularity
    "romantic": 0,     # how desirable you seem
    "loyalty": 0,      # how trustworthy you seem
    "chaos": 0,        # drama, rumors, messiness
}

default rep_with = {
    "Sienna": 0,
    "Jess": 0,
    "Tiffany": 0,
    "Aubrey": 0,
    "Kaia": 0,
    "Misty": 0,
    "Norah": 0,
}


default personality = {
    "Confident": 0,
    "Caring": 0,
    "Selfish": 0
}

# Optional thresholds for personality-based scenes
default personality_threshold = {
    "Confident": 5,
    "Caring": 5,
    "Selfish": 5
}

# Tracks the MC's dominant personality
default mc_personality = "Neutral"

init python:

    # Add personality points
    def add_personality(trait, amount=1):
        personality[trait] += amount

    # Get personality value
    def get_personality(trait):
        return personality[trait]

    # Set personality manually
    def set_personality(trait, value):
        personality[trait] = value

    # Determine dominant personality
    def update_mc_personality():
        global mc_personality
        highest = max(personality, key=personality.get)
        mc_personality = highest
        return mc_personality

init python:
    def add_personality(trait, amount=1):
        personality[trait] += amount

        # Reputation hooks
        if trait == "Confident":
            reputation["social"] += amount
            reputation["romantic"] += amount * 0.5

        if trait == "Caring":
            reputation["loyalty"] += amount
            reputation["romantic"] += amount * 0.25

        if trait == "Selfish":
            reputation["loyalty"] -= amount
            reputation["chaos"] += amount

