from openal import *
class Audio:
    def __init__(self, path, volume = 0.5, position = [0, 0, 0], velocity = [0, 0, 0]):
        self.path = path
        self.position = position
        self.velocity = velocity
        self.volume = volume
        self.source = oalOpen(self.path)
        self.source.set_source_relative(True)
        self.source.set_position(self.position)
        self.source.set_velocity(self.velocity)
        self.source.set_gain(self.volume)
    def play(self):
        self.source.play()
        print(self.source.position)
    def stop(self):
        self.source.stop()