import arcade
import math
from src.Characters.Entity import EntityClass
class PacmanCharacter(EntityClass):

    textures = []
    frame_count = 0
    direction = None

    def __init__(self, width, height, pos, name_file="pacmanki", folder_name="pacman"):

        super().__init__(width, height, pos, name_file, folder_name)
        self.direction = None
        self.desired_direction = None
        self.speed = 2
        self.time_since_last_move = 0
        self.texture = self.textures[0]

    def update(self, grid, delta_time):
        self.update_animation()
        self.move(grid)

