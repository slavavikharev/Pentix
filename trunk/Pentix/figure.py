#!/usr/bin/env python3
import random
from pygame.locals import *
from figures import figures
import game as gm


class Figure:

    def __init__(self):
        self.figure = random.choice(figures)
        if random.choice([0, 1]):
            self.figure = [row[::-1] for row in self.figure]
        self.x = gm.WIDTH // 2 - len(self.figure[0]) // 2
        self.y = -len(self.figure)

    def can_move(self, level, dx, dy, coord=None, figure=None):
        if not figure:
            figure = self.figure
        if not coord:
            coord = (self.x, self.y)
        if coord[0] < 0 or coord[0] + len(figure[0]) > gm.WIDTH or \
                coord[1] + len(figure) > gm.HEIGHT:
            return False
        for i in range(len(figure)):
            for j in range(len(figure[0])):
                if coord[1] + i >= 0 and \
                        figure[i][j] and \
                        level[coord[1] + i + dy][coord[0] + j + dx]:
                    return False
        return True

    def move_aside(self, level, keys):
        if keys[K_LEFT] and self.x > 0 and self.can_move(level, -1, 0):
            self.x -= 1
        if keys[K_RIGHT] and self.x + len(self.figure[0]) < gm.WIDTH and \
                self.can_move(level, 1, 0):
            self.x += 1

    def move_down(self, game, keys):
        if keys[K_DOWN]:
            self.fall_down(game)

    def fall_down(self, game):
        if self.y + len(self.figure) == gm.HEIGHT:
            game.fix_current()
            return
        if not self.can_move(game.level, 0, 1):
            game.fix_current()
            if self.y <= 0:
                game.stop()
            return
        self.y += 1

    def rotate(self, level):
        temp = [[self.figure[j][i]
                 for j in range(len(self.figure) - 1, -1, -1)]
                for i in range(len(self.figure[0]))]
        x = self.x + len(temp) // 2 - len(temp[0]) // 2
        y = self.y - len(temp) // 2 + len(temp[0]) // 2
        for i in range(len(temp[0])):
            if self.can_move(level, 0, 0, (x - i, y), temp):
                self.x = x - i
            elif self.can_move(level, 0, 0, (x + i, y), temp):
                self.x = x + i
            else:
                continue
            self.figure = temp
            self.y = y
            return
