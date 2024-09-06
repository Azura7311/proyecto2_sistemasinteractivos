from Controller import *
from openal import *

class View:
    def __init__(self):
        self.sections = []
        self.sections.append(Section(0, "Welcome to The Lost Warrior", [("Start", 2), ("Instructions", 1), ("Exit", -1)], Audio("./ambient/intro.wav"), None))
        self.sections.append(Section(1, "In this game your objective is to survive through the unknown land of 'The Fountain' and find your way back home. You have to make the right choices to avoid dying. Good luck", [("Go back", 0)], Audio("./ambient/instructions.wav"), None))
        self.sections.append(Section(2, "You find yourself in a strange forest, unknown of all that happened. The only thing you remembered is that you were escaping from someone...\n\nIt's raining and cold. You try to search for refugee. After 5 minutes of walk, you see three paths in front of you. In addition, you seem to hear someone coming from the right, but unknown if it's worth to identify...", [("Right path", 0), ("Front path", 0), ("Left path", 0), ("Hide and wait", 1)], Audio("./ambient/foreststorm.wav"), Audio("./sfx/running_leaves.wav", 1, [10, 0, 0])))
        
        c = Controller(self.sections)
        c.startGame()