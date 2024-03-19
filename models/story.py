class Story:
    characters = []
    acts = []
    plotlines = []
    chapters = []
    summary = ""

    __last_id = 0
    def __init__(self):
        self.id = Story.__last_id
        Story.__last_id += 1