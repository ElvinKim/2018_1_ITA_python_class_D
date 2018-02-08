class Song:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre


class Singer:
    def __init__(self, name, agency):
        self.name = name
        self.agency = agency

    def sing(self, song):
        print(song.title + "을(를) 부르자~~~")


singer = Singer("윤종신", "미스틱")
song = Song("좋니", "발라드")
singer.sing(song)
