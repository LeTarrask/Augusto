class Character:
    __last_id = 0

    def __init__(self):
        self.id = Character.__last_id
        Character.__last_id += 1
        self.name = ""
        self.role = ""
        self.age = ""
        self.occupation = ""
        self.appearance = ""
        self.personality_traits = ""
        self.motivation = ""
        self.backstory = ""
        self.detailedProfile = ""
        self.keyScenes = []

    def to_dict(self):
        return {
            "Name": self.name,
            "Role": self.role,
            "Age": self.age,
            "Occupation": self.occupation,
            "Appearance": self.appearance,
            "Personality Traits": self.personality_traits,
            "Motivation": self.motivation,
            "Backstory": self.backstory
        }