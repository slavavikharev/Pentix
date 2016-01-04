#!/usr/bin/env python3
import sys
import pygame
from pygame.locals import *
import game as gm

pygame.init()

FPS = 30
MOVING = USEREVENT + 1
FALLING = USEREVENT + 2
BOOSTING = USEREVENT + 3
START = USEREVENT + 4


def main():
    resolution = (1024, 768)
    game = gm.Game(False, resolution)
    pygame.mixer.music.load('bg.mp3')
    pygame.mixer.music.play(loops=-1)
    while not game.quit:
        game.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == START:
                temp = game.highscore
                game = gm.Game(game.fullscreen, game.screen_size)
                game.highscore = temp
            elif event.type == VIDEORESIZE:
                game.screen_size = event.dict['size']
                game.draw_main()
            if game.paused:
                continue
            if event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_RIGHT] or keys[K_LEFT]:
                    game.current.move_aside(game, keys)
                    pygame.time.set_timer(MOVING, 300)
                if keys[K_UP]:
                    game.current.rotate(game)
            elif event.type == KEYUP:
                keys = pygame.key.get_pressed()
                if not keys[K_LEFT] and not keys[K_RIGHT]:
                    pygame.time.set_timer(MOVING, 0)
            elif event.type == MOVING:
                pygame.time.set_timer(MOVING, 60)
                keys = pygame.key.get_pressed()
                game.current.move_aside(game, keys)
            elif event.type == FALLING:
                game.current.fall_down(game)
            elif event.type == BOOSTING:
                keys = pygame.key.get_pressed()
                game.current.move_down(game, keys)
        pygame.display.update()
        game.fpsClock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
