class Chapter:
    __last_id = 0
    def __init__(self):
        self.id = Chapter.__last_id
        Chapter.__last_id += 1

    name = ""
    description = ""
    characters = []
    goals = ""
    end_result = ""
    consequences = ""
    scenes = []
    act = ""
    plotpoint = ""

    