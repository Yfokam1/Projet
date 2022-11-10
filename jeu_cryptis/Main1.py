from game import Game
import pygame
V = Game()

while V.running:

    V.curr_menu.display_menu()
    V.game_loop()