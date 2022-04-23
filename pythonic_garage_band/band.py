class Band():
    pass


class Musician():
    instrument = ""
    title = ""
    solo = ""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.title} instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return f"{self.solo}"

class Guitarist(Musician):
    instrument = "guitar"
    title = "Guitarist"
    solo = "face melting guitar solo"

class Bassist(Musician):
    instrument = "bass"
    title = "Bassist"
    solo = "bom bom buh bom"

class Drummer(Musician):
    instrument = "drums"
    title = "Drummer"
    solo = "rattle boom crash"

