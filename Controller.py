from Section import *

class Controller:
    def __init__(self, sections):
        self.sections = sections
    def startGame(self):
        next = 0
        while(next != -1):
            next = self.sections[next].play()