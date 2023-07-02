import pygame

pygame.init()

class Player:

        def __init__(self, world):

                self.x = world.current_level.respawn_x

                self.y = world.current_level.respawn_y

                self.player_rect = pygame.Rect(self.x, self.y, 64, 64)

                self.img = None

                self.animation = 0

                self.animation_counter = 0

                self.facing_right = False

                self.y_velocity = 0

                self.x_velocity = 0

                self.target_x_velocity = 0

                self.acceleration = 0.25

                self.decceleration = 0.25

                self.max_speed = 5

                self.coyote_time = 0

                self.gravity = 1

                self.jump_height = 20

                self.current_level = world.current_level

        def draw(self, screen, camera, animations):

                if self.coyote_time > 1:

                        if self.y_velocity > 0:

                                self.animation = 3

                        else:

                                self.animation = 2

                elif self.x_velocity != 0:

                        self.animation = 1

                else:
                        self.animation = 0

                self.animation_counter += 0.2

                if int(self.animation_counter) >= len(animations[self.animation]):
                        
                                self.animation_counter = 0

                self.img = animations[self.animation][int(self.animation_counter)]            

                if self.facing_right:

                        screen.blit(self.img,(self.player_rect.left - camera.x_offset,self.player_rect.top - camera.y_offset))

                else:

                        screen.blit(pygame.transform.flip(self.img,True,False),(self.player_rect.left - camera.x_offset,self.player_rect.top - camera.y_offset))

                        

        def detect_move(self,event):

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:

                        self.target_x_velocity += self.max_speed

                elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:

                        self.target_x_velocity -= self.max_speed

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:

                        self.target_x_velocity -= self.max_speed

                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:

                        self.target_x_velocity += self.max_speed

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.coyote_time < 6:
                        
                        self.y_velocity = -self.jump_height

        def move(self):

                if self.target_x_velocity == 0:

                        if self.x_velocity != 0:

                                if self.x_velocity < 0:

                                        if self.x_velocity + self.decceleration >= 0:

                                                self.x_velocity = 0

                                        else:

                                                self.x_velocity += self.decceleration

                                else:

                                        if self.x_velocity - self.decceleration <= 0:

                                                self.x_velocity = 0

                                        else:

                                                self.x_velocity -= self.decceleration
                
                        else:
                                
                                self.x_velocity = 0

                else:

                        if self.target_x_velocity < 0:

                                if self.x_velocity - self.acceleration <= self.target_x_velocity:

                                        self.x_velocity = self.target_x_velocity

                                else:

                                        self.x_velocity -= self.acceleration

                        else:

                                if self.x_velocity + self.acceleration >= self.target_x_velocity:

                                        self.x_velocity = self.target_x_velocity

                                else:

                                        self.x_velocity += self.acceleration

                if self.x_velocity > 0:

                        self.facing_right = True

                elif self.x_velocity < 0:

                        self.facing_right = False

                self.player_rect.top += self.y_velocity
                self.y_velocity += self.gravity
                self.player_rect.left += self.x_velocity
                self.coyote_time += 1

                if self.player_rect.bottom > 1000:

                        self.reset()

        def collide(self, world):

                if self.current_level != None:

                        for tile in self.current_level.tiles_to_collide[0]:

                                if self.player_rect.colliderect(tile):

                                        if self.player_rect.bottom >= tile.top and self.y_velocity > 0 and self.player_rect.bottom - self.y_velocity <= tile.top:
                                                
                                                self.player_rect.bottom = tile.top
                                                self.y_velocity = 0
                                                self.coyote_time = 0

                                        elif self.player_rect.top <= tile.bottom and self.y_velocity <= 0 and self.player_rect.top - self.y_velocity + self.gravity >= tile.bottom and self.player_rect.right - self.x_velocity > tile.left and self.player_rect.left - self.x_velocity < tile.right:

                                                self.player_rect.top = tile.bottom
                                                self.y_velocity = 0

                                        elif self.player_rect.right + self.x_velocity >= tile.left and self.x_velocity > 0:

                                                self.player_rect.right = tile.left

                                        else:

                                                self.player_rect.left = tile.right

                        for hazard in self.current_level.tiles_to_collide[1]:

                                if self.player_rect.colliderect(hazard):

                                        self.reset()

                        for portal in self.current_level.tiles_to_collide[2]:

                                if self.player_rect.colliderect(portal):

                                        world.go_to_next_level(self)
                                        self.reset()

        def reset(self):
                        
                self.player_rect.left = self.x
                self.player_rect.top = self.y
                self.y_velocity = 0
                self.x_velocity = 0
