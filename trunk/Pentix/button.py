#!/usr/bin/env python3
import pygame

MOUSEDOWN = False


def draw_button(surface,
                msg, font_size, font_color,
                x, y, width, height,
                common_color, hover_color,
                action=None, args=()):
    global MOUSEDOWN
    mouse = pygame.mouse.get_pos()
    pygame.draw.rect(surface, (30, 30, 30), (x - 5, y + 5, width, height))
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(surface, hover_color, (x, y, width, height))
        if pygame.mouse.get_pressed()[0] and action and not MOUSEDOWN:
            action(*args)
        MOUSEDOWN = pygame.mouse.get_pressed()[0]
    else:
        pygame.draw.rect(surface, common_color, (x, y, width, height))
    font = pygame.font.SysFont("Arial", font_size)
    text = font.render(msg, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    surface.blit(text, text_rect)
