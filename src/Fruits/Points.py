import arcade
import time

class Points_sprite (arcade.Sprite):

    points_textures = []
    points_show = False
    timer = 0

    def __init__(self, width, height, fruit_pos):
        super().__init__()

        self.scale = 2
        self.timer = time.time()
        self.position = fruit_pos
        points_path = arcade.load_texture("C:/Users/kylli/OneDrive/Bureau/pacman-main/pacman-main/images/fruits/200.png")
        self.points_textures.append(points_path)
        self.width = width
        self.height = height
        self.center_x = self.position[0] * width + (width/2)
        self.center_y = self.position[1] * height + (height/2)

        self.texture = self.points_textures[0]


    def points_draw (self):

        if self.points_show == True:
            print("DESSSSSSSSSSSSSSSSSSSSSSSSSIIIIIIIIIIIIIIINNNNNNNNNNN")
            timer = time.time() - self.timer
            while timer < 10:
                self.draw()
                break

            self.points_show = False
