import arcade
import math
from src.Characters.Entity import EntityClass
class Ghosts(EntityClass):

    textures = []
    frame_count = 0
    direction = None

    def __init__(self, width, height, pos, name_file="bug", folder_name="ghosts"):

        super().__init__(width, height, pos, name_file, folder_name)
        self.PLAYER_MOVEMENT_SPEED = 3
        self.desired_direction = arcade.key.RIGHT
        self.direction = arcade.key.RIGHT

        self.texture = self.textures[0]

    def priorX(self, diff):
        if diff>=0:
            return [arcade.key.RIGHT, arcade.key.LEFT]
        return [arcade.key.LEFT, arcade.key.RIGHT]
    def priorY(self, diff):
        if diff >= 0:
            return [arcade.key.UP, arcade.key.DOWN]
        return [arcade.key.DOWN, arcade.key.UP]

    def update(self, grid, player_sprite):

        if (self.center_x % self.width_case == self.width_case / 2) and (self.center_y % self.height_case == self.height_case / 2):
            diff_x = player_sprite.center_x - self.center_x
            diff_y = player_sprite.center_y - self.center_y
            priorDirection = []
            priorX = self.priorX(diff_x)
            priorY = self.priorY(diff_y)
            if abs(diff_x) > abs(diff_y):
                priorDirection.append(priorX[0])
                priorDirection.append(priorY[0])
                priorDirection.append(priorY[1])
                priorDirection.append(priorX[1])
            else:
                priorDirection.append(priorY[0])
                priorDirection.append(priorX[0])
                priorDirection.append(priorX[1])
                priorDirection.append(priorY[1])
            while(len(priorDirection) > 0):
                currDir = priorDirection.pop(0)
                self.direction = currDir
                if (len(priorDirection) > 0 and not self.will_collide(currDir, grid)):
                    break

        self.update_animation()
        self.move(grid)