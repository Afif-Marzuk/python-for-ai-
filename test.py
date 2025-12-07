class Human:
    def __init__(self, name, race):
        self.name = name      # defined in init
        self.race = race      # defined in init

    def talk(self, words):
        self.words = words    # defined dynamically here
        print(self.words)


class aus(Human):
    def wa(self, walk):
        self.w = walk
        return walk


richie = aus("richie", "australian")
richie.wa("hey i can walk wanna see?")
richie.w
