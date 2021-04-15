import random


class Ball(object):

    def __init__(self, pos, size, base_speed):

        self.pos = pos
        self.initial_pos = self.pos
        self.size = size

        self.base_speed = base_speed

        self.x_speed = 0
        self.y_speed = 0

    def release(self):
        choices = [-self.base_speed, self.base_speed]

        self.x_speed = random.choice(choices)
        self.y_speed = random.choice(choices)

    def move(self):
        self.pos = (self.pos[0] + self.x_speed,
                    self.pos[1] + self.y_speed)
