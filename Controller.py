from Section import *
from openal import *
import time
from random import choice
class Controller:
    def __init__(self, sections):
        self.sections = sections
        self.ambient = Audio("./ambient/intro.wav")
        self.ambient.play()
    def startGame(self):
        next = 0
        while(next > -1):
            if next == 8:
                ans = self.minigame()
                if ans == -1:
                    next = 9
                else:
                    next = 10
            actual = self.sections[next]
            if actual.ambient:
                self.ambient.stop()
                self.ambient = actual.ambient
                self.ambient.play()
            if actual.sfx:
                actual.sfx.play()
            next = self.sections[next].play()
    def minigame(self):
        result = 0
        print("Presta atención a la dirección de los pasos. Dispara a la izquierda (0) o derecha(1). Afortunadamente, no te pueden ver tras los arbustos. Preparaté...")
        time.sleep(5)
        print("3...")
        print("2...")
        print("1...")
        print("YA.")
        sfx = oalOpen("./sfx/running_leaves.wav")
        for i in range(5):
            dir = choice([-1, 1])
            sfx.set_position([5 * dir, 0, 0])
            sfx.play()
            ans = input("0/1: ")
            sfx.stop()
            if ans == 0 and dir == 1 or ans == 1 and dir == -1:
                return -1
        return 0
            
    #oalQuit()