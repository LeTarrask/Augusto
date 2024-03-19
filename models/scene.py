class Scene:
    __last_id = 0
    def __init__(self):
        self.id = Scene.__last_id
        Scene.__last_id += 1

    name = ""
    description = ""
    characters = []
    goals = ""
    end_result = ""
    consequences = ""
    act = ""
    plotpoint = ""
    previous_scene = ""
    chapter = ""

    final_text = ""
