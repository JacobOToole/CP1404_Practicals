"""Band class for CP1404"""


class Band:

    def __init__(self, band_name):
        self.band_name = band_name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)
        print(self.musicians)

    def play(self):
        for i in self.musicians:
            if not self.musicians[i]['instruments']:
                return f"{self.musicians[i]['name']} needs an instrument!"
            return f"{self.musicians[i]['name']} is playing {self.musicians[i['instruments']]}"

        if not self.instruments:
            return f"{self.name} needs an instrument!"
        return f"{self.name} is playing: {self.instruments[0]}"

    def __str__(self):
        return f'{self.band_name} {self.musicians}'