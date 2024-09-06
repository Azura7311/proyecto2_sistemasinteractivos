import openal

from Audio import *

class Section:
    def __init__(self, id, text, options, ambient, sfx):
        self.id = id
        self.text = text
        self.options = options
        self.ambient = ambient
        self.sfx = sfx
    def play(self):
        print(self.text)
        if len(self.options) == 0:
            return -1
        else:
            for i in range(len(self.options)):
                print(str(i + 1) + ". " + self.options[i][0])
            choice = -1
            while choice < 0 or choice > len(self.options):
                choice = int(input("Choice: ")) - 1
            return self.options[choice][1]