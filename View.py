from Controller import *

class View:
    def __init__(self):
        sections = []
        sections.append(Section(0, "Welcome to GAME", [("Start", 2), ("Exit", -1)]))
        sections.append(Section(1, "You Died", []))
        sections.append(Section(2, "You find yourself in a strange forest. Unknown of all that happened. It's raining and cold. You try to search for refugee. You see three paths in front of you...", [("Right path", 0), ("Front path", 0), ("Left path", 0), ("Hide", 1)]))
        
        c = Controller(sections)
        c.startGame()