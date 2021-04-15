import pygame


class Drawer(object):
    GREY = (150, 150, 150)

    def __init__(self, screen, width, height, controller,
                 player_racket, bot_racket, ball):

        self.screen = screen
        self.width = width
        self.height = height
        self.controller = controller

        self.player_racket = player_racket
        self.bot_racket = bot_racket
        self.ball = ball

        self.score_font = pygame.font.SysFont("lucidaconsole", self.ball.size)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_mid_line()
        self.draw_scores()
        self.draw_racket(self.player_racket)
        self.draw_racket(self.bot_racket)

        self.draw_ball(self.ball)
        pygame.display.update()

    def draw_mid_line(self):
        for y in range(0, self.height, self.ball.size):
            pygame.draw.line(self.screen, self.GREY, (self.width // 2, y), (self.width // 2, y + self.ball.size // 2))

    def draw_racket(self, racket):
        pygame.draw.rect(self.screen, self.GREY,
                         (racket.pos[0], racket.pos[1], racket.width,
                          racket.height))

    def draw_ball(self, ball):
        if ball.pos is not None:
            pygame.draw.rect(self.screen, self.GREY,
                             (ball.pos[0], ball.pos[1], ball.size, ball.size))

    def draw_scores(self):
        p = self.controller.player_score
        b = self.controller.bot_score

        p_surface = self.score_font.render(str(p), False, self.GREY)
        b_surface = self.score_font.render(str(b), False, self.GREY)

        self.screen.blit(p_surface, (self.width - self.width // 3 - self.ball.size, self.height // 10))
        self.screen.blit(b_surface, (self.width // 3, self.height // 10))
