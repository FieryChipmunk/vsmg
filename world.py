import pygame
from level import Level

pygame.init()

class World:

    def __init__(self, levels, tile_size, palette):

        self.levels = []

        for level in levels:

            new_level = Level(level, tile_size, palette)
            self.levels.append(new_level)

        self.current_level = self.levels[0]

    def draw(self, screen, camera):

        self.current_level.draw(screen, camera)
        
    def update_player_level(self, player):

        player.x = self.current_level.respawn_x
        player.y = self.current_level.respawn_y
        
        player.current_level = self.current_level

    def go_to_next_level(self, player):

        if self.levels[self.levels.index(self.current_level) + 1]:

            player.x = self.levels[self.levels.index(self.current_level) + 1].respawn_x
            player.y = self.levels[self.levels.index(self.current_level) + 1].respawn_y

            self.current_level = self.levels[self.levels.index(self.current_level) + 1]
