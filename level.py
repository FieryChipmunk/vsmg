import pygame

pygame.init()

class Level:

    def __init__(self, input_array, tile_size, imgs):

        self.input_array = input_array

        self.tile_size = tile_size

        self.tiles_to_collide = [[],[],[]]

        self.imgs = imgs

        y = 0
        
        for row in self.input_array:

            x = 0

            for tile in row:

                if tile == 1 or tile == 2:

                    self.tiles_to_collide[0].append(pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))

                elif tile == 3:

                    self.tiles_to_collide[1].append(pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))

                elif tile == 4:

                    self.tiles_to_collide[2].append(pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))

                elif tile == 5:

                    self.respawn_x = x * self.tile_size
                    self.respawn_y = y * self.tile_size
                    
                x += 1

            y += 1

    def draw(self, screen, camera):
        
        y = 0
        
        for row in self.input_array:

            x = 0

            for tile in row:

                if tile == 1:

                    screen.blit(self.imgs[0],(x * self.tile_size - camera.x_offset, y * self.tile_size - camera.y_offset))

                if tile == 2:

                    screen.blit(self.imgs[1],(x * self.tile_size - camera.x_offset, y * self.tile_size - camera.y_offset))

                elif tile == 3:

                    screen.blit(self.imgs[2],(x * self.tile_size - camera.x_offset, y * self.tile_size - camera.y_offset))

                elif tile == 4:

                    screen.blit(self.imgs[3],(x * self.tile_size - camera.x_offset, y * self.tile_size - camera.y_offset))
                  
                x += 1

            y += 1
