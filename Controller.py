from Section import *
from openal import *
import time
import os
from random import choice, randint
class Controller:
    def __init__(self, sections):
        self.sections = sections
        self.ambient = Audio("./ambient/intro.wav")
        self.ambient.play()
        self.sfx = Audio("./sfx/chimney.wav")
        self.sfx.play()
    def startGame(self): # Function to play the game
        next = 0
        while(next > -1): # Each turn the next scene is chosen
            if next == 8: # For minigames
                ans = self.minigame_shoot()
                if ans == -1:
                    next = 9
                else:
                    next = 10
            elif next == 15:
                ans = self.minigame_math()
                if ans == -1:
                    next = 16
                else:
                    next = 17
            actual = self.sections[next]
            if actual.ambient: # Ambient and sfx change
                self.ambient.stop()
                self.ambient = actual.ambient
                self.ambient.play()
            if actual.sfx:
                self.sfx.stop()
                self.sfx = actual.sfx
                actual.sfx.play()
            next = self.sections[next].play()
        
        if next == -1:
            print("Has perdido. Vuelve a intentarlo")
        else:
            print("Has ganado. ¡Felicidades! ¿Ya desbloqueaste el otro final?")
        os.exit()
    # Minigames
    def minigame_shoot(self):
        result = 0
        print("Presta atención a la dirección de los pasos. Dispara a la izquierda (0) o derecha(1). Afortunadamente, no te pueden ver tras los arbustos. Preparaté...")
        self.ambient.stop()
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
            ans = int(input("0/1: "))
            sfx.stop()
            if ans == 0 and dir == 1 or ans == 1 and dir == -1:
                return -1
    def minigame_math(self):
        result = 0
        print("El sistema enemigo está cifrado con problemas matemáticos. Resuelvelos 5 problemas correctamente para desactivarlo.")
        time.sleep(5)
        print("3...")
        print("2...")
        print("1...")
        print("YA.")
        oalQuit()
        self.ambient = oalOpen("./ambient/math.wav")
        self.ambient.play()
        for i in range(5):
            op1 = randint(-7, 12)
            op2 = randint(-7, 12)
            ans = int(input(str(op1) + " + " + str(op2) + " = "))
            if ans != op1 + op2:
                self.ambient.stop()
                return -1
        return 0