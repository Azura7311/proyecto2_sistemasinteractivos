from Section import *

class Controller:
    def __init__(self, sections):
        self.sections = sections
        self.ambient = Audio("./ambient/intro.wav")
        self.ambient.play()
    def startGame(self):
        next = 0
        while(next != -1):
            actual = self.sections[next]
            if actual.ambient:
                self.ambient.stop()
                self.ambient = actual.ambient
                self.ambient.play()
            if actual.sfx:
                actual.sfx.play()
            next = self.sections[next].play()
        oalQuit()