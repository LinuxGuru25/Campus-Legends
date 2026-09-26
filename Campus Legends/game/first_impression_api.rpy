init python:

    class FirstImpressionAPI:

        def __init__(self):
            self.data = {}

        def ensure_character(self, name):
            if name not in self.data:
                self.data[name] = 0

        def add_first_impression(self, name, amount):
            self.ensure_character(name)
            self.data[name] += amount
            renpy.log("First Impression | {}: {}".format(name, self.data[name]))

        def get_first_impression(self, name):
            self.ensure_character(name)
            return self.data[name]

        def set_first_impression(self, name, value):
            self.ensure_character(name)
            self.data[name] = value

    # Global instance
    first_impression_api = FirstImpressionAPI()

init python:

    class CharacterImpressionWrapper:

        def __init__(self, name):
            self.name = name

        def add_first_impression(self, amount):
            first_impression_api.add_first_impression(self.name, amount)

        def get(self):
            return first_impression_api.get_first_impression(self.name)

    # Character wrappers
    jess_api = CharacterImpressionWrapper("Jess")
    sienna_api = CharacterImpressionWrapper("Sienna")
    nick_api = CharacterImpressionWrapper("Nick")

init python:

    girl_impression_apis = {}

    for girl in GIRL_NAMES:
        girl_impression_apis[girl] = CharacterImpressionWrapper(girl)

    # Optional direct variables for convenience
    jess_api = girl_impression_apis["Jess"]
    sienna_api = girl_impression_apis["Sienna"]
    aubrey_api = girl_impression_apis["Aubrey"]
    misty_api = girl_impression_apis["Misty"]
    kaia_api = girl_impression_apis["Kaia"]
    tiffany_api = girl_impression_apis["Tiffany"]
    norah_api = girl_impression_apis["Norah"]

init python:

    def get_all_girl_impressions():
        """
        Returns a clean dictionary:
        {
            "Jess": 3,
            "Sienna": -1,
            "Aubrey": 2,
            ...
        }
        Perfect for UI screens.
        """
        result = {}
        for girl in GIRL_NAMES:
            result[girl] = first_impression_api.get_first_impression(girl)
        return result

init python:

    def get_girl_impression_list():
        """
        Returns a list of tuples:
        [
            ("Jess", 3),
            ("Sienna", -1),
            ("Aubrey", 2),
            ...
        ]
        Perfect for vboxes, hboxes, repeaters, scrollables.
        """
        return [(girl, first_impression_api.get_first_impression(girl)) for girl in GIRL_NAMES]

init python:

    class GirlProfile:

        def __init__(self, name):
            self.name = name

        @property
        def impression(self):
            return first_impression_api.get_first_impression(self.name)

        # Future expansion:
        # @property
        # def romance(self):
        #     return romance_api.get(self.name)

        # @property
        # def reputation(self):
        #     return reputation_api.get(self.name)

    # Auto-generate profiles
    girl_profiles = {girl: GirlProfile(girl) for girl in GIRL_NAMES}

init python:

    def get_phone_character_data():
        """
        Returns a list of dicts:
        [
            {"name": "Jess", "impression": 3},
            {"name": "Sienna", "impression": -1},
            ...
        ]
        Perfect for JSON-like UI structures.
        """
        data = []
        for girl in GIRL_NAMES:
            data.append({
                "name": girl,
                "impression": first_impression_api.get_first_impression(girl)
            })
        return data
