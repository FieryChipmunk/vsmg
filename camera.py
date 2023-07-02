import pygame

pygame.init()

class Camera:

    def __init__(self):

        self.x_offset = 0

        self.y_offset = 0

        self.calculated_x_offset = 0

        self.calculated_y_offset = 0

    def follow_player(self, player):

        self.calculated_x_offset += ((player.player_rect.centerx - 512) - self.calculated_x_offset) / 10
        self.calculated_y_offset += ((player.player_rect.centery - 256) - self.calculated_y_offset) / 10
        
        self.x_offset = int(self.calculated_x_offset)
        self.y_offset = int(self.calculated_y_offset)
            
