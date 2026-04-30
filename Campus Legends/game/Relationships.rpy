
# ============================================================
# RELATIONSHIP POINT SYSTEM
# ============================================================

default rel = {
    "Sienna": 0,
    "Jess": 0,
    "Aubrey": 0,
    "Norah": 0,
    "Tiffany": 0,
    "Kaia": 0,
    "Nick": 0
}

init python:
    # Add or subtract relationship points
    def add_rel(name, amount=1):
        rel[name] += amount

    # Get current relationship points
    def get_rel(name):
        return rel[name]

    # Set relationship points manually
    def set_rel(name, value):
        rel[name] = value

init python:
    def change_points(name, amount=1):
        rel[name] += amount

    def change_points(name, amount=1):
        if name not in rel:
            rel[name] = 0
        rel[name] += amount

init python:

    def check_romance_unlock(name):
        # Safety: auto-create missing keys
        if name not in rel:
            rel[name] = 0

        points = rel[name]

        # Basic romance threshold (customize this)
        if points >= 3:
            renpy.store.__dict__[f"{name.lower()}_romance_unlocked"] = True
        else:
            renpy.store.__dict__[f"{name.lower()}_romance_unlocked"] = False



