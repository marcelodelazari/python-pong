import time
import random
import pygame


class Controller(object):

    def __init__(self, width, height,
                 player_racket, bot_racket, ball):

        self.WIDTH = width
        self.HEIGHT = height

        self.player_racket = player_racket
        self.bot_racket = bot_racket
        self.ball = ball
        self.releasing_ball = True
        self.last_release = time.time()

        self.player_score = 0
        self.bot_score = 0

        self.bot_speed = self.HEIGHT // 70

    def invert_x_axis(self):
        self.ball.x_speed = -self.ball.x_speed

    def invert_y_axis(self):
        self.ball.y_speed = -self.ball.y_speed

    def check_for_score(self):
        x, y = self.ball.pos[0], self.ball.pos[1]
        size = self.ball.size

        if x >= self.WIDTH:
            self.ball.pos = None
            self.last_release = time.time()
            self.releasing_ball = True
            self.bot_score += 1

        elif x <= 0 - size:
            self.ball.pos = None
            self.last_release = time.time()
            self.releasing_ball = True
            self.player_score += 1

    def check_for_player_collision(self):
        if self.ball.x_speed <= 0:
            return False

        ball_x, ball_y = self.ball.pos[0], self.ball.pos[1]
        racket_x, racket_y = self.player_racket.pos

        if ball_x + self.ball.size >= racket_x - self.ball.base_speed // 2 and ball_x + self.ball.size <= racket_x + self.ball.base_speed // 2:
            if ball_y >= racket_y - self.ball.size and ball_y <= racket_y + self.player_racket.height + self.ball.size:
                self.invert_x_axis()
                if random.randrange(4) == 0:
                    self.invert_y_axis()

    def check_for_bot_collision(self):
        if self.ball.x_speed >= 0:
            return False

        ball_x, ball_y = self.ball.pos[0], self.ball.pos[1]
        racket_x, racket_y = self.bot_racket.pos

        if ball_x <= racket_x + self.bot_racket.width + self.ball.base_speed // 2 and ball_x >= racket_x + self.bot_racket.width - self.ball.base_speed // 2:
            if ball_y >= racket_y - self.ball.size and ball_y <= racket_y + self.bot_racket.height + self.ball.size:
                self.invert_x_axis()
                if random.randrange(4) == 0:
                    self.invert_y_axis()

    def check_for_screen_collision(self):
        x, y = self.ball.pos[0], self.ball.pos[1]
        size = self.ball.size

        if y <= 0 or y >= self.HEIGHT - size:
            self.invert_y_axis()

    def move_racket(self, racket):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        racket.pos = (racket.pos[0], mouse_y - racket.height // 2)

    def release_ball(self, last_time):
        if self.releasing_ball:
            if self.ball.pos is None:
                self.ball.pos = (self.ball.initial_pos[0],
                                 random.randrange(self.ball.size + self.ball.base_speed, self.HEIGHT - self.ball.size - self.ball.base_speed))

            if time.time() - last_time > 1:
                self.ball.release()
                self.releasing_ball = False

    def move_bot(self):
        mid_racket = self.bot_racket.pos[1] + self.bot_racket.height // 2

        ball_y = self.ball.pos[1]
        if not self.releasing_ball and self.ball.x_speed < 0:
            target = ball_y
        else:
            target = (self.HEIGHT // 2)

        distance = target - mid_racket
        new_pos = self.bot_racket.pos
        bot_move = random.randrange(self.bot_speed//2, self.bot_speed*2)
        if distance > self.HEIGHT // 100:
            new_pos = (self.bot_racket.pos[0], self.bot_racket.pos[1] + bot_move)
        elif distance < -self.HEIGHT // 100:
            new_pos = (self.bot_racket.pos[0], self.bot_racket.pos[1] - bot_move)
        self.bot_racket.pos = new_pos

    def gameplay(self):

        self.move_racket(self.player_racket)
        self.move_bot()

        self.check_for_bot_collision()
        self.check_for_score()

        if not self.releasing_ball:
            self.ball.move()
        else:
            self.release_ball(self.last_release)

        self.check_for_screen_collision()
        self.check_for_player_collision()
