#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Rect, Surface
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(
        self,
    ):
        menu_option = 0
        # Generate the Music on Menu
        pygame.mixer_music.load("./asset/Menu.mp3")

        # Music Loop
        pygame.mixer_music.play(-1)

        while True:

            # Generate the menu image on screen
            self.window.blit(source=self.surf, dest=self.rect)

            # Generate "Mountain" text
            self.menu_text(
                text_size=50,
                text="MOUNTAIN",
                text_color=COLOR_ORANGE,
                text_center_pos=((WIN_WIDTH / 2), 70),
            )

            # Generate "Shooter" text
            self.menu_text(
                text_size=50,
                text="SHOOTER",
                text_color=COLOR_ORANGE,
                text_center_pos=((WIN_WIDTH / 2), 110),
            )

            # Generate options on menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(
                        text_size=20,
                        text=MENU_OPTION[i],
                        text_color=COLOR_YELLOW,
                        text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i),
                    )
                else:
                    self.menu_text(
                        text_size=20,
                        text=MENU_OPTION[i],
                        text_color=COLOR_WHITE,
                        text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i),
                    )

            # Update screen
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Down Key
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:  # Up Key
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Enter Key
                        return MENU_OPTION[menu_option]

    def menu_text(
        self,
        text_size: int,
        text: str,
        text_color: tuple,
        text_center_pos: tuple,
        antialias=None,
    ):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Unicode", size=text_size
        )
        text_surf: Surface = text_font.render(
            text, antialias, text_color
        ).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    pass
